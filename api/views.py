from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.response import Response

from rest_framework import status

from rest_framework import authentication,permissions

from rest_framework.views import APIView

from django.db.models import Sum

from django.contrib.auth.models import User

from django.utils import timezone

from api.serializers import Userserializer,ExpenceSerializer,IncomeSerializer

from api.models import Expence,Income

from api.permissions import OwnerOnly

from datetime import datetime

# ApiView,Viewset,ModelViewSet


class SignUpView(viewsets.ViewSet):

    def create(self,request,*args,**kwargs):

        serializer=Userserializer(data=request.data) #deserializing

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ExpenceViewSet(viewsets.ModelViewSet):

    serializer_class=ExpenceSerializer

    # queryset=Expence.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)
    
    # def get_queryset(self):

    #     return Expence.objects.filter(owner=self.request.user)
    
                        #  OR override the list() method

    def list(self,request,*args,**kwargs):

        qs=Expence.objects.filter(owner=request.user)

        if 'month' in request.query_params:

            month=request.query_params.get('month')

            qs=qs.filter(created_date__month=month)
            
        if 'year' in request.query_params:

            year=request.query_params.get('year')

            qs=qs.filter(created_date__year=year)

        if 'category' in request.query_params:

            category=request.query_params.get('category')

            qs=qs.filter(category=category)

        if 'priority' in request.query_params:

            priority=request.query_params.get('priority')

            qs=qs.filter(priority=priority)

        if len(request.query_params.keys())==0:

            current_month=timezone.now().month
    
            current_year=timezone.now().year
    
            qs=Expence.objects.filter(created_date__month=current_month,
                                      created_date__year=current_year)
    
        serializer=ExpenceSerializer(qs,many=True)

        return Response(data=serializer.data)

class ExpenceSummaryView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        if 'start_date' in request.query_params and 'end_date' in request.query_params:

            start_date=datetime.strptime(request.query_params.get('start_date'),'%Y-%m-%d').date()

            end_date=datetime.strptime(request.query_params.get('end_date'),'%Y-%m-%d').date()

            all_expences=Expence.objects.filter(owner=request.user,
                                                created_date__range=(start_date,end_date))

        else:
            current_month=timezone.now().month

            current_year=timezone.now().year
    
            all_expences=Expence.objects.filter(owner=request.user,
                                                created_date__month=current_month,
                                                created_date__year=current_year)
            
        total_expence=all_expences.values('amount').aggregate(Total=Sum('amount'))['Total']  #['Total'] is to display only the amount
        
        category_summary=all_expences.values('category').annotate(Total=Sum('amount')).order_by('-Total')

        priority_summary=all_expences.values('priority').annotate(Total=Sum('amount')).order_by('-Total')

        data={
            'expence_total':total_expence,
            'category_summary':category_summary,
            'priority_summary':priority_summary
        }  # datas can be transfered through this dictionary

        return Response(data=data)

class IncomeViewSet(viewsets.ModelViewSet):

    serializer_class=IncomeSerializer

    # queryset=Income.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]


    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):

        qs=Income.objects.filter(owner=request.user)

        if 'month' in request.query_params:

            month=request.query_params.get('month')

            qs=qs.filter(created_date__month=month)
        
        if 'year' in request.query_params:

            year=request.query_params.get('year')

            qs=qs.filter(created_date__year=year)

        if 'category' in request.query_params:

            category=request.query_params.get('category')

            qs=qs.filter(category=category)

        if 'priority' in request.query_params:

            priority=request.query_params.get('priority')

            qs=qs.filter(priority=priority)

        if len(request.query_params.keys())==0:

            current_month=timezone.now().month

            current_year=timezone.now().year

            qs=qs.filter(created_date__month=current_month,
                         created_date__year=current_year)
            
        serializer=IncomeSerializer(qs,many=True)

        return Response(data=serializer.data) 

class IncomeSummaryView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        if 'start_date' in request.query_params and 'end_date' in request.query_params:
           
            start_date=datetime.strptime(request.query_params.get('start_date'),'%Y-%m-%d').date()
            
            end_date=datetime.strptime(request.query_params.get('end_date'),'%Y-%m-%d').date()
            
            all_income=Income.objects.filter(owner=request.user,
                                            created_date__range=(start_date,end_date))

        else:

            current_month=timezone.now().month
    
            current_year=timezone.now().year
    
            all_income=Income.objects.filter(owner=request.user,
                                             created_date__month=current_month,
                                             created_date__year=current_year)
            
        total_incomes=all_income.values('amount').aggregate(Total=Sum('amount'))['Total']
        
        category_summary=all_income.values('category').annotate(Total=Sum('amount')).order_by('-Total')

        data={
            'incomes_total':total_incomes,
            'category_summary':category_summary
        }

        return Response(data=data)

        


