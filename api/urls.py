from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patient', views.PatientViewSet, basename='patient')
router.register(r'charge', views.ChargeViewSet, basename='charge')
router.register(r'payment', views.PaymentViewSet, basename='payment')
router.register(r'emergency', views.EmergencyViewSet, basename='emergency')
router.register(r'bill', views.BillViewSet, basename='bill')
router.register(r'patientType', views.PatientTypeViewSet,
                basename='patientType')

urlpatterns = [
    path('', include(router.urls)),
    path('patientDate/<str:pk>/', views.PatientDateViewSet.as_view()),

    path('chargePatient/<str:pk>/', views.ChargePatientViewSet.as_view()),
    path('paymentPatient/<str:pk>/', views.PaymentPatientViewSet.as_view()),
    path('paymentPost/', views.PaymentPostViewSet.as_view()),

    path('billPatient/<str:pk>/', views.BillPatientViewSet.as_view()),

    path('emergency/<str:pk>/', views.EmergencyDateViewSet.as_view()),

    path('primaryDiagnosis/<str:pk>/',
         views.PrimaryDiagnosisViewSet.as_view()),
    path('primaryDiagnosis/',
         views.PrimaryDiagnosisPostViewSet.as_view()),

    path('patientAllergies/<str:pk>/', views.PatientAllergiesViewSet.as_view()),
    path('patientAllergies/', views.PatientAllergiesPostViewSet.as_view()),

    path('currentOperativePlan/<str:pk>/',
         views.CurrentOperativePlanViewSet.as_view()),
    path('currentOperativePlan/',
         views.CurrentOperativePlanPostViewSet.as_view()),

    path('patientNote/<str:pk>/',
         views.PatientNotesViewSet.as_view()),
    path('patientNote/',
         views.PatientNotesPostViewSet.as_view()),

    path('patientSurgery/<str:pk>/',
         views.PatientSurgeryViewSet.as_view()),
    path('patientSurgery/',
         views.PatientSurgeryPostViewSet.as_view()),

    path('patientVisit/<str:pk>/',
         views.PatientVisitViewSet.as_view()),
    path('patientVisit/',
         views.PatientVisitPostViewSet.as_view()),

    path('patientAppointment/<str:pk>/',
         views.PatientAppointmentViewSet.as_view()),
    path('patientAppointment/',
         views.PatientAppointmentPostViewSet.as_view()),

]
