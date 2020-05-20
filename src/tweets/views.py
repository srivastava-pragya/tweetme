from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
	DeleteView, DetailView, ListView, CreateView, UpdateView
	)
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

# Create
class TweetCreateView(FormUserNeededMixin, CreateView):
	#queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = "/tweet/create"
	#login_url = '/admin/'
	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated:
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
	# 		return self.form_invalid(form)


# def tweet_create_view(request):
# 	form = TweetModelForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.user = request.user
# 		instance.save()
# 	context = {
# 		"form":form
# 	}
# 	return render(request,'tweets/create_view.html', context)

#update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/update_view.html'
	success_url = "/tweet/"

#delete
class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
	model = Tweet
	template_name = 'tweets/delete_confirm.html'
	success_url = reverse_lazy("home")

#Retrieve
class TweetDetailView(DetailView):
	#template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()
	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	# 	obj = get_object_or_404(Tweet, pk=pk)
	# 	return obj

class TweetListView(ListView):
	#template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()
	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context

def tweet_detail_view(request, pk=None):
	#return render(request, "tweets/detail_view.html",{})
	#obj = Tweet.objects.get(pk=pk) #get from database
	obj = get_object_or_404(Tweet, pk=pk)
	print(obj)
	context = { "object": obj }
	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj.content)
# 	context = { "object_list": queryset }
# 	return render(request, "tweets/list_view.html", context)	
