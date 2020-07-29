from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import PictureForm


def image_view(request):
    if request.method == 'POST':
        user_pic = PictureForm(request.POST, request.FILES)
        if user_pic.is_valid():
            user_pic.save()

            return HttpResponseRedirect('thanks')
    else:
        user_pic = PictureForm()
    return render(request, 'client/image_form.html', {'user_pic': user_pic})


def success(request):
    return HttpResponse('successfully uploaded')

