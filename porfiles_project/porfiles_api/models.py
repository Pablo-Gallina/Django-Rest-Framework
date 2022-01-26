from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserPorfile(AbstractBaseUser, PermissionsMixin):
    """Modelo para base de datos para usuarios en el sistema"""
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserPorfileManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','name']

    def get_full_name(self):
        '''Obtener nombre completo del usuario'''
        return self.name
    
    def get_short_name(self):
        '''Obtener nombre corto del usuario'''
        return self.name

    def __str__(self):
        return self.email