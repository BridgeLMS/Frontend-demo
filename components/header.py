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
            ui.link('Home', '/').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
            ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline').style('color: var(--text-titles);')
            ui.link('Home', '/').classes('text-lg mx-4 no-underline').style('color: white;')
            # ui.link('About', '/about').classes('text-lg mx-4')
            ui.link('Courses', '/courses').classes('text-lg mx-4 no-underline').style('color: white;')
            # ui.link('Contact', '/contact').classes('text-lg mx-4 no-underline')
            ui.link('Learner Dashboard', '/dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
            ui.link('Tutor Dashboard', '/tutor-dashboard').classes('text-lg mx-4 no-underline').style('color: white;')
        with ui.row().classes('items-center'):
            ui.button(
                'Get Started', on_click=lambda: ui.navigate.to('/login')).classes(
                'mx-2'
            ).style('background-color: var(--accent); color: black;')
# with ui.row().classes('items-center gap-2'):
#             ui.icon('school').classes('text-3xl text-black')
#             ui.link('BridgeLMS', '/').classes(
#                 'text-2xl font-semibold tracking-tight no-underline text-black'
#             )

# with ui.row().classes('items-center gap-8 text-base font-medium text-gray-700'):
#             with ui.row().classes('items-center gap-1 cursor-pointer hover:text-black'):
#                 ui.label('Courses')
#                 ui.icon('expand_more').classes('text-lg')
#             with ui.row().classes('items-center gap-1 cursor-pointer hover:text-black'):
#                 ui.label('Bootcamps')
#                 ui.icon('expand_more').classes('text-lg')
#             ui.link('Community', '/community').classes(
#                 'no-underline text-gray-700 hover:text-black'
#             )
#             ui.link('About', '/about').classes(
#                 'no-underline text-gray-700 hover:text-black'
#             )
#             ui.link('Flash Sale', '/flash-sale').classes(
#                 'no-underline text-gray-700 hover:text-black'
#             )

# ui.button(
#             'Sign in', on_click=lambda: ui.navigate.to('/login')
#         ).classes(
#             'bg-black text-white rounded-full px-5 py-2 text-base font-semibold shadow-sm hover:bg-gray-900'
#         )
