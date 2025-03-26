import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navi() -> rx.Component:
    return rx.fragment(
        rx.desktop_only(
            rx.hstack(
                rx.text("EMZE Construction", font_size="24px", font_weight="bold", color="white"),
                rx.spacer(),
                rx.link("Home", href="/", color="white"),
                rx.link("Projects", href="/how-we-build", color="white"),
                rx.link("Login", href="/contact", color="white"),
                spacing="2",
                padding_x="40px",
                padding_y="20px",
        ),
        bg="rgba(0, 0, 0, 0.8)",
        width="100%",
        position="fixed",
        top="0",
        z_index="1000",
        box_shadow="lg",

        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "EMZE construction", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="rgba(0, 0, 0, 0.8)",
        width="100%",
        position="fixed",
        top="0",
        z_index="1000",
        box_shadow="lg",
    )