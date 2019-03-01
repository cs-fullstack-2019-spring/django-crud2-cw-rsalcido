from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from .forms import NewContactForm
from .models import  Contact

# Create your views here.
def index(request):
    allcontacts = Contact.objects.all()
    return render(request, "crudApp/index.html", {'contact_list': allcontacts})


def contacts(request):
    new_form = NewContactForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

    return render(request, 'crudApp/contacts.html', {'contactform': new_form})

# third function
def editcontact(request, id):
    user = get_object_or_404(Contact, pk=id)
    edit_form = NewContactForm(request.POST or None, instance=user)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'crudApp/contacts.html', {'contactform': edit_form})

# fourth delete func
def deletecontact(request,id):
    user = get_object_or_404(Contact, pk=id)
    if request.method == 'POST':
        contacts.delete()
        return redirect('index')

    return render(request, 'crudApp/delete.html', {'selectedcontacts': contacts })
