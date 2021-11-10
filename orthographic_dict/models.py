from django.contrib.auth import get_user_model


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
        ('O\'`o\'`', 'O\'`o\'`'), ('G\'`g\'`', 'G\'`g\'`'), ('Shsh', 'Shsh'), ('Chch', 'Chch'), ('Ngng', 'Ngng')

    ]

    _type = models.CharField(choices=LETTERS, max_length=100,  verbose_name='harfni tanlang')
    title = models.CharField(max_length=255, verbose_name='So\n`z ')
    post = models.TextField(verbose_name='So\'`zning manosi')
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

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    _type = models.CharField(choices=TYPE_CHOICES, default=BILMAYMAN, max_length=20)

    class Meta:
        unique_together = ['user', 'word']
