from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import UpdateView
from .models import rout


class rout_list_view(ListView):
    model = rout
    template_name = 'routList/routList.html'
    context_object_name = 'routs'
    ordering = ['-date_set']


class rout_detail_view(DetailView):
    model = rout

class rout_create_view(CreateView):
    model = rout
    fields = ['rout_name', 'grade', 'setter', 'date_set', 'climbed', 'date_climbed', 'attempts', 'notes']
    success_url = '/'

class rout_update_view(UpdateView):
    model = rout
    fields = ['rout_name', 'grade', 'setter', 'date_set', 'climbed', 'date_climbed', 'attempts', 'notes']
    success_url = '/'