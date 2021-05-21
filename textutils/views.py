#i have created this file-suraj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    # check check box value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countingcharacter=request.POST.get('countingcharacter','off')
    #check with check box on
    if removepunc=="on":

    #analyzed=djtext
        punctuations='''!@#$%^&*(){},<>./?~();:'"\|'''
        analyzed=" "
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext=analyzed  # override kardiya after analyzation
        #return render(request,'analyze.html',params)

    if(fullcaps=='on'):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params={'purpose':'change to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char

        params={'purpose':'removed New Line','analyzed_text':analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed=""
        for index ,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params ={'purpose':'remove extraspace','analyzed_text':analyzed}
        djtext=analyzed

    if(countingcharacter == "on"):
        count=0
        analyzed=""
        for char in djtext:
            if len(djtext)>0:
                print("the charcater count is" +str(len(djtext)))
                count+=1
        params={'purpose':'count characters','analyzed_text':count}
        djtext=analyzed
    if(removepunc !="on",newlineremover!="on",extraspaceremover!="on",countingcharacter!="on"):
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")






