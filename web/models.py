from django.db import models

GENDER_CHOICES = [
    (0, 'เลือกเพศ'),
    (1, 'เพศชาย'),
    (2, 'เพศหญิง'),
    (3, 'เพศทางเลือก'),
]
# Create your models here.
class Patient(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    pfirst_name = models.CharField(("ชื่อจริง"),max_length=255)
    plast_name = models.CharField(("นามสกุล"),max_length=255)
    gender = models.IntegerField(("เพศ"),choices=GENDER_CHOICES, default=0)
    age = models.CharField(("อายุ"), max_length=3, default='')

    class Meta:
        """Meta definition for Patient."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Patient."""
        return self.pfirst_name + " " + self.plast_name + " " + self.age



