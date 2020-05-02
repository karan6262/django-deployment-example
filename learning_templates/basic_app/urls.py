from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative, name="relative"),
	path('otherpage/', views.otherpage, name="otherpage"),
]
 