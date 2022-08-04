from rest_framework import serializers
from hospital.models import Medico, Paciente, Historia, PacienteCama, Cama, Planta, VisitaMedica


class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class HistoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'


class PacienteCamaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PacienteCama
        fields = '__all__'


class CamaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cama
        fields = '__all__'


class PlantaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = '__all__'


class VisitaMedicaSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisitaMedica
        fields = '__all__'
