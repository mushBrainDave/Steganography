from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Message
from .forms import NameForm


def index(request):
    hidden_message_list = Message.objects.order_by('-id')[:5]
    return render(request, 'client/index.html', {'hidden_message_list': hidden_message_list})


class IndexView(generic.ListView):
    template_name = 'client/index.html'
    context_object_name = 'hidden_message_list'

    def get_queryset(self):
        return Message.objects.order_by('-id')[:5]


class DetailView(generic.DetailView):
    model = Message
    template_name = 'client/detail.html'


def message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'client/detail.html', {'message': message})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/client/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'client/name.html', {'form': form})
