import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base (models.Model):
    criados = models.DateField('Criacao', auto_now_add=True)
    modificado = models.DateField('Atualizacao', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Recurso(Base):
    ICONE_CHOICES=(
        ('lni-rocket','foguete'),
        ('lni-laptop-phone','notebookCelular'),
        ('lni-cog', 'engrenagem'),
        ('lni-cog', 'engrenagem'),
        ('lni-leaf', 'folha'),
        ('lni-layers', 'camadas'),
    )

    recurso = models.CharField('Feature',max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone',max_length=16,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso

class Servico(Base):
    ICONE_CHOICES=(
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servicos', max_length=100)
    descricao = models.TextField('Descricao',max_length=200)
    icone = models.CharField('Icone',max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome',max_length=100)
    cargo = models.ForeignKey('core.Cargo',verbose_name='Cargo',on_delete=models.CASCADE)
    bio = models.TextField('Bio',max_length=200)
    imagem = StdImageField('Imagem',upload_to=get_file_path,variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome

