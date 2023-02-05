from django.contrib import path
from django.views.generic import TemplateView
app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
]