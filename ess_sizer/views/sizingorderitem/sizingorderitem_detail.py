from django.views.generic import DetailView

from ess_sizer.models import sizingorderitem


class sizingorderitemDetailView(DetailView):
    model = sizingorderitem
    template_name = "sizingorderitem/sizingorderitem_detail.html"
