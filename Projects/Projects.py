import reflex as rx
from Projects.styles import styles
from Projects.pages.index import index
from Projects.pages.courses import courses

class State(rx.State):
    """Define your app state here."""


app = rx.App(
    style=styles.BASE_STYLE
)
