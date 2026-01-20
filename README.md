# Ejercicio 2 – Cliente SMTP en Python

## Descripción
Cliente SMTP en Python con interfaz gráfica Tkinter para enviar correos electrónicos a través de Mailtrap.

## Características
- ✅ Interfaz gráfica con Tkinter
- ✅ No usa STARTTLS (conexión SMTP directa)
- ✅ Campos de configuración: Host, Puerto, Username, Password
- ✅ Dos ventanas grandes:
  - **Izquierda**: Editor de contenido HTML del correo
  - **Derecha**: Respuestas del servidor y log de eventos
- ✅ Uso de `smtplib` y `email.mime`
- ✅ Validación de datos y manejo de errores

## Requisitos
- Python 3.x
- Tkinter (incluido por defecto en Python)
- Cuenta gratuita en Mailtrap

## Configuración de Mailtrap

1. Crear una cuenta gratuita en [Mailtrap](https://mailtrap.io/)
2. Acceder a tu inbox/sandbox
3. Copiar las credenciales SMTP:
   - **Host**: `sandbox.smtp.mailtrap.io`
   - **Puerto**: `2525` (o `25`, `465`, `587`)
   - **Username**: (proporcionado por Mailtrap)
   - **Password**: (proporcionado por Mailtrap)

## Instalación y Ejecución

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd Ejercicio2

# Ejecutar el programa
python main.py
```

## Uso del Programa

1. **Configurar SMTP**: Introduce los datos de Mailtrap en los campos superiores
   - Host: `sandbox.smtp.mailtrap.io`
   - Puerto: `2525`
   - Username: Tu username de Mailtrap
   - Password: Tu password de Mailtrap

2. **Datos del Correo**:
   - De (From): Email del remitente
   - Para (To): Email del destinatario
   - Asunto: Asunto del correo

3. **Contenido del Correo**: Edita el HTML en la ventana izquierda

4. **Enviar**: Haz clic en "Enviar Correo"

5. **Verificar**: Revisa el log en la ventana derecha y verifica el inbox en Mailtrap

## Estructura del Código

- `SMTPClientGUI`: Clase principal que maneja la interfaz y el envío de correos
- `add_log()`: Añade mensajes al log con colores según el nivel (INFO, SUCCESS, ERROR, SERVER)
- `send_email()`: Función que conecta al servidor SMTP y envía el correo

## Capturas de Pantalla

### 1. Programa mostrando envío exitoso
![Captura del programa](capturas/programa_enviado.png)

### 2. Inbox de Mailtrap con correo recibido
![Captura de Mailtrap](capturas/mailtrap_recibido.png)

## Características Técnicas

- **Sin STARTTLS**: Conexión SMTP directa sin cifrado TLS
- **MIME Multipart**: Soporte para contenido HTML
- **Log detallado**: Muestra todas las respuestas del servidor
- **Validación**: Comprueba que todos los campos estén completos
- **Manejo de errores**: Captura y muestra errores de autenticación, SMTP y conexión

## Autor
Creado para el Ejercicio 2 de PSP - DAM 2

## Fecha
Enero 2026
