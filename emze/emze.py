import reflex as rx

from  .pages.main_dash import dash
from  .pages.landing_page import home_page

def index() -> rx.Component:
    # Welcome Page (Index)
    return home_page()
        



app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

app.add_page(
    index,
    title="Emze Construction",
    description="A simple app to manage customer data.",
)

app.add_page(
    dash
)
