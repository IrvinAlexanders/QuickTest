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
 
 
