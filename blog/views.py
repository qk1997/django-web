from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
# imaginary function to handle an uploaded file
from .import picturetochar
from .models import User


class UploadFileForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uname = form.cleaned_data['username']
            hImg = form.cleaned_data['headImg']
            u = User()
            u.username = uname
            u.headImg = hImg
            u.save()
            request.session['user_info'] = uname
            return HttpResponseRedirect('index/done/')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})


def result(request):
    uuu = User.objects.get(username=request.session['user_info'])
    return render(request, 'solvtion.html', {'user': uuu})
