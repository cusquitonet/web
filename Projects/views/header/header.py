import reflex as rx
from Projects.components.link_icon import link_icon
from Projects.components.info_text import info_text
from Projects.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.avatar(
                color_scheme="grass", 
                src="captura1.png",
                variant="solid", 
                high_contrast=False, 
                fallback="CA", 
                size="8"
                ),
                rx.vstack(
                    rx.heading(
                    "Cristian Ahumada",
                    size="8"
                    ),
                    rx.text(
                        " Bienvenido a mi pagina!",
                        margin_top=Size.ZERO.value
                    ),
                    rx.hstack(
                        link_icon("instagram", "https://instagram.com"),
                        link_icon("twitter", "https://x.com"),
                        link_icon("facebook", "https://facebook.com"),
                        link_icon("podcast", "https://spotify.com")
                    ),                
                    align="start"
                )           
            ),
            rx.flex(
                info_text("Aprendiendo!", " Si quieres colaborar eres bienvenido...")
            ),
            rx.text(
                """Tengo un nivel basico de Cobol y estoy iniciando en el mundo de Python. 
                Este proyecto esta hecho en python con reflex, guiandome por los tutoriales de Mouredev"""
            ),
            spacing=Size.BIG.value,
            align="start"
    )