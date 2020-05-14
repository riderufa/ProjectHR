from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

import redis
import pickle
# import os

from .forms import PollForm, PollSetForm, KitForm
from .models import Poll, UserProfile, Question, CheckedPoll

"""
Контроллеры опроса
"""

cache = redis.Redis(host=settings.REDIS_URL, port=6379)
# cache = redis.Redis(host=REDIS_URL, port=27519)
# cache = redis.from_url(os.environ.get("REDIS_URL"))
# r = redis.from_url(os.environ.get("REDIS_URL"))

# class PollList(SuccessMessageMixin, LoginRequiredMixin, ListView):  
class PollList(LoginRequiredMixin, ListView):  
    """
    Список опросов
    """
    model = Poll
    template_name = 'poll/poll/poll_list.html'
    context_object_name = "polls"

    def get_queryset(self):
        current_user = UserProfile.objects.filter(user=self.request.user).first()
        if current_user and current_user.type_user == 2: # Список опросов по конкретному пользователю
            return Poll.objects.filter(user__user=self.request.user).prefetch_related('user')
        return Poll.objects.all().prefetch_related('user').prefetch_related('checked_poll')

    # Добавляем в контекст данные из редис для контроля времени
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # try:
        #     cache.get(f'pu{self.request.user.pk}')
        # except UnicodeError:
        #     poll_pk = ''
        # else:
        #     poll_pk = cache.get(f'pu{self.request.user.pk}')
        poll_pk = cache.get('pu' + str(self.request.user.pk))
        ttl_poll = 0
        if poll_pk:
            try:
                cache.ttl(f'p{pickle.loads(poll_pk)}u{self.request.user.pk}time')
            except UnicodeError:
                ttl_poll = 0
            else:
                ttl_poll = cache.ttl(f'p{pickle.loads(poll_pk)}u{self.request.user.pk}time')
            # ttl_poll = cache.ttl(f'p{pickle.loads(poll_pk)}u{self.request.user.pk}time')
            context['new_poll_pk'] = pickle.loads(poll_pk)
        context['ttl_poll'] = ttl_poll
        return context


class PollDetail(LoginRequiredMixin, DetailView):
    """
    Подробная информация опроса
    """
    model = Poll
    template_name = "poll/poll/poll_details.html"
    queryset = Poll.objects.all().prefetch_related('questions')


class PollCreate(LoginRequiredMixin, CreateView):
    """
    Создание опроса
    """
    template_name = 'poll/poll/poll_create.html'
    form_class = PollForm
    success_url = reverse_lazy('poll:index')

    # Инициализация поля опроса текущим администратором
    def get_initial(self, *args, **kwargs):
        initial = super(PollCreate, self).get_initial(**kwargs)
        initial['admin'] = UserProfile.objects.get(user=self.request.user)
        return initial


class PollEdit(LoginRequiredMixin, UpdateView):
    """
    Редактирование опроса
    """
    template_name = 'poll/poll/poll_edit.html'
    model = Poll
    form_class = PollForm
    success_url = reverse_lazy('poll:index')


class PollSet(LoginRequiredMixin, UpdateView):
    """
    Привязка опроса к конкретному пользователю
    """
    template_name = 'poll/poll/poll_edit.html'
    model = Poll
    form_class = PollSetForm
    success_url = reverse_lazy('poll:index')


class PollDelete(LoginRequiredMixin, DeleteView):
    """
    Удаление опроса
    """
    template_name = 'poll/poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('poll:index')


# class PollUserList(LoginRequiredMixin, ListView):  
#     """
#     """
#     model = Poll
#     template_name = 'poll/poll/poll_list.html'
#     context_object_name = "polls"
