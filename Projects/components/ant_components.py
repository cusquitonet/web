import reflex as rx

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon = rx.image(src="/icons/discord-logo.svg")
    href = "https://discord.gg"
    target = "_blank"
    
    
float_button = FloatButton.create