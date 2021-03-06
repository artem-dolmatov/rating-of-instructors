from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.InstructorListView.as_view(), name='instructor_list'),
    url(r'^(?P<pk>\d+)/$', views.InstructorDetailView.as_view(), name='instructor_detail'),
]