# HACKATON TICSUR

## Etapa 1: Planificación y Especificación Inicial:
### Objetivo

Ante el aumento del uso de medios de transporte alternativos en la ciudad, como bicicletas, scooters y patinetas, se presenta el desafío de la escasez de estacionamientos en la vía pública y en establecimientos, así como la necesidad de gestionarlos de manera eficiente y segura. Se necesita un sistema independiente que permita a un administrador visualizar y organizar los estacionamientos, con enfoque en los alumnos, utilizando GPS para mostrar la disponibilidad de espacios. El objetivo es minimizar costos y garantizar la escalabilidad para futuras actualizaciones del sistema.

### Planificación
### Selección Rápida de Herramientas y Tecnologías: 
Las etapas del desafío incluyen la planificación y especificación inicial del proyecto, donde se asignan roles como la lluvia de ideas en grupo, la visualización del programa y la recopilación de datos. Se aborda el proyecto tomando en cuenta los requisitos necesarios y optimizando el uso de la aplicación.

Se utilizarán herramientas como Trello para la planificación y asignación de tareas, Balsamiq Wireframes para el diseño de bocetos y prototipos, Canva para el desarrollo de elementos visuales como logos e iconos, y Visual Studio Code como editor de código para el desarrollo de la solución.


### Definición de Roles

En nuestro proyecto, Allyson desempeña el rol de diseñar la Arquitectura del Sistema, dado que posee los conocimientos y habilidades básicas necesarias para esta tarea.

Nelson se encarga de la programación en Python en nuestro proyecto, ya que posee habilidades y rapidez para ofrecer soluciones en este lenguaje.

Antv es responsable del análisis y desarrollo de los casos de uso de los requerimientos funcionales en nuestro proyecto.

Paola se encarga de la documentación y organiza las tareas utilizando metodologías ágiles en este proyecto.

## Diseño de Arquitectura del Sistema: 


###  Diseño de Arquitectura del Sistema: 
### Diagramas UML:
Requisitos Funcionales 
 
    A. Registro y Autenticación de Usuarios 
        ◦ Los usuarios (alumnos) deben poder registrarse e iniciar sesión en el sistema. 
            ▪ INICIO DE SESION:
    1- El alumno debe ingresar a la web de la santo tomas y ingresar sus datos para poder ver disponibilidad y poder hacer una reserva de algún lugar del los vehículos de movilidad (bicicletas, scooter, patinetas)
    2- Debe ingresar con su Rut, contraseña que cambio al momento de registrarse con el QR con su carnet de identidad , se le envía un aviso de que se ha hecho la reserve del espacio.
        ◦ Debe haber roles diferenciados para los usuarios, incluyendo administradores de estacionamiento y usuarios regulares eso se define una vez que ingresa a la app se pregunta al usuario si es“ administrador” o “usuario”.
            ▪ INICIO DE SESION DEL GUARDIA
    1- El guardia debe tener un acceso a la base de datos de registro y se le debe capacitar para que controle el sistema, para no generar una equivocación en el registro tanto del alumno como de la bicicleta

    B. Visualización y Búsqueda de Espacios 
        ◦ Los usuarios deben poder visualizar en tiempo real los espacios disponibles para estacionar sus medios de transporte. 
            ▪ DISPONIBILIDAD:
    1-  Debe tener un sensor donde se indique por computadora la disponibilidad del espacio
    2- Que en la web se defina los espacios que están desocupados con un color “verde”, y los espacios ocupados con el color “rojo” en las casillas que estarán organizados por fila y numero, ejemplo: (fila: 2, espacio 4: disponible; fila: 3, espacio 23: ocupado hasta las “??”)
    3- Una vez se envía la señal de espacios disponibles automáticamente se actualiza la app.
    4- Al momento de hacer la reserva del espacio, se debe indicar el tiempo de uso del espacio que se usará
        ◦ Debe existir una función de búsqueda de espacios disponibles ya sea basada en la ubicación actual del usuario, utilizando el GPS del móvil, o mediante una lista por edificio (sede Rodríguez, Sede Pedro de Valdivia, etc). 

 
    C. Reserva de Espacios 
            ▪ HORARIO DE RESERVA
        ◦ Los usuarios deben poder reservar un espacio de estacionamiento en uno o más bloques horarios preconfigurados. Ejemplo (de 08:00-09:59 | de 10:00 – 11:59 | etc). 
CONDICION:
    1- Se debe respetar el horario indicado para la reserva
PRECONCIDION:
    2- Al usuario se le da una penalización que se le enviara al Outlook, y la penalización será que tendrá un tiempo de espera de 5, 10 o 15 minutos para hacer una reserva, (la penalización de cantidad de minutos dependerá de las veces en la que se incumplió la 1ra regla del respeto en cuanto sea del horario de reserva).
HORARIO DE SISTEMA (nivel diario)
        ◦ Los bloques horarios de uso diario pueden ser configurados por los usuarios administradores.  
        ◦ CONDICION: 
    1- Se debe informar al sistema el uso diario o semanal del bicicletero y obviamente se deben respetar las normas de uso.
    • PRECONDICON:
    2- En el caso que se incumplan las normas del buen uso de la app se le hará la misma penalización por no respetar los horarios registrados por el usuario. 






        ◦ AVISO DE EXESO DE HORARIO ASIGNADO
            ▪ El sistema debe notificar al usuario cuando el tiempo de uso esté por expirar (según el bloque), ofreciendo la opción de extenderla. 
            ▪ CONDICONES:
    1- Se le enviara un aviso al usuario que su tiempo esta por expirar restando solo 15 minutos de este, (tiene 15 minutos de tiempo para actualizar su nuevo horario)
    • PRECONDICIONES:
    1- Si el tiempo de cambio de horario concluye, se le sancionara con el tiempo de espera para reservar dependiendo el tiempo que pase después del horario reservado por el usuario
    2- Las sanciones son:
        a. 30 minutos después de la reserva: 5 minutos de tiempo de espera
        b. 1 hora después de la reserva: 10 minutos de tiempo de espera
        c. 1 hora y 30 minutos  de la reserva : 15 minutos de tiempo de espera
        d. 2 horas en delante de la reserva: 20 minutos de tiempo de espera
 
    D. Gestión de Espacios por Administradores:
    • Administrador de sistema
            ▪ Solo los administradores tendrán acceso a la gestión de espacios. Las opciones de añadir, modificar o eliminar espacios de estacionamiento, así como gestionar las reservas, no estarán disponibles para los usuarios regulares. 
            ▪ CONDICIONES
    1- Debe existir una persona encargada de administrar la aplicación y que todos los problemas o asuntos respectivos al bicicletero, sea visto por el pero sea notificados por el usuario
    2- Debe tener acceso completo a la visión del bicicletero a modo visual y sistemáticamente para ver disponibilidad y modificar el mismo caso
    • PRECONDICIONES:
Debe si o si tener una persona encargada de saber sobre el sistema por si se produce un error para que pueda solucionarlo y hacer que la app funcione de forma correcta
    • RESOLUCION DE POBLEMAS
Deben poder manejar conflictos o necesidades especiales relacionadas con las reservas, las cuales son notificadas por los usuarios. 
    • El administrador debe resolver los problemas de los usuarios

    E. Notificaciones 
    • NOTIFICACION DE AVISO
    • CONDICIONES:
        1. Los usuarios deben recibir notificaciones sobre el estado de su reserva (confirmación, expiración, entrega). 
        2. Al correo institucional del usuario se le enviara la 1ra notificación de confirmación de reserva 
        3. Al correo institucional del usuario se le enviara una notificación de expiración de tiempo de reserva para poder ampliar la duración de este mismo.
        4. Al correo institucional del usuario se le enviara una notificación cuando el usuario retira su bici, scooter o patineta
    • PRECONDICIONES
    1. (Condición del paso 2): se le enviara una advertencia con duración de 15 minutos o si no después correrá la penalización de tiempo de espera señalado en los términos de usos de la app
 
    F. Reporte de Incidentes y Uso de Espacios 
    • REPORTE DE EMERGENCIA
        ◦ Los usuarios deben poder reportar problemas o incidentes relacionados con los estacionamientos (por ejemplo, robos o daños). 
        ◦ CONDICIONES:
            ▪ Se debe tener un botón de emergencia que al ser presionado, se le avisara al administrador del sistema y se le enviara un aviso al guardia mas cercano para que vaya a revisar el asunto
            ▪ Tener un botón de llamada a carabineros de chile que al ser presionado se hace una llamada automática para reportar el robo 
            ▪ Tener un botón de daños que al ser presionado, se le mandara un aviso al administrador del sistema que avisara al guardia mas cercano para que realice los papeleos correspondientes
    • INFORMAR DE ALGUNA ANOMALIA EN EL SISTEMA
        ◦ Deben informar al sistema cuando desocupen un espacio de estacionamiento. En este punto se anima a los estudiantes a proponer soluciones innovadoras como el uso de códigos QR, tecnología RFID, o sensores para detectar automáticamente cuando un espacio se desocupa. 
        ◦ El usuario el ingresar la bicicleta  desactiva el sensor laser y el sistema toma como “el espacio está ocupado”, cuando el usuario retira la bici este activaría el sensor laser que indicaría en el sistema que  “el espacio estaría disponible”


### Mockups de la Interfaz de Usuario: 

<a href="https://ibb.co/wJNYvTn"><img src="https://i.ibb.co/N1674X0/f3f68e20-d8a0-4d11-a1a1-665303be03f4-1.jpg" alt="f3f68e20-d8a0-4d11-a1a1-665303be03f4-1" border="0"></a>

<a href="https://ibb.co/LRSPFFz"><img src="https://i.ibb.co/fFMSggY/05f7d9b4-ab6a-4057-8226-7dc37b2dccb4.jpg" alt="05f7d9b4-ab6a-4057-8226-7dc37b2dccb4" border="0"></a>



