import reflex as rx
from pages.landing_page import index
from pages.customer_dash import admin_dashboard



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
app.add_page(index, image="favicon.ico" )
# app.add_page(admin_dashboard)



