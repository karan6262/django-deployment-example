from django.shortcuts import render

def index(request):
	context_dict = {'text':'hello World', 'number':100}
	return render(request,'basic_app/index.html',context_dict)
	
def otherpage(request):
	return render(request, 'basic_app/otherpage.html')

def relative(request):
	return render(request, 'basic_app/relative_url_templates.html')