from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('prop_filter/', views.prop_filter, name='prop_filter'),
    path('property-show/<str:pk>/', views.property_show, name='property_show'),
    path('property-submit/', views.property_submit, name='property_submit'),
    path('propertylist/', views.property, name='property'),
    path('contact/', views.mailMezard, name='mailmezard'),
    # path('profile/<str:pk>/', views.profile, name='profile'),
    # path('c-agent/', views.create_agent, name='c-agent'),
    
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    