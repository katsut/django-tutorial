from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from event.models import Event
from logging import getLogger

logger = getLogger(__name__)


def index(request):
    events = Event.objects.all()
    return render(request, "event/index.html", {"events": events})


def create(request):
    name = request.POST["name"]
    event = Event(name=name, description="test").save()
    logger.info(event)
    return HttpResponseRedirect(reverse("event:index"))
