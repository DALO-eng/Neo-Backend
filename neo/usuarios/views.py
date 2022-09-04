from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usuarios.models import cliente,cuenta
from usuarios.serializers import clienteSerializer,cuentaSerializer
from django.http.response import JsonResponse
# Create your views here.
@csrf_exempt
def clienteApi(request,id=0):
    if request.method=='GET':
        Cliente=cliente.objects.all()
        cliente_serializer=clienteSerializer(Cliente,many=True)
        return JsonResponse(cliente_serializer.data,safe=False)
    elif request.method=='POST':
        datos_cliente=JSONParser().parse(request)
        clientes_serializer=clienteSerializer(data=datos_cliente)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return JsonResponse("!Guardado exitosamente¡",safe=False)
        return JsonResponse('No fue posible guardarlo.',safe=False)
    elif request.method=='PUT':
        Cliente_datos=JSONParser().parse(request)
        client=cliente.objects.get(id_cliente=Cliente_datos['id_cliente'])
        cliente_serializer=clienteSerializer(client,data=Cliente_datos)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("!Actualizado exitosamente¡",safe=False)
        return JsonResponse("No se pudo actualizar",safe=False)
    elif request.method=='DELETE':
        Cliente=cliente.objects.get(id_cliente=id)
        Cliente.delete()
        return JsonResponse("Eliminado exitosamente",safe=False)

#para cuenta
@csrf_exempt
def cuentaApi(request,id=0):
    if request.method=='GET':
        Cuenta=cuenta.objects.all()
        cuenta_serializer=cuentaSerializer(Cuenta,many=True)
        return JsonResponse(cuenta_serializer.data,safe=False)
    elif request.method=='POST':
        datos_cuenta=JSONParser().parse(request)
        cuenta_serializer=cuentaSerializer(data=datos_cuenta)
        if cuenta_serializer.is_valid():
            cuenta_serializer.save()
            return JsonResponse("!Guardado exitosamente¡",safe=False)
        return JsonResponse('No fue posible guardarlo.',safe=False)
    elif request.method=='PUT':
        cuenta_datos=JSONParser().parse(request)
        cuent=cuenta.objects.get(id_cuenta=cuenta_datos['id_cuenta'])
        cuenta_serializer=cuentaSerializer(cuent,data=cuenta_datos)
        if cuenta_serializer.is_valid():
            cuenta_serializer.save()
            return JsonResponse("!Actualizado exitosamente¡",safe=False)
        return JsonResponse("No se pudo actualizar",safe=False)
    elif request.method=='DELETE':
        Cuenta=cuenta.objects.get(id_cuenta=id)
        Cuenta.delete()
        return JsonResponse("Eliminado exitosamente",safe=False)