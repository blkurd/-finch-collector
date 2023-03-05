from django.shortcuts import render

finches = [

      {'name': 'Wowo', 'breed': 'bird', 'description': 'furry', 'age': 2},
      {'name': 'yeye', 'breed': 'skinny', 'description': 'fur', 'age': 5},

]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches })