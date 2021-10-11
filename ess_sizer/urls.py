from ess_sizer.views import sizingorderitemDeleteView
from ess_sizer.views import sizingorderitemUpdateView
from ess_sizer.views import sizingorderitemDetailView
from ess_sizer.views import sizingorderitemCreateView
from ess_sizer.views import sizingorderitemListView
from ess_sizer.views import sizingorderDeleteView
from ess_sizer.views import sizingorderUpdateView
from ess_sizer.views import sizingorderDetailView
from ess_sizer.views import sizingorderCreateView
from ess_sizer.views import sizingorderListView
path('sizingorder/list/', sizingorderListView.as_view(), name='sizingorder_list')
path('sizingorder/create/', sizingorderCreateView.as_view(), name='sizingorder_create')
path('sizingorder/detail/<int:pk>/', sizingorderDetailView.as_view(), name='sizingorder_detail')
path('sizingorder/update/<int:pk>/', sizingorderUpdateView.as_view(), name='sizingorder_update')
path('sizingorder/delete/<int:pk>/', sizingorderDeleteView.as_view(), name='sizingorder_delete')
path('sizingorderitem/list/', sizingorderitemListView.as_view(), name='sizingorderitem_list')
path('sizingorderitem/create/', sizingorderitemCreateView.as_view(), name='sizingorderitem_create')
path('sizingorderitem/detail/<int:pk>/', sizingorderitemDetailView.as_view(), name='sizingorderitem_detail')
path('sizingorderitem/update/<int:pk>/', sizingorderitemUpdateView.as_view(), name='sizingorderitem_update')
path('sizingorderitem/delete/<int:pk>/', sizingorderitemDeleteView.as_view(), name='sizingorderitem_delete')
