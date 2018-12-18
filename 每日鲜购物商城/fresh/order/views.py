from django.shortcuts import render,redirect
from django.http import request
from df_user.models import UserInfo
from df_cart.models import CartInfo
from django.core.paginator import Paginator
from .models import *
from .user_decorator import logins
from django.db import transaction
from datetime import *
from df_goods.views import cart_count
# Create your views here.
#跳转订单页面
def order(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    print(user)
    cart_ids=request.GET.getlist('cart_ids')
    print(cart_ids)
    cart_ids2=[int(item) for item in cart_ids]
    print(cart_ids2)
    carts=CartInfo.objects.filter(id__in=cart_ids2)
    print(carts)
    cart_ids = ','.join(cart_ids)
    context={
        "carts":carts,
        "user":user,
        "cart_ids":cart_ids
    }
    return render(request,"order/place_order.html",context)

@logins
@transaction.atomic
def order_handle(request):

    tran_id = transaction.savepoint()
    cart_ids = request.POST.get('cart_ids')

    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
        order.oid = '%s%s' % (uid, now.strftime('%Y%m%d%H%M%S'))
        order.userinfo_id = uid
        order.odate = now
        order.oaddress = request.POST.get('address')
        order.ototal = 0
        order.save()

        cart_ids1 = [int(item) for item in cart_ids.split(',')]
        total = 0
        for id1 in cart_ids1:  # 遍历
            detail = OrderDetailInfo()  # 创建订单明细对象
            detail.orderinfo = order  # 设置订单明细对象的属性
            cart = CartInfo.objects.get(id=id1)  # 根据id获取购物车对象
            goods = cart.goodsinfo  # 获取此购物车商品对象
            if goods.gstock >= cart.count:  # 判断库存，如果库存大于购买数量
                goods.gstock = goods.gstock - cart.count  # 减少商品库存
                goods.save()  # 新增

                detail.goodsinfo = goods  # 设置订单明细对象的属性：商品
                detail.price = goods.gprice  # 设置订单明细对象的属性：价格
                detail.count = cart.count  # 设置订单明细对象的属性：数量
                detail.save()  # 新增

                total = total + goods.gprice * cart.count  # 计算总计
                cart.delete()  # 删除购物车数据
            else:  # 如果库存小于购买数量
                transaction.savepoint_rollback(tran_id)  # 回滚，到上一次的保存点
                return redirect('/cart/')  # 重定向到购物车页面

        order.ototal = total + 10  # 保存总价：商品总价+邮费
        order.save()  # 更新总价
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('异常:%s' % e)  # 打印异常，也可以记录到日志中
        transaction.savepoint_rollback(tran_id)  # 回滚，到上一次的保存点

    return redirect('/order/show/')


@logins
@transaction.atomic
def order_list(request,pindex):
    uname = request.session['currentUser']
    order_list = OrderInfo.objects.filter(userinfo_id=uname).order_by('-oid')
    paginator = Paginator(order_list, 2)
    if pindex == '':
        pindex = '1'
    page = paginator.page(int(pindex))

    context = {
        'title': '用户中心',
        'page_name': 1,
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'df_user/user_center_order.html', context)


def pay(request,oid):
    order = OrderInfo.objects.get(oid=oid)
    order.oispay = True
    order.save()
    context = {'order': order}
    return render(request, 'order/pay.html', context)

@logins
def show(request,pindex):
    user_id = request.session['user_id']
    order_list = OrderInfo.objects.filter(userinfo_id=user_id).order_by('-oid')
    paginator = Paginator(order_list, 2)
    if pindex == '':
        pindex = '1'
    page = paginator.page(int(pindex))

    context = {
        'title': '用户中心',
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'df_user/user_center_order.html', context)
def gert(request):
    return render(request,"order/pay.html")