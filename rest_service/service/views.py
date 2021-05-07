from django.views.generic import View
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer


class CompaniesDataView(generics.ListCreateAPIView):
    serializer_class = DataSerializer

    def get_queryset(self):
        queryset = Data.objects.all().order_by('-date')
        company_name = self.request.query_params.get('company')
        if company_name is not None:
            queryset = queryset.filter(company=company_name)
        return queryset.order_by('-date')


class CompanyDataView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
