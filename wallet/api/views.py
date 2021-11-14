from rest_framework import viewsets
from rest_framework import status
from .serializers import WalletSerializer
from .permissions import IsUser ,IsOnBoard
from django.contrib.auth.models import User
from wallet.models import Wallet
from django.contrib.auth.mixins import LoginRequiredMixin  # we cannot user @login_requried decorators  on class views
from django.contrib.auth.mixins import UserPassesTestMixin
from users.on_board_mixin import IsOnBoardMixin
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUser,)
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


    @action(methods=['post'], detail=True, permission_classes=[IsUser],url_path='purchased', url_name='purchased')
    def purchased(self, request, pk=None):
        req_user = Wallet.objects.get(user = request.user)
       
        if int(request.data['Ammount']) <= req_user.Ammount :
            req_user.Ammount -= int(request.data['Ammount'])

            req_user.save()
            return Response(status = status.HTTP_201_CREATED)
        else :
            return Response(status = status.HTTP_400_BAD_REQUEST)    
        
    

    
    

