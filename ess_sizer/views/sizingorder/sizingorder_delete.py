from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorder

class sizingorderDeleteView(DeleteView):
    model = sizingorder
    template_name = "sizingorder/sizingorder_delete.html"
    success_url = reverse_lazy('sizingorder_list')