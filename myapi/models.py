from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='User',blank=True, null=True)
    personal_number = models.CharField(max_length=100, verbose_name='Personal Number')
    signImg = models.ImageField(verbose_name="Sign", upload_to="sign", blank=True, null=True)

    def __str__(self):
        return self.name + str(self.id)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("name",)


