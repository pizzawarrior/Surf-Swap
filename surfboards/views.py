from django.shortcuts import render
from surfboards.models import Surfboard, Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.
# Show list of surfboards
@login_required(login_url="/accounts/login/")
def surfboard_list(request):
    surfboards = Surfboard.objects.filter(owner=request.user)
    context = {'surfboards': surfboards}
    return render(request, 'surfboards/list.html', context)
