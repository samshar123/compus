from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add-email/', add_email, name='add-email'),
    path('service/<int:id>/', service_list, name='service-detail'),
    path('service/sub/<int:id>/', service_sub_list, name='service-sub-detail'),
     path('about/', about, name='about'),
     path('pricing/', pricing, name='pricing'),
     path('service/', service, name='service'),
      path('contact/', contact, name='contact'),
      path('project/',project, name='project')
]
