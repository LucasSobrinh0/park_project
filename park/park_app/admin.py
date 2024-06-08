from django.contrib import admin
from .models import *

""" Aqui é onde registramos as configurações que o administrador pode fazer. Por exemplo:
Temos as tabelas relacionais do banco de dados, caso queiramos fazer alguma alteração, podemos fazer pelo admin.
Mas elas precisam estar adicionadas aqui. ENtão vamos adicionar!"""

admin.site.register(Driver)
admin.site.register(Adress)
admin.site.register(Vehicle)
admin.site.register(EntryRegister)
admin.site.register(ParkingSpot)
admin.site.register(ExitRegister)
