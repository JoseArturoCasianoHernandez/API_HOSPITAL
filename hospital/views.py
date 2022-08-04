from rest_framework import viewsets

from .models import Medico
from .serializers import MedicoSerializers

from .models import Paciente
from .serializers import PacienteSerializers

from .models import Historia
from .serializers import HistoriaSerializers

from .models import PacienteCama
from .serializers import PacienteCamaSerializers

from .models import Cama
from .serializers import CamaSerializers

from .models import Planta
from .serializers import PlantaSerializers

from .models import VisitaMedica
from .serializers import VisitaMedicaSerializers


# Create your views here.
class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializers
    queryset = Medico.objects.all()


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializers
    queryset = Paciente.objects.all()


class HistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = HistoriaSerializers
    queryset = Historia.objects.all()


class PacienteCamaViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteCamaSerializers
    queryset = PacienteCama.objects.all()


class CamaViewSet(viewsets.ModelViewSet):
    serializer_class = CamaSerializers
    queryset = Cama.objects.all()


class PlantaViewSet(viewsets.ModelViewSet):
    serializer_class = PlantaSerializers
    queryset = Planta.objects.all()


class VisitaMedicaViewSet(viewsets.ModelViewSet):
    serializer_class = VisitaMedicaSerializers
    queryset = VisitaMedica.objects.all()
