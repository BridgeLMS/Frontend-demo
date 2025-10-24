from nicegui import ui

def footer() -> None:
    """Create the footer component."""
    with ui.element('footer').classes('w-full text-white p-16').style('background-color: #1A2C46'):
        with ui.grid().classes('w-full grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-8'):
            # Column 1: Sign Up For A Newsletter
            with ui.column():
                ui.label('Sign Up For A Newsletter').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                ui.label('Weekly Breaking News Analysis and Cutting Edge Advices On Job Searching.').classes('text-sm font-light')
                with ui.row().classes('w-full items-center mt-4'):
                    ui.input(placeholder='Your email').classes('w-full').props('dark bg-transparent border-b-2 border-gray-400')
                    ui.button(icon='arrow_forward').props('color="yellow-13" text-color="black"').style('background-color: #FDB813;')

            # Column 2: Company
            with ui.column():
                ui.label('Company').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                ui.link('Home', '/').classes('text-white no-underline hover:underline')
                ui.link('About', '/about').classes('text-white no-underline hover:underline')
                ui.link('FAQs', '/faq').classes('text-white no-underline hover:underline')
                ui.link('Contact', '/contact').classes('text-white no-underline hover:underline')

            # Column 3: Get In Touch
            with ui.column():
                ui.label('Get In Touch').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                ui.link('Dashboard', '/dashboard').classes('text-white no-underline hover:underline')
                ui.link('Blog', '/blog').classes('text-white no-underline hover:underline')
                ui.link('Portfolio', '/portfolio').classes('text-white no-underline hover:underline')
                ui.link('Event', '/event').classes('text-white no-underline hover:underline')

            # Column 4: Courses
            with ui.column():
                ui.label('Courses').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                ui.link('Courses', '/courses').classes('text-white no-underline hover:underline')
                ui.link('Details', '/details').classes('text-white no-underline hover:underline')
                ui.link('Membership', '/membership').classes('text-white no-underline hover:underline')
                ui.link('Profile', '/profile').classes('text-white no-underline hover:underline')

            # Column 5: Our Gallery
            with ui.column():
                ui.label('Our Gallery').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                with ui.grid().classes('grid-cols-3 gap-2'):
                    ui.image('assets/Images/BridgeTeam.jpeg').classes('w-16 h-16 object-cover rounded border-2 border-white')
                    ui.image('assets/Images/cyber_ess.jpg').classes('w-16 h-16 object-cover rounded border-2 border-white')
                    ui.image('assets/Images/logo.png.jpg').classes('w-16 h-16 object-cover rounded border-2 border-white')
                    ui.image('assets/Images/Team2.jpeg').classes('w-16 h-16 object-cover rounded border-2 border-white')
                    ui.image('assets/Images/web_dev.jpg').classes('w-16 h-16 object-cover rounded border-2 border-white')
                    with ui.button('View All', on_click=lambda: ui.navigate.to('/courses')).classes('w-16 h-16 bg-yellow-500 text-black flex items-center justify-center rounded'):
                        ui.label('View All').classes('text-center')

        # Bottom bar for social media and copyright
        with ui.element('div').classes('w-full mt-8 pt-4 border-t border-gray-600 flex justify-between items-center'):
            with ui.row().classes('items-center gap-4'):
                ui.icon('lab la-facebook-f', size='lg').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-twitter', size='lg').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-linkedin-in', size='lg').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-instagram', size='lg').classes('cursor-pointer hover.text-yellow-500')
            
            ui.label('© 2025 BridgeLMS. All Rights Reserved').classes('text-sm text-gray-400 center')
