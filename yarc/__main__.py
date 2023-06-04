from pathlib import Path

import typer
from rich import syntax
from rich.console import Console
from rich.markup import escape
from typer import Typer

from yarc import version
from yarc.compiler.YarcCompiler import YarcCompiler
from yarc.grammar import GRAMMAR_DIR
from yarc.grammar.target_mappings import TargetLanguage, translate

app = Typer(
    name="yarc",
    help="YARC - DSL for Synthetic Data Generation",
    add_completion=True,
)
console = Console(log_path=False)


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


@app.callback(invoke_without_command=True)
def common(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the yarc package.",
    )
) -> None:
    pass


@app.command()
def compile(
    input_path: Path,
    output_path: Path = None,
    warnings: bool = False,
    num_scenes: int = None,
    mount: Path = None,
) -> None:
    try:
        with console.status("[magenta]Initializing YARC Compiler") as status:
            compiler = YarcCompiler(
                input=input_path, warnings=warnings, num_scenes=num_scenes, mount=mount
            )
            console.log(f"YARC Compiler Ready")

            status.update(
                f"[magenta]Compining scenario [bold]{input_path.stem}", spinner="runner"
            )
            output = compiler.parse()
            console.log(f"Compiling done")

        errors = compiler.errors
        if len(errors) > 0:
            console.log(f"[red bold]Oh no! There are some errors")
            for error, msg in errors.items():
                console.print(
                    f"[red][bold]:dizzy_face::stop_sign::police_car_light:{error}[/]: {msg}"
                )
            raise typer.Exit(-1)

        if warnings:
            console.log(f"[yellow bold]Mhmm, there is something that could be fixed")
            for warning, msg in compiler.warnings:
                console.print(
                    f"[yellow][bold]:grimacing::warning::megaphone:{warning}[/]: {msg}"
                )

        console.log(f"[bold green]:rocket:Scenario successfully compiled:rocket:")
        if output_path is not None:
            output_path.mkdir(parents=True, exist_ok=True)
            with output_path.open("w") as file:
                file.write(output)
            console.log(
                f"[green]You can find the translated files in [link file://{output_path.absolute()}]{escape(str(output_path.name))}[/] :page_facing_up:"
            )
        else:
            console.print(syntax.Syntax(output))

    except ValueError as ve:
        error, msg = ve.args[0].split(": ")
        console.print(
            f"[red][bold]:dizzy_face::stop_sign::police_car_light:{error}[/]: {msg}"
        )
        typer.Exit(-1)


@app.command(name="translate-grammar")
def translate_grammar(target_language: TargetLanguage, output_dir: Path) -> None:
    with console.status("[magenta]Collecting grammar files") as status:
        grammar_files = sorted(GRAMMAR_DIR.glob("*g"))
        output_dir.mkdir(parents=True, exist_ok=True)

        for path in grammar_files:
            status.update(f"[magenta]Translating [bold]{path.name}")
            _translate(
                target_language=target_language, input_path=path, output_dir=output_dir
            )

    console.log("[bold green]:tada: Grammar translated successfully :tada:")
    console.log(
        f"[green]You can find the translated files in [link file://{output_dir.absolute()}]{escape(str(output_dir))}[/] :open_file_folder:"
    )


def _translate(
    target_language: TargetLanguage, input_path: Path, output_dir: Path
) -> None:
    with input_path.open("r") as f:
        grammar = f.read()

    transformed_grammar = translate(grammar=grammar, target_language=target_language)
    console.log(
        f":white_check_mark:[bold cyan]{input_path.stem}[/] translation completed"
    )

    output_path = output_dir / input_path.name

    with output_path.open("w") as file:
        file.write(transformed_grammar)


if __name__ == "__main__":
    app()
