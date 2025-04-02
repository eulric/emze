import reflex as rx
from ..components.navbar import navi



# Mission Statement Section
def mission_statement() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Our Mission", font_size="36px", font_weight="bold", color="black"),
            rx.text(
                ""
                "We are deeply rooted in the values of trust and quality. We believe that the cornerstone of any successful project lies in the strength of the relationship we build with our clients. Establishing a trustworthy relationship with our clients is paramount to us,"
                " as it allows us to fully understand and cater to their unique needs and aspirations.",
                font_size="20px",
                text_align="center",
                max_width="800px",
                color="black",
            ),
            spacing="2",
            align="center",
        ),
        background_image="url('landing_images/CECCO-Our-History.jpg')",
        bg_size="contain",
        padding_y="100px",
        bg="gray.100",
        height="80vh"
    )

def open_dialog(title: str, description: str) -> rx.Component:
    return rx.dialog(
        rx.dialog_overlay(
            rx.dialog_content(
                rx.dialog_header(title, bg="lightblue", color="darkblue"),
                rx.dialog_body(description, font_size="18px", color="gray.700"),
                rx.dialog_footer(
                    rx.button("Close", on_click=lambda: rx.dialog_close(), bg="mediumseagreen", color="white"),
                ),
            )
        ),
        is_open=True,
    )

# def approach_section() -> rx.Component:
    sections = [
        ("landing_images/person1.png", "Estimation", "Working with clients to capture their vision, meet their priorities."),
        ("landing_images/person2.png","Innovation" , "Precisely budgeting to keep costs in check."),
        ("landing_images/person3.png","Collaboration" , "Incorporating the latest solutions in custom home construction."),
    ]
    


    return rx.box(
        rx.vstack(
            rx.heading("Our Approach", font_size="32px", font_weight="bold"),
            rx.hstack(
                *[
                    rx.box(
                        rx.vstack(
                            rx.heading(title, font_size="24px", font_weight="semibold"),
                            rx.image(src=image, box_size="800px", border_radius="8px"),
                            rx.text(description, font_size="18px"),
                            align="center",
                            padding="5",
                        ),
                        spacing="4",
                        width="33%",
                        
                    )
                    for image, title, description in sections
                ],
                spacing="6",
                justify_content="space-between",
                align_items="center",
            ),
            spacing="6",
            align="center",
            max_width="1000px",
            width="100%",
        ),
        padding_y="100px",
        bg="gray.50",
        display="flex",
        justify_content="center",
    )

def approach_section() -> rx.Component:
    sections = [
        ("landing_images/person1.png", "Estimation", "Working with clients to capture their vision, meet their priorities."),
        ("landing_images/person2.png", "Innovation", "Precisely budgeting to keep costs in check."),
        ("landing_images/person3.png", "Collaboration", "Incorporating the latest solutions in custom home construction."),
    ]

    return rx.box(
        rx.vstack(
            rx.heading("Our Approach", font_size="32px", font_weight="bold"),
            rx.hstack(
                *[
                    rx.box(
                        rx.vstack(
                            rx.heading(title, font_size="24px", font_weight="semibold"),
                            rx.image(src=image, width="300px", height="300px", object_fit="cover", border_radius="8px"),
                            rx.text(description, font_size="18px"),
                            align="center",
                            padding="5",
                        ),
                        spacing="4",
                        width="33%",
                    )
                    for image, title, description in sections
                ],
                spacing="6",
                justify_content="space-between",
                align_items="center",
            ),
            spacing="6",
            align="center",
            max_width="1000px",
            width="100%",
        ),
        padding_y="100px",
        bg="gray.50",
        display="flex",
        justify_content="center",
    )


# Footer 
def footer() -> rx.Component:
    return rx.box(
        rx.text("© 2025 EMZE Construction. All rights reserved.", color="white", text_align="center", font_size="14px"),
        bg="rgba(0, 0, 0, 0.8)",
        padding="20px",
        width="100%",
        position="relative",
        bottom="0",
        box_shadow="lg",
    )

# Main Page Layout
def index() -> rx.Component:
    return rx.box(
        navi(),
        rx.box(
            mission_statement(),
            margin_top="100px"
        ),
        approach_section(),
        footer(),
        height="100vh",
        width="100vw",
        position="relative",

 
    )
