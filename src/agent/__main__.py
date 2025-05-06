import typer
from rich.console import Console
from .chat import chat_stream

app = typer.Typer(add_completion=False, invoke_without_command=True)
console = Console()

def _stream(prompt: str) -> None:
    for token in chat_stream(prompt):
        console.print(token, end="", soft_wrap=True)
    console.print()  # newline

@app.command()
def ask(prompt: str):
    """Send a single prompt and print the reply."""
    _stream(prompt)

@app.callback()
def main(ctx: typer.Context, prompt: str | None = None):
    """
    • No argument  → interactive shell
    • With PROMPT → same as 'ask'
    """
    if prompt is not None:
        _stream(prompt)
        ctx.exit()

    console.print("[bold green]Interactive mode – type 'exit' to quit.[/]\n")
    while True:
        try:
            user = console.input("[cyan]>>> [/]").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user.lower() in {"exit", "quit"}:
            break
        if user:
            _stream(user)

if __name__ == "__main__":
    app()
