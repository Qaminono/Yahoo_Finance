from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompaniesDataView, CompanyDataView

urlpatterns = [
    path('', CompaniesDataView.as_view(), name='all_data'),
    path('<int:pk>', CompanyDataView.as_view(), name='data_by_pk')
]

urlpatterns = format_suffix_patterns(urlpatterns)
