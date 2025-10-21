from nicegui import ui


def footer() -> None:
    """Create the footer component."""
    with ui.footer().classes(
        'flex items-center justify-between bg-gray-800 text-white p-4'
    ):
        ui.label('© 2023 BridgeLMS. All rights reserved.')
        with ui.row():
            ui.link('About', '/about').classes('mx-2')
            ui.link('Contact', '/contact').classes('mx-2')
            ui.link('Privacy', '/privacy').classes('mx-2')
            ui.link('Terms', '/terms').classes('mx-2')
        with ui.row():
            ui.icon('facebook').classes('mx-2')
            ui.icon('twitter').classes('mx-2')
            ui.icon('instagram').classes('mx-2')
