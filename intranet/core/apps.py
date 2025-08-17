from django.apps import AppConfig


class CoreConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'core'

	def ready(self):
		try:
			from django.template import engines
			from django.template.library import import_library
			library = import_library('core.templatetags.compat')
			engine = engines['django'].engine
			if hasattr(engine, 'builtins'):
				if library not in engine.builtins:
					engine.builtins.append(library)
			elif hasattr(engine, 'template_builtins'):
				if library not in engine.template_builtins:
					engine.template_builtins.append(library)
		except Exception:
			pass
