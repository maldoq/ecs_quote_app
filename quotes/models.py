from django.db import models


class Quote(models.Model):
    """Modèle pour les citations"""
    text = models.TextField(verbose_name="Citation")
    author = models.CharField(max_length=200, verbose_name="Auteur")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Citation"
        verbose_name_plural = "Citations"
        ordering = ['id']
    
    def __str__(self):
        return f"{self.author} - {self.text[:50]}..."


class UserQuote(models.Model):
    """Modèle pour associer un utilisateur à une citation"""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    ecole = models.CharField(max_length=200, verbose_name="École")
    email = models.EmailField(verbose_name="Email", unique=True)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name="Citation")
    created_at = models.DateTimeField(auto_now_add=True)

    card_image = models.ImageField(
        upload_to='cards/',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.email}"