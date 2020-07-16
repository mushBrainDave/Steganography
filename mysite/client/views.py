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


def message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'client/detail.html', {'message': message})


def hotel_image_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client/')
    else:
        form = NameForm()
    return render(request, 'client/image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

