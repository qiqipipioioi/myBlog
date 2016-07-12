#coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.conf import settings

import os
import sys
default_encoding = 'utf-8'  
if sys.getdefaultencoding() != default_encoding:  
    reload(sys)  
    sys.setdefaultencoding(default_encoding)  

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70, default='No title!')
    body = models.TextField('正文', null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, null=True)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, 
                                help_text="可选，如若为空将摘取正文的前54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类', 
                                 null=True, 
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


