from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from yarc import version


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="yarc",
    help="YARC - DSL for Synthetic Data Generation",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """
    Print the version of the package.

    Args:
        print_version (bool): Whether to print the version of the package

    Raises:
        Exit: The CLI stops its execution, always raised
    """
    if print_version:
        console.print(f"[yellow]yarc[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the yarc package.",
    ),
) -> None:
    """
    Print a greeting with a giving name.

    Args:
        name (str): The name of the person to greet.
        color (Optional[Color]): The color of the greeting.
        print_version (bool): If true, print the version of the package.

    """
    if color is None:
        color = choice(list(Color))

    greeting: str = f"Hello {name}"
    console.print(f"[bold {color}]{greeting}[/]")


if __name__ == "__main__":
    app()
