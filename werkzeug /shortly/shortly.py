import os
import redis
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from werkzeug.utils import redirect
from urllib.parse import urlsplit  # Updated import

from jinja2 import Environment, FileSystemLoader


class ShortlyApp:
    def __init__(self, config):
        self.redis = redis.Redis(host=config['redis_host'], port=config['redis_port'])

        # Set up Jinja2 environment
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

        # Set up URL routing
        self.url_map = Map([
            Rule('/', endpoint='new_url'),
            Rule('/<short_id>', endpoint='follow_short_link'),
            Rule('/<short_id>+', endpoint='short_link_details')
        ])

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, environ, start_response):
        request = Request(environ)
        adapter = self.url_map.bind_to_environ(environ)
        try:
            endpoint, values = adapter.match()
            response = getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            response = e
        return response(environ, start_response)

    def on_new_url(self, request):
        error = None
        url = ''
        if request.method == 'POST':
            url = request.form['url']
            if not self.is_valid_url(url):
                error = 'Please enter a valid URL'
            else:
                short_id = self.insert_url(url)
                return redirect(f"/{short_id}+")
        return self.render_template('new_url.html', error=error, url=url)

    def is_valid_url(self, url):
        parts = urlsplit(url)  # Use urlsplit to parse the URL
        return parts.scheme in ('http', 'https')

    def insert_url(self, url):
        short_id = self.redis.get(f'reverse-url:{url}')
        if short_id is not None:
            return short_id.decode('utf-8')  # Decode from bytes to str
        url_num = self.redis.incr('last-url-id')
        short_id = self.base36_encode(url_num)
        self.redis.set(f'url-target:{short_id}', url)
        self.redis.set(f'reverse-url:{url}', short_id)
        return short_id

    def base36_encode(self, number):
        assert number >= 0, 'positive integer required'
        if number == 0:
            return '0'
        base36 = []
        while number != 0:
            number, i = divmod(number, 36)
            base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
        return ''.join(reversed(base36))

    def on_follow_short_link(self, request, short_id):
        link_target = self.redis.get(f'url-target:{short_id}')
        if link_target is None:
            raise NotFound()
        self.redis.incr(f'click-count:{short_id}')
        return redirect(link_target.decode('utf-8'))  # Decode from bytes to str

    def on_short_link_details(self, request, short_id):
        link_target = self.redis.get(f'url-target:{short_id}')
        if link_target is None:
            raise NotFound()
        click_count = int(self.redis.get(f'click-count:{short_id}') or 0)
        return self.render_template('short_link_details.html',
            link_target=link_target.decode('utf-8'),  # Decode from bytes to str
            short_id=short_id,
            click_count=click_count
        )


# Entry point
if __name__ == "__main__":
    config = {
        'redis_host': 'localhost',  # Change as necessary
        'redis_port': 6379           # Change as necessary
    }
    app = ShortlyApp(config)
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app.dispatch_request)
