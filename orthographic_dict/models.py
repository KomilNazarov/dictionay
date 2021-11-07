
from django.contrib.auth.models import AbstractUser

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="navbar menyu:")
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Word(models.Model):
    LETTERS = [
        ('Aa', "Aa"), ('Bb', 'Bb'), ('Dd', 'Dd'), ('Ee', 'Ee'), ('Ff', 'Ff'), ('Gg', 'Gg'),
        ('Hh', 'Hh'), ('Ii', 'Ii'), ('Jj', 'Jj'), ('Kk', 'Kk'), ('Ll', 'Ll'), ('Mm', 'Mm'),
        ('Nn', 'Nn'), ('Oo', 'Oo'), ('Pp', 'Pp'), ('Qq', 'Qq'), ('Rr', 'Rr'), ('Ss', 'Ss'),
        ('Tt', 'Tt'), ('Uu', 'Uu'), ('Vv', 'Vv'), ('Xx', 'Xx'), ('Yy', 'Yy'), ('Zz', 'Zz'),
        ('O\n`o\n`', 'O\n`o\n`'), ('G\n`g\n`', 'G\n`g\n`'), ('Shsh', 'Shsh'), ('Chch', 'Chch'), ('Ngng', 'Ngng')

    ]

    _type = models.CharField(choices=LETTERS, max_length=100,  verbose_name='harfni tanlang')
    title = models.CharField(max_length=255, verbose_name='So\n`z ')
    post = models.TextField(verbose_name='So\n`zning manosi')
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Rotatsiya(models.Model):
    BILAMAN = "bilaman"
    BILMAYMAN = "bilmayman"
    TYPE_CHOICES = (
        (BILAMAN, BILAMAN),
        (BILMAYMAN, BILMAYMAN),
    )

    word = models.OneToOneField(Word, on_delete=models.CASCADE)
    _type = models.CharField(choices=TYPE_CHOICES, max_length=15)

