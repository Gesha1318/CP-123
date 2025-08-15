from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib import messages
from .models import Section
from .forms import SectionForm
from accounts.models import SectionMembership
from accounts.forms import SectionMembershipForm


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
			messages.success(request, 'Раздел обновлен')
			return redirect('sections:section_detail', slug=section.slug)
	else:
		form = SectionForm(instance=section)
	return render(request, 'sections/section_form.html', { 'form': form, 'section': section })


@user_passes_test(is_staff)
@login_required
def section_members(request, slug):
	section = get_object_or_404(Section, slug=slug)
	if request.method == 'POST':
		form = SectionMembershipForm(request.POST)
		if form.is_valid():
			membership, _ = SectionMembership.objects.update_or_create(
				user=form.cleaned_data['user'], section=section,
				defaults={
					'permission': form.cleaned_data['permission'],
					'role': form.cleaned_data['role'],
				}
			)
			messages.success(request, 'Права доступа обновлены')
			return redirect('sections:section_members', slug=section.slug)
	else:
		form = SectionMembershipForm()
	memberships = SectionMembership.objects.filter(section=section).select_related('user', 'role')
	return render(request, 'sections/section_members.html', { 'section': section, 'form': form, 'memberships': memberships })
