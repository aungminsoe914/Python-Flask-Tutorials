def application(environ, start_response):
    # Set the HTTP response status and headers
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    
    # Return the response body as a list of bytes
    return [b'Hello World!']

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Create a WSGI server and bind it to localhost on port 8000
    httpd = make_server('localhost', 8000, application)
    print("Serving on http://localhost:8000/ ...")
    
    # Serve until process is killed
    httpd.serve_forever()
