from rest_framework import generics
from base.models import ModelOneForTest as MOFT, ModelTwoForTest as MFTF
from .serializers import ModelOneSerializer as MOS, ModelTwoSerializer as MTS

class MOFTList(generics.ListCreateAPIView):
    serializer_class = MOS
    
    def get_queryset(self):
        queryset = MOFT.objects.all()
        two = self.request.query_params.get('two')
        if two is not None:
            queryset = queryset.filter(two_to_one = two)
        return queryset
    
class MFTFList(generics.ListCreateAPIView):
    serializer_class = MTS
    queryset = MFTF.objects.all()