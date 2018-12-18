from django.shortcuts import render,redirect,loader
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from .models import *
from django.core.urlresolvers import reverse
from hashlib import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import  StringIO,BytesIO
import random,re

from datetime import datetime
from .user_decorator import *
# Create your views here.
from df_goods.models import GoodsInfo
#用户注册

def register(request):
    return render(request,"df_user/register.html",{"title":"用户注册"})
#用户注册保存

def register_handle(request):
    post= request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail=post.get('uemail')
    if pwd !=cpwd:
        return redirect("/user/register/")

    user=UserInfo()
    user.uname=uname
    user.upwd=sha1(pwd.encode('utf-8')).hexdigest()
    user.uemail=uemail
    user.save()
    #注册成功，跳转登录页面
    return redirect('/user/login/')

#验证用户是否存在
def register_exist(request):
    uname=request.GET.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({"count":count})

#用户登录
def login(request):
    uname=request.COOKIES.get('cook','')
    print("###########################")
    print(uname)
    context={'title':'用户登录','error_name':'0','erro_pwd':'0','uname':uname}
    return render(request,"df_user/login.html",context)
#用户登录验证
# def login(func):
#     def login_fun(request,*args,**kwargs):
#         if request.session.has_key('user_id'):
#             return func(request,*args,**kwargs)
#         else:
#             red = HttpResponseRedirect('/user/login')
#             red.set_cookie('url',request.get_full_path())
#             return red
#         return login_fun

def login_handle(request):
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    upwd=sha1(upwd.encode("utf-8")).hexdigest()
    print(upwd)
    cook=post.get('cook')
    users = UserInfo.objects.filter( uname=uname,upwd=upwd)
    print(users)
    if len(users) !=0:
        if upwd==users[0].upwd:
            url=request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            red.set_cookie('url',max_age=-1)
            request.session['currentUser']=uname
            # print(uname)
            # # 写cookie
            # t1 = loader.get_template('df_goods/index.html')
            # requestcontext=RequestContext(request)
            # response=HttpResponseRedirect(reverse('user:goods'))
            # cook = request.POST.get('cook')
            if cook !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['uname']=uname
            return red
            #     HttpResponseRedirecunamet(reverse('user:goods'))
            #     # response = render(request,"df_goods/index.html",{'uname':uname})
            #     print(response)
            #     response.set_cookie("cook",uname,max_age=10000)
            # return response
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname}
            return render(request, "df_user/login.html", context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname}
        return render(request,"df_user/login.html",context)


#商品展示
def user_goods(request):
    return redirect(reverse('goods:index'))


#用户中心

@logins
def user_center_info(request):

    users=UserInfo.objects.get(id=request.session['user_id'])
    # uname = UserInfo.objects.get(id=request.session['user_id']).uname
    goods_list=[]
    goods_ids = request.COOKIES.get('goods_ids','')
    if goods_ids !='':
        goods_id = re.findall("(\d+).*",goods_ids)[0]
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context={
        "title":"用户中心",
        "user":users,
        "goods_list":goods_list
    }
    return render(request,"df_user/user_center_info.html",context)

@logins
def user_center_order(request):
    return render(request,"df_user/user_center_order.html")

@logins
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    print(user)
    if request.method == 'POST':
        post=request.POST
        user.user=post.get('user')
        user.uaddress=post.get('uaddress')
        user.uzipcode=post.get('uzipcode')
        user.uphone = post.get('uphone')
        user.save()

    return render(request,"df_user/user_center_site.html",{'user':user})
def user_insert(request):
    return render(request,"df_user/user_insert.html")
def user_update(request):
    return render(request, "df_user/user_update.html")
def logout(request):
    request.session.flush()
    return redirect('/user/user_goods/')

# 验证码生成
def verification(request):
    width = 120
    height = 30
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('/usr/share/fonts/truetype/padauk/Padauk.ttf',26)
    draw = ImageDraw.Draw(image)
    #添加噪点
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor1())
    #设置验证码格式
    codes = ''
    for t in range(4):
        code = rndChar()
        codes += code
        draw.text((30*t + 5,0),code,font=font,fill=rndColor2())
    #images = images.filter(ImageFilter.BLUR)

    request.session['codes'] = codes
    request.session.set_expiry(0)

    f= BytesIO()
    image.save(f,'jpeg')
    return HttpResponse(f.getvalue(),'images/jpeg')

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def rndChar():
    return str1[random.randrange(0,len(str1))]
def rndColor1():
    return (random.randint(180, 255), random.randint(180, 255), random.randint(180, 255))
def rndColor2():
    return (random.randint(10, 200), random.randint(10, 200), random.randint(10, 200))
#   验证验证码是否正确
def check_userverification(request):
    # 获取输入的验证码
    userverification = request.GET.get('userverification')
    # 0不正确   1正确
    ret = '1'
    # 如果输入的验证码和session中的验证码不同，返回‘0’
    if request.session['codes'].upper() != userverification.upper():
        ret = '0'
    return HttpResponse(ret)
def result(request):
    #   验证码验证
    context = {}
    userverification = request.POST.get('userverification')
    if request.session['codes'].upper() == userverification.upper():
        user = UserInfo()
        user.uname = request.POST.get('username')
        user.upwd=request.POST.get('userpwd')
        user.uemail = request.POST.get('uemail')
        user.upwd = sha1(user.upwd.encode('utf-8')).hexdigest()
        user.save()

        return HttpResponseRedirect('/user/login')
    else:
        return HttpResponseRedirect('/user/register')

