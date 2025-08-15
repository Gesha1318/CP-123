from django.db import models
from django.contrib.auth import get_user_model
from sections.models import Section


class Role(models.Model):
	name = models.CharField("Название", max_length=100, unique=True)
	description = models.CharField("Описание", max_length=255, blank=True)

	class Meta:
		verbose_name = "Роль"
		verbose_name_plural = "Роли"

	def __str__(self):
		return self.name


class SectionMembership(models.Model):
	PERMISSION_VIEW = 'view'
	PERMISSION_EDIT = 'edit'
	PERMISSION_MANAGE = 'manage'

	PERMISSION_CHOICES = [
		(PERMISSION_VIEW, 'Просмотр'),
		(PERMISSION_EDIT, 'Редактирование'),
		(PERMISSION_MANAGE, 'Управление'),
	]

	user = models.ForeignKey(get_user_model(), verbose_name="Пользователь", on_delete=models.CASCADE, related_name='section_memberships')
	section = models.ForeignKey(Section, verbose_name="Раздел", on_delete=models.CASCADE, related_name='memberships')
	role = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True, blank=True)
	permission = models.CharField("Права", max_length=20, choices=PERMISSION_CHOICES, default=PERMISSION_VIEW)
	created_at = models.DateTimeField("Создано", auto_now_add=True)

	class Meta:
		unique_together = ('user', 'section')
		verbose_name = "Доступ к разделу"
		verbose_name_plural = "Доступы к разделам"

	def __str__(self):
		return f"{self.user} -> {self.section} ({self.permission})"
