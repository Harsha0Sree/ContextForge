# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Document


def home(request):
    return HttpResponse("knowledgebase")


def upload_document(request):
    if request.method == "POST":
        title = request.POST["title"]
        file = request.FILES["file"]
        Document.objects.create(title=title, file=file)
        return HttpResponse("success")
    return render(request, "upload.html")

