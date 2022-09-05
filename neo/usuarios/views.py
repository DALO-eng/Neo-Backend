from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usuarios.models import cliente,cuenta,direccion
from usuarios.serializers import clienteSerializer,cuentaSerializer,direccionSerializer,envioSerializer,recibeSerializer
from django.http.response import JsonResponse
from datetime import date
from datetime import datetime
#nuevo

@csrf_exempt
def direccionApi(request,id=0):
    if request.method=='GET':
        Direccion=direccion.objects.get(id_direccion=id)
        direccion_serializer=direccionSerializer(Direccion,many=False)
        return JsonResponse(direccion_serializer.data,safe=False)
    elif request.method=='POST':
        datos_direccion=JSONParser().parse(request)
        direccion_serializer=direccionSerializer(data=datos_direccion)
        if direccion_serializer.is_valid():
            direccion_serializer.save()
            return JsonResponse("Guardado exitosamente",safe=False)
        return JsonResponse('No fue posible guardarlo.',safe=False)
    elif request.method=='PUT':
        Direccion_datos=JSONParser().parse(request)
        dir=direccion.objects.get(id_direccion=id)
        direccion_serializer=direccionSerializer(dir,data=Direccion_datos)
        if direccion_serializer.is_valid():
            direccion_serializer.save()
            return JsonResponse("Actualizado exitosamente",safe=False)
        return JsonResponse("No se pudo actualizar",safe=False)
    elif request.method=='DELETE':
        Direccion=direccion.objects.get(id_direccion=id)
        Direccion.delete()
        return JsonResponse("Eliminado exitosamente",safe=False)

# Create your views here.
@csrf_exempt
def clienteApi(request,id=0):
    if request.method=='GET':
        Cliente=cliente.objects.get(id_cliente=id)
        cliente_serializer=clienteSerializer(Cliente,many=False)
        return JsonResponse(cliente_serializer.data,safe=False)
    elif request.method=='POST':
        datos_cliente=JSONParser().parse(request)
        clientes_serializer=clienteSerializer(data=datos_cliente)
        if clientes_serializer.is_valid():
            if (datetime.strptime(str(date.today()), "%Y-%m-%d")-datetime.strptime(datos_cliente['nacimiento'], "%Y-%m-%d")).days/365>=16:
                clientes_serializer.save()
                return JsonResponse("Guardado exitosamente",safe=False)
            else:
                return JsonResponse('La edad minima para registrarse es 16.',safe=False)
        return JsonResponse('No fue posible guardarlo.',safe=False)
    elif request.method=='PUT':
        Cliente_datos=JSONParser().parse(request)
        client=cliente.objects.get(id_cliente=Cliente_datos['id_cliente'])
        cliente_serializer=clienteSerializer(client,data=Cliente_datos)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Actualizado exitosamente",safe=False)
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
            return JsonResponse("Guardado exitosamente",safe=False)
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

#transaccion
@csrf_exempt
def cuentaApi(request,id=0):
    if request.method=='GET':
        Cuenta=cuenta.objects.all()
        cuenta_serializer=cuentaSerializer(Cuenta,many=True)
        return JsonResponse(cuenta_serializer.data,safe=False)
    elif request.method=='POST':
        datos_envio=JSONParser().parse(request)['enviar']
        datos_recibe=JSONParser().parse(request)['recibir']
        envio_serializer=envioSerializer(data=datos_envio)
        recibe_serializer=JSONParser().parse(request)['']
        if cuenta_serializer.is_valid():
            cuenta_serializer.save()
            return JsonResponse("Guardado exitosamente",safe=False)
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