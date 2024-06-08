from django.test import TestCase
from .models import Driver, Adress, Vehicle, EntryRegister, ParkingSpot, ExitRegister
from django.utils import timezone

"""Esse arquivo serve para escrevermos testes automatizados em python"""

# class ModelsTestCase(TestCase):
#     def setUp(self):
#         # Criar instâncias de modelos para testar
#         self.driver = Driver.objects.create(cpf='12345678900', name='Test Driver', phone='123456789', driver_email='test@example.com', date_of_birth='1990-01-01')
#         self.adress = Adress.objects.create(driver=self.driver, state='State', city='City', street='Street', house_number=1, cep='12345678')
#         self.vehicle = Vehicle.objects.create(driver=self.driver, license_plate='ABC1234', vehicle_model='Model', vehicle_cor='Color', vehicle_year='2020-01-01')
#         self.entry_register = EntryRegister.objects.create(driver_entry=self.driver, vehicle_entry=self.vehicle, date_entry=timezone.now(), parking_spot_status=False)
#         self.parking_spot = ParkingSpot.objects.create(spot_number=1, is_occupied=False)
#         self.exit_register = ExitRegister.objects.create(entry=self.entry_register, exit=timezone.now(), payment=50.00, payment_method='Cash')

#     def test_driver_creation(self):
#         self.assertEqual(self.driver.name, 'Test Driver')

#     def test_adress_creation(self):
#         self.assertEqual(self.adress.state, 'State')

#     def test_vehicle_creation(self):
#         self.assertEqual(self.vehicle.license_plate, 'ABC1234')

#     def test_entry_register_creation(self):
#         self.assertEqual(self.entry_register.driver_entry, self.driver)

#     def test_parking_spot_creation(self):
#         self.assertEqual(self.parking_spot.spot_number, 1)

#     def test_exit_register_creation(self):
#         self.assertEqual(self.exit_register.payment, 50.00)
