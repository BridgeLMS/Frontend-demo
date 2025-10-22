from nicegui import ui


def header() -> None:
    """Create the header component."""
    ui.add_head_html('<link rel="stylesheet" href="/assets/style.css">')
    with ui.header().classes(
        'flex items-center justify-between shadow-md'
    ).style('background-color: var(--card-surface-light); color: var(--text-titles);'):
        ui.label('BridgeLMS').classes('text-2xl font-bold')
        with ui.row().classes('items-center'):
            ui.link('Home', '/').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
            # ui.link('About', '/about').classes('text-lg mx-4')
            ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
            # ui.link('Contact', '/contact').classes('text-lg mx-4 no-underline')
            ui.link('Learner Dashboard', '/dashboard').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
            ui.link('Tutor Dashboard', '/tutor-dashboard').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
        with ui.row().classes('items-center'):
            ui.button(
                'Get Started', on_click=lambda: ui.navigate.to('/login')).classes(
                'mx-2'
            ).style('background-color: var(--accent); color: white;')
