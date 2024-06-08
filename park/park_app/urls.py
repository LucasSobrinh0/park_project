from django.urls import path
from . import views

urlpatterns = [
    # Endpoints relacionados aos motoristas
    path('drivers/', views.DriverListView.as_view(), name='driver-list'), # Lista os motoristas
    path('drivers/create/', views.DriverCreateView.as_view(), name='driver-create'), # Cria um motorista
    path('drivers/<int:pk>/', views.DriverUpdateveView.as_view(), name='driver-detail'), # Detalhes de um motorista específico
    path('drivers/<int:pk>/delete/', views.DriverDestroyView.as_view(), name='driver-delete'), # Remove um motorista

    # Endpoints relacionados aos veículos
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle-list'), # Lista os veículos
    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle-create'), # Cria um veículo
    path('vehicles/<int:pk>/', views.VehicleUpdateView.as_view(), name='vehicle-detail'), # Detalhes de um veículo específico
    path('vehicles/<int:pk>/delete/', views.VehicleDestroyView.as_view(), name='vehicle-delete'), # Remove um veículo

    # Endpoints relacionados aos registros de entrada
    path('entry-registers/', views.EntryRegisterListView.as_view(), name='entry-register-list'), # Lista os registros de entrada
    path('entry-registers/create/', views.EntryRegisterCreateView.as_view(), name='entry-register-create'), # Cria um registro de entrada
    path('entry-registers/<int:pk>/', views.EntryRegisterUpdateView.as_view(), name='entry-register-detail'), # Detalhes de um registro de entrada específico
    path('entry-registers/<int:pk>/delete/', views.EntryRegisterDestroyView.as_view(), name='entry-register-delete'), # Remove um registro de entrada

    # Endpoints relacionados às vagas de estacionamento
    path('parking-spots/', views.ParkingSpotListView.as_view(), name='parking-spot-list'), # Lista as vagas de estacionamento
    path('parking-spots/create/', views.ParkingSpotCreateView.as_view(), name='parking-spot-create'), # Cria uma vaga de estacionamento
    path('parking-spots/<int:pk>/', views.ParkingSpotRetrieveView.as_view(), name='parking-spot-detail'), # Detalhes de uma vaga de estacionamento específica
    path('parking-spots/<int:pk>/delete/', views.ParkingSpotDestroyView.as_view(), name='parking-spot-delete'), # Remove uma vaga de estacionamento

    # Endpoints relacionados aos registros de saída
    path('exit-registers/', views.ExitRegisterListView.as_view(), name='exit-register-list'), # Lista os registros de saída
    path('exit-registers/create/', views.ExitRegisterCreateView.as_view(), name='exit-register-create'), # Cria um registro de saída
    path('exit-registers/<int:pk>/', views.ExitRegisterUpdateView.as_view(), name='exit-register-detail'), # Detalhes de um registro de saída específico
    path('exit-registers/<int:pk>/delete/', views.ExitRegisterDestroyView.as_view(), name='exit-register-delete'), # Remove um registro de saída
]
