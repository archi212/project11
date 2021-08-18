from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':100,'b':500,'c': 800}
    return render(request,'hai.html',context=d)


