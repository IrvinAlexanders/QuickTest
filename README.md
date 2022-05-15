# QuickTest
Prueba técnica de Quick

## ¿Como iniciar?  
Lo primero que hay que tener instalado en la PC a parte de Python es pipenv.  
`pip install --user pipenv` o `pip install pipenv`, pipenv es un entorno virtual  
muy facil de usar.  
Luego de haber instalado __pipenv__ clonamos el repositorio en nuestro ordenador.  
Ejecutamos git bash en la carpeta donde queremos que se clone el repositorio  
y ejecutamos el siguiente comando:  
`git clone https://github.com/IrvinAlexanders/QuickTest.git`, se clonará el  
repositorio en la carpeta donde abrimos el git bash.  
Luego de haber clonado el repositorio, activamos el entorno virtual de pipenv:  
`pipenv shell`, se creará el entorno virtual en la carpeta donde tenemos el  
repositorio clonado. El siguiente paso es instalar las dependencias en el archivo  
`requirements.txt` con el siguiente comando:  
`pipenv install -r requirements.txt`.  
  
 Luego de haber instalado todas las dependencias ya podemos seguir a ejecutar las  
 migraciones si lo es necesario( el repositorio se subió con la base de datos ya lista )  
 con el siguiente comando:  
 `python manage.py makemigrations` y `python manage.py migrate`.  
   
 Seguimos con la ejecución del servidor en local con el siguiente comando:  
 `python manage.py runserver` el servidor correrá en http://localhost:8000/api/ pero  
 primero debemos acceder como administrador en http://localhost:8000/admin , ya hay  
 un usuario configurado `irvin-alexanders@outlook.com` y password `irv26496518`. Si  
 desea crear un usuario nuevo podemos ir a la url http://localhost:8000/admin/User/user/add  
 ya con la sesión iniciada con el usuario pasado anteriormente(Para crearlo desde el  
 principio debemos eliminar la base de datos y ejecutar las migraciones nueva mente y  
 ejecutar: `python manage.py createsuperuser`).  
 
 ## Rutas URI:  
 
 ~~~
 {
    "bills": "http://localhost:8000/api/bills/",
    "client": "http://localhost:8000/api/client/",
    "products": "http://localhost:8000/api/products/",
    "bills_products": "http://localhost:8000/api/bills_products/"
}
 ~~~
 
 Para acceder desde Postman, Insomnia u otro programa, debemos proporcionarle el Token  
 generado ubicado en la url http://localhost:8000/admin/authoken/tokenproxy copiarlo y  
 en postman u otro programa vamos a Headers y en key elegimos `Authorization` y en value  
 `Token 'pegamos el token copiado'`, asi tal cual con la palabra 'Token' al principio  
 seguido del token copiado desde el administrador. Con este paso realizado ya se nos  
 conceden los permisos para utilizar todos los endpoints desde el programa a utilizar.  
   
   ## Login/SigIn de Usuarios:  
     
   ~~~
   {
      "http://localhost:8000/login/",
      "http://localhost:8000/register/"
   }
   ~~~
  
  Podemos registrar y iniciar sesión desde éstas url, con un formulario diferente para cada  
  endpoint, asignandole los Tokens desde http://localhost:8000/admin/authoken/ a cada usuario.  
  
  ##  Descargar e Importar archivos CSV:
  
  ~~~
  {
      "http://localhost:8000/import",
      "http://localhost:8000/export"
  }
  ~~~
  Con `/import` nos abre un formulario donde podemos eligir el archivo a importar y con `/export`  
  nos descarga automáticamente un archivo csv con los registros de clientes.
