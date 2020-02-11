import click

def configure(app):

    @app.cli.command()
    @click.option('--name', '-n', required=True)
    @click.option('--date', '-d', required=True)
    def addevent(name, date):
        #click.echo(f'Name: {name}, Date: {date}')
        try:
            event = app.db['events'].insert_one({'name':name, 'date':date})
            click.echo(f'{name} was add with sucess.')
        except:
            click.echo(f'Insertion event was failure.')