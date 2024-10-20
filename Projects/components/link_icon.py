import reflex as rx
import Projects.styles.styles as styles

def link_icon(icon_name: str, url: str,) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon_name,
            size=30,
            color=rx.color("grass", 11),
            alt=icon_name
        ),
        href=url,
        is_external=True,
        
    )