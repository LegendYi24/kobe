from django.db.models import F, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
num_to_client = ['内科','五官科','神经科','骨科','分泌科','外科']
# Create your views here.
def index_views(request):
    return render(request,'index.html')

def doc_login_views(request):
    # 当请求方式为GET时
    if request.method == 'GET':
        form = Doc_Login_Form()
        return render(request, 'doc_login.html', locals())
    else:
        # 当请求方式为post时，用表单接受医生的登录请求
        account = request.POST['account']
        pwd = request.POST['pwd']
        try:
            res = Doctors.objects.get(account=account,upwd=pwd)
        except:
            # 没有查询出数据，说明账号或密码错误
            errMsg = '登录失败'
            form = Doc_Login_Form()
            return render(request, 'doc_login.html', locals())
        # 成功查询出记录，进入医生主页面
        client_num = int(res.client)
        client_name = num_to_client[client_num-1]
        uname = res.uname
        # 设置session信息
        request.session['uaccount'] = account
        request.session['doc_name'] = res.uname
        request.session['doc_client_num'] = client_num
        return render(request,'doc_index.html',locals())

def doc_loginout_views(request):
    if 'uaccount' in request.session and 'doc_name' in request.session:
        # 获取该医生负责的科室,清空该科室的挂号等待队列
        client_num = request.session['doc_client_num']
        Line.objects.filter(client=client_num).delete()
        # 删除该医生的session信息
        del request.session['uaccount']
        del request.session['doc_name']
    else:
        print('没有获取到session信息')
    return render(request,'index.html')


def pat_login_views(request):
    if request.method == 'GET':
        form = Pat_Login_Form()
        return render(request, 'pat_login.html', locals())
    else:
        # 病人通过表单提交挂号请求
        client_num = int(request.POST['client_num'])
        name = request.POST['name']
        phone = request.POST['phone']
        id = request.POST['id']
        name = request.POST['name']
        # 储存病人的session信息
        request.session['pat_name'] = name
        request.session['pat_phone'] = phone
        request.session['uid'] = id
        request.session['pat_client_num'] = client_num
        client_name = num_to_client[client_num - 1]
        try:
            # 若病人的id在Line表中，代表他已经挂号
            res = Line.objects.get(pat_id=id)
        except:
            # 没有查询到数据，说明该用户可以挂号
            # 先将用户的挂号信息存在挂号表Line中
            Line.objects.create(pat_name = name,pat_id=id,pat_phone=phone,client=client_num)
            # 用户进入挂号成功的主界面
            return render(request, 'pat_index.html', locals())
        # 查询到数据，说明用户已挂号,进入到病人的主界面
        return render(request, 'pat_index.html', locals())

def cancel_login_views(request):
    id = request.session['uid']
    #将此病人的挂号信息从Line表中删除
    pat = Line.objects.filter(pat_id=id)
    num = pat.delete()
    if num[0] == 1:
        # 删除病人的session信息
        del request.session['pat_name']
        del request.session['uid']
        del request.session['pat_phone']
        del request.session['pat_client_num']
        return render(request,'index.html')
    else:
        errMsg = '服务异常，请稍后重试'
        return pat_login_views(request)

def query_line_views(request):
    client_num = request.session['pat_client_num']
    client_name = num_to_client[client_num-1]
    line_list = Line.objects.filter(client=client_num)
    line_num = len(line_list)
    return render(request,'pat_index.html',locals())

def show_line_views(request):
    # 获取医生的基本信息
    client_num = request.session['doc_client_num']
    uname = request.session['doc_name']
    client_name = num_to_client[client_num - 1]
    line_list = Line.objects.filter(client=client_num)
    # 当前该科室的挂号总人数
    line_num = len(line_list)
    if line_num:
        # 如果查询结果不为空,获取当前就诊病人的信息，储存在session信息中
        now_pat = line_list[0]
        now_pat_name = line_list[0].pat_name
        now_pat_id = line_list[0].pat_id
        now_pat_phone = line_list[0].pat_phone
        request.session['now_pat_name'] = now_pat_name
        request.session['now_pat_id'] = now_pat_id
        request.session['now_pat_phone'] = now_pat_phone
        return render(request,'doc_index.html',locals())
    else:
        # 如果查询结果为空
        line_num = '目前没有病人等待就诊'
        return render(request,'doc_index.html',locals())

def next_pat_views(request):
    # 先得到当前医生的信息，方便返回
    client_num = int(request.session['doc_client_num'])
    client_name = num_to_client[client_num - 1]
    uname = request.session['doc_name']
    # 从医生session中获取当前病人的id
    pat_id = request.session['now_pat_id']
    res = Line.objects.filter(pat_id = pat_id).delete()
    if res:
        # delete语句执行成功，返回下一位病人的信息
        client_num = request.session['doc_client_num']
        now_pat = Line.objects.filter(client = client_num)
        if len(now_pat):
            # 如果还有病人等待就诊
            # 更新医生session中的当前病人信息
            request.session['now_pat_name'] = now_pat[0].pat_name
            request.session['now_pat_id'] = now_pat[0].id
            request.session['now_pat_phone'] = now_pat[0].pat_phone
            return render(request,'doc_index.html',locals())
        else:
            # 当前没有病人等待就诊
            request.session['now_pat_name'] = '目前没有病人'
            request.session['now_pat_id'] = ''
            request.session['now_pat_phone'] = ''
            return render(request,'doc_index.html',locals())
    else:
        # delete语句没有执行
        # 一般来说不会出现这种情况
        return render(request,'doc_index.html',locals())


def about_views(request):
    return render(request,'about.html')

def team_views(request):
    return render(request,'team.html')






