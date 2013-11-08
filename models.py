import urllib2
from xml.etree import ElementTree as ET
from django.db import models
from django import forms
from django.shortcuts import get_object_or_404

# Create your models here.
url = 'http://mta.info/status/serviceStatus.txt'
request = urllib2.Request(url, headers={"Accept" : "application/xml"})
u = urllib2.urlopen(request)

tree = ET.parse(u)
rootElem = tree.getroot()

services = []
for child in rootElem:
    services.append(child)

def get_my_services():
    choices_list =[(services[x].tag, x-2) for x in range(2, 7)]
    print choices_list
    return choices_list

class Services(forms.Form):
    def __init__(self):
        super(Services, self).__init__()
        self.fields['services'] = forms.ChoiceField(
            choices=get_my_services())
        #self.choice = self.fields['services'].choices

def get_my_statuses():
    statuses = []
    names = []
    #if type(Services.choice) == type("subway"):
    #    choice = Services.choice
    #else:
    choice = "subway"
    for service in services:
        if service.tag == choice:
            for line in service:
                for entry in line:
                    if entry.tag == 'status':
                        statuses.append(entry)
                    if entry.tag == 'name':
                        names.append(entry)
    
    service_statuses = []
    service_statuses.append("Updated: " + rootElem[1].text)
    for i in range(len(names)):
        service_statuses.append(names[i].text + " / " + statuses[i].text)
    
    statuses_list = [(service_statuses[x], x) for x in range(len(service_statuses))]
    return statuses_list

class ServiceInfo(forms.Form):
    def __init__(self):
        super(ServiceInfo, self).__init__()
        self.fields['service_info'] = forms.ChoiceField(
            choices=get_my_statuses())