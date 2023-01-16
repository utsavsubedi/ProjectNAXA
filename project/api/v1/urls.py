from django.urls import include, path
from rest_framework import routers
from api.v1.views import FileUploadView, ProjectListView, SummaryView, CounterView

router = routers.DefaultRouter()
# router.register(r'excel-upload', views.excel_upload)

urlpatterns = [
    path('', include(router.urls)),
    path('excel-upload/', FileUploadView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('summary/', SummaryView.as_view()),
    path('counts/', CounterView.as_view()),
]