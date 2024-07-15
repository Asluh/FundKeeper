from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

from api.views import *



router=DefaultRouter()
router.register('register',SignUpView,basename='users')
router.register('expenses',ExpenceViewSet,basename='expenses')
router.register('incomes',IncomeViewSet,basename='incomes')




urlpatterns = [
    path('token/',ObtainAuthToken.as_view(),name='token'),
    path('expenses/summary/',ExpenceSummaryView.as_view(),name='exp_summary'),
    path('incomes/summary/',IncomeSummaryView.as_view(),name='inc_summary'),
]+router.urls