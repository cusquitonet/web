import reflex as rx
from Projects.styles import styles
from Projects.pages.index import index
from Projects.pages.courses import courses
from Projects.api.api import repo
from Projects.api.api import live

app = rx.App(
    style=styles.BASE_STYLE
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live", live)