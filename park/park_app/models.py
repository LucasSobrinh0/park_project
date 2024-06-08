from django.db import models

# Models é o arquivo em python onde ficam as tabelas relacionais do banco de dados
# By : Lucas Sobrinho

class Driver(models.Model): # Tabela que contém os dados do motorista. Nenhum campo pode estar em branco
    cpf = models.CharField(max_length=14, unique=True, null=False, primary_key=True) # CPF do motorista, onde o dado é único e é a chave primaria
    name = models.CharField(max_length=50, null=False) # Nome do motorista
    phone = models.CharField(max_length=15, null=False) # Telefone do motorista
    driver_email = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False) # Armazenar data de nascimento do motorista

    def __str__(self) -> str:
        return self.name # Retorna o nome do usuário em string

    class Meta:
        verbose_name_plural = 'Drivers' # Utilizado para não dar conflito quando o nome da classe estiver no plural


class Adress(models.Model): # Tabela que contém o endereço do motorista. Respeitando as normas formais.
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=False) # Chave estrangeira que pega os dados do motorista
    state = models.CharField(max_length=20, null=False) #Estado do motorista
    city = models.CharField(max_length=29, null=False) #Cidade do motorista
    street = models.CharField(max_length=20, null=False) #RUa do motorista
    house_number = models.IntegerField() #Numero da casa do motorista
    cep = models.CharField(max_length=9, null=False) #CEP do motorista

    class Meta:
        verbose_name_plural = 'Adress'


class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=False) # Chave estrangeira que pega os dados do motorista
    license_plate = models.CharField(max_length=8, null=False) # Placa do veiculo
    vehicle_model = models.CharField(max_length=20, null=False) # Modelo do veiculo
    vehicle_cor = models.CharField(max_length=20, null=False) #Cor do veiculo
    vehicle_year = models.DateField() #Ano do veiculo

    class Meta:
        verbose_name_plural = 'Vehicles'


class EntryRegister(models.Model): # Tabela onde registramos a entrada do motorista
    driver_entry = models.ForeignKey(Driver, on_delete=models.CASCADE, null=False) # Chave estrangeira para pegar os dados do motorista
    vehicle_entry = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False) # Chave estrangeira para pegar os dados do veiculo
    date_entry = models.DateTimeField() # Definir a entrada do veiculo
    parking_spot_status = models.BooleanField(default=False)  # Status da vaga (ocupada ou livre)

    class Meta:
        verbose_name_plural = 'EntryRegisters'


class ParkingSpot(models.Model):
    spot_number = models.IntegerField(unique=True)  # Número da vaga
    is_occupied = models.BooleanField(default=False)  # Status da vaga (ocupada ou livre)

    class Meta:
        verbose_name_plural = 'ParkingSpots'


class ExitRegister(models.Model): # Tabela onde registramos a saida do usuário
    entry = models.ForeignKey(EntryRegister, on_delete=models.CASCADE, null=False)  # Chave estrangeira para pegar a entrada
    exit = models.DateTimeField() # Definir a saida do veiculo
    payment = models.DecimalField(max_digits=6, decimal_places=2, null=False) # Registrar pagamento do usuário
    payment_method = models.CharField(max_length=20, null=False) # Registrar método de pagamento

    class Meta:
        verbose_name_plural = 'ExitRegisters'
    