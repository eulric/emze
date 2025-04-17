import reflex as rx

class ContactState(rx.State):
    name: str
    email: str
    message: str

    def submit(self):
        print(f"Message from {self.name}: {self.message}")
        # You could also save this to a file or database

def contact_box() -> rx.Component:
    return rx.flex(
        rx.input(placeholder="Name", on_change=ContactState.set_name),
        rx.input(placeholder="Email", on_change=ContactState.set_email),
        rx.text_area(placeholder="Message", on_change=ContactState.set_message),
        rx.button("Send", on_click=ContactState.submit),
        direction="column",
        spacing="2",
    ),