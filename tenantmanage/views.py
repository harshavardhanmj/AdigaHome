from django.shortcuts import render
from .models import TenantDetails
from .forms import TenantForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
# Create your views here.

class TenantListView(ListView):
	queryset = TenantDetails.objects.all()
	template_name = "tenantSearchList.html"


class TenantCreateView(CreateView):
	template_name = "tenantCreateForm.html"
	form_class = TenantForm
	success_url = '/'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.adhar_img = self.request.FILES['adhar_img']
		obj.pan_img = self.request.FILES['pan_img']
		obj.save()
		return super(TenantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(TenantCreateView, self).get_context_data(*args, **kwargs)
		context["Action"] = "Add"
		return context

class TenantUpdateView(UpdateView):
	queryset = TenantDetails.objects.all()
	template_name = "tenantCreateForm.html"
	form_class = TenantForm
	success_url = '/'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.adhar_img = self.request.FILES['adhar_img']
		obj.pan_img = self.request.FILES['pan_img']
		obj.save()
		return super(TenantUpdateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(TenantUpdateView, self).get_context_data(*args, **kwargs)
		context["Action"] = "Update"
		return context