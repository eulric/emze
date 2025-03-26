import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

def form_card():
    return rx.vstack(
        rx.heading("Request a Quotation", size="3"),
        size="100%",
        
            
    )