from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Section(models.Model):
	name = models.CharField("Название", max_length=200)
	slug = models.SlugField("Слаг", max_length=200, unique=True)
	description = models.TextField("Описание", blank=True)
	parent = models.ForeignKey('self', verbose_name="Родитель", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
	is_private = models.BooleanField("Приватный", default=False)
	members = models.ManyToManyField(User, through='SectionMembership', related_name='sections', verbose_name="Участники")
	created_at = models.DateTimeField("Создан", auto_now_add=True)
	updated_at = models.DateTimeField("Обновлён", auto_now=True)

	class Meta:
		ordering = ['name']
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"

	def __str__(self):
		return self.name


class SectionMembership(models.Model):
	ROLE_CHOICES = (
		('admin', 'Администратор'),
		('editor', 'Редактор'),
		('member', 'Участник'),
	)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='section_memberships', verbose_name="Пользователь")
	section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='memberships', verbose_name="Раздел")
	role = models.CharField("Роль", max_length=20, choices=ROLE_CHOICES, default='member')
	date_joined = models.DateTimeField("Дата вступления", auto_now_add=True)
	
	class Meta:
		unique_together = ('user', 'section')
		verbose_name = "Членство в разделе"
		verbose_name_plural = "Членства в разделах"
		
	def __str__(self):
		return f"{self.user.username} - {self.section.name} ({self.get_role_display()})"
