from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ess_sizer.models import sizingorderitem

class sizingorderitemCreateView(CreateView):
    model = sizingorderitem
    fields = '__all__'
    template_name = "sizingorderitem/sizingorderitem_create.html"
    success_url = reverse_lazy('sizingorderitem_list')
