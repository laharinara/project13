from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'lahari','age':22,'course':['python','sql','web']}
    return render(request,'loop.html',context=d)
def url(request):
    d={'A':[1,2,3,4,5,6],'b':[54,32,86,56]}
    return render(request,'url.html',context=d)