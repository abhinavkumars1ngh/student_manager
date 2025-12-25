from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def add_note(request):
    Note.objects.create(
        user=request.user,
        content=request.POST['content']
    )
    return redirect('dashboard')

@login_required
def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect('dashboard')