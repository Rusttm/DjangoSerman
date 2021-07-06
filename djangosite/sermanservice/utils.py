from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        menu = topMenu.objects.all()
        submenu = topSubMenu.objects.all()
        context['menu'] = menu
        context['submenu'] = submenu
        return context
