from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from mtainfo.models import Services, ServiceInfo
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.
def choice(request):
    form = Services()
    s = request.POST.get('services', False)
    ch = s
    form2 = ServiceInfo(s)
    
    c = RequestContext(request, {
        'form': form,
        'form2': form2,
    })
    return render_to_response('mtainfo/choice.html', c)