from django.shortcuts import render
from django.http import HttpResponse
from .Spoj_with_multithreading import main as mai
from .forms import NewTopicForm,NewTopicForm2
from .models import jain,ta
from .sort_question_tags import main


hits=0 

def home(request):
	hit = jain.objects.filter(id=1)
	for hit in hit:
		hits = hit.hits
	#print(hits)
	hits = hits +1
	jain.objects.filter(id=1).update(hits=hits)
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			#print(new.Spoj_Handle)
			ans = mai(new.Spoj_Handle)
			print(ans)
			l = []
			for ans in ans:
				l.append(ans['name'])
			#print(l)
			return render(request, 'list_question.html', {'list': l})
	else:
		form = NewTopicForm()
	return render(request, 'create.html', {'form': form,'hits':hits})

	
def tags(request):
	if request.method == 'POST':
		form = NewTopicForm2(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			ans = main(new.name)
			print(ans)
		return render(request, 'display_tag.html', {'list': ans})
	else:
		form = NewTopicForm2()
	return render(request, 'display.html', {'form': form})
