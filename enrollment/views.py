from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import SessionModelForm
from .models import Session

# CRUD
# GET -> Retrieve / List
# POST -> Create / Update / DELETE
# Create Retrieve Update Delete

def session_list_view(request):
    # list out objects 
    # could be search
    qs = Session.objects.all() # queryset -> list of python object
    # if request.user.is_authenticated:
    #     my_qs = Session.objects.filter(user=request.user)
    #     qs = (qs | my_qs).distinct()
    context = {'sessions': qs}
    print(context)
    return render(request, 'enrollment/session_list.html', context)


# @login_required
@staff_member_required
def session_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = SessionModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = SessionModelForm()
    context = {'form': form}
    return render(request, 'enrollment/session_create.html', context)

def session_detail_view(request, code):
    print(code)
    session = get_object_or_404(Session, code=code)
    context = {"session": session}
    return render(request,'enrollment/session_detail.html', context)

@staff_member_required
def session_update_view(request, code):
    session = get_object_or_404(Session, code=code)
    form = SessionModelForm(request.POST or None, instance=session)
    if form.is_valid():
        form.save()
    context = {"title": f"Update {session.name}", "form": form}
    return render(request, 'enrollment/session_create.html', context)


@staff_member_required
def session_delete_view(request, code):
    session = get_object_or_404(Session, code=code)
    if request.method == "POST":
        session.delete()
        return redirect("/enrollment/sessions")
    context = {"session": session}
    return render(request, 'enrollment/session_delete.html', context)









