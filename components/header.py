from nicegui import ui


def header() -> None:
    """Create the header component."""
    with ui.header().classes(
        'flex items-center justify-between bg-white text-black shadow-md'
    ):
        ui.label('BridgeLMS').classes('text-2xl font-bold')
        with ui.row().classes('items-center'):
            ui.link('Home', '/').classes('text-lg mx-4 no-underline')
            # ui.link('About', '/about').classes('text-lg mx-4')
            ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline')
            # ui.link('Contact', '/contact').classes('text-lg mx-4 no-underline')
            ui.link('Learner Dashboard', '/dashboard').classes('text-lg mx-4 no-underline')
            ui.link('Tutor Dashboard', '/tutor-dashboard').classes('text-lg mx-4 no-underline')
        with ui.row().classes('items-center'):
            ui.button(
                'Get Started', on_click=lambda: ui.navigate.to('/login')).classes(
                'mx-2'
            )
            
