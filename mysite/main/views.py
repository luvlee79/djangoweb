from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    #templates폴더 안에있는 폴더 및 html파일의 경로를 설정
    return render(request,'main/index.html')

def notice(request):
    noticelist = Notice.objects.all()
    return render(request,'main/notice_list.html', {'noticeList':noticelist})

def notice_view(request,pk):
    notice = Notice.objects.get(pk=pk)
    return render(request, 'main/notice_view.html', {'notice':notice})