from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
def contact(request):
    return render(request, 'personal/basic.html',{'content':['my phone no 12344567899999999 ']})
