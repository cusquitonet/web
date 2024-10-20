import reflex as rx
import Projects.constants as Constants
from Projects.routes import Route
from Projects.components.link_button import link_button
from Projects.components.title import title
from Projects.styles.styles import Size as Size


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button("book-open-text",
                    "Mouredev", 
                    "Cursos para aprender con mouredev!", 
                    Constants.REPO_URL),
        link_button("book-open-text",
                    "Midudev", 
                    "Cursos frontend con JS!", 
                    Constants.REPO_URL),
        link_button("book-open-text",
                    "Youtube", 
                    "Canales para prender a programar", 
                    Constants.REPO_URL),
        link_button("book-open-text",
                    "Discord",
                    "Servidores donde encontraras mucha ayuda", 
                    Constants.REPO_URL),
        link_button("book-open-text",
                    "Github", 
                    "Encuentra miles de lineas de codigo", 
                    Constants.REPO_URL),
        width="100%",
        spacing=Size.INTERMEDIATE.value
    )
