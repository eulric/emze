import reflex as rx
from components.navbar import navi

# Mission Statement Section
def mission_statement() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Our Mission", font_size="40px", font_weight="bold", color="black"),
            rx.text(
                "We are deeply rooted in the values of trust and quality. We believe that the cornerstone of any successful project lies in the strength of the relationship we build with our clients. "
                "Establishing a trustworthy relationship with our clients is paramount to us, as it allows us to fully understand and cater to their unique needs and aspirations.",
                font_size="20px",
                text_align="center",
                max_width="800px",
                color="gray.800",
                line_height="1.6",
            ),
            spacing="4",
            align="center",
        ),
        background_image="url('landing_images/CECCO-Our-History.jpg')",
        bg_size="cover",
        bg_position="center",
        bg_repeat="no-repeat",
        padding_y="120px",
        bg="gray.100",
        height="80vh",
        display="flex",
        align_items="center",
        justify_content="center",
    )

# Approach Section with Modern UI Touches
def approach_section() -> rx.Component:
    sections = [
        ("landing_images/person1.png", "Estimation", "Working with clients to capture their vision, meet their priorities."),
        ("landing_images/person2.png", "Innovation", "Precisely budgeting to keep costs in check."),
        ("landing_images/person3.png", "Collaboration", "Incorporating the latest solutions in custom home construction."),
    ]

    return rx.box(
        rx.vstack(
            rx.heading("Our Approach", font_size="36px", font_weight="bold", color="black", text_align="center"),
            rx.hstack(
                *[
                    rx.box(
                        rx.vstack(
                            rx.image(
                                src=image, 
                                width="320px", 
                                height="320px", 
                                object_fit="cover", 
                                border_radius="12px",
                                box_shadow="lg",
                                transition="transform 0.3s ease-in-out",
                                _hover={"transform": "scale(1.05)"},
                            ),
                            rx.heading(title, font_size="22px", font_weight="semibold", color="black", margin_top="12px"),
                            rx.text(description, font_size="18px", color="gray.700", text_align="center", max_width="280px"),
                            align="center",
                            spacing="4",
                        ),
                        spacing="4",
                        padding="20px",
                        border_radius="10px",
                        bg="white",
                        box_shadow="md",
                        width="33%",
                        text_align="center",
                        transition="all 0.3s ease",
                        _hover={"box_shadow": "xl", "transform": "translateY(-5px)"},
                    )
                    for image, title, description in sections
                ],
                spacing="6",
                justify_content="space-between",
                align_items="center",
            ),
            spacing="8",
            align="center",
            max_width="1100px",
            width="100%",
        ),
        padding_y="120px",
        bg="gray.50",
        display="flex",
        justify_content="center",
    )

# Footer with Social Links
def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("© 2025 EMZE Construction. All rights reserved.", color="white", font_size="14px", text_align="center"),
            rx.hstack(
                rx.link("Facebook", href="#", color="white", font_size="14px", _hover={"text_decoration": "underline"}),
                rx.text("|", color="white"),
                rx.link("Instagram", href="#", color="white", font_size="14px", _hover={"text_decoration": "underline"}),
                rx.text("|", color="white"),
                rx.link("LinkedIn", href="#", color="white", font_size="14px", _hover={"text_decoration": "underline"}),
                spacing="4",
                justify="center",
            ),
            spacing="3",
            align="center",
        ),
        bg="black",
        padding="25px",
        width="100%",
        position="relative",
        bottom="0",
        box_shadow="lg",
    )

# Main Page Layout with Improved Spacing
def index() -> rx.Component:
    return rx.box(
        navi(),
        rx.box(
            mission_statement(),
            margin_top="80px",
        ),
        approach_section(),
        footer(),
        height="100vh",
        width="100vw",
        position="relative",
        min_height="100vh"
    )
