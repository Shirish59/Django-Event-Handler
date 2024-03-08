from django.shortcuts import get_object_or_404, render
from .models import Event
from .models import RecentEvent
# Create your views here.
def home(request):
    pics=Event.objects.all()
    rimage = RecentEvent.objects.all()
    return render(request, 'event.html', {"pics": pics, "rimage": rimage})

def image_detail(request, image_id):
    image = get_object_or_404(Event, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})

def recent_image_detail(request, image_id):
    recent_image = get_object_or_404(RecentEvent, pk=image_id)
    return render(request, 'recent_image_detail.html', {'recent_image': recent_image})