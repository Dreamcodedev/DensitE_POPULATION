# coding :utf-8

import program.world as script
import pytest

def hello(name):
    return "Hello " + name

def test_hello():
    assert hello('Didi')=='Hello Didi'

# - Agent : 
#   - modifier un attribut position
#   - récupérer un attribut position
#   - assigner un dictionnaire en tant qu'attributs
def test_get_position():
    agent=script.Agent(30)
    assert agent.position==30

# - Position :
#   - modifier un attribut longitude_degrees
#   - modifier un attribut latitude_degrees
#   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 

def test_latitude_degrees_range():
    with pytest.raises(AssertionError):
        position=script.Position(100,100)
#   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
#   - récupérer une latitude
#   - récupérer une longitude

# - Zone :
#   - trouver une zone qui contient une position
# Zone.find_zone_that_contains()
#   - ajouter un habitant dans une zone
#   - récupérer toutes les instances Zone (Zone.ZONES)
#   - récupérer la densité de population d'une zone
#   - récupérer l'agréabilité moyenne d'une zone

# - AgreeablenessGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est la densité de population moyenne
#   - la seconde valeur de xy_values est l'agréabilité moyenne

# - IncomeGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est l'âge
#   - la seconde valeur de xy_values est le revenu