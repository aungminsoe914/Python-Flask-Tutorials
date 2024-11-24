
import functools
# ? blueprints and views (ပုံကြမ်း နှင့် အမြင်များ ကိုသက်မှတ်ခြင်း)

from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for
)

from werkzeug.security import check_password_hash,generate_password_hash
from flaskr.db import get_db
#? flaskrဆိုတဲ့ app ရဲ့ db ဆိုတဲ့ python file app ရဲဲ get_db ဆိုတဲ့ function ကိုခေါ်သုံးမှာ


bp = Blueprint('auth',__name__,url_prefix='/auth')
# ! Blueprint သည် Flask app ကို module-wise ခွဲထုတ်ရန်အသုံးပြုတဲ့ feature တစ်ခုဖြစ်ပြီး code structure ကို modular and reusable အဖြစ်စီစဉ်နိုင်စေသည်။

# ? blueprint name ကို auth လို့သက်မှတ်တယ်။ 
# ? သက်မှတ်တာတော့ မှန်တယ် ဒါပေမဲ့ ဘယ်မှာ သက်မှတ်ထားတယ်သိဖို့ (location)
# ? __name__ ဆိုပြီး second argument အနေနဲ့ ဘယ်မှာရှိလဲသိအောင်လုပ်ပေးလိုက်တယ်။ !module-wise!
# ? url_prefix က ဒီပုံကြမ်းနဲ့ သက်ဆိုင်တဲ့ url တွေကိုကိုယ်စားပြူတယ်
# # url_prefix='/auth':

# ဒီ Blueprint နဲ့ သက်ဆိုင်တဲ့ URL တွေအားလုံးကို /auth prefix ထည့်ပေးထားပါတယ်။
# ဥပမာ login route တစ်ခုတည်ဆောက်ရင်, URL က /auth/login လို့ဖြစ်မယ်။
# ! blueprint ကို app factory ထဲမှာကြေငြာဖို့လိုပါသေးတယ်
# ! system တခုလုံးက သိဖို့ ပါ app.register_blueprint().  ကိုသုံးပါ 






