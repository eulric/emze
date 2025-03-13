import reflex as rx

def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Transform Your Workflow ",
                    rx.el.span(
                        "with AI Power",
                        class_name="text-transparent bg-clip-text bg-gradient-to-r from-teal-500 to-blue-500"
                    ),
                    class_name="text-4xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight"
                ),
                rx.el.p(
                    "Streamline your business processes and boost productivity with our innovative platform.",
                    class_name="text-xl text-gray-600 mb-8 max-w-2xl"
                ),
                rx.el.div(
                    rx.el.button(
                        rx.el.div(
                            rx.icon("rocket", class_name="stroke-white w-5 h-5 mr-2"),
                            "Get Started Free",
                            class_name="flex items-center"
                        ),
                        class_name="px-8 py-4 bg-gradient-to-r from-teal-500 to-blue-500 text-white rounded-xl hover:from-teal-600 hover:to-blue-600 transition-all duration-200 font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
                    ),
                    rx.el.button(
                        "Watch Demo", 
                        class_name="px-8 py-4 bg-white text-gray-700 rounded-xl border-2 border-gray-200 hover:border-teal-500 transition-all duration-200 font-semibold"
                    ),
                    class_name="flex items-center space-x-4"
                ),
                class_name="max-w-3xl"
            ),
            class_name="max-w-7xl mx-auto px-4 py-24"
        ),
        id="home",
        class_name="min-h-screen flex items-center bg-gradient-to-br from-white via-teal-50/30 to-blue-50/30"
    )