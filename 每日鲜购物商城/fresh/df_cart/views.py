from django.shortcuts import render,redirect
from .models import *
from .user_decorator import logins
from django.http import JsonResponse
from df_goods.views import cart_count
# Create your views here.
@logins
def cart(request):
    uid =request.session["user_id"]
    print(uid)
    carts=CartInfo.objects.filter(userinfo_id=uid)
    context={
        "carts":carts
    }

    return render(request,"df_cart/cart.html",context)
@logins
def add(request,gid,count):
    uid=request.session['user_id']
    print(uid)
    gid=int(gid)
    print(gid)
    count=int(count)
    carts=CartInfo.objects.filter(userinfo_id=uid,goodsinfo_id=gid)
    if len(carts)>=1:
        cart=carts[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.userinfo_id=uid
        cart.goodsinfo_id=gid
        cart.count=count
    cart.save()


    if request.is_ajax():
        count = cart_count(request)
        return JsonResponse({'count':count})
    else:
        # 重定向
        return redirect('/cart/')
def edit(request,cart_id,count):
    count1 = 1
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count
        cart.count = int(count)
        cart.save()
        data = {'flag': 1}
    except Exception as e:
        data = {'flag': count1}
    return JsonResponse(data)


def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk = int(cart_id))
        cart.delete()
        data = {'flag':1}
    except Exception as e:
        data = {'flag':0}
    return JsonResponse(data)

