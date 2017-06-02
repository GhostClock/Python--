# coding:utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoProject.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('WeSite')
    add_page(cat=python_cat,
             title='Google',
             url='www.google.com')
    add_page(cat=python_cat,
             title='Baidu',
             url='www.baidu.com')
    add_page(cat=python_cat,
             title='souhu',
             url='www.souhu.com')


    django_cat = add_cat('Province')
    add_page(cat=django_cat,
             title='Beijing',
             url='www.beijing.com')
    add_page(cat=django_cat,
             title='Shanghai',
             url='www.shanghai.com')
    add_page(cat=django_cat,
             title='Wuhan',
             url='www.wuhan.com')


    fram_cat = add_cat('People')
    add_page(cat=fram_cat,
             title='Tom',
             url='www.tom.com')
    add_page(cat=fram_cat,
             title='Ghost',
             url='www.ghost.com')

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ('- {0} - {1}'.format(str(c), str(p)))

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat,title=title,url=url,views=views)[0]
    return p

def add_cat(name,views,links):
    c = Category.objects.get_or_create(name=name,views=views,links=links)[0]
    return c


if __name__ == '__main__':
    print 'Starting Rango population Script………………'
    populate()
