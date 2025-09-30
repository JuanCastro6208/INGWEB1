from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"

class PreguntaFrecuente(models.Model):
    pregunta = models.CharField(max_length=200)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    resumen = models.CharField(max_length=250)
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='videojuegos/', blank=True, null=True)

    def __str__(self):
        return self.titulo