from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('upperc', 'off')
    newline = request.POST.get('linerem', 'off')
    extra = request.POST.get('extraSpace', 'off')
    if removepunc == "on" and uppercase == "on":
        punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newline == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!= "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Line removal', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extra == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Line removal', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")