from http.client import HTTPResponse
from django.http import Http404, HttpResponse 
from django.shortcuts import redirect, render

from legal.forms import CaseEntryForm
from .models import CaseEntry ,CaseDetails
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'legal/index.html')

@login_required
def cases(request):
    """Show all the Cases"""
    cases = CaseEntry.objects.filter(owner = request.user).order_by('-date_added')
    context = {'cases':cases}
    return render(request,'legal/cases.html',context)                                                               

@login_required
def case(request,case_id):
    """Show details of the case"""
    try: 
        case = CaseDetails.objects.get(id=case_id) 
        # Make sure the case belongs to the current user.
        if case.owner != request.user:
            raise Http404
        context = {'case':case}
        return render(request,'legal/case.html',context)
    except : 
        html = '<h1> Case Details not published yet</h1>'
        return HttpResponse(html)
    
    # if CaseDetails.objects.get(id=case_id):
    #     case = CaseDetails.objects.get(id=case_id)
    #     context = {'case':case}
    #     return render(request,'legal/case.html',context)
    # else:
    #     return render(request,'legal/cases.html')
@login_required
def new_case(request):
    """Add a new case """
    if request.method != 'POST':
        # No data submitted ; create a bland form
        form = CaseEntryForm()
    else:
        # POST data submitted ; Process data.
        form = CaseEntryForm(data=request.POST)
        if form.is_valid():
            new_case = form.save(commit=False)
            new_case.owner = request.user
            new_case.save()
            return redirect('legal:cases')
    # Display a bland or invalid form.
    context = {'form':form}
    return render(request,'legal/new_case.html',context)
    

@login_required
def delete_case(request,case_id):
    case = CaseEntry.objects.get(id=case_id)
    if case.owner != request.user:
        raise Http404
    case.delete()
    return redirect('legal:cases')