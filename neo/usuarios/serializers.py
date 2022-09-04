from dataclasses import fields
from rest_framework import serializers
from usuarios.models import cliente,cuenta

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=(
            'id_cliente',
            'nombre',
            'cuenta',
            'contrasena',
            'documento',
            'tipo_doc',
            'direccion',
            'correo')

class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=cuenta
        fields=(
            'id_cuenta',
            'convencional',
            'saldo_principal',
            'QR')