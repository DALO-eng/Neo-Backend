from django.db import models

# Create your models here.
class estado_cuenta(models.Model):
    id_estado=models.AutoField(primary_key=True)
    estado=models.CharField(max_length=10,unique=True)
#el estado 1 es activo

class apartamento(models.Model):
    id_apartamento=models.AutoField(primary_key=True)
    conjunto=models.CharField(max_length=200)
    bloque=models.CharField(max_length=200,blank=True,null=True)
    num_apar=models.CharField(max_length=200)

class cuenta(models.Model):
    id_cuenta=models.AutoField(primary_key=True)
    estado=models.ForeignKey(estado_cuenta,on_delete=models.PROTECT,blank=True,default=1)#no se puede eliminar el tipo de estado de la cuenta a la que se apunta
    celular=models.CharField(max_length=10,unique=True)
    contrasena=models.CharField(max_length=4)

class direccion(models.Model):
    id_direccion=models.AutoField(primary_key=True)
    calle=models.IntegerField(blank=True,null=True)
    barrio=models.CharField(max_length=50,blank=True,null=True)
    ciudad=models.CharField(max_length=50)
    casa=models.CharField(max_length=50,blank=True,null=True)
    departamento=models.CharField(max_length=50)
    apartamento=models.ForeignKey(apartamento,on_delete=models.CASCADE,blank=True,null=True)
    vereda=models.CharField(max_length=50,blank=True,null=True)
    carrera=models.IntegerField(blank=True,null=True)

class tipo_doc(models.Model):
    id_tipo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,unique=True)

class cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    cuenta=models.OneToOneField(cuenta,on_delete=models.CASCADE)#al eliminar la cuenta se elimina también la persona
    direccion=models.OneToOneField(direccion,blank=True,null=True,on_delete=models.SET_NULL)#Se hace nulo si se elimina la direccion
    #aunque dos usuarios vivan en la misma direccion, este campo apuntara a tablas diferentes aunque tengan los mismos valores en
    #todos los campos (exepto al campo id_direccion) para facilitar la actualizacion de datos en caso que uno de ellos cambie su
    # direccion
    correo=models.CharField(max_length=320)
    nacimiento=models.DateField()

class documento(models.Model):
    id_doc=models.AutoField(primary_key=True)
    numero=models.CharField(max_length=100,unique=True)
    expedicion=models.DateField()#fecha de expedicion
    tipo=models.ForeignKey(tipo_doc,blank=True,default=1,on_delete=models.PROTECT)#no se puede eliminar el tipo de documento al que hace referencia
    nombre=models.OneToOneField(cliente,on_delete=models.CASCADE)#al eliminar al cliente, tambien se eliminara su documento

class bolsillo(models.Model):
    id_bol=models.AutoField(primary_key=True)
    principal=models.BooleanField(default=False)
    cuenta=models.ForeignKey(cuenta,on_delete=models.CASCADE)#al eliminar la cuenta se elimina tambien el bolsillo
    monto=models.IntegerField(default=0)
    nombre=models.CharField(max_length=10)
    QR=models.CharField(max_length=100,blank=True,null=True,unique=True)

class envio(models.Model):
    id_envio=models.AutoField(primary_key=True)
    envia=models.ForeignKey(bolsillo,on_delete=models.DO_NOTHING)
    fecha=models.DateField()
    IP_envia=models.CharField(max_length=128)
    monto=models.IntegerField()

class recibe(models.Model):
    recibe=models.ForeignKey(bolsillo,on_delete=models.DO_NOTHING)
    id_envio=models.OneToOneField(envio,on_delete=models.DO_NOTHING,primary_key=True)    