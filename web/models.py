from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

GENDER_CHOICES = [   
    (1, 'เพศชาย'),
    (2, 'เพศหญิง'),
    (3, 'เพศทางเลือก'),
]
# Create your models here.
class Hospital(models.Model):
    """Model definition for Hospital."""

    # TODO: Define fields here
    hosname = models.CharField(("ชื่อโรงพยาบาล"), max_length=50)

    class Meta:
        """Meta definition for Hospital."""

        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    def __str__(self):
        """Unicode representation of Hospital."""
        return self.hosname 

class Medic(models.Model):
    """Model definition for Medic."""

    # TODO: Define fields here
    mfirst_name = models.CharField(("ชื่อจริง"), max_length=255)
    mlast_name = models.CharField(("นามสกุล"), max_length=255)
    expertise = models.CharField(("ความเชี่ยวชาญ"), max_length=255)
    affiliation = models.ManyToManyField(Hospital, default=None, null=True, blank=True)
    
    

    class Meta:
        """Meta definition for Medic."""

        verbose_name = 'Medic'
        verbose_name_plural = 'Medics'

    def __str__(self):
        """Unicode representation of Medic."""
        return self.mfirst_name + " " + self.mlast_name + " " + self.expertise + " " + self.affiliation

class Patient(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    pfirst_name = models.CharField(("ชื่อจริง"),max_length=255)
    plast_name = models.CharField(("นามสกุล"),max_length=255)
    gender = models.IntegerField(("เพศ"),choices=GENDER_CHOICES)
    age = models.CharField(("อายุ"), max_length=3, default='')
    medic = models.OneToOneField(Medic, on_delete=models.DO_NOTHING, default='', null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        """Meta definition for Patient."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Patient."""
        return self.pfirst_name + " " + self.plast_name 













    
    















