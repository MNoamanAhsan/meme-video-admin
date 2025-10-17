from django.db import models
import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

class Category(models.Model):
    name=models.CharField(max_length=120)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


class Memes(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='memes')
    title=models.CharField(max_length=350)
    meme=models.FileField(upload_to='memes/videos/',blank=False, null=False)
    tags=models.CharField(max_length=350)

    def __str__(self):
        return self.title
    


@receiver(post_delete, sender=Memes)
def delete_meme_file(sender, instance, **kwargs):
    if instance.meme:
        if os.path.isfile(instance.meme.path):
            os.remove(instance.meme.path)



@receiver(pre_save, sender=Memes)
def delete_old_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return 

    try:
        old_file = Memes.objects.get(pk=instance.pk).meme
    except Memes.DoesNotExist:
        return

    new_file = instance.meme
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)