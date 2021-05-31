from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Post
from .serializers import PostSerializer


def new_post(request):
    return render(request, template_name='blog/add_post.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def update_post_new(request, id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data, template_name='blog/update_post.html',)