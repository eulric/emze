import reflex as rx
from pages.landin_page import index

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...





app = rx.App()
app.add_page(index)

