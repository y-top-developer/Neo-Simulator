import click

from src.UI import UI

@click.group()
def cli():
    pass

@click.command(help=r"Run the simulator")
@click.option("-i", "--initial", help=r"Initial data format")
@click.option("-f", "--final", help=r"Final data format")
@click.option("-s", "--size", help=r"Size of initial data")
@click.option("-l", "--level", help=r"Level type")
@click.option("-p", "--pivot", help=r"Pivot for data", default=' ')
def simulator(initial, final, size, level, pivot):
    ui = UI(initial, final, level, pivot)
    ui.run()

cli.add_command(simulator)

if __name__ == "__main__":
    cli()
