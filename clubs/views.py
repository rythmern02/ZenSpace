from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Club, ClubMembership, ClubMessage
from .forms import ClubForm, ClubMessageForm
from django.contrib import messages as django_messages



def clubs(request):
    return render(request, 'clubs/club_list.html',{'club': clubs})

from django.urls import reverse

def club_detail(request):
    return render(request, "clubs/club_detail.html")
@login_required
def create_club_view(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            membership = ClubMembership(user=request.user, club=club)
            membership.save()
            return redirect('/clubs/club_detail', club_id=club.id)
    else:
        form = ClubForm()
    return render(request, 'clubs/create_club.html', {'form': form})

@login_required
def join_club_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if club.members.filter(id=request.user.id).exists():
        django_messages.warning(request, 'You are already a member of this club.')
    else:
        membership = ClubMembership(user=request.user, club=club)
        membership.save()
        django_messages.success(request, 'You have successfully joined the club.')
    return redirect('club_detail', club_id=club_id)



@login_required
def club_list(request):
    clubs = Club.objects.all()
    return render(request, "clubs/club_list.html", {'clubs': clubs})

