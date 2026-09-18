from django import forms
from .models import Game
from django.utils.text import slugify

class GameUploadForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'python_code']
        widgets = {
            'python_code': forms.Textarea(attrs={'class': 'font-mono text-sm', 'rows': 15, 'placeholder': 'print("Hello from PyScript!")\n\nimport js\njs.console.log("Web loaded!")'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            # Basic slugification
            base_slug = slugify(instance.title)
            slug = base_slug
            counter = 1
            while Game.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            instance.slug = slug
        
        # Hardcode the template to our generic PyScript runner
        instance.template_name = 'games/play_python.html'
        
        if commit:
            instance.save()
        return instance
