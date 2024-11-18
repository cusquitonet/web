import reflex as rx
import Projects.utils as utils
from Projects.components.navbar import navbar_searchbar
from Projects.components.footer import footer
from Projects.views.header import header
from Projects.views.index_links import index_links
from Projects.styles import styles
from Projects.api.api import repo

class IndexState(rx.State):
    @rx.var
    def say_hello(self):
        return repo()

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar_searchbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        ),       
        footer()
    )
    

