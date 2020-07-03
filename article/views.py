from django.shortcuts import render
from .models import Text, Tag, Type
from django.contrib.auth.decorators import login_required
from article.forms import ArticleForm
from datetime import datetime, timedelta

# Create your views here.

month_en = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def index(request):
    now = datetime.now()
    year = now.year
    month = month_en[now.month - 1]
    week_days = now - timedelta(days=7)
    texts= Text.objects.filter(enable=True, uploadtime__gte=week_days)
    for text in texts:
    	text.month = month_en[text.uploadtime.month - 1]
    	text.day = text.uploadtime.day
    	if len(text.text) > 255:
    		text.text = text.text[:255] + '...'

    return render(request,"index.html", locals())


def tag(request):
	name = request.GET.get('tag', None)
	if tag is None:
		texts = Text.objects.filter(enable=True)
	else:
		texts = Text.objects.filter(enable=True, tag__name=name)

	print(texts)
	return render(request, "tag.html", locals())

def type(request):
	name = request.GET.get('type', None)
	if type is None:
		texts = Type.objects.filter(enable=True)
	else:
		texts = Type.objects.filter(enable=True, type__name=name)
	print(texts)
	return render(request, "type.html", locals())

@login_required
def upload_article(request):
	success = None
	tags = Tag.objects.all()

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



