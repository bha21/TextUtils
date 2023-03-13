# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a target="_blank" href= "https://www.icai.org/">www.icai.org</a> ''')

# def about(request):
#     return HttpResponse("about")

def index(request):
    return render(request,"index.html")
    # param = {'name':"Bhavesh",'place':"Bhayander"}
    # return render(request,"index.html",param)
    # return HttpResponse('''Home  <a  href= "removepunc">Remove punc</a> 
    #                              <a  href= "capitalizefirst">Capitalize first</a>
    #                              <a  href= "newlineremove">New line remove</a>
    #                              <a  href= "spaceremove">Space remove</a>
    #                              <a  href= "charcount">Char count</a>''')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    # analyzed = djtext
    if (removepunc == "on"):
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char      
        params = {'purpose':'Removed Punctuations',"Length_of_text":len(analyzed) ,'analyzed_text':analyzed}
        # params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase',"Length_of_text":len(analyzed),'analyzed_text':analyzed}
        # params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and  char != "\r":
                analyzed = analyzed + char   
        
        params = {'purpose':'Removed NewLine',"Length_of_text":len(analyzed),'analyzed_text':analyzed}
        # params = {'purpose':'Removed NewLine','analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    elif (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char   
        params = {'purpose':'Space remover',"Length_of_text":len(analyzed),'analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    elif (charcount=="on"):
        analyzed = ""
        for  char in djtext:
                analyzed = analyzed + char        
        params = {'purpose':'Removed NewLine',"Length_of_text":len(analyzed),'analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    else:
        return HttpResponse("ERROR")
# def capfirst(request):
#     return HttpResponse("<h1>Capitalize first</h1>  <a  href= "'http://127.0.0.1:8000/'">Back</a>")

# def newlineremove(request):
#     return HttpResponse("<h1>New Line Remove</h1>  <a  href= "'http://127.0.0.1:8000/'">Back</a>")

# def spaceremove(request):
#     return HttpResponse("<h1>Space remove</h1>  <a  href= "'http://127.0.0.1:8000/'">Back</a>")

# def charcount(request):
#     return HttpResponse("<h1>Char Count</h1>  <a  href= "'http://127.0.0.1:8000/'">Back</a>")
