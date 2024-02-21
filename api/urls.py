from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register("employee",views.Employeeviewset,basename="employee")

urlpatterns = [
    path('', include(router.urls)),
]
