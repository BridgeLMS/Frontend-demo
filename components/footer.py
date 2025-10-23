from nicegui import ui


def footer() -> None:
    """Create the footer component."""
    with ui.footer().classes(
        'flex items-center justify-around w-full text-white p-4'
    ).style('background: linear-gradient(to right, #000428, #004e92);'):
        ui.label('© 2023 BridgeLMS. All rights reserved.')
        with ui.row():
            # ui.link('About', '/about').classes('mx-2')
            ui.link('Contact', '/contact').classes('mx-2 no-underline')
            ui.link('Privacy', '/privacy').classes('mx-2 no-underline')
            ui.link('Terms', '/terms').classes('mx-2 no-underline')
        with ui.row():
            ui.icon('facebook').classes('mx-2')
            ui.icon('twitter').classes('mx-2')
            ui.icon('instagram').classes('mx-2')
