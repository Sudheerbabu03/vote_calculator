from django.shortcuts import render

# Create your views here.
def vote(request):
    return render(request,'votecheck.html')
def vote_check(request):
    res=''
    num=request.POST.get('num')
    if request.method=='POST':
        if num is None:
            res='Pls enter age '
        try:
            age=int(num)    
            if age>=18:
                res='You are eligible for vote'
            else:
                res='You are not eligible for vote' 
        except ValueError:
            res='invalid input pls enter age'        

    return render(request,'votecheck.html',{'num':num,'res':res})    
def calci(request):
    return render(request,'calculator.html')