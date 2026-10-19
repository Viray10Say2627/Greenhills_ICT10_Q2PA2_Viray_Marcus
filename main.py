#Working with Sets
from pyscript import display, document


Grade_8_Members = {'Paolo Liwag', 'Aj Alburo', 'Brent Guilliermo'}
Grade_9_Members = {'Zhaimer Mamacotao', 'Liam Omañia', 'Arkin Estacio'}
Grade_10_Members = {'Al-Makram Arbison', 'Sebastian Uclaray', 'Aj Darimbang', 'Joaquin Tabije', 'Brenton Dela Fuente'}
Grade_11_Members = {'Enzo Villiegas', 'Vito De Guzman', 'Seth Ngo'}

Current_members = (Grade_8_Members | Grade_9_Members | Grade_10_Members | Grade_11_Members)

def varsity(e):
    document.getElementById('results').innerHTML = ''
    First_name = document.getElementById('first_name').value.title().strip()
    Last_name = document.getElementById('last_name').value.title().strip()
    player = First_name + " " + Last_name

    if player in Current_members:
        display(f'Current members are{(Current_members)}', target='results')
        display(f'Current members are{len(Current_members)}', target='results')

    else:
        Current_members.add(player)
        display(f'{player} was added to Varsity', target='results')
        display(f'Current members are {len(Current_members)}')

    display(f'Current members: {", ".join(sorted(Current_members))}', target='results')