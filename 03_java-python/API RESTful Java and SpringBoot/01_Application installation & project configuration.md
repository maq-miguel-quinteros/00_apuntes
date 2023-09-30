# Development environment configuration

Para empezar a trabajar tenemos que hacer la configuración del ambiente de desarrollo, es decir, instalar los programas necesarios para poder programar en JAVA con SpringBoot.

## JDK (JAVA Development Kit)

JDK (JAVA Development Kit) es un paquete con programas para compilar, interpretar y ejecutar el código java así como también un compendio de código pre diseñado para facilitar la creación de aplicaciones java. Contiene:

1. __JRE__ (Java Runtime Environment): es el conjunto de programas y librerías necesarias para ejecutar las aplicaciones java, este programa se puede instalar de manera independiente y es posible que ya lo tengas en tu computadora.

2. __Javac__ (Java compiler): es el programa encargado de compilar el código java y pasarlo a bytecode, que es el lenguaje que interpreta la máquina virtual de java JVM que es parte de JRE.

3. __Java Archive Tool__: es el programa encargado de ensamblar en un paquete las clases java compiladas en un programa ejecutable llamado JAR.

### Amazon Corretto OpenJDK 17

Java SE: Java Standard Edition es la plataforma central de programación de Java. Contiene todas las bibliotecas y API que cualquier programador necesita para el desarrollo de Java. Open Java Development Kit (OpenJDK) es la implementación gratuita y de código abierto de Java SE.

Amazon Corretto es una distribución de OpenJDK sin costo, multiplataforma y lista para producción. Se puede usar como un reemplazo directo para muchas distribuciones de Java SE y cuenta con soporte a largo plazo y gratuito de Amazon. Le permite ejecutar el mismo entorno en la nube, en las instalaciones y en su máquina local.

> Descargar [Amazon Corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/downloads-list.html)

## IntelliJ IDEA

IntelliJ IDEA es un programa conocido como IDE (Integrated Development Environment) el cual contiene herramientas útiles para programar tales como un editor de código, explorador de archivos, depurador de código, plugins para trabajar con sistemas de versionado como git, compilador y ejecutor de código, visor de base de datos, entre otras, la idea de estos programas es que como desarrollador no tengas que usar ningún otro programa para trabajar.

Para instalar IntellIJ deberás ir a su sitio web. Recuerda seleccionar la versión community que es gratis aunque carece de algunas características que tiene la versión de pago.

> Descargar [IntellIJ](https://www.jetbrains.com/idea/download)

## Gradle Build Tool

Gradle Build Tool es una herramienta de __automatización de compilación__ de código abierto rápida, confiable y adaptable, con un lenguaje de compilación declarativo elegante y extensible. Tiene un gestor de dependencias que se encarga de la descarga y configuración de las mismas.

> La automatización de compilación es el proceso de automatizar la creación de una compilación de software y los procesos asociados, que incluyen: compilar el código fuente de la computadora en código binario , empaquetar código binario y ejecutar pruebas automatizadas.

### Instalar Gradle

Para instalar Gradle descargamos el archivo comprimido desde la su web. Creamos una carpeta en la unidad C del equipo de la forma `C:\Gradle`. Descomprimimos el archivo descargado en esta carpeta (puede demorar varios minutos). Quedará una estructura de la forma `C:\Gradle\gradle-8...`.

> Descargar [Gradle Build Tool](https://gradle.org/releases/)

### Configurar las variables de entorno

En el explorador de archivos tenemos que hacer clic derecho sobre `Equipo`, seleccionar `propiedades` y dirigirnos a `configuración avanzada del sistema`, después de esto hacemos clic en el botón `Variables de entorno`.

En la ventana de `Variables de entorno` vamos a la fila `Path` y tocamos en el botón `Editar`. Agregamos el la ruta `C:\Gradle\gradle-8.3\bin` y aceptamos todos los cambios.

## Spring Initializr

Para crear el proyecto vamos a utilizar Spring Initializr, mediante este creamos los archivos básicos necesarios así como la estructura de directorios recomendada para comenzar a trabajar en una aplicación de Java que utilice el Spring Framework implementado con Spring Boot.

> Ingresar en [Spring Initializr](https://start.spring.io/)

![spring_initializr](https://raw.githubusercontent.com/maq-miguel-quinteros/00_apuntes/main/03_java-python/API%20RESTful%20Java%20and%20SpringBoot/wip/img/spring_initializr.png)

* El gestor de proyecto será `Gradle`

* El Lenguaje será `Java`
* La versión de spring boot debe ser la menos reciente y más estable (que no tenga ninguna marca entre paréntesis)
* En grupo será, para el ejemplo, `com.librosantigal.bd`
* Luego en artifact seré `stock`
* En packaging vamos a indicar `jar` y en java indicar la versión `17`.

Por último en el panel de la derecha agregamos las dependencias `H2 database`, `Spring Data JPA`, `Spring Web` y `Rest Repositories`.

Una vez terminada la configuración tocamos en `Generate` para descargar un archivo comprimido con nuestro proyecto. Descomprimimos esta carpeta en la ubicación que mas nos convenga.

## Iniciar IntelliJ IDEA y probar la aplicación

Iniciamos IntelliJ y tocamos en el botón de abrir o importar, te preguntará por el directorio del proyecto y deberás indicar la ruta a la carpeta previamente extraída, una vez que se seleccione la carpeta pulsar el botón ok, luego espera a que el proyecto se cargue por completo.

Para ejecutar el proyecto y probar que todo esté funcionando correctamente vamos al plugin de Gradle ubicado en la parte superior derecha del IntelliJ, allí encontrarás un árbol de directorios con las tareas de Gradle, deberás hacer doble click sobre la tarea `bootRun` ubicada dentro de la carpeta `task/application`.

![bootRun](https://raw.githubusercontent.com/maq-miguel-quinteros/00_apuntes/main/03_java-python/API%20RESTful%20Java%20and%20SpringBoot/wip/img/bootRun.png)

Vamos a ver, en la parte inferior del IntelliJ, que aparece la consola de ejecución con los registros de qué está sucediendo a medida que inicia la aplicación. Cuando veamos el mensaje
```
    Started StockApplication in ... seconds (JVM running for ...)
```
significa que la aplicación ya inició. Si ingresamos, desde el navegador, a la ruta [__localhost:8080__](http://localhost:8080/) vamos a ver un JSON con una entrada llamada profile, parece poco pero hasta ahora lograste crear una aplicación Gradle de Java con Spring Boot, importarla en el IntelliJ, compilarla y ejecutarla.

Para detener la aplicación pulsa sobre el botón rojo ubicado a la izquierda del panel de ejecución o arriba a la derecha del IntelliJ.
