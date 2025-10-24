from nicegui import ui

def show_footer() -> None:
    """Create the footer component."""
    with ui.element('footer').classes('w-full text-white').style('background-color: #1A2C46'):
        # Main content with padding
        with ui.element('div').classes('p-8'):
            with ui.grid().classes('w-full grid-cols-1 sm:grid-cols-2 md:grid-cols-8 gap-8'):
                # Column 1: Sign Up For A Newsletter
                with ui.column().classes('md:col-span-3'):
                    ui.label('Sign Up For A Newsletter').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                    ui.label('Weekly Educational News Analysis and Cutting Edge Advices On Job Searching.').classes('text-sm font-light')
                    with ui.row().classes('w-full items-stretch mt-4 no-wrap'):
                        ui.input(placeholder='Your Email Address').classes('flex-grow').props('dense').style('background-color: white; border-radius: 0;')
                        ui.button(icon='arrow_forward').props('text-color="black"').style('background-color: #FDB813; border-radius: 0;')

                # Column 2: Get In Touch
                with ui.column():
                    ui.label('Get In Touch').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                    ui.link('Home', '/').classes('text-white no-underline hover:underline')
                    ui.link('About', '/about').classes('text-white no-underline hover:underline')
                    ui.link('FAQs', '/faq').classes('text-white no-underline hover:underline')
                    ui.link('Contact', '/contact').classes('text-white no-underline hover:underline')

                # Column 3: Get In Touch
                with ui.column():
                    ui.label('Links').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                    ui.link('Learner Dashboard', '/dashboard').classes('text-white no-underline hover:underline')
                    ui.link('Tutor Daashboard', '/tutor-dashboard').classes('text-white no-underline hover:underline')
                    ui.link('Courses', '/Courses').classes('text-white no-underline hover:underline')
                    ui.link('Events', '/event').classes('text-white no-underline hover:underline')

                # Column 4: Categories
                with ui.column():
                    ui.label('Categories').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                    ui.link('Programming', '/Programming').classes('text-white no-underline hover:underline')
                    ui.link('Web Design', '/Web Design').classes('text-white no-underline hover:underline')
                    ui.link('Cybersecurity', '/Cybersecurity').classes('text-white no-underline hover:underline')
                    ui.link('Analytics', '/Analytics').classes('text-white no-underline hover:underline')

                # # Column 5: Our Gallery
                # with ui.column().classes('md:col-span-2'):
                #     ui.label('Our Gallery').classes('text-lg font-bold').style('font-size: 1.2em; font-weight: 700;')
                #     ui.separator().classes('w-1/4 my-2 bg-yellow-500')
                #     with ui.grid().classes('grid-cols-4 gap-2'):
                #         ui.image('/assets/Images/BridgeTeam.jpeg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/cyber_ess.jpg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/logo.png.jpg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/Team2.jpeg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/web_dev.jpg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/BridgeTeam.jpeg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/cyber_ess.jpg').classes('w-full h-16 object-cover rounded')
                #         ui.image('/assets/Images/logo.png.jpg').classes('w-full h-16 object-cover rounded')

        # Bottom bar with logo, social media, and Join Now button
        with ui.element('div').classes('w-full px-8 py-1 border-t border-gray-600 flex justify-between items-center'):
            with ui.row().classes('items-center'):
                ui.image('/assets/Images/logo.png.jpg').classes('w-8 h-8 mr-2')
                with ui.column().classes('gap-0'):
                    ui.label('BridgeLMS').classes('text-lg font-bold')
                    ui.label('Bridging the Learning Gap').classes('text-xs')
            with ui.row().classes('items-center gap-4'):
                ui.icon('lab la-facebook-f', size='sm').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-twitter', size='sm').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-linkedin-in', size='sm').classes('cursor-pointer hover:text-yellow-500')
                ui.icon('lab la-google-plus-g', size='sm').classes('cursor-pointer hover:text-yellow-500')
            ui.button('Join Now', on_click=lambda: ui.navigate.to('/signup')).style('background-color: #FDB813; color: black;')
