from django.shortcuts import render, redirect
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer




class View(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ORM коллекція
        self.queryset = Post.objects.all()
        self.serializer_class = PostSerializer

    def get(self, request, id='0'):
        if id == '0':
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response({'posts': serializer.data}, template_name='blog/index.html')
        else:
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, template_name='blog/post.html')

    def post(request: Request):
        account = request.user.username
        post = Post(author=account)
        serializer = PostSerializer(post, data=request.POST)
        if serializer.is_valid():
                serializer.save()
        post = Post(author=account, **serializer.data)
        post.save()
        return redirect('home')

    def put(request,id):
        account = request.user.username
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post, data=request.POST)
        if serializer.is_valid():
            serializer.save()
        post = Post(author=account,pk=id,**serializer.data)
        post.save()
        return redirect('get', 0)

    def delete(request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('home')





