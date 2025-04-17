import reflex as rx
from ..components.contact_form import ContactState, contact_box
from ..components.navbar import navi, footer





# Mission Statement Section
def landing_image() -> rx.Component:
    return rx.fragment(
    rx.flex(
        rx.box(
            rx.image(
                class_name="landing-image",
                src="landing_images/landing_image.jpeg",
                alt="Architecture",
                width="1500",
                height="800",
                align="center",
                object_fit="cover",
                object_position="center",
                style={
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "z-index": "-1",
                },
            ),
        ),
    ),
)


def services() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Our Services", size="7", font_weight="bold", color="white"),
            rx.spacer(),
            rx.separator(size="4", color="white"),
            rx.box(
                rx.flex(
                    # Left Column (Image)
                    rx.box(
                        rx.image(
                            src="landing_images/Image-4.jpeg",
                            alt="Project Visual",
                            width="100%",
                            height="auto",
                            style={
                                "border-radius": "0.5rem",
                                "opacity": "0.8",
                                "max-height": "500px",
                                "object-fit": "cover",
                            },
                        ),
                        width=["100%", "50%"],  # Full width on small screens
                        padding="1rem",
                        display=["none", "block"],  # Hide on very small screens
                    ),
                    # Right Column (Text Content)
                    rx.box(
                        rx.vstack(
                            rx.heading("• Project Management", text_align="center", size="6"),
                            rx.text(
                                "From the initial stages of cost estimation and project acquisition, "
                                "EMZE Construction offers comprehensive project management and coordination services. "
                                "Our team is dedicated to meticulously planning every aspect of your project, "
                                "ensuring that all activities are seamlessly integrated and executed. "
                                "We oversee the entire process from conceptual design to final execution, "
                                "with a keen focus on maintaining timelines, budgets, and quality standards.",
                                font_size="1.125rem",
                                margin_bottom="1.5rem",
                                text_align="center",
                            ),
                            rx.heading("• Home Renovation", text_align="center", size="6"),
                            rx.text(
                                "Whether it's adding a new door to enhance accessibility, "
                                "replacing an old floor with stylish and durable materials, "
                                "or changing the color of your house to give it a fresh new look, "
                                "EMZE Construction is committed to fulfilling all your home renovation needs.",
                                font_size="1.125rem",
                                margin_bottom="1.5rem",
                                text_align="center",
                            ),
                            align="center",
                        ),
                        width=["100%", "50%"],
                        padding="1rem",
                    ),
                    wrap="wrap",
                    justify="center",
                    align="center",
                ),
                max_width="1200px",
                width="100%",
                padding_y="4rem",
                id="services",
            )
        ),
        padding="2rem",
    ),
        

      

 

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Who we are", size="7", font_weight="bold", color="white"),
            rx.spacer(),
            rx.separator(size="4", color="white"),
            rx.box(
                rx.flex(

                    rx.box(
                        rx.vstack(
                            
                            rx.text(
                                "EMZE Construction is a premier construction company specializing in a wide range of services, "
                                "including project management, home renovation, and more. Our team of experienced professionals "
                                "is dedicated to delivering high-quality results that exceed our clients' expectations. "
                                "With a commitment to excellence and a focus on customer satisfaction, we strive to be your "
                                "trusted partner in all your construction needs.",
                                font_size="1.125rem",
                                margin_bottom="1.5rem",
                                text_align="center",
                            ),
                           
                            ),
                        align="center",
                        width=["100%", "50%"],
                        padding="1rem",
                    ),

                        
                    rx.box(
                        rx.image(
                            src="landing_images/Image-2.jpeg",
                            alt="Project Visual",
                            width="100%",
                            height="auto",
                            style={
                                "border-radius": "0.5rem",
                                "opacity": "0.8",
                                "max-height": "500px",
                                "object-fit": "cover",
                            },
                        ),
                        width=["100%", "50%"],  # Full width on small screens
                        padding="1rem",
                        display=["none", "block"],  # Hide on very small screens
                    wrap="wrap",
                    justify="center",
                    align="center",
                ),

            
                max_width="1200px",
                width="100%",
                padding_y="4rem",
                id="services",
            ),
        ),),
    ),




def contact_us() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Contact Us", size="7", font_weight="bold", color="white"),
            rx.spacer(),
            rx.separator(size="4", color="white"),

            rx.flex(
                rx.box(
                rx.text(
                    "For inquiries, quotes, or to discuss your project needs, please reach out to us. "
                    "We look forward to collaborating with you and bringing your vision to life.",
                    font_size="1.125rem",
                    margin_bottom="1.5rem",
                    text_align="center",
                    align="center",
                ),
                
                ),

                rx.box(
                    # contact_box(),
                    
                    rx.dialog.root(
                        rx.dialog.trigger(rx.button("Send a Message", color_scheme="teal")),
                        rx.dialog.content(
                            rx.dialog.title("Contact Us"),
                            rx.dialog.description(
                                "We’d love to hear from you. Fill out the form below."
                            ),
                            rx.dialog.description(
                                contact_box(),
                            ),
                            rx.dialog.close(
                                rx.button("Close Dialog", size="3", align="right", variant="ghost", mt="2"),
                            ),
                        ),
                        width="100%",
                        
                    ),
                    align="center",

                ),

                wrap="wrap",
                justify="center",
                align="center",
                direction="column",
            ),
            item_align="center",
            align="center",
            width=["100%", "50%"],
            padding="1rem",
            max_width="1200px",
            padding_y="4rem",
        ),
                

)






# Main Page Layout
def index() -> rx.Component:
    return rx.box(
        navi(),
        landing_image(),
        services(),
        about(),

   
        contact_us(),
                
        
        footer(),
        height="100vh",
        width="100vw",
        position="relative",
        justify_content="center",
        align_items="center",

 
    )
