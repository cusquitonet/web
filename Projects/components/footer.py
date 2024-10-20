import reflex as rx
import datetime
from Projects.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"2023 - {datetime.date.today().year}"
        ),
        rx.link(
            "@CUSQUITONET",
            href="https://cusquitonet.com",
            color_scheme="grass",
            is_external=True,
            margin_top=Size.ZERO.value
        ),
        rx.link(
            rx.image(
            src="favicon.ico"
            ),
            href="https://reflex.dev/"        
        ),
        font_size=Size.MEDIUM.value,
        marging_bottom=Size.BIG.value,
        align="center"
    )