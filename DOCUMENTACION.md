# Documentación del Código - Cliente SMTP

## Estructura del Programa

### 1. Imports
```python
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
```

- **tkinter**: Librería para crear interfaces gráficas
- **smtplib**: Protocolo SMTP para envío de correos
- **email.mime**: Creación de mensajes MIME (Multipurpose Internet Mail Extensions)
- **datetime**: Para timestamps en los logs

### 2. Clase Principal: SMTPClientGUI

#### Constructor `__init__(self, root)`
Inicializa la interfaz gráfica con:
- Configuración de ventana principal (1200x700 px)
- Frame de configuración SMTP (host, puerto, username, password)
- Frame de datos del correo (from, to, subject)
- Dos ventanas grandes (editor HTML y log)
- Botones de acción

#### Método `add_log(self, message, level="INFO")`
Añade mensajes al log con:
- Timestamp automático
- Niveles de log: INFO, ERROR, SUCCESS, SERVER
- Colores diferentes según el nivel:
  - ERROR: Rojo (#e74c3c)
  - SUCCESS: Verde (#27ae60)
  - SERVER: Azul (#3498db)
  - INFO: Color por defecto

#### Método `send_email(self)`
Proceso completo de envío:

1. **Validación de datos**:
   - Verifica que todos los campos estén completos
   - Valida que el puerto sea un número

2. **Creación del mensaje MIME**:
   ```python
   message = MIMEMultipart("alternative")
   message["Subject"] = subject
   message["From"] = from_email
   message["To"] = to_email
   html_part = MIMEText(html_content, "html")
   message.attach(html_part)
   ```

3. **Conexión SMTP (SIN STARTTLS)**:
   ```python
   server = smtplib.SMTP(host, port)
   # NO se usa: server.starttls()
   ```

4. **Autenticación**:
   ```python
   server.login(username, password)
   ```

5. **Envío del correo**:
   ```python
   server.send_message(message)
   ```

6. **Cierre de conexión**:
   ```python
   server.quit()
   ```

7. **Manejo de errores**:
   - `SMTPAuthenticationError`: Error en username/password
   - `SMTPException`: Otros errores SMTP
   - `Exception`: Errores generales

## Diferencias entre Puertos SMTP

### Puerto 25
- Puerto SMTP estándar
- Sin cifrado por defecto
- A menudo bloqueado por ISPs

### Puerto 2525
- Puerto alternativo no estándar
- Usado por servicios como Mailtrap
- No bloqueado por ISPs

### Puerto 465
- SMTP sobre SSL (SMTPS)
- Cifrado desde el inicio
- Depreciado pero aún usado

### Puerto 587
- Puerto estándar para envío de correo
- Usa STARTTLS para cifrado
- Recomendado por RFC

**En este ejercicio usamos 2525 SIN STARTTLS**

## MIME Multipart

### ¿Qué es MIME?
MIME (Multipurpose Internet Mail Extensions) es un estándar que permite:
- Enviar contenido en diferentes formatos (texto plano, HTML, imágenes)
- Adjuntar archivos
- Usar diferentes codificaciones de caracteres

### MIMEMultipart("alternative")
Permite enviar el mismo contenido en múltiples formatos:
- Texto plano (para clientes que no soportan HTML)
- HTML (para clientes modernos)

El cliente de correo elige la mejor versión que puede mostrar.

### Ejemplo Completo
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Crear mensaje
message = MIMEMultipart("alternative")
message["Subject"] = "Asunto"
message["From"] = "from@example.com"
message["To"] = "to@example.com"

# Añadir contenido HTML
html = "<h1>Hola</h1><p>Este es un correo HTML</p>"
html_part = MIMEText(html, "html")
message.attach(html_part)
```

## Ventajas de este Diseño

1. **Interfaz intuitiva**: Tkinter con layout organizado
2. **Log detallado**: Visibilidad completa del proceso
3. **Editor HTML**: Permite personalizar completamente el contenido
4. **Manejo de errores**: Mensajes claros para cada tipo de error
5. **Sin archivos externos**: Todo en un solo script

## Posibles Mejoras

1. **Guardar plantillas HTML**
2. **Adjuntar archivos**
3. **Lista de destinatarios múltiples**
4. **Historial de correos enviados**
5. **Configuración persistente** (guardar credenciales de forma segura)
6. **Preview del HTML** renderizado
7. **Validación de formato de email**
8. **Soporte para CC y BCC**

## Seguridad

⚠️ **IMPORTANTE**: 
- NO subir credenciales reales a GitHub
- Usar variables de entorno para datos sensibles en producción
- Este código es para fines educativos y pruebas con Mailtrap
- Mailtrap NO envía correos reales, solo los captura para pruebas

## Referencias

- [Documentación smtplib](https://docs.python.org/3/library/smtplib.html)
- [Documentación email.mime](https://docs.python.org/3/library/email.mime.html)
- [Documentación Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Mailtrap Documentation](https://help.mailtrap.io/)
