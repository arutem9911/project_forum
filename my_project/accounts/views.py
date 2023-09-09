from django.core.paginator import Paginator
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import views, login, get_user_model
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accounts.models import User


class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main_page')


class LogoutView(views.LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.GET.get(
            'next',
            self.request.POST.get(
                'next',
                reverse_lazy('all_topics')
            )
        )


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user/detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        topics = self.object.topics.order_by('created_at')
        comments = self.object.comments.order_by('created_at')
        paginator = Paginator(
            object_list=topics,
            per_page=self.paginate_related_by,
            orphans=self.paginate_related_orphans
        )
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs |= {
            'page_obj': page,
            'topics': page.object_list,
            'is_paginated': page.has_other_pages()
        }
        return super().get_context_data(**kwargs)



