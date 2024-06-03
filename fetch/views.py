from django.db.utils import IntegrityError
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Posts

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'fetch/index.html')
    
    def post(
            self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponse | JsonResponse:
        import json
        data = json.loads(request.body.decode("utf-8"))
        post, created = Posts.objects.get_or_create(**data)
        if created:
            return HttpResponseRedirect('success')
        return JsonResponse({
            'dataError': True,
            'id': post.id, # type: ignore
        })


def success(request):
    posts = Posts.objects.all()
    return render(request, 'fetch/success.html', {"posts": posts})