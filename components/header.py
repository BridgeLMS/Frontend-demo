from nicegui import ui


def header() -> None:
    """Create the header component."""
    ui.add_head_html('<link rel="stylesheet" href="/assets/style.css">')

    with ui.element('header').classes(
        'flex items-center justify-between shadow-md w-full p-4'
    ).style('background: linear-gradient(to right, #000428, #004e92); color: white;'):
        
        with ui.row().classes('items-center'):
            ui.image('/assets/Images/logo.png.jpg').classes('w-12')
            ui.label('BridgeLMS').classes('text-2xl font-bold')
        with ui.row().classes('items-center'):
            ui.link('Home', '/').classes('text-lg mx-4 no-underline').style('color: white;')
            ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline').style('color: white;')
            # ui.link('About', '/about').classes('text-lg mx-4')
            # ui.link('Contact', '/contact').classes('text-lg mx-4 no-underline')
            ui.link('Learner Dashboard', '/dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
            ui.link('Tutor Dashboard', '/tutor-dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
        with ui.row().classes('items-center'):
    with ui.header().classes('w-full shadow-md').style('background: linear-gradient(to right, #000428, #004e92); color: white;'):
        with ui.row().classes('w-full items-center px-8 py-4'):
            with ui.row().classes('items-center'):
                ui.image('/assets/Images/logo.png.jpg').classes('w-12')
                ui.label('BridgeLMS').classes('text-2xl font-bold')
            
            with ui.row().classes('items-center ml-8'):
                ui.link('Home', '/').classes('text-lg mx-4 no-underline').style('color: white;')
                ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline').style('color: white;')
                ui.link('Learner Dashboard', '/dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
                ui.link('Tutor Dashboard', '/tutor-dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
            
            ui.space()  # This will push the button to the right
            
            ui.button(
                'Get Started', on_click=lambda: ui.navigate.to('/login')
            ).style('background-color: var(--accent); color: black;')
