from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetailClassView(DetailView):
    model = Item
    template_name = 'food/details.html'


class AddClassView(CreateView):
    model = Item
    template_name = 'food/add_item_form.html'
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    


class UpdateClassView(UpdateView):
    model = Item
    template_name = 'food/add_item_form.html'
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    success_url = reverse_lazy('food:index')


class DeleteClassView(DeleteView):
    model = Item
    template_name = 'food/delete_item.html'
    success_url = reverse_lazy('food:index')


