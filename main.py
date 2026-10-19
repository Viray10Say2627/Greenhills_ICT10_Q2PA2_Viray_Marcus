#Working with Sets
from pyscript import display, document


def add_member(e):
    document.getElementById('result').innerHTML = ''
    First_name = document.getElementById('first_name').value.title().strip()
    Last_name = document.getElementById('last_name').value.title().strip()

    Grade_8_Members = {'Paolo Liwag', 'Aj Alburo', 'Brent Guilliermo'}
    Grade_9_Members = {'Zhaimer Mamacotao', 'Liam Omañia', 'Arkin Estacio'}
    Grade_10_Members = {'Al-Makram Arbison', 'Sebastian Uclaray', 'Aj Darimbang', 'Joaquin Tabije', 'Brenton Dela Fuente'}
    Grade_11_Members = {'Enzo Villiegas', 'Vito De guzman', 'Seth Ngo'}

    all_members = (Grade_8_Members | Grade_9_Members | Grade_10_Members | Grade_11_Members)

    display(all_members, target='results')
    display({len(all_members)}, target='results')

