from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorderitem

class sizingorderitemDeleteView(DeleteView):
    model = sizingorderitem
    template_name = "sizingorderitem/sizingorderitem_delete.html"
    success_url = reverse_lazy('sizingorderitem_list')