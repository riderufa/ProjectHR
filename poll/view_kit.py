from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.contrib import messages

from .forms import KitForm, KitEditForm
# from .models import Poll, UserProfile, Question, Kit, CheckedPoll
from .models import Poll, Kit, Question
from .sender import post_save_kit, post_delete_kit


"""
Контроллеры связующей таблицы вопрос-опрос
"""

# Привязка сигналов
post_save.connect(post_save_kit, sender=Kit)
post_delete.connect(post_delete_kit, sender=Kit)


class KitList(LoginRequiredMixin, DetailView):  
    """
    Список элементов связующей таблицы
    """
    model = Poll
    template_name = 'poll/poll/kit_list.html'
    context_object_name = "poll"
    queryset = Poll.objects.all().prefetch_related('kitpoll').prefetch_related('kitpoll__question')
    

class KitCreate(LoginRequiredMixin, CreateView, SingleObjectMixin):
    """
    Создание элементов связующей таблицы
    """
    template_name = 'poll/kit/kit_create.html'
    form_class = KitForm
    model = Kit

    # Инициализация поля формы конкретным опросом
    def get_initial(self, *args, **kwargs):
        initial = super(KitCreate, self).get_initial(**kwargs)
        initial['poll'] = Poll.objects.get(pk=self.kwargs['pk'])
        return initial

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('poll:kit_list', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        """
        Проверка на суммарное время вопросов
        """
        poll = Poll.objects.prefetch_related('questions').get(pk=self.kwargs['pk'])
        result = poll.questions.aggregate(Sum('time_limit'))
        if result['time_limit__sum']:
            sum_time = result['time_limit__sum'] + form.instance.question.time_limit
        else:
            sum_time = form.instance.question.time_limit
        if sum_time > poll.time_limit:
            response = super().form_invalid(form)
            messages.add_message(self.request, messages.INFO, 'Суммарное время вопросов больше времени опроса. Замените вопрос или измените его время.', extra_tags='alert-danger')
            return response
        return super(KitCreate, self).form_valid(form)


class KitDelete(LoginRequiredMixin, DeleteView):
    """
    Удаление элементов связующей таблицы
    """
    template_name = 'poll/kit/kit_delete.html'
    model = Kit

    def get_success_url(self):
        return reverse_lazy('poll:kit_list', kwargs={'pk': self.object.poll.pk})


class KitEdit(LoginRequiredMixin, UpdateView):
    """
    Редактирование элементов связующей таблицы
    """
    template_name = 'poll/kit/kit_edit.html'
    model = Kit
    form_class = KitEditForm
    
    def get_success_url(self):
        return reverse_lazy('poll:kit_list', kwargs={'pk': self.object.poll.pk})
