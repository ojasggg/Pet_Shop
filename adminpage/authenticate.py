from django.shortcuts import redirect
from Home.models import Registered
from django.contrib import messages

class Authentication:
    def valid_user(function):
        def wrap(request):
            try:
                Registered.objects.get(username = 'ojasggg' ,password = 'Kathmandu123')
                return function(request)

            except:
                messages.warning(request,'Please Login First')
            return redirect('/adm/login/')
        return wrap