from django.conf.urls import url

from .views import IndexView

app_name = 'images'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]
