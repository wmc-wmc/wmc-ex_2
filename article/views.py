from django.shortcuts import render
from .models import Text
# Create your views here.
def index(request):
    texts= Text.objects.all()
    return render(request,"index.html", locals())