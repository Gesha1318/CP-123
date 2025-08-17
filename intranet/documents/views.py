from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sections.models import Section
from accounts.models import SectionMembership
from .models import Article, File


@login_required
def create_article(request, section_slug):
	section = get_object_or_404(Section, slug=section_slug)
	if not SectionMembership.objects.filter(user=request.user, section=section, permission__in=[SectionMembership.PERMISSION_EDIT, SectionMembership.PERMISSION_MANAGE]).exists():
		return render(request, '403.html', status=403)
	if request.method == 'POST':
		title = request.POST.get('title', '').strip()
		slug = request.POST.get('slug', '').strip()
		content = request.POST.get('content', '').strip()
		attachment = request.FILES.get('attachment')
		if not title or not slug:
			messages.error(request, 'Укажите заголовок и URL-метку')
		else:
			article = Article.objects.create(section=section, title=title, slug=slug, content=content, author=request.user, attachment=attachment)
			messages.success(request, 'Статья создана')
			return redirect(article.get_absolute_url())
	return render(request, 'documents/create_article.html', { 'section': section })


@login_required
def article_detail(request, section_slug, article_slug):
	section = get_object_or_404(Section, slug=section_slug)
	if section.is_private and not SectionMembership.objects.filter(user=request.user, section=section).exists():
		return render(request, '403.html', status=403)
	article = get_object_or_404(Article, section=section, slug=article_slug, is_published=True)
	return render(request, 'documents/article_detail.html', { 'section': section, 'article': article })


@login_required
def upload_file(request, section_slug):
	section = get_object_or_404(Section, slug=section_slug)
	if not SectionMembership.objects.filter(user=request.user, section=section, permission__in=[SectionMembership.PERMISSION_EDIT, SectionMembership.PERMISSION_MANAGE]).exists():
		return render(request, '403.html', status=403)
	if request.method == 'POST' and request.FILES.get('file'):
		title = request.POST.get('title', '').strip() or request.FILES['file'].name
		file = request.FILES['file']
		File.objects.create(section=section, title=title, file=file, uploaded_by=request.user)
		messages.success(request, 'Файл загружен')
		return redirect('sections:section_detail', slug=section.slug)
	return render(request, 'documents/upload_file.html', { 'section': section })
