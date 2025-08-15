from django.db import models
from django.contrib.auth import get_user_model


class Section(models.Model):
	name = models.CharField("Название", max_length=200)
	slug = models.SlugField("Слаг", max_length=200, unique=True)
	description = models.TextField("Описание", blank=True)
	parent = models.ForeignKey('self', verbose_name="Родитель", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
	is_private = models.BooleanField("Приватный", default=False)
	created_at = models.DateTimeField("Создан", auto_now_add=True)
	updated_at = models.DateTimeField("Обновлён", auto_now=True)

	class Meta:
		ordering = ['name']
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"

	def __str__(self):
		return self.name
