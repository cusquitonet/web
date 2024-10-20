import reflex as rx
import Projects.styles.styles as styles

def title(title: str) -> rx.Component:
    return rx.heading(
                    title,
                    size="6", 
                    style=styles.title_stile
            )