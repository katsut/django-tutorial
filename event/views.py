from django.http import HttpResponse, HttpResponseRedirect
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


def edit(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "event/edit.html", {"event": event})


def update(request, event_id):
    # TODO: implements
    logger.info("update")
    event = Event.objects.get(id=event_id)
    event.name = request.POST["name"]
    event.description = request.POST["description"]
    event.published = request.POST["published"]
    event.save()
    return HttpResponseRedirect(reverse("event:index"))
