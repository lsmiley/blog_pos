from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorderitem

class sizingorderitemUpdateView(UpdateView):
    model = sizingorderitem
    fields = '__all__'
    template_name = "sizingorderitem/sizingorderitem_update.html"
    success_url = reverse_lazy('sizingorderitem_list')
