from django.db import models

# Create your models here.
class estado_cuenta(models.Model):
    id_estado=models.AutoField(primary_key=True)
    estado=models.CharField(max_length=10,unique=True)
#el estado 1 es activo

class cuenta(models.Model):
    id_cuenta=models.AutoField(primary_key=True)
    estado=models.ForeignKey(estado_cuenta,on_delete=models.PROTECT,blank=True,default=1)#no se puede eliminar el tipo de estado de la cuenta a la que se apunta
    celular=models.CharField(max_length=10,unique=True)
    contrasena=models.CharField(max_length=4)

class tipo_doc(models.Model):
    id_tipo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,unique=True)

class cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    cuenta=models.OneToOneField(cuenta,on_delete=models.CASCADE)#al eliminar la cuenta se elimina también la persona
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
    cuenta=models.ForeignKey(cuenta,on_delete=models.CASCADE)#al eliminar la cuenta se elimina tambien el bolsillo
    monto=models.IntegerField(blank=True,default=0)
    nombre=models.CharField(blank=True,default="principal",max_length=10)
    QR=models.CharField(max_length=500,blank=True,null=True,unique=True)

class envio(models.Model):
    id_envio=models.AutoField(primary_key=True)
    envia_id=models.ForeignKey(bolsillo,on_delete=models.DO_NOTHING,related_name="%(class)s_envia")
    recibe_id=models.ForeignKey(bolsillo,on_delete=models.DO_NOTHING,related_name="%(class)s_recibe")
    fecha=models.DateField()
    IP_envia=models.CharField(max_length=128)
    monto=models.IntegerField()