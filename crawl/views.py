from django.shortcuts import render
from django.http import HttpResponse
from .Spoj_with_multithreading import main
from .forms import NewTopicForm

def home(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			print(new.name)
			return HttpResponse("hi")
	else:
		form = NewTopicForm()
	return render(request, 'create.html', {'form': form})

	
