#coding:utf-8
from django.conf.urls import url
from blog import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.FirstView.as_view(), name = 'first'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name = 'detail'),
    url(r'^blog/index$', views.IndexView.as_view(), name = 'index'),
    url(r'^blog/category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name = 'category'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT})
]
