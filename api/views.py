from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta, date

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Patient.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = PatientSerializer


class PatientDateViewSet(APIView):
    serializer_class = PatientSerializer

    def get(self, request, pk):
        startdate = pk
        startDate = datetime.strptime(startdate, '%Y-%m-%d')
        enddate = startDate + timedelta(days=365)
        endDate = enddate.strftime('%Y-%m-%d')
        queryset = Patient.objects.filter(
            created_at__range=[pk, endDate])
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)


class PrimaryDiagnosisViewSet(APIView):
    serializer_class = PrimaryDiagnosisSerializer

    def get(self, request, pk):
        queryset = PatientAllergies.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PrimaryDiagnosisPostViewSet(APIView):
    serializer_class = PrimaryDiagnosisSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class PatientAllergiesViewSet(APIView):
    serializer_class = PatientAllergiesSerializer

    def get(self, request, pk):
        queryset = PatientAllergies.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PatientAllergiesPostViewSet(APIView):
    serializer_class = PatientAllergiesSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class CurrentOperativePlanViewSet(APIView):
    serializer_class = CurrentOperativePlanSerializer

    def get(self, request, pk):
        queryset = CurrentOperativePlan.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CurrentOperativePlanPostViewSet(APIView):
    serializer_class = CurrentOperativePlanSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class PatientNotesViewSet(APIView):
    serializer_class = PatientNotesSerializer

    def get(self, request, pk):
        queryset = PatientNotes.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PatientNotesPostViewSet(APIView):
    serializer_class = PatientNotesSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class PatientSurgeryViewSet(APIView):
    serializer_class = PatientSurgerySerializer

    def get(self, request, pk):
        queryset = PatientSurgery.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PatientSurgeryPostViewSet(APIView):
    serializer_class = PatientSurgerySerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class PatientVisitViewSet(APIView):
    serializer_class = PatientVisitSerializer

    def get(self, request, pk):
        queryset = PatientVisit.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PatientVisitPostViewSet(APIView):
    serializer_class = PatientVisitSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class PatientTypeViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientTypeSerializer


class PatientAppointmentViewSet(APIView):
    serializer_class = PatientAppointMentSerializers

    def get(self, request, pk):
        queryset = PatientAppointment.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PatientAppointmentPostViewSet(APIView):
    serializer_class = PatientAppointMentSerializers

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response('Data not valid!')


class EmergencyViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Emergency.objects.filter(
        created_at__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = EmergencySerializer


class EmergencyDateViewSet(APIView):
    serializer_class = EmergencySerializer

    def get(self, request, pk):
        startdate = pk
        startDate = datetime.strptime(startdate, '%Y-%m-%d')
        enddate = startDate + timedelta(days=365)
        endDate = enddate.strftime('%Y-%m-%d')
        queryset = Emergency.objects.filter(date__range=[pk, endDate])
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)


class ChargePatientViewSet(APIView):
    serializer_class = ChargeSerializer

    def get(self, request, pk):
        charges = Charge.objects.filter(patientId=pk)
        serializer = self.serializer_class(charges, many=True)
        return Response(data=serializer.data)


class ChargeViewSet(viewsets.ModelViewSet):
    serializer_class = ChargeSerializer
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentPatientViewSet(APIView):
    serializer_class = PaymentSerializer

    def get(self, request, pk):
        payment = Payment.objects.filter(patientID=pk)
        serializer = self.serializer_class(payment, many=True)
        return Response(data=serializer.data)


class PaymentPostViewSet(APIView):
    serializer_class = PaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)


class BillViewSet(viewsets.ModelViewSet):
    fiscalYear = FiscalYear.objects.latest('id')
    queryset = Bill.objects.filter(
        date__range=[fiscalYear.startdate, fiscalYear.enddate])
    serializer_class = BillSerializer


class BillPatientViewSet(APIView):
    serializer_class = BillSerializer

    def get(self, request, pk):
        queryset = Bill.objects.filter(patient__id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)

class SampleViewSet(viewsets.ModelViewSet):
    serializer_class = SampleSerializer

class SampleTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTypeSerializer

class SampleTestViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTestSerializer

class SampleTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SampleTypeTestSerializer

