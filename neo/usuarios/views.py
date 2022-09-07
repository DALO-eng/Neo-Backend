from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usuarios.models import cliente,cuenta,bolsillo,documento
from usuarios.serializers import clienteSerializer,cuentaSerializer,documentoSerializer,bolsilloSerializer
from django.http.response import JsonResponse
from datetime import date
from datetime import datetime
import uuid
import json

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
            if (datetime.strptime(str(date.today()), "%Y-%m-%d")-datetime.strptime(datos_cliente['nacimiento'], "%Y-%m-%d")).days/365>=18:
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
#registro
@csrf_exempt
def logeo(request):
    if request.method=='POST':
        datos=JSONParser().parse(request)
        datos_cuenta=datos["cuenta"]
        datos_cliente=datos["cliente"]
        datos_doc=datos["documento"]
        cuenta_serializer=cuentaSerializer(data=datos_cuenta)
        if cuenta_serializer.is_valid():
            cuenta_serializer.save()#se crea primero la cuenta
            cuent=cuenta.objects.get(celular=datos_cuenta['celular'])#se busca la cuenta recien creada
            id=cuentaSerializer(cuent,many=False).data['id_cuenta']#id de la cuenta asignada
            datos_cliente['cuenta']=id
            cliente_serializer=clienteSerializer(data=datos_cliente)
            if cliente_serializer.is_valid():
                cliente_serializer.save()
                client=cliente.objects.get(cuenta=id)
                nom=clienteSerializer(client,many=False).data['id_cliente']
                datos_doc['nombre']=nom
                documento_serializer=documentoSerializer(data=datos_doc)
                if documento_serializer.is_valid():
                    documento_serializer.save()
                    #bolsillo_serializer=bolsilloSerializer(data=json.dumps({'cuenta':id}))#se crea el bolsillo principal para la cuenta
                    #if bolsillo_serializer.is_valid():
                        #bolsillo_serializer.save()
                    return JsonResponse("Bienvenido a la familia Neo, tu registro fue exitoso",safe=False)
                    #else:
                        #client.delete()
                        #cuent.delete()
                        #a=documento.objects.get(numero=datos_doc["numero"])
                        #a=documentoSerializer(a,many=False)
                        #a.delete()
                        #return JsonResponse("No se pudo crear el bolsillo principal",safe=False)
                else:
                    client.delete()
                    cuent.delete()
                    return JsonResponse("algo fallo en los datos de documento",safe=False)
            else:
                cuent.delete()#se elimina la cuenta recien creada
                return JsonResponse("Hubo un error en el registro de datos personales",safe=False)
        else:
            return JsonResponse("Datos de acceso a la cuenta incorrectos",safe=False)
    else:
        return JsonResponse("Error en el tipo de solicitud, vuelva a intentarlo",safe=False)

#logeo
@csrf_exempt
def login(request):
    if request.method=='GET':
        datos=JSONParser().parse(request)
        cuent=cuenta.objects.filter(celular=datos['numero']).first()
        if cuent==None:
            return JsonResponse("Esa cuenta no existe",safe=False)
        else:
            cuenta_serializer=cuentaSerializer(cuent,many=False)
            if cuenta_serializer.data['contrasena']==datos['contrasena']:
                return JsonResponse(uuid.uuid4(),safe=False)
            else:
                return JsonResponse("clave de acceso incorrecta",safe=False)
    else:
        return JsonResponse("Error en el tipo de solicitud, vuelva a intentarlo",safe=False)