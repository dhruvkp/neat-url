from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import Map
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
import urllib2
import simplejson as json
import uuid
from django.contrib.sites.models import Site

# Create your views here.
def home(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
def keywords(request):
    url=request.POST['url']
    try:
        #Open url and get keywords from API
        webrequset=urllib2.urlopen(url)
        api_url='http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=91603ab8dfbef41c5a8190e41afe817133e4676e&outputMode=json&url='
        access_url=api_url+url
        request_var=urllib2.urlopen(access_url)
        data_var=request_var.read()
        responses=json.loads(data_var)#Parse Json
        content=responses['keywords'][0]['text']
        lenn=len(responses['keywords'])
        counter=0
        rel = 0
        for i in range (1,lenn):
            content=content+"\n"+responses['keywords'][i]['text']
            if(float(responses['keywords'][i]['relevance'])>0.9):
                rel=i
        #Generate Unique token
        #unique_id=uuid.uuid1()
        #id_ahead=str(unique_id).split('-')[0]
        i=0
        for i in range (0,rel):
            count=Map.objects.raw('Select count(*) from app_map where tocken=\''+responses['keywords'][i]['text']+'\'')
            return HttpResponse(count)
            if(count==0):
                break
        result_url="http://"+request.get_host()+"/"+responses['keywords'][i]['text']
        result_url.replace(" ","-")
        map_object=Map.objects.create(tocken=responses['keywords'][i]['text'],ourl=url,keywords=content,status=1);
        map_object.save();
        return HttpResponse(result_url)
    except:
        return HttpResponse("URL does not exist.")
def redirect(request, tocken):
    contents=''
    map_object= Map.objects.raw('SELECT * from app_map where tocken=\''+tocken+'\'')[0]
    contents=map_object.ourl
    try:
        webrequest=urllib2.urlopen(contents)
    except:
        url='http://webcache.googleusercontent.com/search?q=cache:'+contents
        return HttpResponseRedirect(url)
    return HttpResponseRedirect(contents)
