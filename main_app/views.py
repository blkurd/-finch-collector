
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# finches = [

#       {'name': 'Wowo', 'breed': 'bird', 'description': 'furry', 'age': 2},
#       {'name': 'yeye', 'breed': 'skinny', 'description': 'fur', 'age': 5},

# ]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches })

def finches_detail(request, finch_id):
  finches = Finch.objects.get(id= finch_id)
  # return render(request, 'finches/detail.html', {'finches': finches })


  # first we'll get a list of ids of toys the finch owns
  id_list = finch.toys.all().values_list('id')
  # then we'll make a list of the toys the finch does not have
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })

class FinchCreate(CreateView):
    model = Finch
    # the fields attribute is required for a createview. These inform the form
    fields = '__all__'
    # we could also have written our fields like this:
    # fields = ['name', 'breed', 'description', 'age']
    # we need to add redirects when we make a success
    # success_url = '/finches/{finch_id}'
    # or, we could redirect to the index page if we want
    # success_url = '/finches'
    # what django recommends, is adding a get_absolute_url method to the model

class FinchUpdate(UpdateView):
    model = Finch
    # let's use custom fields to disallow renaming a finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, finch_id):
    # create a ModelForm instance from the data in request.POST
    form = FeedingForm(request.POST)

    # we need to validate the form, that means "does it match our data?"
    if form.is_valid():
        # we dont want to save the form to the db until is has the finch id
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)

# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    # define what the inherited method is_valid does(we'll update this later)
    def form_valid(self, form):
        # we'll use this later, but implement right now
        # we'll need this when we add auth
        # super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
