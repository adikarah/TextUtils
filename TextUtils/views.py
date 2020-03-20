# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:37:58 2020

@author: UPLC
"""

#This file is created by me-"Praveen"
from django.http import HttpResponse
from django.shortcuts import render


    
def index(request):
    
    return  render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #Get the text
    #djtext=request.GET.get('text','default')
    djtext=request.POST.get('text','default')
    
    #Check checkcase values
    #removepunc=request.GET.get('removepunc','off')
    removepunc=request.POST.get('removepunc','off')
    #fullcaps=request.GET.get('fullcaps','off')
    fullcaps=request.POST.get('fullcaps','off')
    #newlineremover=request.GET.get('newlineremover','off')
    newlineremover=request.POST.get('newlineremover','off')
    #extraspaceremover=request.GET.get('extraspaceremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    #charcount=request.GET.get('charcount','off')
    charcount=request.POST.get('charcount','off')
    
    
    #Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Converted into UpperCase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)    
    
    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'New lines removed','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)   

    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Extra spaces removed','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params) 

    if charcount=='on':
        #analyzed=""
        ans=str(len(djtext))
        params={'purpose':'Total characters are:','analyzed_text':analyzed + ans}
        
        #return render(request,'analyze.html',params)
    if removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on":
        return HttpResponse("Please Choose any operator!")
    
    '''else:
        return HttpResponse("Error")'''
    return render(request,'analyze.html',params)






'''def removepunc(request):
    #Get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc <a href='/'>back</a>")'''

'''def capfirst(request):
    return HttpResponse("capitalize first <a href='/'>back</a>")

def newlineremove(request):
    return HttpResponse("newline remove <a href='/'>back</a>")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount <a href='/'>back</a>")'''





