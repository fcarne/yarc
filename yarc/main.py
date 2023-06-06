from typing import Annotated, Optional

from pathlib import Path

import typer
from black import FileMode, format_str
from rich import syntax
from rich._emoji_codes import EMOJI
from rich.console import Console
from rich.markup import escape
from typer import Typer

from yarc import version
from yarc.compiler.handlers.exceptions import YARCException
from yarc.compiler.YarcCompiler import YarcCompiler
from yarc.grammar import GRAMMAR_DIR
from yarc.grammar.language_mappings import Language, translate

EMOJI["warning"] = "⚠️ "
EMOJI["heart_hands"] = "🫶 "
EMOJI["heart_hands_dark_skin_tone"] = "🫶🏿 "
EMOJI["heart_hands_light_skin_tone"] = "🫶🏻 "
EMOJI["heart_hands_medium-dark_skin_tone"] = "🫶🏾 "
EMOJI["heart_hands_medium-light_skin_tone"] = "🫶🏼 "
EMOJI["heart_hands_medium"] = "🫶🏽 "

app = Typer(
    name="yarc",
    add_completion=False,
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    rich_markup_mode="rich",
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
        console.print(f"[bright_magenta]yarc[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.callback(
    invoke_without_command=True,
    epilog=":flying_saucer: Made with :heart_hands: by [bold deep_pink2]Federico Carne :flying_saucer:",
)
def common(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            is_eager=True,
            help="Prints the version of the yarc package and exit.",
        ),
    ] = None,
) -> None:
    """
    :rocket: [bright_magenta bold]YARC Compiler[/] :rocket:

    Compile [cyan]YARC scenarios[/] into executable code and run it in your favorite 3D engine :artist_palette:
    """


@app.command(no_args_is_help=True)
def compile(
    input: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            show_default=False,
            help="[cyan]Path to scenario[/] to compile.",
        ),
    ],
    output_file: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            file_okay=True,
            dir_okay=False,
            writable=True,
            show_default=False,
            help="[cyan]Path[/] to the output file. If not present, output to console",
        ),
    ] = None,
    warnings: Annotated[
        bool,
        typer.Option("--warnings", "-w", help="Wheter to show also [yellow]warnings"),
    ] = False,
    lib: Annotated[
        Optional[str],
        typer.Option(
            "--lib",
            "--library",
            "-l",
            show_default=False,
            help="Overwrites the [blue]lib[/] setting in the input file",
            rich_help_panel="Overwrite settings :control_knobs: ",
        ),
    ] = None,
    num_scenes: Annotated[
        Optional[int],
        typer.Option(
            "--num-scenes",
            "-n",
            min=0,
            show_default=False,
            help="Overwrites the [blue]num_scenes[/] setting in the input file",
            rich_help_panel="Overwrite settings :control_knobs: ",
        ),
    ] = None,
    mount: Annotated[
        Optional[Path],
        typer.Option(
            "--mount",
            "-m",
            file_okay=False,
            dir_okay=True,
            show_default=False,
            help="Overwrites the [blue]mount[/] setting in the input file",
            rich_help_panel="Overwrite settings :control_knobs: ",
        ),
    ] = None,
) -> None:
    """:hammer_and_wrench:  Compile a [magenta]YARC scenario[/] into [cyan]executable code[/] for a specific engine. :hammer_and_wrench:"""
    try:
        with console.status(
            "[magenta]Preparing for liftoff... YARC Compiler initializing for launch",
            spinner="runner",
        ) as status:
            compiler = YarcCompiler(
                input=input,
                lib=lib,
                warnings=warnings,
                num_scenes=num_scenes,
                mount=mount,
            )
            console.log(f"Ready for ignition! Compiler primed and standing by")

            status.update(
                f"[magenta]Countdown in progress... Compiling scenario [bold]{input.stem}",
                spinner="moon",
            )
            output = compiler.compile()
            console.log(f"Compilation complete! Final checks before liftoff initiated")
            console.print()

        errors = compiler.errors
        if len(errors) > 0:
            console.print(
                f"[red bold]:police_car_light: Houston, we have a problem! An error has occurred in your script. Please take immediate action to resolve the issue :police_car_light:"
            )
            for error, msg in errors.items():
                console.print(
                    f"[red][bold]:police_car_light: {error}[/]: {escape(msg)}"
                )
            console.print()

        if warnings:
            console.print(
                f"[yellow bold]:warning: Attention! Anomaly detected in your code. Investigate and correct before launching into the unknown :warning:"
            )
            for warning, msg in compiler.warnings.items():
                console.print(f"[yellow][bold]:warning: {warning}[/]: {escape(msg)}")
            console.print()

        if len(errors) > 0:
            raise typer.Exit(-1)

        formatted = format_str(output, mode=FileMode())
        console.print(
            f"[bold green]:rocket: Mission accomplished! Your scenario has been successfully compiled, ready for launch! :rocket:"
        )
        if output_file is not None:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with output_file.open("w") as f:
                f.write(formatted)
            console.print(
                f"[green]You can find the compiled scenario in [link file://{output_file.absolute()}]{escape(str(output_file))}[/] :page_facing_up:"
            )
        else:
            console.print(syntax.Syntax(code=formatted, lexer="python"))
    except YARCException as e:
        console.print(
            f"[red bold]:boom: Abort! Fatal error detected in your script. Mission compromised! :boom:"
        )
        console.print(f"[red][bold]:boom: {e.error_type.type}[/]: {escape(e.message)}")
        typer.Exit(-1)


@app.command(no_args_is_help=True)
def translate_grammar(
    language: Annotated[
        Language,
        typer.Argument(
            case_sensitive=False,
            show_default=False,
            help="[cyan]Target language[/] for translation.",
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Argument(
            file_okay=False,
            dir_okay=True,
            writable=True,
            show_default=False,
            help="[cyan]Output directory[/] in which store the translated grammar.",
        ),
    ],
) -> None:
    """:notebook: Translate the [magenta]YARC grammar[/] in order to use it within a specific [cyan]programming language[/]. :notebook:"""
    with console.status(
        "[magenta]Preparing checklist... Gathering grammar files", spinner="earth"
    ) as status:
        grammar_files = sorted(GRAMMAR_DIR.glob("*g"))
        output_dir.mkdir(parents=True, exist_ok=True)

        for path in grammar_files:
            status.update(
                f"[magenta]Translating [bold]{path.name}... Ensuring accurate translation"
            )
            _translate(
                target_language=language,
                grammar_path=path,
                output_dir=output_dir,
            )

    console.print(
        "[bold green]:white_check_mark: Grammar translation successful. Checklist complete. Launch sequence initiated :white_check_mark:"
    )
    console.print(
        f"[green]:open_file_folder: You can find the translated grammar in [link file://{output_dir.absolute()}]{escape(str(output_dir))}[/] :open_file_folder:"
    )


def _translate(target_language: Language, grammar_path: Path, output_dir: Path) -> None:
    with grammar_path.open("r") as f:
        grammar = f.read()

    transformed_grammar = translate(grammar=grammar, language=target_language)
    console.log(
        f"Translation of [bold cyan]{grammar_path.stem}[/] complete. Ready for integration"
    )

    output_path = output_dir / grammar_path.name

    with output_path.open("w") as file:
        file.write(transformed_grammar)


if __name__ == "__main__":
    app()
