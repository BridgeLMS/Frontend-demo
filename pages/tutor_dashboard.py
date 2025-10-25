from nicegui import ui
from components.header import show_header as app_header
from components.footer import show_footer


def tutor_dashboard() -> None:
    """Create the tutor dashboard page."""
    async def logout():
        with ui.dialog() as dialog, ui.card():
            ui.label('Are you sure you want to log out?')
            with ui.row():
                ui.button('Yes', on_click=lambda: (dialog.close(), ui.navigate.to('/login')))
                ui.button('No', on_click=dialog.close)
        await dialog

    app_header()
    ui.add_head_html('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
    ui.add_css('''
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    :root {
        --brand: #6C5CE7;
        --banner: #A29BFE;
        --dark: #2d3436;
        --light: #dfe6e9;
        --background: #f5f6fa;
    }
    body {
        font-family: 'Poppins', sans-serif;
        background-color: var(--background);
        color: var(--dark);
    }
    .grid {
        display: grid;
        gap: 1.5rem;
        grid-template-columns: 240px 1fr;
    }
    .sidebar .q-btn {
        width: 100%;
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        font-weight: 500;
    }
    .sidebar .q-btn .q-btn__content {
        display: flex !important;
        flex-direction: row !important;
        justify-content: flex-start !important;
        align-items: center !important;
        gap: 1rem !important;
    }
    .sidebar .q-btn:hover {
        background-color: var(--light);
    }
    .card {
        border-radius: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        background: white;
        padding: 2rem;
    }
    ''')
    with ui.element('div').classes('grid p-8'):
        # ---------- LEFT SIDEBAR ----------
        with ui.column().classes('sidebar space-y-2'):
            ui.button('Home', icon='house', on_click=lambda: ui.navigate.to('/')).props('flat no-caps')
            ui.button('Courses', icon='book', on_click=lambda: ui.navigate.to('/create_course')).props('flat no-caps')
            ui.button('Mailbox', icon='mail', on_click=lambda: ui.navigate.to('/mailbox')).props('flat no-caps')
            ui.button('Calendar', icon='calendar_today', on_click=lambda: ui.navigate.to('/calendar')).props('flat no-caps')
            # ui.button('Bookmarks', icon='bookmark').props('flat no-caps')
            # ui.button('Review', icon='reviews').props('flat no-caps')
            # ui.button('Add Listing', icon='add').props('flat no-caps')
            ui.button('My Profile', icon='person').props('flat no-caps')
            ui.button('Logout', icon='logout', on_click=logout).props('flat color=negative no-caps')


        # ---------- MAIN CONTENT ----------
        with ui.column().classes('space-y-6'):
            # Breadcrumb
            with ui.row().classes('items-center text-gray-500'):
                ui.icon('home')
                ui.label('Home')
                ui.icon('chevron_right')
                ui.label('Courses')

            ui.label('Your Courses').classes('text-3xl font-bold')

            # Course Card
            with ui.card().classes('w-full'):
                with ui.row().classes('w-full no-wrap items-start gap-8'):
                    # Image
                    ui.image('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80').classes('w-[300px] rounded-lg object-cover')
                    
                    # Content
                    with ui.column().classes('flex-grow'):
                        # Top row: Title, Price
                        with ui.row().classes('w-full justify-between items-start'):
                            ui.label('Become a PHP Master and Make Money').classes('text-2xl font-bold')
                            with ui.column().classes('items-end gap-0'):
                                ui.label('₵199').classes('text-md text-gray-400 line-through')
                                ui.label('₵120').classes('text-2xl font-bold text-gray-800')

                        # Middle row: Details
                        with ui.row().classes('items-center gap-4 mt-2'):
                            ui.image('https://randomuser.me/api/portraits/men/1.jpg').classes('w-8 h-8 rounded-full')
                            with ui.column().classes('gap-0'):
                                ui.label('Teacher').classes('text-xs text-gray-500')
                                ui.label('KENY WHITE').classes('text-sm font-bold')
                            
                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('3 Categories').classes('text-xs text-gray-500')
                                ui.label('BACKEND').classes('text-sm font-bold')

                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('3 Review').classes('text-xs text-gray-500')
                                with ui.row().classes('items-center gap-0'):
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star_border', size='sm', color='amber')
                                    ui.icon('star_border', size='sm', color='amber')
                            
                            ui.chip('Pending', color='teal').classes('text-white ml-4')

                        # Bottom part: Description and Buttons
                        ui.label('Course Description').classes('text-lg font-bold mt-6 mb-2')
                        ui.label('Learn PHP to build dynamic, high-earning web applications — from freelance websites to e-commerce platforms and content management systems.').classes('text-sm text-gray-600')

                        with ui.row().classes('w-full gap-4 mt-8'):
                            ui.button('Approve', color='teal').props('outline rounded').classes('border-2')
                            ui.button('Cancel', color='red').props('outline rounded').classes('border-2')

            # Course Card 2
            with ui.card().classes('w-full'):
                with ui.row().classes('w-full no-wrap items-start gap-8'):
                    # Image
                    ui.image('https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80').classes('w-[300px] rounded-lg object-cover')
                    
                    # Content
                    with ui.column().classes('flex-grow'):
                        # Top row: Title, Price
                        with ui.row().classes('w-full justify-between items-start'):
                            ui.label('Advanced Web Development').classes('text-2xl font-bold')
                            with ui.column().classes('items-end gap-0'):
                                ui.label('₵250').classes('text-md text-gray-400 line-through')
                                ui.label('₵180').classes('text-2xl font-bold text-gray-800')

                        # Middle row: Details
                        with ui.row().classes('items-center gap-4 mt-2'):
                            ui.image('https://randomuser.me/api/portraits/women/2.jpg').classes('w-8 h-8 rounded-full')
                            with ui.column().classes('gap-0'):
                                ui.label('Teacher').classes('text-xs text-gray-500')
                                ui.label('JANE DOE').classes('text-sm font-bold')
                            
                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('4 Categories').classes('text-xs text-gray-500')
                                ui.label('FRONTEND').classes('text-sm font-bold')

                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('5 Review').classes('text-xs text-gray-500')
                                with ui.row().classes('items-center gap-0'):
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star_half', size='sm', color='amber')
                            
                            ui.chip('Approved', color='green').classes('text-white ml-4')

                        # Bottom part: Description and Buttons
                        ui.label('Course Description').classes('text-lg font-bold mt-6 mb-2')
                        ui.label('Dive deep into modern web development with React, Node.js, and more. Build complex applications and master the full stack.').classes('text-sm text-gray-600')

                        with ui.row().classes('w-full gap-4 mt-8'):
                            ui.button('View', color='blue').props('outline rounded').classes('border-2')
                            ui.button('Delete', color='red').props('outline rounded').classes('border-2')

            # Course Card 3
            with ui.card().classes('w-full'):
                with ui.row().classes('w-full no-wrap items-start gap-8'):
                    # Image
                    ui.image('https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80').classes('w-[300px] rounded-lg object-cover')
                    
                    # Content
                    with ui.column().classes('flex-grow'):
                        # Top row: Title, Price
                        with ui.row().classes('w-full justify-between items-start'):
                            ui.label('Data Science with Python').classes('text-2xl font-bold')
                            with ui.column().classes('items-end gap-0'):
                                ui.label('₵300').classes('text-md text-gray-400 line-through')
                                ui.label('₵220').classes('text-2xl font-bold text-gray-800')

                        # Middle row: Details
                        with ui.row().classes('items-center gap-4 mt-2'):
                            ui.image('https://randomuser.me/api/portraits/men/3.jpg').classes('w-8 h-8 rounded-full')
                            with ui.column().classes('gap-0'):
                                ui.label('Teacher').classes('text-xs text-gray-500')
                                ui.label('JOHN SMITH').classes('text-sm font-bold')
                            
                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('2 Categories').classes('text-xs text-gray-500')
                                ui.label('DATA SCIENCE').classes('text-sm font-bold')

                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('4 Review').classes('text-xs text-gray-500')
                                with ui.row().classes('items-center gap-0'):
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star_border', size='sm', color='amber')
                            
                            ui.chip('Pending', color='teal').classes('text-white ml-4')

                        # Bottom part: Description and Buttons
                        ui.label('Course Description').classes('text-lg font-bold mt-6 mb-2')
                        ui.label('Learn to analyze data, create beautiful visualizations, and use machine learning with Python, Pandas, and Scikit-learn.').classes('text-sm text-gray-600')

                        with ui.row().classes('w-full gap-4 mt-8'):
                            ui.button('Approve', color='teal').props('outline rounded').classes('border-2')
                            ui.button('Cancel', color='red').props('outline rounded').classes('border-2')

            # Course Card 4
            with ui.card().classes('w-full'):
                with ui.row().classes('w-full no-wrap items-start gap-8'):
                    # Image
                    ui.image('https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=800&q=80').classes('w-[300px] rounded-lg object-cover')
                    
                    # Content
                    with ui.column().classes('flex-grow'):
                        # Top row: Title, Price
                        with ui.row().classes('w-full justify-between items-start'):
                            ui.label('Digital Marketing Masterclass').classes('text-2xl font-bold')
                            with ui.column().classes('items-end gap-0'):
                                ui.label('₵180').classes('text-md text-gray-400 line-through')
                                ui.label('₵150').classes('text-2xl font-bold text-gray-800')

                        # Middle row: Details
                        with ui.row().classes('items-center gap-4 mt-2'):
                            ui.image('https://randomuser.me/api/portraits/women/4.jpg').classes('w-8 h-8 rounded-full')
                            with ui.column().classes('gap-0'):
                                ui.label('Teacher').classes('text-xs text-gray-500')
                                ui.label('EMILY ROSE').classes('text-sm font-bold')
                            
                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('5 Categories').classes('text-xs text-gray-500')
                                ui.label('MARKETING').classes('text-sm font-bold')

                            with ui.column().classes('gap-0 ml-4'):
                                ui.label('5 Review').classes('text-xs text-gray-500')
                                with ui.row().classes('items-center gap-0'):
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                                    ui.icon('star', size='sm', color='amber')
                            
                            ui.chip('Approved', color='green').classes('text-white ml-4')

                        # Bottom part: Description and Buttons
                        ui.label('Course Description').classes('text-lg font-bold mt-6 mb-2')
                        ui.label('Master SEO, content marketing, social media, and more to grow any business online.').classes('text-sm text-gray-600')

                        with ui.row().classes('w-full gap-4 mt-8'):
                            ui.button('View', color='blue').props('outline rounded').classes('border-2')
                            ui.button('Delete', color='red').props('outline rounded').classes('border-2')
    show_footer()
