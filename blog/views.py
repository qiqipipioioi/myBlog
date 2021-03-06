#coding:utf-8
from django.shortcuts import render
from blog.models import Article
from blog.models import Category
from django.template import RequestContext
from django.views.generic import ListView, DetailView
import markdown2

class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    
    def get_queryset(self):
        article_list = Article.objects.filter(status='p').order_by('-created_time')
        return article_list


class FirstView(ListView):
    template_name = "blog/first.html"
    context_object_name = "article_first"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p').order_by('-last_modified_time')
        first_article = article_list[0]
        first_article.body = markdown2.markdown(first_article.body, 
                extras=['fenced-code-blocks', "cuddled-lists", "metadata", "tables", "spoiler"])
        return first_article

    def require_n_line(self, n, text, m = 0):
        m1 = text.find('\r\n', m+1)
        if n == 1:
            return m1
        else:
            return self.require_n_line(n-1, text, m1)

    def get_context_data(self, **kwargs):
        rest_articles = Article.objects.filter(status='p').order_by('-last_modified_time')[1:]
        for article in rest_articles:
            mark = self.require_n_line(10, article.body)
            article.abstract = article.body[0:mark]
            article.abstract = markdown2.markdown(article.abstract,
                extras=['fenced-code-blocks', "cuddled-lists", "metadata", "tables", "spoiler"])
        kwargs['article_rest'] = rest_articles
        return super(FirstView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    # 指定视图获取哪个model

    template_name = "blog/detail.html"
    # 指定要渲染的模板文件

    context_object_name = "article"
    # 在模板中需要使用的上下文名字

    pk_url_kwarg = 'article_id'
    # 这里注意，pk_url_kwarg用于接收一个来自url中的主键，然后会根据这个主键进行查询
    # 我们之前在urlpatterns已经捕获article_id

    # 指定以上几个属性，已经能够返回一个DetailView视图了，为了让文章以markdown形式展现，我们重写get_object()方法。
    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks', "cuddled-lists", "metadata", "tables", "spoiler"])
        return obj


class CategoryView(ListView):
# 继承自ListView,用于展示一个列表

    template_name = "blog/index.html"
    # 指定需要渲染的模板

    context_object_name = "article_list"
    # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self):
        #get_queryset 的作用已在第一篇中有介绍，不再赘述
        article_list = Article.objects.filter(category=self.kwargs['cate_id'],status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        return super(CategoryView, self).get_context_data(**kwargs)

