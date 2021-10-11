from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorder

class sizingorderUpdateView(UpdateView):
    model = sizingorder
    fields = '__all__'
    template_name = "sizingorder/sizingorder_update.html"
    success_url = reverse_lazy('sizingorder_list')
