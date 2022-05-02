from django.db import models
from django.utils.translation import ugettext_lazy as _

class Overview(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('title'))
    image = models.ImageField(upload_to='overview', verbose_name=_('image'))
    fullname = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('fullanem'))
    abbreviated_name = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('abreviated_name'))
    main_functions = models.TextField(verbose_name=_('main_functions'))
    legal_basis = models.TextField(verbose_name=_('legal_basis'))
    main_goals = models.TextField(verbose_name=_('main_goals'))
    priority_areas = models.TextField(verbose_name=_('priority_areas'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('overview')
        verbose_name_plural = _('overviews')


class Structure(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('title'))
    image = models.ImageField(upload_to='overview', verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('structure')
        verbose_name_plural = _('structures')


class Administration(models.Model):
    positions = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('positions'))
    image = models.ImageField(upload_to='administration', verbose_name=_('image'))
    fullname = models.CharField(max_length=100, verbose_name=_('fullname'))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone'))
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('email'))
    reseption_of_sitizens = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('reseption_of_sitizens'))
    functional_duties = models.TextField(verbose_name=_('functional_duties'))
    biography = models.TextField(verbose_name=_('biography'))

    def __str__(self):
        return self.positions

    class Meta:
        verbose_name = _('administration')
        verbose_name_plural = _('administrations')


class CentralOffice(models.Model):
    positions = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('positions'))
    image = models.ImageField(upload_to='administration', verbose_name=_('image'))
    fullname = models.CharField(max_length=100, verbose_name=_('fullname'))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone'))
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('email'))
    departament = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('departament'))

    def __str__(self):
        return self.positions

    class Meta:
        verbose_name = _('centraloffice')
        verbose_name_plural = _('centraloffices')


class FightAgainstCorruption(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('title'))
    text1 = models.TextField(verbose_name=_('text1'))
    text2 = models.TextField(verbose_name=_('text2'))
    text3 = models.TextField(verbose_name=_('text3'))
    text4 = models.TextField(verbose_name=_('text4'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('fightagainstcorruption')
        verbose_name_plural = _('fightagainstcorruptions')


class TerritorialDivisions(models.Model):
    region = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('region'))
    region_departament = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('region_departament'))
    # bu yerda image ga tushadigan rasm
    image = models.ImageField(upload_to='td', verbose_name=_('image'))
    # bu yerda boshliq, 1 chi va 2 chi o'rinbosarlar nomeri berilgan
    phone_head = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone_head'))
    phone_1deputy_head = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone_1deputy_head'))
    phone_deputy_head = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone_deputy_head'))
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('address'))
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('email'))
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('website'))

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = _('territorialdivision')
        verbose_name_plural = _('territorialdivisions')


# bu yerda  Ifsatast bu Institute for staff advanced training and statistical research ning qisqartmasi
class Ifsatasr(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name=_('address'))
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('phone'))
    fax = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('fax'))
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('email'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('ifsatasr')
        verbose_name_plural = _('ifsatasrs')


class Board(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('title'))
    text1 = models.TextField(verbose_name=_('text1'))
    text2 = models.TextField(verbose_name=_('text2'))
    text3 = models.TextField(verbose_name=_('text3'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('board')
        verbose_name_plural = _('boards')

class InternationalPartnership(models.Model):
    memorandums = models.TextField(verbose_name=_('memorandums'))
    news = models.TextField(verbose_name=_('news'))
    content = models.TextField(verbose_name=_('content'))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('internationalpartnership')
        verbose_name_plural = _('internationalpartnerships')


class StatisticalCouncil(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='title')
    board_structure = models.TextField(verbose_name='board_structure')
    board_charter = models.TextField(verbose_name='board_charter')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('statistical_council')
        verbose_name_plural = _('statistical_councils')


class PublicCouncil(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='title')
    text1 = models.TextField(verbose_name='text1')
    text2 = models.TextField(verbose_name='text2')
    text3 = models.TextField(verbose_name='text3')
    text4 = models.TextField(verbose_name='text4')
    text5 = models.TextField(verbose_name='text5')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('public_council')
        verbose_name_plural = _('public_councils')


class YoungPolicy(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='title')
    text1 = models.TextField(verbose_name='text1')
    text2 = models.TextField(verbose_name='text2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('young_policy')
        verbose_name_plural = _('young_policy')


class Vacancies(models.Model):
    content = models.CharField(max_length=500, null=True, blank=True)
    salary = models.CharField(max_length=500, null=True, blank=True)
    rate = models.CharField(max_length=500, null=True, blank=True)
    extra_charge = models.CharField(max_length=500, null=True, blank=True)
    qualification_requirements = models.CharField(max_length=500, null=True, blank=True)
