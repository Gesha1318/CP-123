from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib import messages
from .models import Section
from .forms import SectionForm
from accounts.models import SectionMembership



def is_staff(user):
	return user.is_staff


@login_required
def section_list(request):
	user = request.user
	sections = Section.objects.filter(Q(is_private=False) | Q(memberships__user=user)).distinct()
	return render(request, 'sections/section_list.html', { 'sections': sections })


@login_required
def section_detail(request, slug):
	section = get_object_or_404(Section, slug=slug)
	if section.is_private and not SectionMembership.objects.filter(user=request.user, section=section).exists():
		return render(request, '403.html', status=403)
	members = SectionMembership.objects.filter(section=section).select_related('user', 'role')
	# show only published articles
	section = Section.objects.get(pk=section.pk)  # refresh instance
	return render(request, 'sections/section_detail.html', { 'section': section, 'members': members })


@user_passes_test(is_staff)
@login_required
def section_create(request):
	if request.method == 'POST':
		form = SectionForm(request.POST)
		if form.is_valid():
			section = form.save()
			messages.success(request, 'Раздел создан')
			return redirect('sections:section_detail', slug=section.slug)
	else:
		form = SectionForm()
	return render(request, 'sections/section_form.html', { 'form': form })


@user_passes_test(is_staff)
@login_required
def section_edit(request, slug):
	section = get_object_or_404(Section, slug=slug)
	if request.method == 'POST':
		form = SectionForm(request.POST, instance=section)
		if form.is_valid():
			form.save()
			messages.success(request, 'Сохранено')
			return redirect('sections:section_detail', slug=section.slug)
	else:
		form = SectionForm(instance=section)
	return render(request, 'sections/section_form.html', { 'form': form, 'section': section })


@login_required
def section_members(request, slug):
	section = get_object_or_404(Section, slug=slug)
	if not request.user.is_staff:
		return render(request, '403.html', status=403)
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		permission = request.POST.get('permission')
		if user_id and permission in [SectionMembership.PERMISSION_VIEW, SectionMembership.PERMISSION_EDIT, SectionMembership.PERMISSION_MANAGE]:
			SectionMembership.objects.get_or_create(user_id=user_id, section=section, defaults={'permission': permission})
			messages.success(request, 'Права обновлены')
	return render(request, 'sections/section_members.html', { 'section': section, 'members': SectionMembership.objects.filter(section=section) })
