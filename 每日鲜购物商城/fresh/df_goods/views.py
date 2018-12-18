from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from df_cart.models import CartInfo
from django.db.models import Sum


# Create your views here.
# 商品主页面
def index(request):
    typelist = TypeInfo.objects.all()

    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]

    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]

    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]

    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]

    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]

    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    type52 = typelist[0]

    context = {
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51, 'type52': type52,
        'cart_count': cart_count(request),
    }
    return render(request, 'df_goods/index.html', context)


# 商品详情
def detail(request, id):
    '''
        跳转到商品详情页面
    '''
    # 点击量的增加
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick + 1
    title = goods.gtypeinfo
    goods.save()
    news = goods.gtypeinfo.goodsinfo_set.order_by('-id')[0:4]
    context = {'g': goods,
               "news": news,
               "id": id,
               'title': title,
               'cart_count': cart_count(request)
               }
    response = render(request, 'df_goods/detail.html', context)
    goods_ids = request.COOKIES.get('goods_ids')
    print(goods_ids)
    if goods_ids != '':  # 判断是否有浏览记录，如果有继续浏览
        goods_ids1 = ",".split(goods_ids)  # 拆分为列表
        if goods_ids1.count(id) >= 1:  # 如果有商品记录，则删除
            goods_ids1.remove(id)
        goods_ids1.insert(0, id)  # 添加到第一个
        if len(goods_ids1) >= 6:  # 如果达到6个则删除最后一个，因为最近浏览是5个
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)  # 拼接为字符串
    else:
        goods_ids = int(id)  # 如果没有浏览记录，则直接加
    response.set_cookie('goods_ids', goods_ids)  # 写入cookie

    return response


# 查看更多
def list(request, id, pindex, sort):
    typeinfo = TypeInfo.objects.get(pk=int(id))
    print(typeinfo)
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == "1":
        goods_list = GoodsInfo.objects.filter(gtypeinfo_id=int(id)).order_by('-id')
    elif sort == "2":
        goods_list = GoodsInfo.objects.filter(gtypeinfo_id=int(id)).order_by('gprice')
    elif sort == "3":
        goods_list = GoodsInfo.objects.filter(gtypeinfo_id=int(id)).order_by('-gclick')
    paginator = Paginator(goods_list, 15)
    page = paginator.page(int(pindex))
    context = {
        "page": page,
        "paginator": paginator,
        "typeinfo": typeinfo,
        "sort": sort,
        "news": news,
        "cart_count": cart_count(request)
    }
    return render(request, 'df_goods/list.html', context)


# 搜索功能
def find(request):
    """
    模糊查询
    查询标题或者内容
    """
    keyword = request.GET.get("keyword", '').strip()
    sort = request.GET.get("sort", '1')
    pindex = request.GET.get('pindex', '1')
    goods_list = GoodsInfo.objects.filter(
        Q(gtitle__icontains=keyword) | Q(gcontect__icontains=keyword)
    )
    if sort == '1':
        goods_list = goods_list.order_by('-id')
    elif sort == "2":
        goods_list = goods_list.order_by('gprice')
    elif sort == "3":
        goods_list = goods_list.order_by('-gclick')
    news = GoodsInfo.objects.all().order_by('-id')[0:2]
    paginator = Paginator(goods_list, 15)
    page = paginator.page(pindex)
    context = {
        "page": page,
        "paginator": paginator,
        "sort": sort,
        "news": news,
        "keyword": keyword,
        'cart_count': cart_count(request)
    }
    return render(request, 'df_goods/find.html', context)


# 计算目前的购买数量
def cart_count(request):
    count = 0
    user_id = request.session.get('user_id')
    if user_id:
        ret = CartInfo.objects.filter(userinfo_id=user_id).aggregate(num=Sum('count'))
        count = ret['num']
        return count


# 抽奖
def luck(request):
    return render(request, "df_goods/luck.html")
