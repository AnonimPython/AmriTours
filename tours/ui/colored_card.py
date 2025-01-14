import reflex as rx

def colored_card(
        icon: str,
        text: str,
        bgcolor: str,
        icon_color: str,
        id_box: str,
        url: str,
        width: str = "90px",
        height: str = "90px",
    ) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.icon(tag=icon,color=icon_color),
                rx.text(text, size="3",color="black"),
                align="center",
                justify="center",
                height="100%",
                width="100%",
                spacing="2",
            ),
            id=id_box,
            style={
                "align_self": "center",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "background-color": bgcolor,
                # "border": f"2px {border_color} solid",
                "border-radius":"10px",
                "width":width,"height":height
            },
        ),
        href=url,
        style={"text_decoration": "none"},
    )
