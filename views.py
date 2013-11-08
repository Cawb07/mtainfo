from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from fieldtest.models import ContactForm, Services, ServiceInfo
from django.core.urlresolvers import reverse

# Create your views here.
def choice(request):
    form = Services()
    form2 = ServiceInfo()
    
    return render(request, 'mtainfo/choice.html', {
        'form': form,
        'form2': form2,
    })

c = ""
def servicechoice(request, service_id):
    s = get_object_or_404(Services, service_id)
    selected_choice = s.choice_set.get(pk=request.Post['choice'])
    c = selected_choice.text
    
    #return HttpResponseRedirect(reverse('fieldtest:choice', args=(s.id,), kwargs=None))

class Selection:
    def __init__(self):
        self.choice = c
    
    