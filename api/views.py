from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta, date
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.

class ReferByViewSet(viewsets.ModelViewSet):
    serializer_class = ReferBySerializer

# LOGIN/REGISTER VIEWS <--.

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def Login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def Register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    else :
        return Response("Error")

# LOGIN / REGISTER -->

# PATIENT VIEWS <--

class PatientViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Patient.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = PatientSerializer        

class PatientDateViewSet(APIView):
    serializer_class = PatientSerializer
    
    def get(self, request, pk):
        try :
            startdate = pk
            startDate = datetime.strptime(startdate, '%Y-%m-%d')
            enddate = startDate + timedelta(days=365)
            endDate = enddate.strftime('%Y-%m-%d')
            queryset = Patient.objects.filter(
                created_at__range=[pk, endDate])
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data)
        except :
            return Response('Not found!')

class PatientPrimaryDiagnosisViewSet(APIView):
    serializer_class = PrimaryDiagnosisSerializer

    def get(self, request, pk):
        try:
            queryset = PrimaryDiagnosis.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not found!')


  
class PrimaryDiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = PrimaryDiagnosisSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = PrimaryDiagnosis.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])


class PatientAllergiesViewSet(APIView):
    serializer_class = PatientAllergiesSerializer

    def get(self, request, pk):
        try :
            queryset = PatientAllergies.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not found!')

class AllergiesViewSet(viewsets.ModelViewSet):
    serializer_class = PatientAllergiesSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = PatientAllergies.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])


class PatientCurrentOperativePlanViewSet(APIView):
    serializer_class = CurrentOperativePlanSerializer

    def get(self, request, pk):
        try:
            queryset = CurrentOperativePlan.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not Found!')



class CurrentOperativePlanViewSet(viewsets.ModelViewSet):
    serializer_class = CurrentOperativePlanSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = CurrentOperativePlan.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])



class PatientNotesViewSet(APIView):
    serializer_class = PatientNotesSerializer

    def get(self, request, pk):
        try :
            queryset = PatientNotes.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not found!')


class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = PatientNotesSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = PatientNotes.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])


class PatientSurgeryViewSet(APIView):
    serializer_class = PatientSurgerySerializer

    def get(self, request, pk):
        try:
            queryset = PatientSurgery.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not found!')



class SurgeryViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSurgerySerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = PatientSurgery.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])


class PatientVisitViewSet(APIView):
    serializer_class = PatientVisitSerializer

    def get(self, request, pk):
        try:
            queryset = PatientVisit.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('Not found!')



class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = PatientVisitSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = PatientVisit.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])



class CheckOutViewSet(APIView):
    serializer_class = PatientVisitSerializer

    def get(self,request,pk):
        try:
            queryset = PatientVisit.objects.filter(patient=pk).latest('id')
        except:
            return Response('Not found!')
        serializer = self.serializer_class(queryset)
        return Response(data=serializer.data)

    def put(self, request, pk, format=None):
        try :
            snippet = PatientVisit.objects.filter(patient=pk).latest('id')
        except:
            return Response('Not found!')
        serializer = self.serializer_class(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, "Updated succesfully!")

    def delete(self, request, pk, format=None):
        snippet = PatientVisit.objects.id(id=pk)
        snippet.delete()
        return Response("Deleted succesfully!")


class PatientTypeViewSet(viewsets.ModelViewSet):
    queryset = TypePatient.objects.all()
    serializer_class = PatientTypeSerializer

class PatientTypeListViewSet(APIView):
    serializer_class = PatientTypeSerializer

    def get(self,request):
        try:
            queryset = TypePatient.objects.all()
            serializer = self.serializer_class(data=queryset,many=True)
            return Response(data=serializer.data)
        except:
            return Response('Not found!')

class PatientAppointmentViewSet(APIView): # PatientAppointment id get data.
    serializer_class = PatientAppointMentSerializers

    def get(self, request, pk):
        try:
            queryset = PatientAppointment.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except :
            return Response('Not found!')


class AppointmentViewSet(viewsets.ModelViewSet): # PatientAppointment get all data and post.
    serializer_class = PatientAppointMentSerializers
    queryset = PatientAppointment.objects.all()


class EmergencyViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Emergency.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = EmergencySerializer


class EmergencyDateViewSet(APIView):
    serializer_class = EmergencySerializer

    def get(self, request, pk):
        try:
            startdate = pk
            startDate = datetime.strptime(startdate, '%Y-%m-%d')
            enddate = startDate + timedelta(days=365)
            endDate = enddate.strftime('%Y-%m-%d')
            queryset = Emergency.objects.filter(date__range=[pk, endDate])
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data)
        except:
            return Response('Not found!')

class EmergencyPatientViewSet(APIView):
    serializer_class = EmergencySerializer

    def get(self,request,pk):
        try:
            emergency = Emergency.objects.filter(patientImpacted=pk)
            serializer = self.serializer_class(emergency,many=True)
            return Response(data=serializer.data)

        except:
            return Response('Nt found!')



# PATIENT VIEWS -->

# BILLING VIEWS <--

class ChargePatientViewSet(APIView):
    serializer_class = ChargeSerializer

    def get(self, request, pk):
        try:
            charges = Charge.objects.filter(patientId=pk)
            serializer = self.serializer_class(charges, many=True)
            return Response(data=serializer.data)

        except:
            return Response('Nt found!')

    


class ChargeViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Charge.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = EmergencySerializer


class PaymentViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Payment.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = PaymentSerializer


class PaymentPatientViewSet(APIView):
    serializer_class = PaymentSerializer

    def get(self, request, pk):
        try:
            payment = Payment.objects.filter(patientID=pk)
            serializer = self.serializer_class(payment, many=True)
            return Response(data=serializer.data)

        except:
            return Response('Nt found!')




class BillViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Bill.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = BillSerializer


class BillPatientViewSet(APIView):
    serializer_class = BillSerializer

    def get(self, request, pk):
        try:
            queryset = Bill.objects.filter(patient=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data)

        except:
            return Response('Nt found!')

# BILLING -->

# Laboratory <--
class SampleViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Sample.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = SampleSerializer

class PatientSampleViewSet(APIView):
    serializer_class = SampleSerializer

    def get(self,request,pk):
        try:
            queryset = Sample.objects.filter(patientId=pk)
            serializer = SampleSerializer(queryset,many=True)
            return Response(data=serializer.data)
        except:
            return Response('Not found!')
    

class SampleTypeTestViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTypeTestSerializer
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = SampleTypeTest.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])


class SampleSampleTypeTestViewSet(APIView):
    serializer_class = SampleTypeTestSerializer_2

    def get(self,request,pk):
        try:
            queryset = SampleTypeTestSerializer.objects.get(sampleId=pk)
            serializer = self.serializer_class(queryset)
            return Response(data=serializer.data)
        except:
            return Response('Not found!')

    def put(self,request,pk):
        obj = SampleTypeTest.objects.get(id=pk)
        
        serializer = SampleTypeTestSerializer_2(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        

class SampleTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTypeSerializer
    queryset = SampleType.objects.all()



class SampleTestViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTestSerializer
    queryset = SampleTest.objects.all()

class TypeSampleTestViewSet(APIView):
    serializer_class = SampleTestSerializer
    
    def get(self,request,pk):
        try:
            queryset = SampleTest.objects.filter(sampleType=pk)
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data)
        except:
            return Response('Not found!')



# Laboratory -->






