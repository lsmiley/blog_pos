from django.views.generic import DetailView

from ess_sizer.models import sizingorder


class sizingorderDetailView(DetailView):
    model = sizingorder
    template_name = "sizingorder/sizingorder_detail.html"
