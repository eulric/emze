import reflex as rx


from .pages.landing_page import index
from .pages.dashboard import  dash_board




app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)



app.add_page(index, route="/")
app.add_page(dash_board, route="/dash")