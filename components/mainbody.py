import reflex as rx
from components.request_quotation import form_card
from components.navbar import navi

def main_content():
        return rx.vstack(
                rx.flex(
                    rx.box(
                            rx.heading("Who we are", color="black",size="9"),
                            rx.text("We are a company deeply rooted in the values "
                            "of trust and quality. We believe that the cornerstone of any "
                            "successful project lies in the strength of the relationship we "
                            "build with our clients. Establishing a trustworthy relationship "
                            "with our clients is paramount to us, as it allows us to fully "
                            "understand and cater to their unique needs and aspirations.", as_="p", color="black", size="6"),
                    ),
                ),
                    

                padding="10%",
        )