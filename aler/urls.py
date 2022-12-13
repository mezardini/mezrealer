from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.register, name='register'),
    path('signin', views.login, name='login'),
    path('signout', views.signout, name='signout'),
    path('prop_filter', views.prop_filter, name='prop_filter'),
    path('property-show/<str:pk>/', views.property_show, name='property_show'),
    path('property-show-photos/<str:pk>/', views.photoshow, name='photoshow'),
    path('property-submit', views.property_submit, name='property_submit'),
    path('propertylist', views.property, name='property'),
    path('contact', views.contact, name='contact'),
    path('agent', views.agent, name='agent'),
    path('about', views.about, name='about'),
    path('property-submit/', views.property_submit, name='property_submit'),
    path('propertylist/', views.property, name='property'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('agent/', views.agent, name='agent'),
    path('about/', views.about, name='about'),
    path('signup/', views.register, name='register'),
    path('signin/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('property-show/<str:pk>', views.property_show, name='property_show'),
    
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    