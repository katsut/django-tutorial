from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from event.models import Choice, Event
from logging import getLogger

logger = getLogger(__name__)


def index(request):
    events = Event.objects.all()
    return render(request, "event/index.html", {"events": events})


def create(request):
    name = request.POST["name"]
    datelist = request.POST["datelist"]
    event = Event(name=name, description="test")
    event.save()
    choices = Choice.objects.bulk_create(
        [Choice(event=event, date=date) for date in datelist.split("\n")]
    )
    logger.info(event)
    logger.info(choices)
    return HttpResponseRedirect(reverse("event:index"))


def edit(request, event_id):
    event = Event.objects.get(id=event_id)
    datelist = []
    for choice in event.choices.all():
        datelist.append(choice.date)

    return render(
        request, "event/edit.html", {"event": event, "datelist": "\n".join(datelist)}
    )


def update(request, event_id):
    event = Event.objects.get(id=event_id)
    event.name = request.POST["name"]
    event.description = request.POST["description"]
    event.published = request.POST["published"]
    datelist = request.POST["datelist"]
    event.save()

    choices = event.choices.all()
    for choice in choices:
        Choice.delete(choice)

    Choice.objects.bulk_create(
        [Choice(event=event, date=date) for date in datelist.split("\n")]
    )
    return HttpResponseRedirect(reverse("event:index"))
