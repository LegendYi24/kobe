from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import AreaInfo
from django.http import HttpResponse, JsonResponse

def area1(request):
    return render(request, 'area/area.html')


# 获取省数据
def province(request):
    provinceList = AreaInfo.objects.filter(aParent__isnull=True)
    print(provinceList)
    list1 = []
    for item in provinceList:
        list1.append([item.id, item.atitle])
    return JsonResponse({'data': list1})

# 获取市数据
def city(request, pid):
    print(pid)
    cityList = AreaInfo.objects.filter(aParent_id=pid)
    list1 = []
    for item in cityList:
        list1.append([item.id, item.atitle])
    return JsonResponse({'data': list1})


# 获取区县数据
def county(request, pid):
    print(pid)
    countyList = AreaInfo.objects.filter(aParent_id=pid)
    list1 = []
    for item in countyList:
        list1.append([item.id, item.atitle])
    return JsonResponse({'data': list1})