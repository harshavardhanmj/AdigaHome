from django import forms
from .models import TenantDetails

class DateInput(forms.DateInput):
	input_type = 'date'

class TenantForm(forms.ModelForm):
	class Meta:
		model = TenantDetails
		fields = [
			'first_name',
			'last_name',
			'pg_name',
			'phone_number',
			'email',
			'address',
			'adhar_img',
			'pan_img',
			'room_no',
			'occupatin',
			'rent',
			'food_required',
			'food_amt',
			'advance_amt',
			'joining_date',
			'status',
			'vacate_date',
		]

		widgets = {'joining_date' : DateInput(), 'vacate_date' : DateInput()}
	
	def __init__(self, *args, **kwargs):
		super(TenantForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['first_name'].widget.attrs['required'] = True
		self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pg_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pg_name'].widget.attrs['required'] = True
		self.fields['phone_number'].widget.attrs.update({'class' : 'form-control'})
		self.fields['phone_number'].widget.attrs['required'] = True
		self.fields['email'].widget.attrs.update({'class' : 'form-control'})
		self.fields['email'].widget.attrs['required'] = True
		self.fields['address'].widget.attrs.update({'class' : 'form-control'})
		self.fields['address'].widget.attrs['required'] = True
		self.fields['adhar_img'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['adhar_img'].widget.attrs['required'] = True
		self.fields['pan_img'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['pan_img'].widget.attrs['required'] = True
		self.fields['room_no'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_no'].widget.attrs['required'] = True
		self.fields['occupatin'].widget.attrs.update({'class' : 'form-control'})
		self.fields['occupatin'].widget.attrs['required'] = True
		self.fields['rent'].widget.attrs.update({'class' : 'form-control'})
		self.fields['rent'].widget.attrs['required'] = True
		self.fields['food_required'].widget.attrs.update({'class' : 'form-control'})
		self.fields['food_required'].widget.attrs['required'] = True
		self.fields['food_amt'].widget.attrs.update({'class' : 'form-control'})
		self.fields['food_amt'].widget.attrs['required'] = True
		self.fields['advance_amt'].widget.attrs.update({'class' : 'form-control'})
		self.fields['joining_date'].widget.attrs.update({'class' : 'form-control'})
		self.fields['joining_date'].widget.attrs['required'] = True
		self.fields['status'].widget.attrs.update({'class' : 'form-control'})
		self.fields['vacate_date'].widget.attrs.update({'class' : 'form-control'})