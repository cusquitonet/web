import reflex as rx
import datetime
from Projects.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"2023 - {datetime.date.today().year}"
        ),
        rx.link(
                rx.hstack(
                    rx.icon(
                    tag="github",
                    size=25
                ),
                "@CUSQUITONET"                               
                ),
                href="https://github.com/cusquitonet/web",
                color_scheme="lime",
                is_external=True
        ),
        rx.link(
            rx.image(
            src="/favicon.ico"
            ),
            href="https://reflex.dev/",
            is_external=True        
        ),
        font_size=Size.MEDIUM.value,
        marging_bottom=Size.BIG.value,
        align="center"
    )