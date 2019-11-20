from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^services$', views.services, name='services'),
    url(r'^about$', views.about, name='about'),
    url(r'^news$', views.news, name='news'),
    url(r'^studentForm$', views.student, name='student'),
    url(r'^businessForm$', views.business, name='business'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


