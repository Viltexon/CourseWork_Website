from django import forms
from .models import Tourism, Newsletter, Research, Specializations, Modules, News


class TourismForm(forms.ModelForm):
    class Meta:
        model = Tourism
        fields = ('t_name', 'personal', 't_mail', 't_message')
        widgets = {
          't_message': forms.Textarea(attrs={'rows':4, 'cols':50}),
        }

class NewsletterForm(forms.ModelForm):
  class Meta:
    model = Newsletter
    fields = ('s_mail', )

# https://docs.djangoproject.com/en/3.0/howto/custom-model-fields/

class ResearchForm(forms.ModelForm):
    
  class Meta:
    model = Research
    fields = ('r_topic', 'mod', 'prop_name', 'prop_mail', 'r_message', 'r_status' )
    widgets = {
          'r_message': forms.Textarea(attrs={'rows':8, 'cols':150}),
        }


# Specializations as array? as multiple forms? 
# https://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms

# # Specializations sp_name
# class SpecializationCheckForm(forms.Form):
#     spec_name = forms.BooleanField()

class NewsForm(forms.ModelForm):

  class Meta:
    model = News
    fields = ('res', 'title', 'content', 'n_date', 'author' )
    widgets = {
          'content': forms.Textarea(attrs={'rows':8, 'cols':150}),
        }
  
  def __init__(self, *args, **kwargs):
        super (NewsForm, self).__init__(*args,**kwargs) # populates the post
        self.fields['res'].queryset = Research.objects.filter(r_status='finished')

