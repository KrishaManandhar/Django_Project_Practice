from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'TextUtils.html')

def analyze(request):
    text_of_textarea = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')

    punctuations = '''!()-[]{};:'"\,<>.?/@#$%^&*_~'''
    analyzed = ""

    if removepunc == 'on':
      for char in text_of_textarea:
            if char not in punctuations:
                analyzed = analyzed + char
    else:
        return HttpResponse('Error')
    parameter = {'purpose':'remove punctuation','analyzed_text': analyzed}
    return render(request,'analyze.html',parameter)