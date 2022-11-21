from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patient', views.PatientViewSet, basename='patient')       # Patient
router.register(r'primaryDiagnosis', views.PrimaryDiagnosisViewSet, basename='primaryDiagnosis') # Patient
router.register(r'allergies', views.AllergiesViewSet, basename='allergy') # Patient
router.register(r'currentOperativePlan', views.CurrentOperativePlanViewSet, basename='currentOperativePlan') # Patient
router.register(r'note', views.NotesViewSet, basename='note') # Patient
router.register(r'surgery', views.SurgeryViewSet, basename='surgery') # Patient
router.register(r'appointment', views.AppointmentViewSet, basename='appointment') # Patient
router.register(r'visit', views.VisitViewSet, basename='visit') # Patient
router.register(r'emergency', views.EmergencyViewSet, basename='emergency') # Patient
router.register(r'charge', views.ChargeViewSet, basename='charge')          # Billing
router.register(r'payment', views.PaymentViewSet, basename='payment')       # Billing
router.register(r'bill', views.BillViewSet, basename='bill')                # Billing
router.register(r'patientType', views.PatientTypeViewSet,                   # PatientType
                basename='patientType')
router.register(r'referBy', views.ReferByViewSet,                           # ReferBy
                basename='referBy')
router.register(r'sample', views.SampleViewSet,           # Laboratory
                basename='sample')
router.register(r'sampleTypeTest', views.SampleTypeTestViewSet,    # Laboratory
                basename='sampleTypeTest')
router.register(r'sampleType', views.SampleTypeViewSet,   # Laboratory
                basename='sampleType')
router.register(r'sampleTest', views.SampleTestViewSet,   # Laboratory
                basename='sampleTest')

urlpatterns = [
    path('', include(router.urls)),

    # LOGIN/REGISTER ---------------------------------------------------
    path('login/', views.Login, name='LoginPage'),
    path('register/', views.Register, name='RegisterPage'),
    # LOGIN/REGISTER ---------------------------------------------------

    # PATIENT ---------------------------------------------------
    path('patientDate/<str:pk>/', views.PatientDateViewSet.as_view()),
    path('patientPrimaryDiagnosis/<str:pk>/',
         views.PatientPrimaryDiagnosisViewSet.as_view()),

    path('patientAllergies/<str:pk>/', views.PatientAllergiesViewSet.as_view()),

    path('patientCurrentOperativePlan/<str:pk>/',
         views.PatientCurrentOperativePlanViewSet.as_view()),


    path('patientNote/<str:pk>/',
         views.PatientNotesViewSet.as_view()),

    path('patientSurgery/<str:pk>/',
         views.PatientSurgeryViewSet.as_view()),

    path('patientVisit/<str:pk>/',
         views.PatientVisitViewSet.as_view()),

    path('patientCheckout/<str:pk>/',views.CheckOutViewSet.as_view()),

    path('patientType/',views.PatientTypeListViewSet.as_view()),


    path('patientAppointment/<str:pk>/',
         views.PatientAppointmentViewSet.as_view()),
    path('emergency/<str:pk>/', views.EmergencyDateViewSet.as_view()),
    path('emergencyPatient/<str:pk>/', views.EmergencyPatientViewSet.as_view()),
    # PATIENT ---------------------------------------------------

    # BILLING ---------------------------------------------------
    path('chargePatient/<str:pk>/', views.ChargePatientViewSet.as_view()),

    path('paymentPatient/<str:pk>/', views.PaymentPatientViewSet.as_view()),

    path('billPatient/<str:pk>/', views.BillPatientViewSet.as_view()),
    # BILLING ---------------------------------------------------

    # LABORATORY ---------------------------------------------------

    path('typeSampleTest/<str:pk>/',views.TypeSampleTestViewSet.as_view()),
    path('patientSample/<str:pk>/',views.PatientSampleViewSet.as_view()),
    path('sampleSampleTypeTest/<str:pk>/',views.SampleSampleTypeTestViewSet.as_view()),

]
