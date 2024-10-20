import reflex as rx
import Projects.utils as utils
from Projects.routes import Route
from Projects.components.navbar import navbar_searchbar
from Projects.components.footer import footer
from Projects.views.header import header
from Projects.views.courses_links import courses_links
from Projects.styles import styles


@rx.page(
    route=Route.COURSES.value,
    title=utils.course_title,
    description=utils.course_description,
    image=utils.preview,
    meta=utils.course_meta
)

def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar_searchbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            )
        ),       
        footer()
    )
    