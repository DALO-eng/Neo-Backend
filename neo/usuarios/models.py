from django.db import models

# Create your models here.
class estado_cuenta(models.Model):
    id_estado=models.AutoField(primary_key=True)
    estado=models.CharField(max_length=10,unique=True)
#el estado 0 es activo

class cuenta(models.Model):
    id_cuenta=models.AutoField(primary_key=True)
    convencional=models.CharField(max_length=100,unique=True)
    saldo_principal=models.IntegerField(default=0)
    QR=models.CharField(max_length=100,blank=True,null=True,unique=True)
    estado=models.ForeignKey(estado_cuenta,on_delete=models.PROTECT)#no se puede eliminar el tipo de estado de la cuenta a la que se apunta

class direccion(models.Model):
    id_direccion=models.AutoField(primary_key=True)
    calle=models.CharField(max_length=50,blank=True,null=True)
    barrio=models.CharField(max_length=50,blank=True,null=True)
    ciudad=models.CharField(max_length=50)
    casa=models.CharField(max_length=50,blank=True,null=True)
    departamento=models.CharField(max_length=50)
    apartamento=models.CharField(max_length=50,blank=True,null=True)
    vereda=models.CharField(max_length=50,blank=True,null=True)

class tipo_doc(models.Model):
    id_tipo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,unique=True)

class cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    cuenta=models.OneToOneField(cuenta,on_delete=models.CASCADE)#al eliminar la cuenta se elimina también la persona
    contrasena=models.CharField(max_length=4)
    direccion=models.OneToOneField(direccion,blank=True,null=True,on_delete=models.SET_NULL)#Se hace nulo si se elimina la direccion
    #aunque dos usuarios vivan en la misma direccion, este campo apuntara a tablas diferentes aunque tengan los mismos valores en
    #todos los campos (exepto al campo id_direccion) para facilitar la actualizacion de datos en caso que uno de ellos cambie su
    # direccion
    correo=models.CharField(max_length=320)

class documento(models.Model):
    id_doc=models.AutoField(primary_key=True)
    numero=models.CharField(max_length=100,unique=True)
    expedicion=models.DateField()#fecha de expedicion
    tipo=models.ForeignKey(tipo_doc,on_delete=models.PROTECT)#no se puede eliminar el tipo de documento al que hace referencia
    nombre=models.OneToOneField(cliente,on_delete=models.CASCADE)#al eliminar al cliente, tambien se eliminara su documento