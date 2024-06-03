from django.shortcuts import get_object_or_404, render
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect, HttpResponse
from django.db.utils import IntegrityError

from .models import Posts

# Create your views here.

def index(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'fetch/index.html')
    if request.method == "POST":
        import json
        data = json.loads(request.body.decode("utf-8"))
        value = get_object_or_404(Posts, pk=data["id"])
        print(f"{value = }")
        if value is not None:
            return render(request, "fetch/index.html", {'error': True})
        Posts.objects.create(**data)
        return HttpResponseRedirect("success")
        # try:
        #     Posts.objects.create(**data)
        # except IntegrityError:
        #     return render(request, 'fetch/index.html', {
        #         "error": "Already created"
        #     })
    return HttpResponseRedirect('success')


def success(request):
    posts = Posts.objects.all()
    return render(request, 'fetch/success.html', {"posts": posts})