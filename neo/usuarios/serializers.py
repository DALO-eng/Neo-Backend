from dataclasses import fields
from rest_framework import serializers
#from neo.usuarios.models import direccion
from usuarios.models import cliente,cuenta,direccion

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=(
            'id_cliente',
            'nombre',
            'cuenta',
            'contrasena',
            'direccion',
            'correo',
            'nacimiento'
            )

class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=cuenta
        fields=(
            'id_cuenta',
            'convencional',
            'saldo_principal',
            'QR',
            'estado',
            'celular'
            )

class direccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=direccion
        fields=(
            'id_direccion',
            'calle',
            'barrio',
            'ciudad',
            'casa',
            'departamento',
            'apartamento',
            'carrera'
            )