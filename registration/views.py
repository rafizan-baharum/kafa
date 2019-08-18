from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import ApplicantModelForm
from .models import Applicant

# CRUD
# GET -> Retrieve / List
# POST -> Create / Update / DELETE
# Create Retrieve Update Delete

def applicant_list_view(request):
    # list out objects 
    # could be search
    qs = Applicant.objects.all().registered() # queryset -> list of python object
    # if request.user.is_authenticated:
    #     my_qs = Applicant.objects.filter(user=request.user)
    #     qs = (qs | my_qs).distinct()
    context = {'applicants': qs}
    return render(request, 'registration/applicant_list.html', context)


# @login_required
@staff_member_required
def applicant_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = ApplicantModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ApplicantModelForm()
    context = {'form': form}
    return render(request, 'registration/applicant_create.html', context)

def applicant_detail_view(request, mykid_no):
    print(mykid_no)
    applicant = get_object_or_404(Applicant, mykid_no=mykid_no)
    context = {"applicant": applicant}
    return render(request,'registration/applicant_detail.html', context)

@staff_member_required
def applicant_update_view(request, mykid_no):
    applicant = get_object_or_404(Applicant, mykid_no=mykid_no)
    form = ApplicantModelForm(request.POST or None, instance=applicant)
    if form.is_valid():
        form.save()
    context = {"title": f"Update {applicant.name}", "form": form}
    return render(request, 'registration/applicant_create.html', context)


@staff_member_required
def applicant_delete_view(request, mykid_no):
    applicant = get_object_or_404(Applicant, mykid_no=mykid_no)
    if request.method == "POST":
        applicant.delete()
        return redirect("/registration/applicants")
    context = {"applicant": applicant}
    return render(request, 'registration/applicant_delete.html', context)









