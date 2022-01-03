from django.shortcuts import render
from .models import Post_0, Post_1, Post_2, Post_3, Post_4, Post_5
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


@login_required
@permission_required('main.view_post_0', raise_exception=True)
def main(request):
    context = {'info_0': Post_0.objects.all(), 'info_1': Post_1.objects.all(),
               'info_2': Post_2.objects.all(), 'info_3': Post_3.objects.all(),
               'info_4': Post_4.objects.all(), 'info_5': Post_5.objects.all(),
              }
    return render(request, 'main/main.html', context)


class PostListView0 (PermissionRequiredMixin, generic.ListView, APIView):
    permission_classes = (HasAPIKey,)
    permission_required = 'main.view_post_0'
    model = Post_0
    context_object_name = 'info_0'
    template_name = 'main/form0.html'
    queryset = Post_0.objects.all()


class PostListView1 (PermissionRequiredMixin, generic.ListView):
    permission_required = 'main.view_post_1'
    model = Post_1
    context_object_name = 'info_1'
    template_name = 'main/form1.html'
    queryset = Post_1.objects.all()


class PostListView2 (PermissionRequiredMixin, generic.ListView):
    permission_required = 'main.view_post_2'
    model = Post_2
    context_object_name = 'info_2'
    template_name = 'main/form2.html'
    queryset = Post_2.objects.all()


class PostListView3 (PermissionRequiredMixin, generic.ListView):
    permission_required = 'main.view_post_3'
    model = Post_3
    context_object_name = 'info_3'
    template_name = 'main/form3.html'
    queryset = Post_3.objects.all()


class PostListView4 (PermissionRequiredMixin, generic.ListView):
    permission_required = 'main.view_post_4'
    model = Post_4
    context_object_name = 'info_4'
    template_name = 'main/form4.html'
    queryset = Post_4.objects.all()


class PostListView5 (PermissionRequiredMixin, generic.ListView):
    permission_required = 'main.view_post_5'
    model = Post_5
    context_object_name = 'info_5'
    template_name = 'main/form5.html'
    queryset = Post_5.objects.all()