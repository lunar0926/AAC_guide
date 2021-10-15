from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post

# XML 파싱
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def resources(request):
    # 문자열 포맷팅으로 변수를 입력받아서 xml링크에 넣기.
    # xml파일을 읽어서 파싱하기 - 태그값 가져오기
    
    # xml_file = ''
    # doc = ET.parse(xml_file)
    # #root 노드 가져오기
    # root = doc.getroot()


    return render(request, 'resources.html')


def community(request):
    posts = Post.objects.all()

    return render(request, 'community.html', {'posts':posts})


def detail(request, post_id):
    selected_post = Post.objects.get(pk=post_id)

    return render(request, 'detail.html', {'selected_post':selected_post})


def search(request):
    post_list = Post.objects.order_by('-id')
    search_keyword = request.GET.get('q','')
    # 해당 인풋에 적은 검색 키워드가 있으면
    if search_keyword:
        # title,content 에 search keyword 가 있는 post 오브젝트들만 가지고 와주세여
        post_list = post_list.filter(post_title__icontains = search_keyword)| post_list.filter(post_content__icontains = search_keyword)
        return render(request,'search.html',{'post_list':post_list})
    # 없으면 그냥 search.html render
    else:
        return render(request,'search.html')


def contact(request):
    return render(request, 'contact.html')


def conclusion(request):
    return render(request, 'conclusion.html')


def thank(request):
    return render(request, 'thank.html')
