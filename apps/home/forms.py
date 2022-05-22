from django  import forms
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('user','bio','image','gender','github_link','linkedin_link',)

class ApplicationForm(forms.ModelForm):
    """Form definition for Application."""

    class Meta:
        """Meta definition for Applicationform."""

        model = Application
        fields = ('user','category','app_name','stage','description','requirements','logo','company','version','size','setup',)

class FeedbackForm(forms.ModelForm):
    """Form definition for Feedback."""

    class Meta:
        """Meta definition for Feedbackform."""

        model = Feedback
        fields = ('name','email','contact_no','description',)
