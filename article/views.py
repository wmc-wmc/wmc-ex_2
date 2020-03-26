from django.shortcuts import render
from .models import Text
# Create your views here.
def index(request):
    texts= Text.objects.all()
    return render(request,"index.html", locals())


def subject(request):
	subject = request.GET.get('s', None)
	if subject is None:
		texts = Text.objects.filter(enable=True)
	else:
		texts = Text.objects.filter(enable=True, subject=subject)

	print(texts)
	return render(request, "subjects.html", locals())


