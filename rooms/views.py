from django.views.generic import ListView, DetailView

from . import models

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    painate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

"""

    function based view
    
    ---
    if you want this function,
    change file name (templates/rooms/room_detail.html -> templates/rooms/detail.html)
    ---
    
from django.http import Http404
from django.shortcuts import render

def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", {'room': room})
    except models.Room.DoesNotExist:
        raise Http404()
        
"""
class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
