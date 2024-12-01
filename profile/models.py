from django.contrib.auth.models import User
from django.db import models

from profile.utils import BaseModel


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Skill Name')

    def __str__(self):
        return self.name


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    bio = models.TextField(blank=True, verbose_name='Bio')
    skills = models.ManyToManyField(Skill, blank=True,
                                    related_name='profiles')

    job_experience = models.TextField(blank=True,
                                      verbose_name='Job Experience')
    education = models.TextField(blank=True,
                                 verbose_name='Education')
    certificates = models.TextField(blank=True,
                                    verbose_name='Certificates')

    def __str__(self):
        return f'{self.user.username} profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']
