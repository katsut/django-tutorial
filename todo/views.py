
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from todo import models


def index(request):
    # データを撮ってくる
    all_todo = models.Todo.objects.all()
    # htmlにわたすデータ
    context = {
        'todos': all_todo
    }
    return render(request, 'index.html', context)

def create(request):
    # データを登録
    title = request.POST.get('title')
    new_todo = models.Todo()
    new_todo.title = title
    new_todo.save()
    return HttpResponseRedirect(reverse("todo:index"))


def edit(request, todo_id):
    target_todo = models.Todo.objects.get(id=todo_id)
    context = {
        'todo': target_todo
    }
    return render(request, 'edit.html', context)

def update(request, todo_id):
    # 今のデータを取得
    target_todo = models.Todo.objects.get(id=todo_id)
    
    # データを登録
    target_todo.title = request.POST.get('title')
    target_todo.save()
    return HttpResponseRedirect(reverse("todo:index"))


def delete(request, todo_id):
    target_todo = models.Todo.objects.get(id=todo_id)
    target_todo.delete()
    return HttpResponseRedirect(reverse("todo:index"))
