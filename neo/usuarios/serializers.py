from dataclasses import fields
from rest_framework import serializers
from usuarios.models import envio
#from neo.usuarios.models import direccion
from usuarios.models import cliente,cuenta,direccion

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=(
            'id_cliente',
            'nombre',
            'cuenta',
            'direccion',
            'correo',
            'nacimiento'
            )

class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=cuenta
        fields=(
            'id_cuenta',
            'estado',
            'celular',
            'contrasena'
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

class envioSerializer(serializers.ModelSerializer):
    class Meta:
        model=envio
        fields=(
            'id_envio',
            'envia',
            'fecha',
            'IP_envia',
            'monto'
        )

class recibeSerializer(serializers.ModelSerializer):
    class Meta:
        model=envio
        fields=(
            'recibe',
            'id_envio'
        )