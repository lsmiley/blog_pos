from django.views.generic import ListView

from ess_sizer.models import sizingorder

class sizingorderListView(ListView):
    model = sizingorder
    template_name = "sizingorder/sizingorder_list.html"
