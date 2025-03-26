import reflex as rx
from pages.landing_page import index

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

style={    
    "height": "100vh",
    "width": "100vw",
    "font" : "Arial"
    }




app = rx.App(style=style)
app.add_page(index)

