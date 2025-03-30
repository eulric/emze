import reflex as rx

# Sample data for demonstration
payments_data = [
    {"customer": "John Doe", "amount": "$2,500", "status": "Paid", "date": "2025-03-28"},
    {"customer": "Jane Smith", "amount": "$1,200", "status": "Pending", "date": "2025-03-27"},
    {"customer": "Mike Johnson", "amount": "$3,800", "status": "Paid", "date": "2025-03-26"},
]

status_data = [
    {"customer": "John Doe", "project": "House Renovation", "status": "In Progress"},
    {"customer": "Jane Smith", "project": "Kitchen Remodel", "status": "Completed"},
    {"customer": "Mike Johnson", "project": "New Construction", "status": "Pending"},
]

comments_data = [
    {"customer": "John Doe", "comment": "Great progress so far!", "date": "2025-03-29"},
    {"customer": "Jane Smith", "comment": "Can we adjust the timeline?", "date": "2025-03-28"},
]

# Sidebar for navigation
def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Admin Dashboard", font_size="24px", color="white", margin_bottom="20px"),
            rx.link("Payments", href="#", color="white", _hover={"text_decoration": "underline"}),
            rx.link("Project Status", href="#", color="white", _hover={"text_decoration": "underline"}),
            rx.link("Customer Comments", href="#", color="white", _hover={"text_decoration": "underline"}),
            spacing="4",
        ),
        bg="gray.900",
        color="white",
        padding="30px",
        height="100vh",
        width="250px",
        position="fixed",
    )

# Payments Table
def payments_section() -> rx.Component:
    return rx.box(
        rx.heading("Payments", font_size="20px", margin_bottom="10px"),
        rx.table.root(
            rx.table.header(
                rx.table.row(rx.table.column_header_cell("Customer"), 
                      rx.table.column_header_cell("Amount"), 
                      rx.table.column_header_cell("Status"), 
                      rx.table.column_header_cell("Date"))),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(payment["customer"]), 
                        rx.table.cell(payment["amount"]),
                        rx.table.cell(payment["status"]), 
                        rx.table.cell(payment["date"]))
                    for payment in payments_data
                ]
            ),
        ),
        bg="white",
        padding="20px",
        border_radius="10px",
        box_shadow="md",
    )

# Project Status Table
def status_section() -> rx.Component:
    return rx.box(
        rx.heading("Project Status", font_size="20px", margin_bottom="10px"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.header("Customer"), 
                    rx.table.header("Project"), 
                    rx.table.header("Status"))),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(status["customer"]), 
                        rx.table.cell(status["project"]),
                        rx.table.cell(status["status"]))
                    for status in status_data
                ]
            ),
        ),
        bg="white",
        padding="20px",
        border_radius="10px",
        box_shadow="md",
    )

# Customer Comments Section
def comments_section() -> rx.Component:
    return rx.box(
        rx.heading("Customer Comments", font_size="20px", margin_bottom="10px"),
        rx.vstack(
            *[
                rx.box(
                    rx.text(f"{comment['customer']}:", font_weight="bold"),
                    rx.text(comment["comment"], font_size="16px"),
                    rx.text(comment["date"], font_size="12px", color="gray.500"),
                    padding="10px",
                    bg="gray.100",
                    border_radius="8px",
                    width="100%",
                )
                for comment in comments_data
            ],
            spacing="4",
        ),
        bg="white",
        padding="20px",
        border_radius="10px",
        box_shadow="md",
    )

# Main Admin Dashboard Layout
def admin_dashboard() -> rx.Component:
    return rx.box(
        sidebar(),
        rx.box(
            rx.vstack(
                payments_section(),
                # status_section(),
                comments_section(),
                spacing="6",
            ),
            margin_left="270px",  # Adjusted for sidebar width
            padding="40px",
            width="calc(100vw - 270px)",
        ),
        width="100vw",
        height="100vh",
        bg="gray.50",
    )
