from django.urls import path
from .views import exchange
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'exchange_app'

urlpatterns = [
    path('', views.exchange, name='exchange'),

 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
