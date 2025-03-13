# This is the landing page of the web app where user will be login
# This will also contain the cookie function to keep track of website visits.

import reflex as rx




def navbar():
    return rx.box(
            rx.box(
                rx.hstack(
                    rx.desktop_only(
                        rx.hstack(
                        rx.link("Home", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                        rx.link("Services", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                        rx.link("About", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                            
                        rx.box(rx.button("LOGIN", align="end",),
                                position="fixed",
                                right="20px",
                                top="25px",
                            ),      
                        ),
                    ),

                rx.mobile_and_tablet(
                    rx.hstack(
                        rx.link("Home", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                        rx.link("Services", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                        rx.link("About", href="#", padding="1em", display=["none", "block", "block"], size="6",),
                        
                    rx.box(rx.button("LOGIN", align="end",),
                                position="fixed",
                                right="20px",
                                top="25px",
                        ),
                    ),
                ),


                bg=rx.color("accent", 3),
                box_shadow="0px 10px 10px rgba(255, 255, 250, 0.2)",
                width="100%",
                height="auto",
                max_width="100%",
                max_height="100%",
                flex_wrap="wrap",
                margin="1px",
                position="fixed",
                ),

        
    ),
)


def headerBox():
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading("EMZE Construction", size="9", align="center"),
                rx.text("Design - Integrate - Develop", size="6", align="center"),
                align="center",
                line_height="9",
                padding_top="150px",
                padding="128",
                bg=rx.color("accent",2),
                width="100%",
                height="auto",
            ),


    width="100%",
    height="100%",
    max_width="100%",
    max_height="100%",
    ),
)

def captionBox():
    return rx.box(
        rx.vstack(
            rx.center(
                rx.box(
                    rx.section(
                        rx.heading("Design", margin_bottom="12px"),
                        rx.flex(
                            rx.text.strong("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                    margin_bottom="12px",
                                    ),
                            rx.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                    margin_bottom="12px",
                                    ),
                            flex_wrap="wrap",
                            padding_left="20px",
                            padding_right="20px",
                            ),

                        max_width="600px", 
                        max_height="auto",
                        ),
                    ),
            
                rx.box(
                    rx.image(src="landing/Image-1.jpeg", 
                        width="400px", 
                        height="auto", 
                        max_width="auto", 
                        max_height="auto", 
                        border_radius="15px 50px 30px"
                        ),
                    padding="50px",
                ),
                align="center",
                width="100%",
            ),
            
            rx.center(
                rx.box(
                    rx.box(
                    rx.image(src="landing/Image-2.jpeg", 
                        width="400px", 
                        height="auto", 
                        max_width="auto", 
                        max_height="auto", 
                        border_radius="15px 50px 30px"
                        ),
                    padding="50px",
                    ),
                ),

                                rx.box(
                    rx.section(
                        rx.heading("Planning", margin_bottom="12px"),
                        rx.flex(
                            rx.text.strong("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                    margin_bottom="12px",
                                    ),
                            rx.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                    margin_bottom="12px",
                                    ),
                            flex_wrap="wrap",
                            padding_left="20px",
                            padding_right="20px",
                            ),

                        max_width="600px", 
                        max_height="auto",
                        ),
                    ),

            
            align="center",
            width="100%",
            height="auto",
            bg=rx.color("white"),
        ),
        )
    )



def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "About", size="4", weight="bold", as_="h3"
        ),
        footer_item("Team", "/#"),
        footer_item("Project Info", "/#"),
        footer_item("Content Management", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Documentation", size="4", weight="bold", as_="h3"
        ),
        footer_item("Python Reflex", "https://reflex.dev/"),
        footer_item("Hostinger", "https://www.hostinger.com/vps-hosting"),
        footer_item("OpnVPN", "https://openvpn.net/"),
        spacing="1",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("x", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer_nav() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(

                        rx.heading(
                            "EMZE Construction",
                            size="5",
                            weight="bold",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "© 2024 EMZE Construction LLC",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="2",
                flex_direction=["column", "column", "row"],
                width="70%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="2",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
        bg=rx.color("accent", 3),
    )     
  


def home_page():
    return rx.fragment(
        navbar(),
        headerBox(),
        captionBox(),
        rx.divider(),
        footer_nav(),

    )

    


   



