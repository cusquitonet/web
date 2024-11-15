import reflex as rx
from Projects.routes import Route

def navbar_searchbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/balloon.png",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                        rx.heading(
                        "Cusquito Net", 
                        size="3", 
                        weight="bold",
                        color_scheme="gray"
                        ),
                        href=Route.INDEX.value
                    ),
                    align_items="center",
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="1",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/balloon.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                        rx.heading(
                        "Cusquito Net", 
                        size="3", 
                        weight="bold",
                        color_scheme="gray"
                        ),
                        href=Route.INDEX.value
                    ),
                    align_items="center",
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="1",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),        
        bg=rx.color("lime", 3),
        padding="0.5em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )