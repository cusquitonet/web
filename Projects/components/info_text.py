import reflex as rx
from Projects.styles.styles import Size as Size

def info_text(title: str, body: str,) -> rx.Component:
    return rx.box(
        rx.text(title, as_='b', color_scheme="lime"),
        body,
        size=Size.MEDIUM.value
    )