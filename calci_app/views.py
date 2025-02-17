from django.shortcuts import render # type: ignore

# Create your views here.
def calci(request):
    return render(request,'calculator.html')
def display(request):
    n1=int(request.POST.get('txtnum1'))
    n2=int(request.POST.get('txtnum2'))
    op=request.POST.get('operation')
    if op=='Add':
        res=n1+n2
    elif op=='Sub':
        res=n1-n2 
    elif op=='Mul':
        res=n1*n2
    else:
        try:
            res=n1/n2 
        except:
            res='pls change value calculation is not possible'     
    return render(request,'calculator.html',{'txtnum1':n1,'txtnum2':n2,'res':res})     
def vote(request):
    return render(request,'votecheck.html')          