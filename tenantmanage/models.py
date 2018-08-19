from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class TenantDetails(models.Model):
	first_name = models.CharField(null=True,blank=True,max_length=320)
	last_name = models.CharField(null=True,blank=True,max_length=320)
	pg_name = models.CharField(null=True,blank=True,max_length=320)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '999999999'. Up to 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)
	email = models.EmailField(max_length=520,null=True,blank=True)
	address = models.TextField(null=True,blank=True)
	height_field = models.IntegerField(null=True, blank=True)
	width_field = models.IntegerField(null=True, blank=True)
	adhar_img = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
	height_field1 = models.IntegerField(null=True, blank=True)
	width_field1 = models.IntegerField(null=True, blank=True)
	pan_img = models.ImageField(null=True, blank=True, width_field="width_field1", height_field="height_field1")
	room_no = models.CharField(max_length=50,null=True, blank=True)
	occupatin = models.CharField(max_length=320,null=True, blank=True)
	rent = models.IntegerField(null=True, blank=True)
	food_choices = (('Yes', 'Yes'), ('No', 'No'))
	food_required = models.CharField(null=True, blank=True,max_length=100,choices=food_choices,default=food_choices[0][0])
	food_amt = models.IntegerField(null=True, blank=True)
	advance_amt = models.IntegerField(null=True, blank=True)
	joining_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
	status_choices = (('Active', 'Active'), ('Inactive', 'Inactive'))
	status = models.CharField(null=True, blank=True,max_length=100,choices=status_choices,default=status_choices[0][0])
	vacate_date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
	log_date = models.DateField(auto_now=False, auto_now_add=True,null=True)

	def __str__(self):
		return self.first_name