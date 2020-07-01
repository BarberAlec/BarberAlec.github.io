#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
"""
Provide an extension of datetime to manage revolutionnary date
"""

# remove some warning
# pylint: disable=line-too-long



from __future__ import print_function
import datetime

WIKI_BASE_URL = "https://fr.wikipedia.org/wiki/"
TROPICAL_YEAR = 365.24219878
FRENCH_REVOLUTIONARY_EPOCH = datetime.date(1792, 9, 22)

REV_DAY_NAMES = ['Primidi', 'Duodi', 'Tridi', 'Quartidi', 'Quintidi', 'Sextidi', 'Septidi',
                 'Octidi', 'Nonidi', 'Décadi']
REV_MONTH_NAMES = ['Vendémiaire', 'Brumaire', 'Frimaire', 'Nivôse', 'Pluviôse', 'Ventôse',
                   'Germinal', 'Floréal', 'Prairial', 'Messidor', 'Thermidor', 'Fructidor']
BASE_MONTH_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/"
REV_MONTH_IMAGES = [
    "c/cd/Vendémiaire_commence_le_22_septembre.jpg",
    "6/62/Brumaire_commence_le_23_octobre.jpg",
    "e/e3/Frimaire_commence_le_22_novembre.jpg",
    "b/b6/Nivôse_commence_le_22_décembre.jpg",
    "0/09/Pluviôse_commence_le_21_ou_22_janvier.jpg",
    "7/7a/Ventôse_commence_le_20_ou_21_février.jpg",
    "0/0a/Germinal_commence_le_21_ou_22_mars.jpg",
    "f/fe/Floréal_commence_le_21_avril.jpg",
    "4/4b/Prairial_commence_le_21_mai.jpg",
    "a/af/Messidor_commence_le_21_ou_22_juin.jpg",
    "b/bb/Thermidor_commence_le_20_ou_21_juillet.jpg",
    "8/8c/Fructidor_commence_le_21_ou_22_août.jpg"
]
SANSCULOTTIDES = ['Jour de la vertu', 'Jour du génie', 'Jour du travail', 'Jour de l’opinion',
                  'Jour des récompenses', 'Jour de la Révolution']

FETES = [
    [# Vendémiaire
        ("le Raisin", "Raisin", "🍇"),
        ("le Safran", "Safran (épice)"),
        ("la Châtaigne", "Châtaigne", "🌰"),
        ("le Colchique", "Colchique"),
        ("le Cheval", "Cheval", "🐴🐎"),
        ("la Balsamine", "Balsaminaceae"),
        ("la Carotte", "Carotte", "🥕"),
        ("l’Amarante", "Amarante (plante)"),
        ("le Panais", "Panais"),
        ("la Cuve", "Cuve"),
        ("la Pomme de terre", "Pomme de terre", "🥔"),
        ("l’Immortelle", "Immortelle commune"),
        ("le Potiron", "Potiron", "🎃"),
        ("le Réséda", "Réséda"),
        ("l’Âne", "Âne"),
        ("la Belle de nuit", "Mirabilis jalapa"),
        ("la Citrouille", "Citrouille", "🎃"),
        ("le Sarrasin", "Sarrasin (plante)"),
        ("le Tournesol", "Tournesol", "🌻"),
        ("le Pressoir", "Pressoir"),
        ("le Chanvre", "Chanvre"),
        ("la Pêche", "Pêche (fruit)", "🍑"),
        ("le Navet", "Navet"),
        ("l’Amaryllis", "Amaryllis (plante)"),
        ("le Bœuf", "Bos taurus", "🐮🐂"),
        ("l’Aubergine", "Aubergine", "🍆"),
        ("le Piment", "Piment", "🌶"),
        ("la Tomate", "Tomate", "🍅"),
        ("l’Orge", "Orge commune", "🌾"),
        ("le Tonneau", "Tonneau (récipient)")],
    [# Brumaire
        ("la Pomme", "Pomme", "🍎🍏"),
        ("le Céleri", "Céleri"),
        ("la Poire", "Poire", "🍐"),
        ("la Betterave", "Betterave"),
        ("l’Oie", "Oie"),
        ("l’Héliotrope", "Héliotrope"),
        ("la Figue", "Figue"),
        ("la Scorsonère", "Scorsonère"),
        ("l’Alisier", "Sorbus torminalis"),
        ("la Charrue", "Charrue"),
        ("le Salsifis", "Salsifis"),
        ("la Mâcre", "Mâcre nageante"),
        ("le Topinambour", "Topinambour"),
        ("l’Endive", "Endive"),
        ("le Dindon", "Dinde", "🦃"),
        ("le Chervis", "Chervis"),
        ("le Cresson", "Cresson de fontaine"),
        ("la Dentelaire", "Plumbago"),
        ("la Grenade", "Grenade (fruit)"),
        ("la Herse", "Herse (agriculture)"),
        ("la Bacchante", "Baccharis halimifolia"),
        ("l’Azerole", "Azerole"),
        ("la Garance", "Garance des teinturiers"),
        ("l’Orange", "Orange (fruit)", "🍊"),
        ("le Faisan", "Faisan"),
        ("la Pistache", "Pistache"),
        ("le Macjonc", "Gesse tubéreuse"),
        ("le Coing", "Coing"),
        ("le Cormier", "Cormier"),
        ("le Rouleau", "Rouleau agricole")],
    [# Frimaire
        ("la Raiponce", "Raiponce (plante)"),
        ("le Turneps", "Betterave fourragère"),
        ("la Chicorée", "Chicorée"),
        ("la Nèfle", "Nèfle"),
        ("le Cochon", "Cochon", "🐷🐖🐽🥓"),
        ("la Mâche", "Mâche"),
        ("le Chou-fleur", "Chou-fleur"),
        ("le Miel", "Miel", "🍯"),
        ("la Genièvre", "Juniperus communis"),
        ("la Pioche", "Pioche", "⛏"),
        ("la Cire", "Cire"),
        ("le Raifort", "Raifort"),
        ("le Cèdre", "Cèdre"),
        ("le Sapin", "Sapin", "🌲"),
        ("le Chevreuil", "Chevreuil", "🦌"),
        ("l’Ajonc", "Ajonc"),
        ("le Cyprès", "Cyprès"),
        ("le Lierre", "Hedera"),
        ("la Sabine", "Juniperus sabina"),
        ("le Hoyau", "Hoyau"),
        ("l’Érable sucré", "Érable à sucre", "🍁"),
        ("la Bruyère", "Bruyère"),
        ("le Roseau", "Roseau"),
        ("l’Oseille", "Oseille"),
        ("le Grillon", "Gryllidae"),
        ("le Pignon", "Pignon de pin"),
        ("le Liège", "Liège (matériau)"),
        ("la Truffe", "Truffe (champignon)"),
        ("l’Olive", "Olive"),
        ("la Pelle", "Pelle (outil)")],
    [# Nivôse
        ("la Tourbe", "Tourbe"),
        ("la Houille", "Houille"),
        ("le Bitume", "Bitume"),
        ("le Soufre", "Soufre"),
        ("le Chien", "Chien", "🐶🐕"),
        ("la Lave", "Lave", "🌋"),
        ("la Terre végétale", "Humus"),
        ("le Fumier", "Fumier", "💩"),
        ("le Salpêtre", "Nitrate de potassium"),
        ("le Fléau", "Fléau (agriculture)"),
        ("le Granit", "Granit"),
        ("l’Argile", "Argile"),
        ("l’Ardoise", "Ardoise"),
        ("le Grès", "Grès (géologie)"),
        ("le Lapin", "Oryctolagus cuniculus", "🐰🐇"),
        ("le Silex", "Silex"),
        ("la Marne", "Marne (géologie)"),
        ("la Pierre à chaux", "Calcaire"),
        ("le Marbre", "Marbre"),
        ("le Van", "Van (agriculture)"),
        ("la Pierre à plâtre", "Gypse"),
        ("le Sel", "Chlorure de sodium"),
        ("le Fer", "Fer"),
        ("le Cuivre", "Cuivre"),
        ("le Chat", "Chat", "🐱🐈"),
        ("l’Étain", "Étain"),
        ("le Plomb", "Plomb"),
        ("le Zinc", "Zinc"),
        ("le Mercure", "Mercure (chimie)"),
        ("le Crible", "Tamis")],
    [# Pluviôse
        ("la Lauréole", "Lauréole"),
        ("la Mousse", "Bryophyta"),
        ("le Fragon", "Ruscus aculeatus"),
        ("le Perce-neige", "Perce-neige"),
        ("le Taureau", "Taureau", "🐮🐂"),
        ("le Laurier tin", "Viorne tin"),
        ("l’Amadouvier", "Amadouvier"),
        ("le Mézéréon", "Bois-joli"),
        ("le Peuplier", "Peuplier"),
        ("la Cognée", "Cognée"),
        ("l’Ellébore", "Hellébore"),
        ("le Brocoli", "Brocoli", "🥦"),
        ("le Laurier", "Laurus nobilis"),
        ("l’Avelinier", "Corylus avellana"),
        ("la Vache", "Vache", "🐮🐄"),
        ("le Buis", "Buis"),
        ("le Lichen", "Lichen"),
        ("l’If", "Taxus"),
        ("la Pulmonaire", "pulmonaria"),
        ("la Serpette", "Serpette"),
        ("le Thlaspi", "Thlaspi"),
        ("le Thimele", "Daphné garou"),
        ("le Chiendent", "Chiendent"),
        ("la Trainasse", "Renouée des oiseaux"),
        ("le Lièvre", "Lièvre", "🐰🐇"),
        ("la Guède", "Guède"),
        ("le Noisetier", "Noisetier"),
        ("le Cyclamen", "Cyclamen"),
        ("la Chélidoine", "Chelidonium majus"),
        ("le Traîneau", "Traîneau")],
    [# Ventôse
        ("le Tussilage", "Tussilage"),
        ("le Cornouiller", "Cornus (plante)"),
        ("le Violier", "Vélar"),
        ("le Troène", "Troène"),
        ("le Bouc", "Bouc (animal)", "🐐"),
        ("l’Asaret", "Asaret"),
        ("l’Alaterne", "Nerprun alaterne"),
        ("la Violette", "Viola (genre végétal)"),
        ("le Marceau", "Saule marsault"),
        ("la Bêche", "Bêche"),
        ("la Narcisse", "Narcissus"),
        ("l’Orme", "Orme"),
        ("la Fumeterre", "Fumeterre"),
        ("le Vélar", "Erysimum"),
        ("la Chèvre", "Chèvre", "🐐"),
        ("l’Épinard", "Épinard"),
        ("le Doronic", "Doronicum"),
        ("le Mouron", "Mouron (flore)"),
        ("le Cerfeuil", "Cerfeuil commun"),
        ("le Cordeau", "Cordeau"),
        ("la Mandragore", "Mandragore"),
        ("le Persil", "Persil"),
        ("la Cochléaire", "Cochlearia"),
        ("la Pâquerette", "Pâquerette"),
        ("le Thon", "Thon"),
        ("le Pissenlit", "Pissenlit"),
        ("la Sylvie", "Anémone sylvie"),
        ("la Capillaire", "Capillaire de Montpellier"),
        ("le Frêne", "Frêne"),
        ("le Plantoir", "Plantoir")],
    [# Germinal
        ("la Primevère", "Primevère"),
        ("le Platane", "Platane"),
        ("l’Asperge", "Asperge"),
        ("la Tulipe", "Tulipe", "🌷"),
        ("la Poule", "Poule (animal)", "🐔🐓"),
        ("la Bette", "Bette (plante)"),
        ("le Bouleau", "Bouleau"),
        ("la Jonquille", "Jonquille"),
        ("l’Aulne", "Aulne"),
        ("le Couvoir", "Couvoir"),
        ("la Pervenche", "Pervenche"),
        ("le Charme", "Charme"),
        ("la Morille", "Morchella"),
        ("le Hêtre", "Fagus sylvatica"),
        ("l’Abeille", "Abeille", "🐝"),
        ("la Laitue", "Laitue"),
        ("le Mélèze", "Mélèze"),
        ("la Ciguë", "Apiaceae"),
        ("le Radis", "Radis"),
        ("la Ruche", "Ruche"),
        ("le Gainier", "Arbre de Judée"),
        ("la Romaine", "Laitue romaine"),
        ("le Marronnier", "Marronnier commun"),
        ("la Roquette", "Roquette (plante)", "🌼"),
        ("le Pigeon", "Pigeon", "🐦🕊"),
        ("le Lilas (commun)", "Syringa vulgaris"),
        ("l’Anémone", "Anémone"),
        ("la Pensée", "Viola (genre végétal)"),
        ("la Myrtille", "Myrtille"),
        ("le Greffoir", "Greffoir")],
    [# Floréal
        ("la Rose", "Rose (fleur)", "🌹"),
        ("le Chêne", "Chêne", "🌳"),
        ("la Fougère", "Fougère"),
        ("l’Aubépine", "Aubépine"),
        ("le Rossignol", "Rossignol", "🐦"),
        ("l’Ancolie", "Ancolie"),
        ("le Muguet", "Muguet de mai"),
        ("le Champignon", "Champignon", "🍄"),
        ("la Hyacinthe", "Hyacinthus"),
        ("le Râteau", "Râteau (outil)"),
        ("la Rhubarbe", "Rhubarbe"),
        ("le Sainfoin", "Sainfoin"),
        ("le Bâton-d'or", "Erysimum"),
        ("le Chamérisier", "Lonicera xylosteum"),
        ("le Ver à soie", "Ver à soie", "🐛"),
        ("la Consoude", "Consoude"),
        ("la Pimprenelle", "Pimprenelle"),
        ("la Corbeille d'or", "Corbeille d'or"),
        ("l’Arroche", "Arroche"),
        ("le Sarcloir", "Sarcloir"),
        ("le Statice", "Armérie maritime"),
        ("la Fritillaire", "Fritillaire"),
        ("la Bourrache", "Bourrache"),
        ("la Valériane", "Valériane"),
        ("la Carpe", "Carpe (poisson)", "🐟"),
        ("le Fusain", "Fusain d'Europe"),
        ("la Civette", "Ciboulette (botanique)"),
        ("la Buglosse", "Anchusa"),
        ("le Sénevé", "Moutarde blanche"),
        ("la Houlette", "Houlette (agriculture)")],
    [# Prairial
        ("la Luzerne", "Luzerne cultivée"),
        ("l’Hémérocalle", "Hémérocalle"),
        ("le Trèfle", "Trèfle", "☘🍀"),
        ("l’Angélique", "Angelica"),
        ("le Canard", "Canard", "🦆"),
        ("la Mélisse", "Mélisse"),
        ("le Fromental", "Fromental (plante)"),
        ("le Lis martagon", "Lis martagon"),
        ("le Serpolet", "Serpolet"),
        ("la Faux", "Faux (outil)"),
        ("la Fraise", "Fraise (fruit)", "🍓"),
        ("la Bétoine", "Bétoine"),
        ("le Pois", "Pois"),
        ("l’Acacia", "Robinia pseudoacacia"),
        ("la Caille", "Caille"),
        ("l’Œillet", "Œillet"),
        ("le Sureau", "Sureau"),
        ("le Pavot", "Pavot"),
        ("le Tilleul", "Tilleul"),
        ("la Fourche", "Fourche"),
        ("le Barbeau", "Centaurea cyanus"),
        ("la Camomille", "Camomille romaine"),
        ("le Chèvrefeuille", "Chèvrefeuille"),
        ("le Caille-lait", "Caille-lait"),
        ("la Tanche", "Tanche"),
        ("le Jasmin", "Jasmin"),
        ("la Verveine", "Verveine"),
        ("le Thym", "Thym"),
        ("la Pivoine", "Pivoine"),
        ("le Chariot", "Chariot")],
    [# Messidor
        ("le Seigle", "Seigle", "🌾"),
        ("l’Avoine", "Avoine cultivée"),
        ("l’Oignon", "Oignon"),
        ("la Véronique", "Véronique (plante)"),
        ("le Mulet", "Mulet"),
        ("le Romarin", "Romarin"),
        ("le Concombre", "Concombre", "🥒"),
        ("l’Échalote", "Échalote"),
        ("l’Absinthe", "Absinthe (plante)"),
        ("la Faucille", "Faucille"),
        ("la Coriandre", "Coriandre"),
        ("l’Artichaut", "Artichaut"),
        ("la Girofle", "Girofle"),
        ("la Lavande", "Lavande"),
        ("le Chamois", "Chamois"),
        ("le Tabac", "Tabac", "🚬"),
        ("la Groseille", "Groseille"),
        ("la Gesse", "Lathyrus"),
        ("la Cerise", "Cerise", "🍒"),
        ("le Parc", "Parc", "🏞"),
        ("la Menthe", "Menthe", "🌿"),
        ("le Cumin", "Cumin"),
        ("le Haricot", "Haricot"),
        ("l’Orcanète", "Orcanette des teinturiers"),
        ("la Pintade", "Pintade"),
        ("la Sauge", "Sauge"),
        ("l’Ail", "ail cultivé"),
        ("la Vesce", "Vesce"),
        ("le Blé", "Blé", "🌾"),
        ("la Chalemie", "Chalemie")],
    [# Thermidor
        ("l’Épeautre", "Épeautre", "🌾"),
        ("le Bouillon-blanc", "Bouillon-blanc"),
        ("le Melon", "Melon (plante)", "🍈"),
        ("l’Ivraie", "Ivraie"),
        ("le Bélier", "Bélier", "🐏"),
        ("la Prêle", "Sphenophyta"),
        ("l’Armoise", "Armoise"),
        ("la Carthame", "Carthame"),
        ("la Mûre", "Mûre (fruit de la ronce)"),
        ("l’Arrosoir", "Arrosoir"),
        ("le Panic", "Panic (plante)"),
        ("la Salicorne", "Salicorne"),
        ("l’Abricot", "Abricot"),
        ("le Basilic", "Basilic (plante)"),
        ("la Brebis", "Mouton", "🐑"),
        ("la Guimauve", "Guimauve officinale"),
        ("le Lin", "Lin cultivé"),
        ("l’Amande", "Amande"),
        ("la Gentiane", "Gentiane"),
        ("l’Écluse", "Écluse"),
        ("la Carline", "Carline"),
        ("le Câprier", "Câprier"),
        ("la Lentille", "Lentille cultivée"),
        ("l’Aunée", "Inule"),
        ("la Loutre", "Loutre"),
        ("la Myrte", "Myrte"),
        ("le Colza", "Colza"),
        ("le Lupin", "Lupin"),
        ("le Coton", "Coton"),
        ("le Moulin", "Moulin")],
    [# Fructidor
        ("la Prune", "Prune (fruit)"),
        ("le Millet", "Millet (graminée)", "🌾"),
        ("le Lycoperdon", "Vesse-de-loup"),
        ("l’Escourgeon", "Escourgeon", "🌾"),
        ("le Saumon", "Saumon"),
        ("la Tubéreuse", "Tubéreuse"),
        ("le Sucrion", "Escourgeon"),
        ("l’Apocyn", "Asclépiade commune"),
        ("la Réglisse", "Réglisse"),
        ("l’Échelle", "Échelle (outil)"),
        ("la Pastèque", "Pastèque", "🍉"),
        ("le Fenouil", "Fenouil"),
        ("l’Épine vinette", "Épine vinette"),
        ("la Noix", "Noix"),
        ("la Truite", "Truite", "🍣"),
        ("le Citron", "Citron", "🍋"),
        ("la Cardère", "Cardère sauvage"),
        ("le Nerprun", "Rhamnus"),
        ("la Tagette", "Tagetes"),
        ("la Hotte", "Panier"),
        ("l’Églantier", "Rosa canina"),
        ("la Noisette", "Noisette"),
        ("le Houblon", "Houblon", "🍺"),
        ("le Sorgho", "Sorgho commun"),
        ("l’Écrevisse", "Écrevisse", "🦐"),
        ("la Bigarade", "Bigarade"),
        ("la Verge d'or", "Verge d'or"),
        ("le Maïs", "Maïs", "🌽"),
        ("le Marron", "Marron (fruit)", "🌰"),
        ("le Panier", "Panier")]
]

def int_to_roman(value):
    """
    Convert from decimal to Roman
    """
    if not 0 <= value < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(value // ints[i])
        result.append(nums[i] * count)
        value -= ints[i] * count
    return "".join(result)

# The core functionalty of PyEphem lives in the C-language _libastro
# module, which packages the astronomy routines from XEphem as
# convenient Python types.

import _libastro as _libastro
from datetime import datetime as _datetime
from datetime import timedelta as _timedelta
from datetime import tzinfo as _tzinfo
pi = 3.14159265359

__version__ = '3.7.7.1'

twopi = pi * 2.
halfpi = pi / 2.
quarterpi = pi / 4.
eighthpi = pi / 8.

degree = pi / 180.
arcminute = degree / 60.
arcsecond = arcminute / 60.
half_arcsecond = arcsecond / 2.
tiny = arcsecond / 360.

c = 299792458.  # exact speed of light in meters/second
meters_per_au = _libastro.meters_per_au
earth_radius = _libastro.earth_radius
moon_radius = _libastro.moon_radius
sun_radius = _libastro.sun_radius

B1900 = 2415020.3135 - _libastro.MJD0
B1950 = 2433282.4235 - _libastro.MJD0
J2000 = _libastro.J2000

# We make available several basic types from _libastro.

Angle = _libastro.Angle
degrees = _libastro.degrees
hours = _libastro.hours

Date = _libastro.Date
hour = 1. / 24.
minute = hour / 60.
second = minute / 60.

default_newton_precision = second / 10.

delta_t = _libastro.delta_t
julian_date = _libastro.julian_date

Body = _libastro.Body
Planet = _libastro.Planet
PlanetMoon = _libastro.PlanetMoon
FixedBody = _libastro.FixedBody
EllipticalBody = _libastro.EllipticalBody
ParabolicBody = _libastro.ParabolicBody
HyperbolicBody = _libastro.HyperbolicBody
EarthSatellite = _libastro.EarthSatellite

readdb = _libastro.readdb
readtle = _libastro.readtle
constellation = _libastro.constellation
separation = _libastro.separation
now = _libastro.now

millennium_atlas = _libastro.millennium_atlas
uranometria = _libastro.uranometria
uranometria2000 = _libastro.uranometria2000

# We also create a Python class ("Mercury", "Venus", etcetera) for
# each planet and moon for which _libastro offers specific algorithms.

for index, classname, name in _libastro.builtin_planets():
    exec('''
class %(name)s(_libastro.%(classname)s):
    "Create a Body instance representing %(name)s"
    __planet__ = %(index)r
''' % dict(name=name, classname=classname, index=index))

del index, classname, name

# We now replace two of the classes we have just created, because
# _libastro actually provides separate types for two of the bodies.

Jupiter = _libastro.Jupiter
Saturn = _libastro.Saturn
Moon = _libastro.Moon

# Newton's method.

def newton(f, x0, x1, precision=default_newton_precision):
    """Return an x-value at which the given function reaches zero.

    Stops and declares victory once the x-value is within ``precision``
    of the solution, which defaults to a half-second of clock time.

    """
    f0, f1 = f(x0), f(x1)
    while f1 and abs(x1 - x0) > precision and f1 != f0:
        x0, x1 = x1, x1 + (x1 - x0) / (f0/f1 - 1)
        f0, f1 = f1, f(x1)
    return x1

# Find equinoxes and solstices.

_sun = Sun()                    # used for computing equinoxes

def holiday(d0, motion, offset):
    """Function that assists the finding of equinoxes and solstices."""

    def f(d):
        _sun.compute(d)
        return (_sun.ra + eighthpi) % quarterpi - eighthpi
    d0 = Date(d0)
    _sun.compute(d0)
    angle_to_cover = motion - (_sun.ra + offset) % motion
    if abs(angle_to_cover) < tiny:
        angle_to_cover = motion
    d = d0 + 365.25 * angle_to_cover / twopi
    return date(newton(f, d, d + hour))

def previous_vernal_equinox(date):
    """Return the date of the previous vernal equinox."""
    return holiday(date, -twopi, 0)

def next_vernal_equinox(date):
    """Return the date of the next vernal equinox."""
    return holiday(date, twopi, 0)

def previous_summer_solstice(date):
    """Return the date of the previous summer solstice."""
    return holiday(date, -twopi, pi + halfpi)

def next_summer_solstice(date):
    """Return the date of the next summer solstice."""
    return holiday(date, twopi, pi + halfpi)

def previous_autumnal_equinox(date):
    """Return the date of the previous autumnal equinox."""
    return holiday(date, -twopi, pi)

def next_autumnal_equinox(date):
    """Return the date of the next autumnal equinox."""
    return holiday(date, twopi, pi)

def previous_winter_solstice(date):
    """Return the date of the previous winter solstice."""
    return holiday(date, -twopi, halfpi)

def next_winter_solstice(date):
    """Return the date of the next winter solstice."""
    return holiday(date, twopi, halfpi)

# Common synonyms.

next_spring_equinox = next_vernal_equinox
previous_spring_equinox = previous_vernal_equinox

next_fall_equinox = next_autumn_equinox = next_autumnal_equinox
previous_fall_equinox = previous_autumn_equinox = previous_autumnal_equinox

# More-general functions that find any equinox or solstice.

def previous_equinox(date):
    """Return the date of the previous equinox."""
    return holiday(date, -pi, 0)

def next_equinox(date):
    """Return the date of the next equinox."""
    return holiday(date, pi, 0)

def previous_solstice(date):
    """Return the date of the previous solstice."""
    return holiday(date, -pi, halfpi)

def next_solstice(date):
    """Return the date of the next solstice."""
    return holiday(date, pi, halfpi)

# Find phases of the Moon.

_moon = Moon()                  # used for computing Moon phases

def _find_moon_phase(d0, motion, target):
    """Function that assists the finding of moon phases."""

    def f(d):
        _sun.compute(d)
        _moon.compute(d)
        slon = _libastro.eq_ecl(d, _sun.g_ra, _sun.g_dec)[0]
        mlon = _libastro.eq_ecl(d, _moon.g_ra, _moon.g_dec)[0]
        return (mlon - slon - antitarget) % twopi - pi
    antitarget = target + pi
    d0 = Date(d0)
    f0 = f(d0)
    angle_to_cover = (- f0) % motion
    if abs(angle_to_cover) < tiny:
        angle_to_cover = motion
    d = d0 + 29.53 * angle_to_cover / twopi
    return date(newton(f, d, d + hour))

def previous_new_moon(date):
    """Return the date of the previous New Moon."""
    return _find_moon_phase(date, -twopi, 0)

def next_new_moon(date):
    """Return the date of the next New Moon."""
    return _find_moon_phase(date, twopi, 0)

def previous_first_quarter_moon(date):
    """Return the date of the previous First Quarter Moon."""
    return _find_moon_phase(date, -twopi, halfpi)

def next_first_quarter_moon(date):
    """Return the date of the next First Quarter Moon."""
    return _find_moon_phase(date, twopi, halfpi)

def previous_full_moon(date):
    """Return the date of the previous Full Moon."""
    return _find_moon_phase(date, -twopi, pi)

def next_full_moon(date):
    """Return the date of the next Full Moon."""
    return _find_moon_phase(date, twopi, pi)

def previous_last_quarter_moon(date):
    """Return the date of the previous Last Quarter Moon."""
    return _find_moon_phase(date, -twopi, pi + halfpi)

def next_last_quarter_moon(date):
    """Return the date of the next Last Quarter Moon."""
    return _find_moon_phase(date, twopi, pi + halfpi)

# We provide a Python extension to our _libastro "Observer" class that
# can search for circumstances like transits.

class CircumpolarError(ValueError): pass
class NeverUpError(CircumpolarError): pass
class AlwaysUpError(CircumpolarError): pass

def describe_riset_search(method):
    method.__doc__ += """, returning its date.

    The search starts at the `date` of this `Observer` and is limited to
    the single circuit of the sky, from antitransit to antitransit, that
    the `body` was in the middle of describing at that date and time.
    If the body did not, in fact, cross the horizon in the direction you
    are asking about during that particular circuit, then the search
    must raise a `CircumpolarError` exception like `NeverUpError` or
    `AlwaysUpError` instead of returning a date.

    """
    return method

class Observer(_libastro.Observer):
    """A location on earth for which positions are to be computed.

    An `Observer` instance allows you to compute the positions of
    celestial bodies as seen from a particular latitude and longitude on
    the Earth's surface.  The constructor takes no parameters; instead,
    set its attributes once you have created it.  Defaults:

    `date` - the moment the `Observer` is created
    `lat` - zero degrees latitude
    `lon` - zero degrees longitude
    `elevation` - 0 meters above sea level
    `horizon` - 0 degrees
    `epoch` - J2000
    `temp` - 15 degrees Celsius
    `pressure` - 1010 mBar

    """
    __slots__ = [ 'name' ]
    elev = _libastro.Observer.elevation

    def copy(self):
        o = self.__class__()
        o.date = self.date
        o.lat = self.lat
        o.lon = self.lon
        o.elev = self.elev
        o.horizon = self.horizon
        o.epoch = self.epoch
        o.temp = self.temp
        o.pressure = self.pressure
        return o

    def __repr__(self):
        """Return a useful textual representation of this Observer."""
        return ('<ephem.Observer date=%r epoch=%r'
                " lon='%s' lat='%s' elevation=%sm"
                ' horizon=%s temp=%sC pressure=%smBar>'
                % (str(self.date), str(self.epoch),
                   self.lon, self.lat, self.elevation,
                   self.horizon, self.temp, self.pressure))

    def compute_pressure(self):
        """Set the atmospheric pressure for the current elevation."""
        # Formula from the ISA Standard Atmosphere
        self.pressure = (1013.25 * (1 - 0.0065 * self.elevation / 288.15)
                         ** 5.2558761132785179)

    def _compute_transit(self, body, start, sign, offset):
        """Internal function used to compute transits."""

        if isinstance(body, EarthSatellite):
            raise TypeError(
                'the next and previous transit methods do not'
                ' support earth satellites because of their speed;'
                ' please use the higher-resolution next_pass() method'
                )

        def f(d):
            self.date = d
            body.compute(self)
            return degrees(offset - sidereal_time() + body.g_ra).znorm

        if start is not None:
            self.date = start
        sidereal_time = self.sidereal_time
        body.compute(self)
        ha = sidereal_time() - body.g_ra
        ha_to_move = (offset - ha) % (sign * twopi)
        if abs(ha_to_move) < tiny:
            ha_to_move = sign * twopi
        d = self.date + ha_to_move / twopi
        result = Date(newton(f, d, d + minute))
        return result

    def _previous_transit(self, body, start=None):
        """Find the previous passage of a body across the meridian."""

        return self._compute_transit(body, start, -1., 0.)

    def _next_transit(self, body, start=None):
        """Find the next passage of a body across the meridian."""

        return self._compute_transit(body, start, +1., 0.)

    def _previous_antitransit(self, body, start=None):
        """Find the previous passage of a body across the anti-meridian."""

        return self._compute_transit(body, start, -1., pi)

    def _next_antitransit(self, body, start=None):
        """Find the next passage of a body across the anti-meridian."""

        return self._compute_transit(body, start, +1., pi)

    def previous_transit(self, body, start=None):
        """Find the previous passage of a body across the meridian."""

        original_date = self.date
        d = self._previous_transit(body, start)
        self.date = original_date
        return d

    def next_transit(self, body, start=None):
        """Find the next passage of a body across the meridian."""

        original_date = self.date
        d = self._next_transit(body, start)
        self.date = original_date
        return d

    def previous_antitransit(self, body, start=None):
        """Find the previous passage of a body across the anti-meridian."""

        original_date = self.date
        d = self._previous_antitransit(body, start)
        self.date = original_date
        return d

    def next_antitransit(self, body, start=None):
        """Find the next passage of a body across the anti-meridian."""

        original_date = self.date
        d = self._next_antitransit(body, start)
        self.date = original_date
        return d

    def disallow_circumpolar(self, declination):
        """Raise an exception if the given declination is circumpolar.

        Raises NeverUpError if an object at the given declination is
        always below this Observer's horizon, or AlwaysUpError if such
        an object would always be above the horizon.

        """
        if abs(self.lat - declination) >= halfpi:
            raise NeverUpError('The declination %s never rises'
                               ' above the horizon at latitude %s'
                               % (declination, self.lat))
        if abs(self.lat + declination) >= halfpi:
            raise AlwaysUpError('The declination %s is always'
                                ' above the horizon at latitude %s'
                                % (declination, self.lat))

    def _riset_helper(self, body, start, use_center, rising, previous):
        """Internal function for finding risings and settings."""

        if isinstance(body, EarthSatellite):
            raise TypeError(
                'the rising and settings methods do not'
                ' support earth satellites because of their speed;'
                ' please use the higher-resolution next_pass() method'
                )

        def visit_transit():
            d = (previous and self._previous_transit(body)
                 or self._next_transit(body)) # if-then
            if body.alt + body.radius * use_radius - self.horizon <= 0:
                raise NeverUpError('%r transits below the horizon at %s'
                                   % (body.name, d))
            return d

        def visit_antitransit():
            d = (previous and self._previous_antitransit(body)
                 or self._next_antitransit(body)) # if-then
            if body.alt + body.radius * use_radius - self.horizon >= 0:
                raise AlwaysUpError('%r is still above the horizon at %s'
                                    % (body.name, d))
            return d

        # Determine whether we should offset the result for the radius
        # of the object being measured, or instead pretend that rising
        # and setting happens when its center crosses the horizon.
        if use_center:
            use_radius = 0.0
        else:
            use_radius = 1.0

        # Save self.date so that we can restore it before returning.
        original_date = self.date

        # Start slightly to one side of the start date, to prevent
        # repeated calls from returning the same solution over and over.
        if start is not None:
            self.date = start
        if previous:
            self.date -= default_newton_precision
        else:
            self.date += default_newton_precision

        # Take a big leap towards the solution, then Newton takes us home.
        body.compute(self)
        heading_downward = (rising == previous) # "==" is inverted "xor"
        if heading_downward:
            on_lower_cusp = (body.alt + body.radius * use_radius
                             - self.horizon > tiny)
        else:
            on_lower_cusp = (body.alt + body.radius * use_radius
                             - self.horizon < - tiny)

        az = body.az
        on_right_side_of_sky = ((rising == (az < pi)) # inverted "xor"
                                or (az < tiny
                                    or pi - tiny < az < pi + tiny
                                    or twopi - tiny < az))

        def f(d):
            self.date = d
            body.compute(self)
            return body.alt + body.radius * use_radius - self.horizon

        try:
            if on_lower_cusp and on_right_side_of_sky:
                d0 = self.date
            elif heading_downward:
                d0 = visit_transit()
            else:
                d0 = visit_antitransit()
            if heading_downward:
                d1 = visit_antitransit()
            else:
                d1 = visit_transit()

            d = (d0 + d1) / 2.
            result = Date(newton(f, d, d + minute))
            return result
        finally:
            self.date = original_date

    @describe_riset_search
    def previous_rising(self, body, start=None, use_center=False):
        """Search for the given body's previous rising"""
        return self._riset_helper(body, start, use_center, True, True)

    @describe_riset_search
    def previous_setting(self, body, start=None, use_center=False):
        """Search for the given body's previous setting"""
        return self._riset_helper(body, start, use_center, False, True)

    @describe_riset_search
    def next_rising(self, body, start=None, use_center=False):
        """Search for the given body's next rising"""
        return self._riset_helper(body, start, use_center, True, False)

    @describe_riset_search
    def next_setting(self, body, start=None, use_center=False):
        """Search for the given body's next setting"""
        return self._riset_helper(body, start, use_center, False, False)

    def next_pass(self, body, singlepass=True):
        """Return the next rising, culmination, and setting of a satellite.
        
        If singlepass is True, return next consecutive set of
            (rising, culmination, setting).
        If singlepass is False, return 
            (next_rising, next_culmination, next_setting)
        """

        if not isinstance(body, EarthSatellite):
            raise TypeError(
                'the next_pass() method is only for use with'
                ' EarthSatellite objects because of their high speed'
                )

        result = _libastro._next_pass(self, body)
        # _libastro behavior is singlepass=False
        if ((not singlepass)
                or (None in result) 
                or (result[4] >= result[0])):
            return result
        # retry starting just before next_rising
        obscopy = self.copy()
        # Almost always 1 minute before next_rising except
        # in pathological case where set came immediately before rise
        obscopy.date = result[0] - min(1.0/1440,
                            (result[0] - result[4])/2)
        result = _libastro._next_pass(obscopy, body)
        if result[0] <= result[2] <= result[4]:
            return result
        raise ValueError("this software is having trouble with those satellite parameters")
        

del describe_riset_search

# Time conversion.

def _convert_to_seconds_and_microseconds(date):
    """Converts a PyEphem date into seconds"""
    microseconds = int(round(24 * 60 * 60 * 1000000 * date))
    seconds, microseconds = divmod(microseconds, 1000000)
    seconds -= 2209032000  # difference between epoch 1900 and epoch 1970
    return seconds, microseconds




class _UTC(_tzinfo):
    ZERO = _timedelta(0)
    def utcoffset(self, dt):
        return self.ZERO
    def dst(self, dt):
        return self.ZERO
    def __repr__(self):
        return "<ephem.UTC>"


UTC = _UTC()


def to_timezone(date, tzinfo):
    """"Convert a PyEphem date into a timezone aware Python datetime representation."""
    seconds, microseconds = _convert_to_seconds_and_microseconds(date)
    date = _datetime.fromtimestamp(seconds, tzinfo)
    date = date.replace(microsecond=microseconds)
    return date

# Coordinate transformations.

class Coordinate(object):
    def __init__(self, *args, **kw):

        # Accept an optional "epoch" keyword argument.

        epoch = kw.pop('epoch', None)
        if epoch is not None:
            self.epoch = epoch = Date(epoch)
        if kw:
            raise TypeError('"epoch" is the only keyword argument'
                            ' you can use during %s instantiation'
                            % (type(self).__name__))

        # Interpret a single-argument initialization.

        if len(args) == 1:
            a = args[0]

            if isinstance(a, Body):
                a = Equatorial(a.a_ra, a.a_dec, epoch = a.a_epoch)

            for cls in (Equatorial, Ecliptic, Galactic):
                if isinstance(a, cls):

                    # If the user omitted an "epoch" keyword, then
                    # use the epoch of the other object.

                    if epoch is None:
                        self.epoch = epoch = a.epoch

                    # If we are initialized from another of the same
                    # kind of coordinate and epoch, simply copy the
                    # coordinates and epoch into this new object.

                    if isinstance(self, cls) and epoch == a.epoch:
                        self.set(*a.get())
                        return

                    # Otherwise, convert.

                    ra, dec = a.to_radec()
                    if epoch != a.epoch:
                        ra, dec = _libastro.precess(
                            a.epoch, epoch, ra, dec
                            )
                    self.from_radec(ra, dec)
                    return

            raise TypeError(
                'a single argument used to initialize %s() must be either'
                ' a coordinate or a Body, not an %r' % (type(a).__name__,)
                )

        # Two arguments are interpreted as (ra, dec) or (lon, lat).

        elif len(args) == 2:
            self.set(*args)
            if epoch is None:
                self.epoch = epoch = Date(J2000)

        else:
            raise TypeError(
                'to initialize %s you must pass either a Body,'
                ' another coordinate, or two coordinate values,'
                ' but not: %r' % (type(self).__name__, args,)
                )

class Equatorial(Coordinate):
    """An equatorial sky coordinate in right ascension and declination."""

    def get(self):
        return self.ra, self.dec

    def set(self, ra, dec):
        self.ra, self.dec = hours(ra), degrees(dec)

    to_radec = get
    from_radec = set

class LonLatCoordinate(Coordinate):
    """A coordinate that is measured with a longitude and latitude."""

    def set(self, lon, lat):
        self.lon, self.lat = degrees(lon), degrees(lat)

    def get(self):
        return self.lon, self.lat

    @property
    def long(self):
        return self.lon

    @long.setter
    def long(self, value):
        self.lon = value

class Ecliptic(LonLatCoordinate):
    """An ecliptic latitude and longitude."""

    def to_radec(self):
        return _libastro.ecl_eq(self.epoch, self.lon, self.lat)

    def from_radec(self, ra, dec):
        self.lon, self.lat = _libastro.eq_ecl(self.epoch, ra, dec)

class Galactic(LonLatCoordinate):
    """A galactic latitude and longitude."""

    def to_radec(self):
        return _libastro.gal_eq(self.epoch, self.lon, self.lat)

    def from_radec(self, ra, dec):
        self.lon, self.lat = _libastro.eq_gal(self.epoch, ra, dec)

# For backwards compatibility, provide lower-case names for our Date
# and Angle classes, and also allow "Lon" to be spelled "Long".

date = Date
angle = Angle
LongLatCoordinate = LonLatCoordinate



def annee_de_la_revolution(date):
    """
    Find corresponding revolutionnary year of current date
    """
    # Time are in UT (time at Greenwich meridian, so 0°)
    # but we want the equinox at Paris meridian time so 2°20'13,82" (the one used in 1792)
    # using the IGN value 2°20'13,82", add 14ms...
    # see http://geodesie.ign.fr/contenu/fichiers/Meridiens_greenwich_paris.pdf (fr)
    # => +0.15581138888888888888 hour == .00649214120370370370
    lasteq = Date(previous_autumnal_equinox(date) + 0.00649214120370370370)
    nexteq = Date(next_autumn_equinox(date) + 0.00649214120370370370)


#    print(lasteq, nexteq)
    neq_dt = nexteq.datetime()
    if neq_dt.year == date.year and neq_dt.month == date.month and neq_dt.day == date.day:
        #the autumn equinox is the day we ask for (but after 00:00), so the lasteq is the current day
        lasteq = nexteq

    year = ((lasteq - Date(FRENCH_REVOLUTIONARY_EPOCH)) / TROPICAL_YEAR) + 1
    return (int(year), lasteq.datetime().date())

def d_to_french_revolutionary(date):
    """
    return a dictionnary contain revolutionnary information

    'an' : Year number
    'mois': nb month, if > len(month) this are the extra Revolutionnaries months (ie extra days)
            starting 0
    'jour': nb days in month, starting 0
    'decade': nb of the decade in the year ( ~week number)
    """
    rdate = {}
    rdate['an'], equinoxe = annee_de_la_revolution(date)
    nb_day_in_year = (date - equinoxe).days
    rdate['mois'] = nb_day_in_year // 30
    rdate['jour'] = nb_day_in_year % 30
    rdate['decade'] = (rdate['jour'] // 10) + 1 + 3*rdate['mois']
    return rdate



class RDate(datetime.date):
    """
    Revolutionnary datetime.date
    """
    def __new__(cls, year, month, day):
        return datetime.date.__new__(cls, year, month, day)

    def revo(self):
        """
        revo uple
        """
        return d_to_french_revolutionary(self)

    def revol_strftime(self, fmt):
        """ modify fmt with specific revol format """
        rdate = d_to_french_revolutionary(self)
        newformat = []
        push = lambda val: newformat.append(str(val))
        i, n = 0, len(fmt)
        while i < n:
            char = fmt[i]
            i += 1
            if char == "%":
                if i < n:
                    char = fmt[i]
                    i += 1
                    if char == "r":
                        if i < n:
                            char = fmt[i]
                            i += 1
                            if char == "A":
                                # Decadeday as locale’s full name.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push(SANSCULOTTIDES[rdate['jour'] % 10])
                                else:
                                    push(REV_DAY_NAMES[rdate['jour'] % 10])
                            elif char == "w":
                                # Decadeday as a decimal number, where 0 is Primid and 9 is Decadi.
                                push(rdate['jour'] % 10)
                            elif char == "d":
                                #Day of the month as a zero-padded decimal number.
                                push("%02d" % (rdate['jour'] + 1))
                            elif char == "B":
                                #Month as locale’s full name
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    push(REV_MONTH_NAMES[rdate['mois']])
                            elif char == "I":
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    push("{}{}".format(BASE_MONTH_IMAGE,
                                                       REV_MONTH_IMAGES[rdate['mois']]))
                            elif char == "m":
                                #Month as a zero-padded decimal number
                                push("%02d" % (rdate['mois'] + 1))
                            elif char == "y":
                                #Year as decimal number.
                                push(rdate['an'])
                            elif char == "Y":
                                #Year as Roman number.
                                push(int_to_roman(rdate['an']))
                            elif char == "W":
                                #Decade number in the year.
                                push(rdate['decade'])
                            elif char == "f":
                                #fete of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push(SANSCULOTTIDES[rdate['jour'] % 10])
                                else:
                                    push(FETES[rdate['mois']][rdate['jour']][0])
                            elif char == "F":
                                #wikipedia url of the fete of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    resource = FETES[rdate['mois']][rdate['jour']][1]
                                    push("{}{}".format(WIKI_BASE_URL, resource.replace(" ", "_")))
                            elif char == "u":
                                #unicode of the day.
                                if rdate['mois'] >= len(REV_MONTH_NAMES):
                                    push("")
                                else:
                                    try:
                                        push(FETES[rdate['mois']][rdate['jour']][2])
                                    except IndexError:
                                        push("")
                            else:
                                push("%r")
                                push(char)
                        else:
                            push("%r")


                    else:
                        push("%")
                        push(char)
                else:
                    push("%")
            else:
                push(char)


        newformat = "".join(newformat)
        if self.year < 1900:
            return newformat
        else:
            return self.strftime(newformat)

    def __format__(self, fmt):
        """
            add some new format to display date
            %r should start any revolutionarry modifiator

            %rA Week^WDecadeday as locale’s full name.
            %rw Week^WDecadeday as a decimal number, where 0 is Primid and 9 is Decadi.

            %rd Day of the month as a zero-padded decimal number.
            %rB Month as locale’s full name
            %rI link to wikipedia image for the month.
            %rm Month as a zero-padded decimal number.
            %ry Year as decimal number.
            %rY Year as Roman number.
            %rW Decade number in the year.
            %rf grain, pasture, trees, roots, flowers, fruits, animal, tool associated with the day
            %rF link to the french wikipage associated with the day
            %ru unicode emoji associated with the day (if exist, else empty)
        """
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.revol_strftime(fmt)
        return str(self)


def my_display(argv):
    """
    display date as I want
    """
    ldate = RDate.today()
    prefix = "Nous sommes le"
    if len(argv) == 2:
        ldate = None
        try:
            delay = int(argv[1])
            tdate = datetime.date.today() + datetime.timedelta(delay)
            ldate = RDate(tdate.year, tdate.month, tdate.day)
            if delay == 0:
                prefix = "Aujourd’hui ({0:%A %d %B %Y}) nous sommes le".format(ldate)
            elif delay == 1:
                prefix = "Demain ({0:%A %d %B %Y}) sera le".format(ldate)
            elif delay == 2:
                prefix = "Après-demain ({0:%A %d %B %Y}) sera le".format(ldate)
            elif delay == -1:
                prefix = "Hier ({0:%A %d %B %Y}) était le".format(ldate)
            elif delay == -2:
                prefix = "Avant-hier ({0:%A %d %B %Y}) était le".format(ldate)
            else:
                prefix = "Le {0:%A %d %B %Y} correspond à".format(ldate)
        except ValueError:
            print("value error")
    if len(argv) == 4:
        ldate = RDate(int(argv[1]), int(argv[2]), int(argv[3]))
        prefix = "Le {0:%A %d %B %Y} correspond à".format(ldate)
    print("Salut et fratern·soror·ité !")
    print("Salut et fraternité !")
    print("{0} {1:%rA %rd %rB %rY (%ry/%rm/%rd)}".format(prefix, ldate))
    fete_name = "{0:%rf} {0:%ru} ".format(ldate).strip()
    if fete_name.startswith("le "):
        article = "au"
        fete_name = fete_name[3:]
    else:
        article = "à"
    print("Cette journée est dédiée {} {} {:%rF}".format(article, fete_name, ldate))
    print("{0:%rB : %rI}".format(ldate))

    print("")

if __name__ == "__main__":
    import sys
    my_display(sys.argv)
