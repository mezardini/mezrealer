from django.shortcuts import render, redirect
from .models import Property,  Photo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate, login, logout
from .filters import PropertyFilter, PriceFilter
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    propertys = Property.objects.all()
    # photo = Photo.objects.filter(prop=propertys)
    
    # agents = Agent.objects.all()


    context = {'propertys':propertys}
    return render(request, 'index.html', context)


def prop_filter(request):
    propertys = Property.objects.all()
    property_type = PropertyFilter(request.GET, queryset=propertys)
    f = PriceFilter({'request.GET': '1800000', 'request.GET': '5000000'}, queryset=propertys)

    context = {'propertys':propertys, 'property_type':property_type, 'f':f}
    return render(request, 'apartment.html', context)

def property(request):
    propertys = Property.objects.all()    
    property_type = PropertyFilter(request.GET, queryset=propertys)
    f = PriceFilter({'request.GET': '1800000', 'request.GET': '5000000'}, queryset=propertys)

    prop_pagi = Paginator(propertys, 2 )

    page_num = request.GET.get('page')

    page = prop_pagi.get_page(page_num)


    context = {'propertys':propertys, 'property_type':property_type, 'f':f, 'page':page, 'count':prop_pagi.count}
    return render(request, 'property.html', context)



def property_submit(request):

    if request.method == 'POST':
    
        images = request.FILES.getlist('images')
        image_list = []

        
        property = Property.objects.create(
                    title = request.POST.get('title'),
                    description = request.POST.get('description'),
                    address = request.POST.get('address'),
                    property_type = request.POST.get('property_type'),
                    floor_plan = request.FILES.get('floor_plan'),
                    price = str(request.POST.get('price')),
                    year_of_build = request.POST.get('year_of_build'),
                    contract_type = request.POST.get('contract_type'),
                    home_area = str(request.POST.get('home_area')),
                    bedrooms = request.POST.get('bedrooms'),
                    bathrooms = request.POST.get('bathrooms'),
                    agent_name = request.POST.get('name'),
                    agent_mail = request.POST.get('mail'),
                    parking = request.POST.get('parking'),
                    
                )
        property.save()

        for image in images:
            photo = Photo.objects.create(
                prop = property,
                photos = image
            )
            photo.save()
            
            
    
        return redirect('property_submit')

    return render(request, 'property-submit.html')

def property_show(request, pk):
    propertys = Property.objects.get(id=pk)
    prop_agent = propertys.agent_mail
    prop_agent_name = propertys.agent_name
    property = Property.objects.all()
    photos = propertys.photo_set.all()
    reviews = propertys.property_review_set.all()
    # agents = Agent.objects.all()
    
    if request.method == 'POST':
        sender = request.POST.get('sender')
        body = request.POST.get('body')
        send_mail(
            'Message from Realer',
            'Hello, ' + prop_agent_name + ' you have a message from ' + sender + ' here is the message; ' + body ,
            'settings.EMAIL_HOST_USER',
            [prop_agent],
            fail_silently=False,
        )
        

    # prop_photo = propertys.photos.set_all()'prop-photo':prop_photo

    context = {'propertys':propertys, 'property':property, 'photos':photos, 'reviews':reviews}
    return render(request, 'property-show.html', context)


def mailMezard(request):

    if request.method == 'POST':
        sender = request.POST.get('sender')
        body = request.POST.get('body')
        send_mail(
            'Message from ' + sender,
            body,
            'settings.EMAIL_HOST_USER',
            ['mezardini@gmail.com'],
            fail_silently=False,
        )
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def error_404_view(request, exception):
   
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')