from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.start, name='start'),
    path('login/',views.login, name='login'),
    path('index/',views.index, name='index'),
    path('host1/',views.host1, name='host1'),
    path('<int:id>/client',views.client, name='client'),
    path('register/', views.register, name='register'),
    path('register_submit/', views.register_submit, name='register_submit'),
    path('client_form_submit/', views.client_form_submit, name='client_form_submit'),
    path('handlelogout/', views.handlelogout, name="handlelogout") ,
    path('hostlogout/', views.hostlogout, name="hostlogout") ,
    path('checkout/', views.checkout, name="checkout") ,
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)