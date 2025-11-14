from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def note_list(request):
    # 公開フィード（owner is NULL）
    notes = Note.objects.filter(owner__isnull=True).order_by('-id')
    return render(request, 'notes/list.html', {'notes': notes, 'can_delete': False})

@login_required
def note_list_me(request):
    notes = Note.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'notes/list.html', {'notes': notes, 'can_delete': True})

@login_required
def note_new(request):
    if request.method == 'POST':
        Note.objects.create(owner=request.user,
        title=request.POST['title'],
        content=request.POST.get('content',''))
        messages.success(request, 'メモを作成しました。')
        return redirect('note_list_me')
    return render(request, 'notes/form.html')

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    note.delete()
    messages.success(request, '削除しました。')
    return redirect('note_list_me')
