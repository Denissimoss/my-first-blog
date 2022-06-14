from django.shortcuts import render

from main.forms import ormForm

def create(request):
    form = ormForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ormForm(request.POST)
        # create a form instance and populate it with data from the request:
      
        # check whether it's valid:
        if form.is_valid():
          
                form.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ormForm()

    return render(request, 'create.html', {'form': form})
