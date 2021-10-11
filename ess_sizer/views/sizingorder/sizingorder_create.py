from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorder

class sizingorderCreateView(CreateView):
    model = sizingorder
    fields = '__all__'
    template_name = "sizingorder/sizingorder_create.html"
    success_url = reverse_lazy('sizingorder_list')
