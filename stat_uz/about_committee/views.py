from django.shortcuts import render

from about_committee.models import *
from django.views.generic import TemplateView, ListView, DetailView


class HomeTemplateViews(TemplateView):
    template_name = 'index.html'

class OverviewListView(ListView):
    model = Overview
    template_name = 'overview.html'

class StructureListView(ListView):
    model = Structure
    template_name = 'structure.html'


class AdministrationListView(ListView):
    model = Administration
    template_name = 'administration.html'


class FunctionalDuties(DetailView):
    model = Administration
    template_name = 'functional_duties.html'


class Biography(DetailView):
    model = Administration
    template_name = 'biography.html'

class CentralofficeListView(ListView):
    model = CentralOffice
    template_name = 'centraloffice.html'


class FightagainstcorruptionListView(ListView):
    model = FightAgainstCorruption
    template_name = 'fightagainstcorruption.html'


class TerritorialDivisionsListView(ListView):
    model = TerritorialDivisions
    template_name = 'territorialdivisions.html'

class BoardListView(ListView):
    model = Board
    template_name = 'board.html'


class IfsatasrListView(ListView):
    model = Ifsatasr
    template_name = 'ifsatasr.html'


class InternationalPartnershipListView(ListView):
    model = InternationalPartnership
    template_name = 'internationalpartnership.html'


class StatisticalCouncilListView(ListView):
    model = StatisticalCouncil
    template_name = 'statisticalouncil.html'

class PublicCouncilListView(ListView):
    model = PublicCouncil
    template_name = 'public_council.html'


class YoungPolicyListView(ListView):
    model = YoungPolicy
    template_name = 'young_policy.html'


class VacanciesListView(ListView):
    model = Vacancies
    template_name = 'vacancies.html'


