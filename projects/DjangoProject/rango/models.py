from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    views = models.IntegerField(default=0)
    links = models.IntegerField(default=0)
    def __unicode__(self):
        return unicode(self.name)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.FileField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.title)
