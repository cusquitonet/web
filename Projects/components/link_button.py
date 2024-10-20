import reflex as rx
import Projects.styles.styles as styles

def link_button(icono: str, title: str, body: str, url: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.icon(
                        tag=icono,
                        size=30,
                        alt=title
                    ),
                    rx.vstack(
                        rx.text(title, 
                                style=styles.button_title_style,
                                weight="bold"),
                        rx.text(body, style=styles.button_body_style)
                    ),                    
                ),
                size="2",               
                color_scheme="grass",
                variant="surface"
            ),
            href=url,
            is_external=True,
            width="100%"
    )