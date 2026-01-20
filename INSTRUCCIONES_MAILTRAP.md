# Instrucciones para Configurar Mailtrap

## Paso 1: Crear Cuenta en Mailtrap

1. Visita [https://mailtrap.io/](https://mailtrap.io/)
2. Haz clic en "Sign Up" o "Start Free Trial"
3. Regístrate con tu email o cuenta de Google/GitHub
4. Confirma tu email si es necesario

## Paso 2: Acceder a las Credenciales SMTP

1. Una vez dentro, ve a tu **Inbox** (bandeja de entrada)
2. En el panel izquierdo, verás tu inbox de prueba (generalmente llamado "My Inbox" o "Demo inbox")
3. Haz clic en el inbox
4. En la parte superior derecha, verás **"SMTP Settings"** o **"Show Credentials"**

## Paso 3: Copiar las Credenciales

Verás algo como esto:

```
Host: sandbox.smtp.mailtrap.io
Port: 2525 (o 25, 465, 587)
Username: 4fa963cb7ea663
Password: 5e0714957e23cd
Auth: Plain
TLS: Optional (NO usaremos STARTTLS en este ejercicio)
```

## Paso 4: Configurar el Programa

1. Abre el programa `main.py`
2. En los campos de configuración SMTP, introduce:
   - **Host**: `sandbox.smtp.mailtrap.io`
   - **Puerto**: `2525` (o el que prefieras: 25, 465, 587)
   - **Username**: El username que copiaste de Mailtrap
   - **Password**: El password que copiaste de Mailtrap

## Paso 5: Enviar Correo de Prueba

1. Configura los datos del correo:
   - **De (From)**: Cualquier email (ej: `prueba@ejemplo.com`)
   - **Para (To)**: Cualquier email (ej: `destino@ejemplo.com`)
   - **Asunto**: El asunto que desees

2. Edita el contenido HTML en la ventana izquierda (opcional)

3. Haz clic en **"Enviar Correo"**

4. Observa el log en la ventana derecha:
   - Verás mensajes de conexión
   - Autenticación exitosa
   - Confirmación de envío

## Paso 6: Verificar en Mailtrap

1. Vuelve a tu navegador con Mailtrap abierto
2. Refresca el inbox (F5)
3. Deberías ver el correo recibido en la lista
4. Haz clic en el correo para ver su contenido HTML

## Notas Importantes

- **Mailtrap NO envía correos reales**: Es un servicio de prueba que captura los correos
- Los correos solo se ven en el inbox de Mailtrap, nunca llegan a destinatarios reales
- Perfecto para pruebas y desarrollo
- La cuenta gratuita tiene un límite de correos por mes (generalmente 500)

## Capturas de Pantalla Requeridas

Para el ejercicio, necesitas tomar 2 capturas:

1. **Captura del programa** mostrando:
   - El mensaje de éxito en el log
   - Los datos de configuración (puedes ocultar la password)
   - El contenido HTML del correo

2. **Captura de Mailtrap** mostrando:
   - El inbox con el correo recibido
   - El contenido HTML del correo renderizado
   - Los detalles del correo (From, To, Subject)

## Solución de Problemas

### Error de Autenticación
- Verifica que el username y password sean correctos
- Cópialos directamente desde Mailtrap (evita espacios extras)

### Error de Conexión
- Verifica que el host sea `sandbox.smtp.mailtrap.io`
- Prueba diferentes puertos: 2525, 25, 465, 587
- Verifica tu conexión a Internet

### El correo no aparece en Mailtrap
- Refresca la página (F5)
- Espera unos segundos
- Verifica que el log muestre "Correo enviado exitosamente"
