"""Provides the TUI (Terminal User Interface) for the expy_tui project."""
from textual.app import App


class MyApp(App):
    """Textual app implementation for expy_tui project."""


if __name__ == "__main__":
    app = MyApp()
    app.run()
