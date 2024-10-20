import reflex as rx

# comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "blueball.png"

_meta = [
    {"name": "og:title", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@pipiahumada"}
]

# index

index_title = "Cusquitonet"
index_description = "Mi primera pagina en reflex"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)

# cursos

course_title = "Cusquitonet | Cursos"
course_description = "Cursos que estoy haciendo"

course_meta = [
    {"name": "og:title", "content": course_title},
    {"name": "og:description", "content": course_description}
]
course_meta.extend(_meta)