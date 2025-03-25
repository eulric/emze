import reflex as rx
from components.navbar import navi


def index():
    return rx.container(
        navi(),
        width="100%",
    )