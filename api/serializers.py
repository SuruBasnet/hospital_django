from rest_framework import serializers
from .models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePatient
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)
        instance.cmp_id 
        cmpBasicInfo.objects.get(cmp_id)
        


class PrimaryDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDiagnosis
        fields = '__all__'


class PatientAllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAllergies
        fields = '__all__'


class CurrentOperativePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentOperativePlan
        fields = '__all__'


class PatientNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientNotes
        fields = '__all__'


class PatientSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSurgery
        fields = '__all__'


class PatientVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisit
        fields = '__all__'


class PatientAppointMentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientAppointment
        fields = '__all__'


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'
        depth = 5

class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = '__all__'

class SampleTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTest
        fields = '__all__'
       

class SampleTypeTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTypeTest
        fields = '__all__'


class SampleTypeTestSerializer_2(serializers.ModelSerializer):
    class Meta:
        model = SampleTypeTest
        fields = '__all__'

class ReferBySerializer(serializers.ModelSerializer):
    class Meta:
        model = Referby
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')