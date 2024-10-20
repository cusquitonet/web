import reflex as rx
from Projects.routes import Route
from Projects.components.link_button import link_button
from Projects.components.title import title
from Projects.styles.styles import Size as Size


def index_links() -> rx.Component:
    return rx.vstack(
        title("Mis recursos"),
        link_button("book-open-text",
                    "Cursos gratis", 
                    "Recursos para aprender programacion!", 
                    Route.COURSES.value,
                    is_external=False),
        link_button("twitch",
                    "Twitch", 
                    "Algun dia haremos directos", 
                    "https://www.twitch.tv/cusquito79"),
        link_button("youtube",
                    "Youtube", 
                    "Canal para compartir los videos que haga", 
                    "https://www.youtube.com/@cusquito79"),
        link_button("bot",
                    "Discord",
                    "Mi servidor en la comunidad", 
                    "https://discord.gg/cusquito79"),
        link_button("github",
                    "Github", 
                    "Ingresa a mis repositorios", 
                    "https://github.com/cusquitonet"),
        width="100%",
        spacing=Size.INTERMEDIATE.value
    )
