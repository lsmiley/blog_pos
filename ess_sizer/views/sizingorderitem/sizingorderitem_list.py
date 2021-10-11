from django.views.generic import ListView

from ess_sizer.models import sizingorderitem

class sizingorderitemListView(ListView):
    model = sizingorderitem
    template_name = "sizingorderitem/sizingorderitem_list.html"
