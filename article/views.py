from django.shortcuts import render
from .models import Text
from django.contrib.auth.decorators import login_required
from article.forms import ArticleForm


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


@login_required
def upload_article(request):
	success = None

	if request.method != 'POST':
		return render(request, 'upload.html', locals())

	form = ArticleForm(request.POST, request.FILES)

	if not form.is_valid():
		return render(request, 'upload.html', locals())

	article = form.save(commit=True)

	article.from_user = request.user
	article.save()

	success = "Success"

	return render(request, "upload.html", locals())



