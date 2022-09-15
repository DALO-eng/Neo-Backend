from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usuarios.models import cliente,cuenta,bolsillo,documento,envio
from usuarios.serializers import clienteSerializer,cuentaSerializer,documentoSerializer,bolsilloSerializer,envioSerializer
from django.http.response import JsonResponse
from datetime import date
from datetime import datetime
import uuid
import json
from rest_framework.exceptions import AuthenticationFailed,MethodNotAllowed
from django.db.models import Q

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
        local=datos["negocio"]
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
                    bolsillo_serializer=bolsilloSerializer(data={"cuenta":id})#se crea el bolsillo principal para la cuenta
                    if bolsillo_serializer.is_valid():
                        bolsillo_serializer.save()
                        if local==1:
                            negocio_serializer=bolsilloSerializer(data={"cuenta":id,"nombre":"negocio"})
                            if negocio_serializer.is_valid():
                                negocio_serializer.save()
                        return JsonResponse("Bienvenido a la familia Neo, tu registro fue exitoso",safe=False)
                    else:
                        try:
                            f=3/0
                        except ZeroDivisionError:
                            client.delete()
                            cuent.delete()
                            a=documento.objects.get(numero=datos_doc["numero"])
                            a=documentoSerializer(a,many=False)
                            a.delete()
                            return JsonResponse("No se pudo crear el bolsillo principal",safe=False)
                else:
                    try:
                        f=3/0
                    except ZeroDivisionError:
                        client.delete()
                        cuent.delete()
                        return JsonResponse("algo fallo en los datos de documento",safe=False)
            else:
                try:
                    f=3/0
                except ZeroDivisionError:
                    cuent.delete()#se elimina la cuenta recien creada
                    return JsonResponse("Hubo un error en el registro de datos personales",safe=False)
        else:
            try:
                f=3/0
            except ZeroDivisionError:
                return JsonResponse("Datos de acceso a la cuenta incorrectos",safe=False)
    else:
        try:
            f=3/0
        except ZeroDivisionError:
            return JsonResponse("Error en el tipo de solicitud, vuelva a intentarlo",safe=False)

#logeo
@csrf_exempt
def login(request):
    if request.method=='POST':
        datos=JSONParser().parse(request)
        cuent=cuenta.objects.filter(celular=datos['numero']).first()
        if cuent==None:
            return JsonResponse("la cuenta no existe",safe=False)
        else:
            cuenta_serializer=cuentaSerializer(cuent,many=False)
            if cuenta_serializer.data['contrasena']==datos['contrasena']:
                dataCuent=bolsillo.objects.filter(cuenta=cuenta_serializer.data["id_cuenta"],nombre="principal").first()
                dataBol=bolsilloSerializer(dataCuent,many=False)
                a=cliente.objects.filter(cuenta=cuenta_serializer.data["id_cuenta"]).first()
                clientData=clienteSerializer(a,many=False)
                return JsonResponse({"monto":dataBol.data["monto"],"nombre":clientData.data["nombre"],"id_cuenta":cuenta_serializer.data["id_cuenta"]},safe=False)
                #return JsonResponse(clientData.data,safe=False)
            else:
                return JsonResponse("clave de acceso incorrecta",safe=False)
    else:
        return JsonResponse("esta solicitud debe ser de tipo post",safe=False)

#envio
@csrf_exempt
def enviar(request):
    if request.method=="POST":
        datos=JSONParser().parse(request)
        if datos["monto"]>0:
            remitente=bolsillo.objects.filter(cuenta=datos["envia"]["id_cuenta"],nombre=datos["envia"]["nombre"]).first()
            # remitenteSer=bolsilloSerializer(remitente,many=False)
            # return JsonResponse(remitenteSer.data,safe=False)
            if remitente==None:
                return JsonResponse("No se encuentra el remitente en nuestra base de datos",safe=False)
            else:
                enviaSerializer=bolsilloSerializer(remitente,many=False)
                if bolsilloSerializer(remitente,many=False).data['monto']>=datos["monto"]:
                    cuent=cuenta.objects.filter(celular=datos["recibe"]["celular"]).first()
                    IDcuent=cuentaSerializer(cuent,many=False).data["id_cuenta"]
                    #return JsonResponse(IDcuent,safe=False)
                    receptor=bolsillo.objects.filter(cuenta=IDcuent,nombre=datos["recibe"]["nombre"]).first()
                    if receptor==None:
                        return JsonResponse("No se encuentra al receptor en nuestra base de datos, verifique numero de celular y bolsillo",safe=False)
                    elif bolsilloSerializer(receptor,many=False).data["id_bol"]==enviaSerializer.data["id_bol"]:
                        return JsonResponse("Un bolsillo no se puede enviar dinero a si mismo",safe=False)
                    else:
                        a=enviaSerializer.data
                        a["monto"]=a["monto"]-datos["monto"]
                        recibeSerializer=bolsilloSerializer(receptor,many=False)
                        #return JsonResponse(recibeSerializer.data,safe=False)
                        b=recibeSerializer.data
                        b["monto"]=b["monto"]+datos["monto"]
                        datos={
                            "envia_id":enviaSerializer.data["id_bol"],
                            "recibe_id":recibeSerializer.data["id_bol"],
                            "fecha":str(datetime.today().strftime('%Y-%m-%d')),
                            "monto":datos["monto"]
                        }
                        env=envioSerializer(data=datos)
                        enviaSerializer=bolsilloSerializer(remitente,data=a)
                        recibeSerializer=bolsilloSerializer(receptor,data=b)
                        if env.is_valid()and enviaSerializer.is_valid()and recibeSerializer.is_valid():
                            env.save()
                            enviaSerializer.save()
                            recibeSerializer.save()
                            return JsonResponse("Transaccion exitosa.",safe=False)
                        else:
                            return JsonResponse("hubo un error inesperado, lo sentimos",safe=False)
                else:
                    return JsonResponse("Saldo insuficiente.",safe=False)
        else:
            return JsonResponse("El monto a enviar debe ser un numero positivo",safe=False)
    else:
        return JsonResponse("Error en el tipo de solicitud, vuelva a intentarlo",safe=False)

#bolsillos
@csrf_exempt
def bol(request,id):
    if request.method=="GET":
        bols=bolsillo.objects.filter(cuenta_id=id)
        bolSerializer=bolsilloSerializer(bols,many=True)
        return JsonResponse(bolSerializer.data,safe=False)
    else:
        return JsonResponse("El metodo para esta peticion debe ser GET.",safe=False)

#historial
@csrf_exempt
def hist(request,id):
    if request.method=="GET":
        envios=envio.objects.order_by("fecha").filter(Q(envia_id=id)|Q(recibe_id=id))
        envSerializer=envioSerializer(envios,many=True)
        return JsonResponse(envSerializer.data,safe=False)
    else:
        return JsonResponse("El metodo para esta peticion debe ser GET.",safe=False)

#consignar
@csrf_exempt
def consig(request):
    if request.method=="PUT":
        datos=JSONParser().parse(request)
        cuent=cuenta.objects.filter(celular=datos["celular"]).first()
        cuenSeri=cuentaSerializer(cuent,many=False)
        bol=bolsillo.objects.filter(cuenta=cuenSeri.data["id_cuenta"],nombre=datos["nombre"]).first()
        if bol==None:
            return JsonResponse("No se encontro el destino",safe=False)
        else:
            bolS=bolsilloSerializer(bol,many=False)
            nuevData=bolS.data
            nuevData["monto"]=nuevData["monto"]+datos["monto"]
            bol1=bolsilloSerializer(bol,data=nuevData)
            if bol1.is_valid():
                bol1.save()
                return JsonResponse("consignacion exitosa.",safe=False)
            else:
                return JsonResponse("No se pudo hacer la consignacion",safe=False)
    else:
        return JsonResponse("El metodo para esta peticion debe ser POST.",safe=False)