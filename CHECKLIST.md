# Checklist de Entrega - Ejercicio 2

## ✅ Requisitos del Programa

- [x] No usar STARTTLS ✓
- [x] Campos de entrada para Host, Puerto, Username, Password ✓
- [x] Dos ventanas grandes:
  - [x] Izquierda: Editor de texto HTML (contenido del correo) ✓
  - [x] Derecha: Respuestas del servidor y mensajes de log/error ✓
- [x] Usar smtplib y email.mime ✓

## ✅ Configuración de Mailtrap

- [ ] Crear cuenta gratuita en Mailtrap
- [ ] Obtener credenciales:
  - [ ] Username
  - [ ] Password
  - [ ] Host (sandbox.smtp.mailtrap.io)
  - [ ] Puerto (2525)
- [ ] Enviar al menos un correo correctamente

## ✅ Capturas de Pantalla

- [ ] **Captura 1**: Programa mostrando mensaje enviado correctamente
  - Guardar como: `capturas/programa_enviado.png`
  - Debe mostrar:
    - Configuración SMTP
    - Datos del correo
    - Log con "¡Correo enviado exitosamente!"

- [ ] **Captura 2**: Inbox de Mailtrap con correo recibido
  - Guardar como: `capturas/mailtrap_recibido.png`
  - Debe mostrar:
    - Lista de correos en el inbox
    - Contenido HTML del correo
    - Detalles (From, To, Subject)

## ✅ Documentación

- [ ] Pegar ambas capturas en el documento del Ejercicio 1
- [ ] Añadir explicación breve si es necesario

## ✅ Entrega en GitHub

- [ ] Subir código del programa (main.py) ✓
- [ ] Subir las dos capturas de pantalla
- [ ] Subir el documento con las capturas
- [ ] Verificar que el repositorio sea público o compartido con el profesor

## Comandos Git para Subir

```bash
# Inicializar repositorio (si no existe)
git init

# Añadir todos los archivos
git add .

# Commit
git commit -m "Ejercicio 2: Cliente SMTP Python con Tkinter"

# Conectar con repositorio remoto
git remote add origin <URL_DE_TU_REPOSITORIO>

# Subir a GitHub
git push -u origin main
```

## Verificación Final

- [ ] El código se ejecuta sin errores
- [ ] Las capturas están en la carpeta `capturas/`
- [ ] El documento está actualizado con ambas capturas
- [ ] Todo está subido a GitHub
- [ ] El README.md tiene instrucciones claras

## Archivos que Deben Estar en GitHub

```
Ejercicio2/
├── main.py                      ✓ (Código principal)
├── README.md                    ✓ (Instrucciones)
├── DOCUMENTACION.md             ✓ (Explicación técnica)
├── INSTRUCCIONES_MAILTRAP.md    ✓ (Guía de Mailtrap)
├── .gitignore                   ✓ (Archivos ignorados)
├── CHECKLIST.md                 ✓ (Este archivo)
├── capturas/
│   ├── README.md                ✓ (Instrucciones de capturas)
│   ├── programa_enviado.png     ⏳ (Por hacer)
│   └── mailtrap_recibido.png    ⏳ (Por hacer)
└── documento_ejercicio1y2.pdf   ⏳ (Por hacer)
```

## Pasos Siguientes

1. **Configurar Mailtrap**:
   - Ir a https://mailtrap.io/
   - Crear cuenta gratuita
   - Obtener credenciales SMTP

2. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

3. **Configurar credenciales en la aplicación**:
   - Introducir Host, Puerto, Username, Password

4. **Enviar correo de prueba**:
   - Completar datos del correo
   - Clic en "Enviar Correo"

5. **Tomar capturas**:
   - Captura del programa con éxito
   - Captura de Mailtrap con correo recibido

6. **Actualizar documento**:
   - Añadir capturas al documento del Ejercicio 1
   - Guardar como PDF

7. **Subir a GitHub**:
   - Commit y push de todo el contenido

## Notas Importantes

⚠️ **NO subir credenciales reales**: El .gitignore ya está configurado
✅ **Mailtrap es seguro**: No envía correos reales, solo pruebas
📸 **Calidad de capturas**: Asegúrate de que se vean claramente
📝 **Documentación**: Los archivos MD explican todo el proceso

## Contacto

Si tienes dudas sobre el ejercicio, revisa:
1. README.md - Instrucciones generales
2. INSTRUCCIONES_MAILTRAP.md - Configuración de Mailtrap
3. DOCUMENTACION.md - Explicación técnica del código
