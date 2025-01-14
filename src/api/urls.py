from django.urls import path

from api.views import StoreListView, VisitCreateView

urlpatterns = [
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("visits/", VisitCreateView.as_view(), name="visit-create"),
]
