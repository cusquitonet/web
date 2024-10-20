import reflex as rx
from Projects.components.navbar import navbar_searchbar
from Projects.components.footer import footer
from Projects.views.header.header import header
from Projects.views.links.links import links
from Projects.styles import styles

# class State(rx.State):
#    pass


def index() -> rx.Component:
    return rx.box(
        navbar_searchbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        ),       
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
