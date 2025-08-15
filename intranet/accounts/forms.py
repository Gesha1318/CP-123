from django import forms
from .models import SectionMembership


class SectionMembershipForm(forms.ModelForm):
	class Meta:
		model = SectionMembership
		fields = ["user", "permission", "role"]