from django.db import models
# from tinymce.models import HTMLField
# Create your models here.

# from froala_editor.fields import FroalaField


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return r"Category:{id:%s,name:%s}" % (self.id, self.name)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    # content2 = HTMLField(blank=True)
    # content3 = FroalaField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    tags=models.ManyToManyField("Tag",related_name='articles')
    def __str__(self):
        return r"Article:{id:%s,title:%s,category:%s}" % (self.id, self.title,  self.category.name if self.category else '无')


class UserExtend(models.Model):
    birthday = models.DateField(null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return r'UserExtend:{nickname:%s}' % self.nickname


class Tag(models.Model):
    name = models.CharField(max_length=50)
