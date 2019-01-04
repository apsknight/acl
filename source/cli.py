import click
import keyring
import getpass
from source.scrapper import attempt
from tabulate import tabulate

@click.command()
@click.option('-r', '--roll', prompt='Roll Number', help='Enter the Roll Number for ERP Login.')
def attendance(roll):
    """
    Get the credentials first
    """
    password = keyring.get_password('ERP', roll)
    if password == None:
        password = getpass.getpass("Password: ")
        ans = input("Do you want to store your password?(y/N)")
        if ans=='y':
            keyring.set_password('ERP', roll, password)
            

    # Fetch attendance from ERP and Pretty Print it on Terminal.
    
    response = attempt(roll, password)
    
    if not response:
        click.secho('Invalid Credentials, Login failed.', fg='red', bold=True)
    else:
        table = make_table(response)
        print(tabulate(table, headers=["Subject Name", "Attended", "Percentage"],
                tablefmt="fancy_grid"))

def make_table(response):
    result = list()
    for (code, data) in response.items():
        row = list()
        row.append(data['name'])
        row.append(data['attended'] + '/' + data['total'])
        row.append(data['percentage'])
        result.append(row)

    return result
