from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [	
	url(r'^$', views.APIRootView.as_view(), name='api-root'),
	url(r'^signup/$', views.APISignUpView.as_view(), name='api-signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)