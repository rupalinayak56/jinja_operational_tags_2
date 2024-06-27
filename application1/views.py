from django.shortcuts import render

# Create your views here.
def style(request):
    d={"name":"Parshu","age":61}
    return render(request,"style.html",context=d)
