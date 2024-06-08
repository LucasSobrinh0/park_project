from rest_framework import generics, status
from rest_framework.response import Response
from .models import Driver, Vehicle, EntryRegister, ParkingSpot, ExitRegister
from .serializers import DriverSerializer, VehicleSerializer, EntryRegisterSerializer, ExitRegisterSerializer, ParkingSpotSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

"""Esse é o arquivo onde criamos as funcionalidades da api"""

# Classe base para as operações relacionadas aos motoristas
class DriverBaseView(generics.GenericAPIView):
    queryset = Driver.objects.all()  # Queryset para operações de busca
    serializer_class = DriverSerializer  # Serializador para operações de serialização/deserialização
    permission_classes = [IsAuthenticated, IsAdminUser] # Variavel utilizada para não permitir acesso de usuario deslogado e não administrador

# Endpoint para criação de motoristas
class DriverCreateView(DriverBaseView, generics.CreateAPIView):
    pass

# Endpoint para listagem de motoristas
class DriverListView(DriverBaseView, generics.ListAPIView):
    pass

# Endpoint para atualização de dados de motoristas
class DriverUpdateveView(DriverBaseView, generics.RetrieveUpdateAPIView):
    pass

# Endpoint para remoção de motoristas
class DriverDestroyView(DriverBaseView, generics.DestroyAPIView):
    pass

# Classe base para operações relacionadas aos veículos
class VehicleBaseView(generics.GenericAPIView):
    queryset = Vehicle.objects.all()  # Queryset para operações de busca
    serializer_class = VehicleSerializer  # Serializador para operações de serialização/deserialização
    permission_classes = [IsAuthenticated, IsAdminUser]

# Endpoint para criação de veículos
class VehicleCreateView(VehicleBaseView, generics.CreateAPIView):
    pass

# Endpoint para listagem de veículos
class VehicleListView(VehicleBaseView, generics.ListAPIView):
    pass

# Endpoint para atualização de dados de veículos
class VehicleUpdateView(VehicleBaseView, generics.RetrieveUpdateAPIView):
    pass

# Endpoint para remoção de veículos
class VehicleDestroyView(VehicleBaseView, generics.DestroyAPIView):
    pass

# Classe base para operações relacionadas aos registros de entrada
class EntryRegisterBaseView(generics.GenericAPIView):
    queryset = EntryRegister.objects.all()  # Queryset para operações de busca
    serializer_class = EntryRegisterSerializer  # Serializador para operações de serialização/deserialização
    permission_classes = [IsAuthenticated, IsAdminUser]

# Endpoint para criação de registros de entrada
class EntryRegisterCreateView(generics.CreateAPIView):
    queryset = EntryRegister.objects.all()
    serializer_class = EntryRegisterSerializer

    # Método personalizado para criação de registros de entrada
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Verifica se a vaga de estacionamento está ocupada
            vehicle_entry = serializer.validated_data['vehicle_entry']
            parking_spot = vehicle_entry.parking_spot
            if parking_spot.is_occupied:
                return Response({"error": "A vaga está ocupada."}, status=status.HTTP_400_BAD_REQUEST)
            # Marca a vaga como ocupada
            parking_spot.is_occupied = True
            parking_spot.save()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para listagem de registros de entrada
class EntryRegisterListView(EntryRegisterBaseView, generics.ListAPIView):
    pass

# Endpoint para atualização de registros de entrada
class EntryRegisterUpdateView(EntryRegisterBaseView, generics.RetrieveUpdateAPIView):
    pass

# Endpoint para remoção de registros de entrada
class EntryRegisterDestroyView(EntryRegisterBaseView, generics.DestroyAPIView):
    pass

# Classe base para operações relacionadas às vagas de estacionamento
class ParkingSpotBaseView(generics.GenericAPIView):
    queryset = ParkingSpot.objects.all()  # Queryset para operações de busca
    serializer_class = ParkingSpotSerializer  # Serializador para operações de serialização/deserialização
    permission_classes = [IsAuthenticated, IsAdminUser]

# Endpoint para criação de vagas de estacionamento
class ParkingSpotCreateView(ParkingSpotBaseView, generics.CreateAPIView):
    pass

# Endpoint para listagem de vagas de estacionamento
class ParkingSpotListView(ParkingSpotBaseView, generics.ListAPIView):
    pass

# Endpoint para busca de detalhes de uma vaga de estacionamento específica
class ParkingSpotRetrieveView(ParkingSpotBaseView, generics.RetrieveAPIView):
    pass

# Endpoint para remoção de vagas de estacionamento
class ParkingSpotDestroyView(ParkingSpotBaseView, generics.DestroyAPIView):
    pass

# Classe base para operações relacionadas aos registros de saída
class ExitRegisterBaseView(generics.GenericAPIView):
    queryset = ExitRegister.objects.all()  # Queryset para operações de busca
    serializer_class = ExitRegisterSerializer  # Serializador para operações de serialização/deserialização
    permission_classes = [IsAuthenticated, IsAdminUser]

# Endpoint para criação de registros de saída
class ExitRegisterCreateView(generics.CreateAPIView):
    queryset = ExitRegister.objects.all()
    serializer_class = ExitRegisterSerializer

    # Método personalizado para criação de registros de saída
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Verifica se a vaga de estacionamento está ocupada
            entry_register = serializer.validated_data['entry']
            parking_spot = entry_register.vehicle_entry.parking_spot
            if not parking_spot.is_occupied:
                return Response({"error": "Não há veículo estacionado nesta vaga."}, status=status.HTTP_400_BAD_REQUEST)
            # Marca a vaga como desocupada
            parking_spot.is_occupied = False
            parking_spot.save()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint para listagem de registros de saída
class ExitRegisterListView(ExitRegisterBaseView, generics.ListAPIView):
    pass

# Endpoint para atualização de registros de saída
class ExitRegisterUpdateView(ExitRegisterBaseView, generics.RetrieveUpdateAPIView):
    pass

# Endpoint para remoção de registros de saída
class ExitRegisterDestroyView(ExitRegisterBaseView, generics.DestroyAPIView):
    pass
