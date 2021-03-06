from Model.Model import Model
import click
import os
from time import sleep
os.system("color")


dataPath: str = "world.json"


@click.group()
def start() -> None:
    pass


@start.command('generate')
def generate() -> None:
    """Generate new world"""
    world.generate()
    close()


@start.command("make_step")
def makeStep() -> None:
    world.makeStep()
    close()

@start.command("make_several_steps")
@click.option('-n', '--number', default=-1, help = "Num > 0")
def makeSeveralSteps(number: int) -> None:
    try:
        if number < 0:
            raise
    except Exception:
        print("Number of steps cant be lower than zero")
        raise SystemExit
    print("\033[H\033[J ")
    for _ in range(number):
        print(world)
        sleep(0.5)
        world.makeStep()
        print("\033[H\033[J ")
    close()

@start.command("add_object")
@click.option('-o', '--object', default="Ground", help = "Plant, Ground, Herbivore or Predator")
@click.option('-x', '--xcoord', default=0, help = "from 0 to 14")
@click.option('-y', '--ycoord', default=0, help = "from 0 to 14")
def addObject(object: str, xcoord: int, ycoord: int) -> None:
    """Add object on map by coords"""
    try:
        if object not in ("Plant", "Herbivore", "Ground", "Predator"):
            raise
    except Exception:
        print("Wrong object type")
        raise SystemExit
    try:
        if ycoord < 0 or xcoord < 0:
            raise
    except Exception:
        print("Coordinates cant be lower than zero")
        raise SystemExit
    world.addObject(object, xcoord, ycoord)
    close()

@start.command("show")
def show() -> None:
    close()


def close() -> None:
    print(world)
    try:
        world.save(dataPath)
    except FileNotFoundError:
        print("Wrong datapath")
        raise SystemExit


if __name__ == "__main__":
    world: Model = Model()
    try:
        world.load(dataPath)
    except FileNotFoundError:
        print("Wrong datapath")
        raise SystemExit
    start()
    