# from django.db import models
from django.contrib.gis.db import models
from stdimage import StdImageField

# Create your models here.
class Establecimiento(models.Model):
    gml_id = models.CharField(max_length=80)
    id_est = models.FloatField()
    tipo = models.CharField(max_length=80)
    tipo_descr = models.CharField(max_length=80)
    nombre_est = models.CharField(max_length=80)
    lat_est = models.FloatField()
    long_est = models.FloatField()
    codigo_sni = models.CharField(max_length=80)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.nombre_est

class Escuelas(models.Model):
    gml_id = models.CharField(max_length=80)
    codigo = models.CharField(max_length=80)
    nom_dep = models.CharField(max_length=80)
    nom_prov = models.CharField(max_length=80)
    cat_sec = models.CharField(max_length=80)
    nom_mun = models.CharField(max_length=80)
    observacio = models.CharField(max_length=80)
    cod_le = models.FloatField()
    cantue = models.FloatField()
    point_x = models.FloatField()
    point_y = models.FloatField()
    cod_prin = models.CharField(max_length=80)
    nom_prin = models.CharField(max_length=80)
    cod_sie = models.CharField(max_length=80)
    establecim = models.CharField(max_length=80)
    geom = models.PointField(srid=4326)
    
    def __str__(self):
        return self.establecim

class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=80, blank=True, null=True, help_text="Ingrese el nombre de la categoria (ej. Accidente, Bloqueo, Obras, etc.)")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre_categoria

class Tag(models.Model):
    nombre_tag = models.CharField(max_length = 50, help_text="Ingrese un nombre para el tag (ej. kermes, trabajos, accidente, accidente de moto, choque de autos, etc.)")
    def __str__(self):
        return self.nombre_tag

class Incidentes(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    direccion = models.CharField(max_length=200, help_text="Ingrese la direccion del incidente")
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=True, null=True)
    fecha_back = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Ingrese una breve descripcion del incidente")
    # foto = models.ImageField(upload_to='fotos/')
    image = StdImageField(upload_to='media/img/', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True}
    })
    tag = models.ManyToManyField('Tag', blank=True)

    INCIDENTE_ESTADO = (
        ('r', 'Reportado'),
        ('c', 'Confirmado'),
        ('e', 'Eliminado'),
    )
    estado = models.CharField(max_length=1, choices=INCIDENTE_ESTADO, blank=True, default='r', help_text='Estado del Incidente')

    geom = models.PointField(srid=4326)

    class Meta:
        ordering = ["-fecha", "categoria"]
        verbose_name_plural = "Incidentes"

    def __str__(self):
        return '{0} ({1}) {2}'.format(self.id, self.categoria.nombre_categoria, self.descripcion)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Incidente
        """
        return reverse('incidente-detail', args=[str(self.id)])

    def lista_tags(self):
        """
        Crea una lista de Tags. Esto se requiere para mostrar Tag en Admin.
        """
        return ', '.join([ tag.nombre_tag for tag in self.tag.all()[:3] ])
    lista_tags.short_description = 'tags'

    # @property
    # def popup_content(self):
    #     popup = "<span>Proprietario: </span>{}".format(
    #         self.owner)
    #     popup += "<span>Direccion: </span>{}".format(
    #         self.direccion)
    #     popup += "<span>Fecha: </span>{}".format(
    #         date(self.fecha, "d/m/Y"))
    #     popup += "<span>Descripcion: </span>{}".format(
    #         self.descripcion)
    #     popup += "<span>Categoria: </span>{}".format(
    #         self.categoria)
    #     popup += "<span>Foto: </span>{}".format(
    #         self.image.url)
    #     return popup
