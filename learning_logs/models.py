from django.db import models  # type: ignore


# Create your models here.
class Topic(models.Model):
    """Un tema sobre el que está aprendiendo el usuario"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena"""
        return self.text
  
    
class Entry(models.Model):
    """Algo específico aprendido sobre un tema"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

  
class Meta:
    verbose_name_plural = 'entries'
        
    def __str__(self):
        """Devuelve una cadena simple que representa la entrada"""
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
