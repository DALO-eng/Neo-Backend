Activar entorno virtual: env\Scripts\activate
Encender el servidor: python neo\manage.py runserver
actualizar la BD: python neo\manage.py makemigrations usuarios
guardar cambios: python neo\manage.py migrate usuarios

Instrucciones para hacer deploy:
1. Descargar el repositorio
2. Abrir la terminal en la carpeta donde se encuentra el manage.py
3. heroku login
4. git init
5. heroku git:remote -a neo-bank-project
6. git add .
7. git commit -am "message"
8. git push -f heroku master

ADVERTENCIA: Las Restricciones que se presentan en las solitudes son unicamente las que se validan por parte de Backend de la pagina. En la parte de
Fronent hay restricciones para las variables.

Registrer:

    -Enlace: http://127.0.0.1:8000/registro/
    -Tipo de solicitud: POST
    -Formato json:
    {
        "cuenta":{"celular":"","contrasena":""},
        "cliente":{"nombre":"","correo":"","nacimiento":""},
        "documento":{"numero":"","expedicion":"","tipo":},
        "negocio":
    }
    Ejemplo:
    {
        "cuenta":{"celular":"3142612626","contrasena":"7777"},
        "cliente":{"nombre":"Soila Rosa","correo":"soila@mail.com","nacimiento":"2001-12-17"},
        "documento":{"numero":"44444","expedicion":"2001-03-06"},
        "negocio":1
    }
    -Restricciones:

        ♠ El campo celular del json "cuenta" es unico.
        ♠ El campo contrasena es de maximo 4 caracteres (no tiene por que ser unico)
        ♠ salvo el campo tipo en el json documento, todos los campos son obligatorios. En el caso del campo tipo, tiene un valor por defecto de 1.
        ♠ Si la solicitud no es de tipo POST la solicitud devolverá un mensage de errror.

    -Indicaciones:

        ♠ El campo nacimiento corresponde a la fecha de nacimiento del cliente.
        ♠ El campo tipo puede tener los valores 1, 2 o 3 (es una llave foránea), dónde 1 es cédula de ciudadanía, 2 cédula de extranjeria y 3 pasaporte
        (como no se aceptan menores de edad no se admitirán documentos de tipo registro civil ni tarjeta de identidad, valga la aclaración).
        ♠ El campo "negocio" indica si el cliente quiere crear un bolsillo destinado a negocio al momento de crear la cuenta; si es 1 se crea dicho
        bolsillo, si es cualquier otro valor no se creará (en el caso del ejemplo si se creó el bolsillo)

Logeo:

    - Enlace: http://127.0.0.1:8000/login/

    - Tipo de solicitud: GET

    - Formato JSON:
        {
            "numero":"",
            "contrasena":
        }
        Ejemplo:
        {
            "numero":"3142617626",
            "contrasena":"7777"
        }

    -Ejemplo de respuesta:
        {"monto": 0, "nombre": "Casimiro Buenavista", "id_cuenta": 29}
    -Restricciones:

        ♠ El campo "numero" debe tener un maximo de 10 caracteres.
        ♠ El campo "contrasena" debe tener un maximo de 4 caracteres.
        ♠ Ambos campos son obligatorios

    - Indicaciones:
    
        ♠ En caso que el logeo no sea correcto, se retornará un mensaje de error (uno de esos errores posibles es el tipo de solicitud)
        ♠ En caso de logeo correcto, lo único que hace la solicitud es retornar una cadena pseudoaleatoria para que el navegador pueda controlar el
        inicio de sesión. Por ahora solo la retorna, no la almacena ni hace ningún tipo de registro o función adicional.

Envio:

    -Enlace: http://127.0.0.1:8000/enviar/

    -Tipo de solicitud: POST

    -Formato JSON:
        {
            "envia":{"id_cuenta":,"nombre":},
            "recibe":{"celular":,"nombre":},
            "monto":
        }

    - indicaciones:
        ♠ Los datos del campo "envia" son el ID de la cuenta que va a enviar el dinero (el cual se recibe al momento de iniciar sesion) y
        el nombre del bolsillo desde el que se va a enviar. Si es el bolsillo principal su nombre será "principal" y si es el bolsillo de negocio
        su nombre será "negocio" (lo mismo aplica para el bolsillo remitente).
        ♠ Los datos del campo recibe son el numero celular del receptor del dienro y el nombre del bolsillo al cual se le enviara.
    -Ejemplo de envio valido:
    {
    "envia":{"id_cuenta":10,"nombre":"secundario"},
    "recibe":{"celular":3228829696,"nombre":"principal"},
    "monto":1
    }

    Nota: el nombre secundario del bolsillo que envia es un nombre personalizado que se agrego por medio de consultas sql.

    -En caso de exito el mensage que se retornara es "Transaccion exitosa."

Bolsillos:

    -Método: GET

    -Enlace: http://127.0.0.1:8000/bol/id

    -La variable id es el ID de la cuenta a la que se le quiere consultar los bolsillos.

    -Si se encuentran bolsillos para la cuenta se retornará una lista con los JSON de cada bolsillo, si no se encuetra ninguno se retornará una lista
    vacía.

-Historial:

    -Método: GET

    -Enlace: http://127.0.0.1:8000/bol/id

    -Indicaciones:

        ♠ La variable id es la ID de la cuenta a la que se le quiere ver el historial.
        ♠ este Enlace solo muestra el historial del bolsillo principal de la cuenta
        ♠ Si la solicitud es exitosa devolverá una lista de JSON con todos los envios tanto en los que se envio dinero como en los que se recibió.
        ♠ La lista de envios esta ordenada por fecha independientemente de si fue un envio o si se recibio dinero.

Consignacion:

    -metodo: "PUT"
    -Ejemplo Json:
    {
    "celular":"3842617626",
    "monto":50000000,
    "nombre":"negocio"
}

    -enlace: http://127.0.0.1:8000/consignacion/