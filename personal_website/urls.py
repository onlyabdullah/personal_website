from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from blog.helpers import get_latest_posts

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='home.html', extra_context={'latest_posts': get_latest_posts()}), name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
