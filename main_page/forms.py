from django import forms
from .models import Post

class ModelForm(forms.ModelForm):
	#field_order = ['image', 'breed', 'name', 'contact', 'address', 'additional_info', ]
#	image = forms.ImageField()
#	breed = forms.CharField(max_length=100)
#	name = forms.CharField(max_length=100)
#	contact = forms.IntegerField()
#	address = forms.CharField()
#	additional_info = forms.CharField()
	#date_posted = forms.DateTimeField(default=timezone.now())

	class Meta:
		model = Post
		#fields = ['img1', 'breed', 'name', 'contact', 'address', 'additional_info']
		fields = ['img1', 'breed']

	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['img1'].widget.attrs={
			'id': 'fileupload',
			'class': 'btn btn-primary',
			'style': 'background-color: #3f51b5;'}

class ModelForm2(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['img1', 'breed', 'name', 'contact', 'address', 'additional_info']

	def __init__(self, *args, **kwargs):
		super(ModelForm2, self).__init__(*args, **kwargs)
		self.fields['img1'].widget.attrs={
			'id': 'fileupload',
			'class': 'btn btn-primary',
			'style': 'background-color: #3f51b5;'}
