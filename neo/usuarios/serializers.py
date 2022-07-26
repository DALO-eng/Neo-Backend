from dataclasses import fields
from rest_framework import serializers
from usuarios.models import envio
#from neo.usuarios.models import direccion
from usuarios.models import cliente,cuenta,documento,bolsillo

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=(
            'id_cliente',
            'nombre',
            'cuenta',
            'correo',
            'nacimiento'
            )

class documentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=documento
        fields=(
            'id_doc',
            'numero',
            'expedicion',
            'tipo',
            'nombre'
        )

class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=cuenta
        fields=(
            'id_cuenta',
            'estado',
            'celular',
            'contrasena',
            'colchon'
            )


class envioSerializer(serializers.ModelSerializer):
    class Meta:
        model=envio
        fields=(
            'id_envio',
            'envia_id',
            "recibe_id",
            'fecha',
            'monto'
        )

class bolsilloSerializer(serializers.ModelSerializer):
    class Meta:
        model=bolsillo
        fields=(
            'id_bol',
            'cuenta',
            'monto',
            'nombre',
            'QR'
        )