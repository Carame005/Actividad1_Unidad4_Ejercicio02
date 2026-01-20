import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class SMTPClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente SMTP - Mailtrap")
        self.root.geometry("1200x700")
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # ========== Sección de Configuración SMTP ==========
        config_frame = ttk.LabelFrame(main_frame, text="Configuración SMTP", padding="10")
        config_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Host
        ttk.Label(config_frame, text="Host:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.host_entry = ttk.Entry(config_frame, width=30)
        self.host_entry.grid(row=0, column=1, padx=5, pady=5)
        self.host_entry.insert(0, "sandbox.smtp.mailtrap.io")
        
        # Puerto
        ttk.Label(config_frame, text="Puerto:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.port_entry = ttk.Entry(config_frame, width=10)
        self.port_entry.grid(row=0, column=3, padx=5, pady=5)
        self.port_entry.insert(0, "2525")
        
        # Username
        ttk.Label(config_frame, text="Username:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.username_entry = ttk.Entry(config_frame, width=30)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Password
        ttk.Label(config_frame, text="Password:").grid(row=1, column=2, sticky=tk.W, padx=5)
        self.password_entry = ttk.Entry(config_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # ========== Sección de Datos del Correo ==========
        email_frame = ttk.LabelFrame(main_frame, text="Datos del Correo", padding="10")
        email_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # From
        ttk.Label(email_frame, text="De (From):").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.from_entry = ttk.Entry(email_frame, width=40)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.from_entry.insert(0, "remitente@ejemplo.com")
        
        # To
        ttk.Label(email_frame, text="Para (To):").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.to_entry = ttk.Entry(email_frame, width=40)
        self.to_entry.grid(row=0, column=3, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.to_entry.insert(0, "destinatario@ejemplo.com")
        
        # Subject
        ttk.Label(email_frame, text="Asunto:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.subject_entry = ttk.Entry(email_frame, width=40)
        self.subject_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.subject_entry.insert(0, "Prueba desde Cliente SMTP Python")
        
        email_frame.columnconfigure(1, weight=1)
        email_frame.columnconfigure(3, weight=1)
        
        # ========== Dos Ventanas Grandes ==========
        content_frame = ttk.Frame(main_frame)
        content_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        # Ventana Izquierda - Editor HTML
        left_frame = ttk.LabelFrame(content_frame, text="Contenido del Correo (HTML)", padding="5")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        self.html_editor = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=50, height=20)
        self.html_editor.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Contenido HTML de ejemplo
        default_html = """<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: #2c3e50; }
        p { color: #34495e; line-height: 1.6; }
        .footer { margin-top: 20px; color: #7f8c8d; font-size: 12px; }
    </style>
</head>
<body>
    <h1>¡Hola desde Cliente SMTP Python!</h1>
    <p>Este es un correo de prueba enviado desde un cliente SMTP personalizado creado con Python y Tkinter.</p>
    <p><strong>Características:</strong></p>
    <ul>
        <li>Interfaz gráfica con Tkinter</li>
        <li>Soporte para HTML</li>
        <li>Conexión SMTP sin STARTTLS</li>
        <li>Log de respuestas del servidor</li>
    </ul>
    <div class="footer">
        <p>Enviado el """ + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + """</p>
    </div>
</body>
</html>"""
        self.html_editor.insert("1.0", default_html)
        
        # Ventana Derecha - Log de Respuestas
        right_frame = ttk.LabelFrame(content_frame, text="Respuestas del Servidor y Log", padding="5")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=20, 
                                                   bg="#f8f9fa", fg="#2c3e50")
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # ========== Botones ==========
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.send_button = ttk.Button(button_frame, text="Enviar Correo", command=self.send_email)
        self.send_button.grid(row=0, column=0, padx=5)
        
        self.clear_log_button = ttk.Button(button_frame, text="Limpiar Log", command=self.clear_log)
        self.clear_log_button.grid(row=0, column=1, padx=5)
        
        # Log inicial
        self.add_log("Sistema iniciado correctamente.", "INFO")
        self.add_log("Configure los datos de SMTP de Mailtrap y pulse 'Enviar Correo'.", "INFO")
    
    def add_log(self, message, level="INFO"):
        """Añade un mensaje al log con timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] [{level}] {message}\n"
        
        self.log_text.insert(tk.END, log_message)
        
        # Colores según el nivel
        if level == "ERROR":
            start_index = self.log_text.index("end-2c linestart")
            end_index = self.log_text.index("end-1c")
            self.log_text.tag_add("error", start_index, end_index)
            self.log_text.tag_config("error", foreground="#e74c3c")
        elif level == "SUCCESS":
            start_index = self.log_text.index("end-2c linestart")
            end_index = self.log_text.index("end-1c")
            self.log_text.tag_add("success", start_index, end_index)
            self.log_text.tag_config("success", foreground="#27ae60", font=("TkDefaultFont", 9, "bold"))
        elif level == "SERVER":
            start_index = self.log_text.index("end-2c linestart")
            end_index = self.log_text.index("end-1c")
            self.log_text.tag_add("server", start_index, end_index)
            self.log_text.tag_config("server", foreground="#3498db")
        
        self.log_text.see(tk.END)
    
    def clear_log(self):
        """Limpia el log de respuestas"""
        self.log_text.delete("1.0", tk.END)
        self.add_log("Log limpiado.", "INFO")
    
    def send_email(self):
        """Envía el correo electrónico usando SMTP"""
        # Obtener datos de configuración
        host = self.host_entry.get().strip()
        port = self.port_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        from_email = self.from_entry.get().strip()
        to_email = self.to_entry.get().strip()
        subject = self.subject_entry.get().strip()
        html_content = self.html_editor.get("1.0", tk.END)
        
        # Validación básica
        if not all([host, port, username, password, from_email, to_email, subject]):
            self.add_log("Error: Todos los campos son obligatorios.", "ERROR")
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        try:
            port = int(port)
        except ValueError:
            self.add_log("Error: El puerto debe ser un número.", "ERROR")
            messagebox.showerror("Error", "El puerto debe ser un número válido.")
            return
        
        self.add_log("=" * 60, "INFO")
        self.add_log("Iniciando envío de correo...", "INFO")
        self.add_log(f"Host: {host}:{port}", "INFO")
        self.add_log(f"De: {from_email} -> Para: {to_email}", "INFO")
        
        try:
            # Crear mensaje
            self.add_log("Creando mensaje MIME...", "INFO")
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = from_email
            message["To"] = to_email
            
            # Añadir contenido HTML
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            self.add_log("Mensaje MIME creado correctamente.", "SUCCESS")
            
            # Conectar al servidor SMTP (sin STARTTLS)
            self.add_log(f"Conectando al servidor SMTP {host}:{port}...", "INFO")
            server = smtplib.SMTP(host, port)
            server.set_debuglevel(0)  # Cambiar a 1 para ver más detalles
            
            # Obtener respuesta de conexión
            self.add_log("Conexión establecida.", "SUCCESS")
            
            # Login
            self.add_log(f"Autenticando como {username}...", "INFO")
            response = server.login(username, password)
            self.add_log(f"Respuesta del servidor: {response}", "SERVER")
            self.add_log("Autenticación exitosa.", "SUCCESS")
            
            # Enviar correo
            self.add_log("Enviando correo...", "INFO")
            result = server.send_message(message)
            
            if result:
                self.add_log(f"Advertencia: Algunos destinatarios rechazados: {result}", "ERROR")
            else:
                self.add_log("¡Correo enviado exitosamente!", "SUCCESS")
                self.add_log("Verifique su inbox en Mailtrap.", "SUCCESS")
            
            # Cerrar conexión
            server.quit()
            self.add_log("Conexión cerrada.", "INFO")
            self.add_log("=" * 60, "INFO")
            
            messagebox.showinfo("Éxito", "¡Correo enviado correctamente!\nVerifique su inbox en Mailtrap.")
            
        except smtplib.SMTPAuthenticationError as e:
            error_msg = f"Error de autenticación: {str(e)}"
            self.add_log(error_msg, "ERROR")
            self.add_log("Verifique el username y password de Mailtrap.", "ERROR")
            messagebox.showerror("Error de Autenticación", error_msg)
            
        except smtplib.SMTPException as e:
            error_msg = f"Error SMTP: {str(e)}"
            self.add_log(error_msg, "ERROR")
            messagebox.showerror("Error SMTP", error_msg)
            
        except Exception as e:
            error_msg = f"Error inesperado: {str(e)}"
            self.add_log(error_msg, "ERROR")
            messagebox.showerror("Error", error_msg)


def main():
    root = tk.Tk()
    app = SMTPClientGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
