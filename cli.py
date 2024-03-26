import click
import imgkit
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name

w = 3125
options = {
    "disable-smart-width": "",
    "width": w,  # Width of the screenshot
    "zoom": w / 1000,
}


def highlight_code(code: str, language: str) -> str:
    """Helper function to highlight code in the specified language."""
    lexer = get_lexer_by_name(language, stripall=True)
    style = get_style_by_name("default")
    formatter = HtmlFormatter(linenos=True, style=style, full=True, noclasses=True)
    return highlight(code, lexer, formatter)


@click.command()
@click.argument("code_path", type=click.Path(exists=True))
@click.argument("language", type=click.STRING)
@click.argument("output_path", type=click.Path())
def produce_code_image(code_path: str, language: str, output_path: str) -> None:
    """
    CLI tool to convert code to an image.

    Parameters
    ----------
    code_path : str
        Path to the txt file with code

    language : str
        Language of the code.

    output : str
        Path to save the image.
    """
    # Read the code from the file
    with open(code_path, "r") as f:
        code = f.read()

    # Highlight the sample code
    highlighted_code = highlight_code(code, language)

    # Convert HTML to an image with specified options
    imgkit.from_string(highlighted_code, output_path, options=options)


if __name__ == "__main__":
    produce_code_image()
