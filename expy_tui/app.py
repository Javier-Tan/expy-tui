"""Provides the TUI (Terminal User Interface) for the expy_tui project."""
import logging

from textual.app import App

FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(level = logging.DEBUG,
                    filename="./logs/app.log",
                    format=FORMAT)

class MyApp(App):
    """Textual app implementation for expy_tui project."""


if __name__ == "__main__":
    app = MyApp()
    app.run()
