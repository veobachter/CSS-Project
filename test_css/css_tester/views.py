from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context,RequestContext

def Default(request):


	toPrint = 'Testing Django-CSS'

	t = get_template("index.html")
	query = request.POST.items()

	
	html = t.render(RequestContext(request,{"testPrint":toPrint}))
	return HttpResponse(html)
