from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Farmacia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class StockMedicamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name="stocks")
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name="stocks")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('farmacia', 'medicamento')

    def __str__(self):
        return f"{self.medicamento.nombre} en {self.farmacia.nombre} - Precio: ${self.precio} - Stock: {self.stock}"
