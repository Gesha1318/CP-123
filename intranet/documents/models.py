from django.db import models
from django.contrib.auth import get_user_model
from sections.models import Section


def upload_to_article(instance, filename):
	return f"articles/{instance.section.slug}/{filename}"


def upload_to_file(instance, filename):
	return f"files/{instance.section.slug}/{filename}"


class Article(models.Model):
	section = models.ForeignKey(Section, verbose_name="Раздел", on_delete=models.CASCADE, related_name='articles')
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("Слаг", max_length=255)
	content = models.TextField("Содержимое")
	author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.SET_NULL, null=True, blank=True)
	is_published = models.BooleanField("Опубликовано", default=True)
	created_at = models.DateTimeField("Создано", auto_now_add=True)
	updated_at = models.DateTimeField("Обновлено", auto_now=True)

	class Meta:
		unique_together = ('section', 'slug')
		ordering = ['-created_at']
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"

	def __str__(self):
		return self.title


class File(models.Model):
	section = models.ForeignKey(Section, verbose_name="Раздел", on_delete=models.CASCADE, related_name='files')
	title = models.CharField("Название", max_length=255)
	file = models.FileField("Файл", upload_to=upload_to_file)
	uploaded_by = models.ForeignKey(get_user_model(), verbose_name="Загрузил", on_delete=models.SET_NULL, null=True, blank=True)
	created_at = models.DateTimeField("Загружено", auto_now_add=True)

	class Meta:
		verbose_name = "Файл"
		verbose_name_plural = "Файлы"

	def __str__(self):
		return self.title
