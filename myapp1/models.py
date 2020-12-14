from django.db import models

# Create your models here.

class Gallery(models.Model):
    #自定义Gallery的属性
    description = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='作品标题',max_length=50)
    #title是自定义的项目，所以做以下定义
    def __str__(self):
        return self.title