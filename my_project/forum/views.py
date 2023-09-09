from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from forum.models import Topic, Comment
from .forms import SearchForm, TopicModelForm, CommentModelForm
from django.db.models import Q
from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class TopicsIndexView(ListView):
    template_name = 'topics/all_topics.html'
    context_object_name = 'topics'
    model = Topic
    ordering = ['created_at']
    paginate_by = 5
    paginate_orphans = 0
    page_kwarg = 'page'  # default 'page'

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(short_description__icontains=self.search_value)
            qs = qs.filter(query)
        return qs

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')

    def get_search_form(self):
        return SearchForm(self.request.GET)


class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = 'topics/create_topic.html'
    model = Topic
    form_class = TopicModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # return reverse('detail_project', kwargs={'id': self.object.id})
        return reverse('all_topics')


class DetailTopicView(DetailView):
    raise_exception = True
    template_name = 'topics/detail_topic.html'
    model = Topic
    context_object_name = 'topic'
    pk_url_kwarg = 'id'
    extra_context = {'form': CommentModelForm}

    def dispatch(self, request, *args, **kwargs):
        request.session['topic_id'] = kwargs.get('id')
        request.session['author_id'] = request.user.id
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            comments=self.object.comment.order_by('-created_at'),
            **kwargs
        )


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'comments/create_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_topic', kwargs={'id': self.object.topic.id})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/create_comment.html'
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.author_id = self.request.session.get('author_id')
        form.instance.topic_id = self.request.session.get('topic_id')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_topic', kwargs={'id': self.object.topic.id})
