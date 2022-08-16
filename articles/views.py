from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article, Comment
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# Create your views here.

class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'ArticlesList'
    login_url = 'login'

class ArticlesDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article-detailed.html'
    context_object_name = 'Article'
    login_url = 'login'


class ArticlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article-update.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ArticlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('articles')

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request,*args,**kwargs)
    
class CommentsCreateView(CreateView):
    model = Comment
    template_name = 'article_detailed.html'
