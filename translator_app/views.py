from django.shortcuts import render
from .core.model import english_to_french
import json

# Create your views here.
def index(request):
	template_name = 'fairseq.html'
	if request.method == 'POST':
		if request.POST.get('sourceText') == None:
			input_text = ""
		input_text = request.POST.get('sourceText')
	
	en2fr = english_to_french(input_text).replace("&apos;", "\'")
	
	context = {
		"translated_text": en2fr,
	}

	return render(request, template_name, context)