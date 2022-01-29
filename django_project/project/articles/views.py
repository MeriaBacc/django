from multiprocessing import context
from unittest import result
from django.shortcuts import render

from .models import Article

# Create your views here.
def article(request):
    result = Article.object.all()
    context = {"listearticle":result}
    return render(request, 'articles/article.html',context)
