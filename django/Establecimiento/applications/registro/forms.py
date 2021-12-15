from django import forms
from .models import PersonalDocente, PersonalNoDocente

class PersonalDocenteForm(forms.ModelForm):
    """Form definition for PersonalDocente."""

    class Meta:
        """Meta definition for PersonalDocenteform."""

        model = PersonalDocente
        fields = (
            'first_name',
            'last_name',
            'materia',
            'id',
            )

       
