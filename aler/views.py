from django.shortcuts import render, redirect
from .models import Property, Agent, Photo, Property_review
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .filters import PropertyFilter, PriceFilter
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.
def index(request):
    propertys = Property.objects.all()
    photo = Photo.objects.filter(prop=propertys)
    
    agents = Agent.objects.all()


    context = {'propertys':propertys, 'photo':photo, 'agents':agents}
    return render(request, 'index.html', context)

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']

        if not request.POST.get('email'):
            messages.error(request, "Email cannot be blank.")
            return redirect('login')

        if not request.POST.get('password'):
            messages.error(request, "Password cannot be blank.")
            return redirect('login')

        user = auth.authenticate(request, username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'signin.html')

    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
                messages.error(request, "User already exists.")
                return redirect('register')

        if not request.POST.get('password1'):
            messages.error(request, "Password cannot be blank.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "User already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                return redirect('login')

    
    return render(request, 'signup.html')


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



def signout(request):
    logout(request)
    return redirect('login') 

@login_required(login_url='login')
def property_submit(request):

    if request.method == 'POST':
    
        images = request.FILES.getlist('images')
        image_list = []

        
        property = Property.objects.create(
                    title = request.POST.get('title'),
                    description = request.POST.get('description'),
                    address = request.POST.get('address'),
                    town = request.POST.get('town'),
                    state = request.POST.get('state'),
                    property_type = request.POST.get('property_type'),
                    floor_plan = request.FILES.get('floor_plan'),
                    price = str(request.POST.get('price')),
                    year_built = request.POST.get('year_built'),
                    contract_type = request.POST.get('contract_type'),
                    home_area = str(request.POST.get('home_area')),
                    bedrooms = request.POST.get('bedrooms'),
                    bathrooms = request.POST.get('bathrooms'),
                    agent = request.user,
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
    property = Property.objects.all()
    photos = propertys.photo_set.all()
    reviews = propertys.property_review_set.all()
    agents = Agent.objects.all()
    
    if request.method == 'POST':
        review = Property_review.objects.create(
            property = propertys,
            body = request.POST.get('body'),
            creator = request.POST.get('name'),
        )
        review.save()

    # prop_photo = propertys.photos.set_all()'prop-photo':prop_photo

    context = {'propertys':propertys, 'property':property, 'photos':photos, 'reviews':reviews, 'agents':agents }
    return render(request, 'property-show.html', context)

def photoshow(request, pk):
    propertys = Property.objects.get(id=pk)
    photos = propertys.photo_set.all()

    context = {'propertys':propertys, 'photos':photos}
    return render(request, 'photos.html', context)

def agent(request):
    agents = Agent.objects.all()
    
    if request.method == 'POST':
        searched = request.POST['searched']
        agentx = User.objects.filter(first_name__contains = searched)
        return render(request, 'search_agent.html', {'searched':searched, 'agents':agents, 'agentx':agentx})

    
    context = {'agents':agents}
    return render(request, 'agents.html', context)

def contact(request):
    return render(request, 'contact.html')

def profile(request, pk):
    agent = Agent.objects.get(id=pk)
    property = Property.objects.all()
    prop_count = Property.objects.filter(agent=agent)

    if request.method == 'POST':
        agent = Agent.objects.create(
            user = request.user,
            bio = request.POST.get('bio'),
            phone = request.POST.get('phone'),
            city = request.POST.get('city'),
            company = request.POST.get('company'),
            photo = request.FILES.get('photo'),
        )
        agent.save()

    

    context = {'agent':agent, 'prop_count':prop_count}
    return render(request, 'profile.html', context)

def about(request):
    return render(request, 'about.html')

def error_404_view(request, exception):
   
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')