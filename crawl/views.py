from django.shortcuts import render
from django.http import HttpResponse
from .Spoj_with_multithreading import main
from .forms import NewTopicForm
from .Spoj_with_multithreading import main

def home(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			print(new.name)
			ans = main(new.name)
			#print(ans)
			l = []
			for ans in ans:
				l.append(ans['name'])
			print(l)
			return render(request, 'list_question.html', {'list': l})
	else:
		form = NewTopicForm()
	return render(request, 'create.html', {'form': form})

	
