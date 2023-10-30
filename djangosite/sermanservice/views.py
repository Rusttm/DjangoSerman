from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import  *
from .forms import  *
from .utils import  *
import sys
#sys.path.insert(0, '/home/rusttm/Desktop/moisklad/MoiSklad')
# sys.path.insert(0, '/home/pi/Desktop/moisklad/MoiSklad')
# sys.path.insert(0, '/home/rusttm/telegrambot/MoiSklad')
sys.path.insert(0, '/home/rusttm/PycharmProjects/SermanBot/MoiSklad')

import run_reports


# Create your views here.


def home_view(request):
    if True:
        return render(request, 'sermanservice/index.html')
    return HttpResponse('<h1> Your home page </h1>')

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'sermanservice/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.gget_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))


def login_view(request):
    if True:
        return render(request, 'sermanservice/index.html')
    return HttpResponse('<h1> Your home page </h1>')

def top_menu_view(request, item_menu_id):
    list_par_in_menu = topMenu.objects.all()
    list_par_in_submenu = topSubMenu.objects.all()
    activeparam = item_menu_id
    activesub = 1
    context = {'topmenu':list_par_in_menu,
                'submenu':list_par_in_submenu,
                'activep': activeparam,
                'activesub': activesub}
    if True:
        return render(request, 'sermanservice/servicebase.html', context=context)
    return HttpResponse('<h1> Your home page </h1>')

def sub_menu_view(request, sub_item_menu_id):
    list_par_in_menu = topMenu.objects.all()
    list_par_in_submenu = topSubMenu.objects.all()
    activeparam_id = topSubMenu.objects.get(id=sub_item_menu_id).top.pk
    print('activeparam_id',activeparam_id)
    activeparam = topMenu.objects.get(id=activeparam_id).pk
    print('activeparam',activeparam)

    activesub = sub_item_menu_id
    context = {'topmenu':list_par_in_menu,
                'submenu':list_par_in_submenu,
                'activep': activeparam,
                'activesub': activesub}
    if True:
        return render(request, 'sermanservice/servicebase.html', context=context)
    return HttpResponse('<h1> Your home page </h1>')


def form_view(request):
    form = ReportForm(request.POST or None)
    comment = 'Nothing'
    answer_type_report = 'Nothing'
    if form.is_valid():
        answer = request.POST
        t = run_reports.report_forming(answer).report_data()
        #report_type = answer['type_report']
        print(t)
        #form = ReportForm()
        comment = t
        pass
    context = {
        'form': form,
        'comment': comment
    }
    return render(request, "sermanservice/my_form.html", context)


def pars_form_view(request):
    form = ParsingForm(request.POST or None)
    comment = 'Nothing'
    answer_type_report = 'Nothing'
    if form.is_valid():
        answer = request.POST
        t = run_reports.pars_forming(answer).report_data()
        #report_type = answer['type_report']
        print(t)
        #form = ReportForm()
        comment = t
        pass
    context = {
        'form': form,
        'comment': comment
    }
    return render(request, "sermanservice/my_parsing_form.html", context)

