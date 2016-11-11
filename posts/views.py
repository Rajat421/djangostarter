from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect, redirect
from django.http import HttpResponse

from .models import Posts
from .forms import PostForm


def post_create(request):
    forms= PostForm(request.POST or None)
    if forms.is_valid():
        instance=forms.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("posts:detail", kwargs={"id": instance.id}))
    context={
        "forms":forms
    }
    return render(request, "post_create.html", context)

def post_detail(request,id):
   # queryset = Posts.objects.get(id=id)
    queryset = get_object_or_404(Posts,id=id)
    context = {
        "object_list": queryset
    }
    return render(request,"post_detail.html",context)

def post_list(request):
    queryset = Posts.objects.all()
    context={
        "object_list" :queryset
    }
    return render(request,"posts_list.html",context)

def post_delete(request,id):
    queryset = get_object_or_404(Posts,id=id)
    queryset.delete()
    return redirect("posts:list")


def post_update(request,id):
   # queryset = Posts.objects.get(id=id)
    queryset = get_object_or_404(Posts,id=id)
    forms = PostForm(request.POST or None,instance=queryset)
    if forms.is_valid():
        instance = forms.save(commit=False)
        instance.save()
        print "hello"
        return HttpResponseRedirect(reverse("posts:detail", kwargs={"id":id}))

    context = {
        "object_list": queryset,
        "forms":forms
    }
    return render(request,"post_create.html",context)


# Create your views here.
