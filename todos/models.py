from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False) 
    created_at = models.DateField(auto_now_add=True, null=False, blank=False) #data de criação
    deadline = models.DateField(verbose_name="Data de Entrega",null=False, blank=False) #prazo
    finished_at = models.DateField(null=True)#data que foi finalizado

    class Meta:
        ordering = ["deadline"]
    
    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()