from nicegui import ui
from components.header import show_header as app_header
from components.footer import show_footer

def dashboard() -> None:
    """Create the learner dashboard page."""
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
            ui.button('Home', icon='dashboard', on_click=lambda: ui.navigate.to('/')).props('flat no-caps').classes('w-full !justify-start text-black')
            ui.button('My Courses', icon='book', on_click=lambda: ui.navigate.to('/courses')).props('flat no-caps').classes('w-full !justify-start text-black')
            ui.button('Mailbox', icon='mail', on_click=lambda: ui.navigate.to('/mailbox')).props('flat no-caps').classes('w-full !justify-start text-black')
            ui.button('Calendar', icon='calendar_today', on_click=lambda: ui.navigate.to('/calendar')).props('flat no-caps').classes('w-full !justify-start text-black')
            ui.button('My Profile', icon='person').props('flat no-caps').classes('w-full !justify-start text-black')

        # ---------- MAIN CONTENT ----------
        with ui.column().classes('space-y-6'):
            # Breadcrumb
            with ui.row().classes('items-center text-gray-500'):
                ui.icon('home')
                ui.label('Home')
                ui.icon('chevron_right')
                ui.label('Learner Dashboard')

            ui.label('Welcome to the Learners Dashboard').classes('text-2xl font-bold')

            with ui.row().classes('w-full gap-8 items-stretch'):
                # Enrolled Courses
                with ui.card().classes('flex-1'):
                    ui.label('Enrolled Courses').classes('text-2xl font-bold mb-4')
                    with ui.column().classes('w-full space-y-4'):
                        courses = [
                            ('Become a PHP Master and Make Money', 'Proffessor Ernest Manu', 75),
                            ('Advanced Web Development', 'Maame Jane phd', 45),
                            ('Data Science with Python', 'Dr. Yaw Boadi', 90),
                        ]
                        for title, teacher, progress in courses:
                            with ui.column().classes('w-full'):
                                with ui.row().classes('w-full justify-between items-center'):
                                    ui.label(title).classes('font-bold')
                                    ui.label(f'{progress}%').classes('font-bold text-lg')
                                ui.label(f'with {teacher}').classes('text-gray-500 text-sm')
                                ui.linear_progress(value=progress/100).classes('w-full mt-2')
                                with ui.row().classes('w-full justify-end gap-2 mt-2'):
                                    ui.button('Continue', on_click=lambda: ui.navigate.to('/course_details')).props('flat dense')
                                    with ui.dialog() as dialog, ui.card():
                                        ui.label('Are you sure you want to quit this course?')
                                        with ui.row():
                                            ui.button('Yes', on_click=lambda: ui.notify('Course quit!'))
                                            ui.button('No', on_click=dialog.close)
                                    ui.button('Quit', on_click=dialog.open).props('flat dense color=negative')
                
                # Upcoming Assignments & Recent Messages
                with ui.column().classes('w-1/3 gap-8'):
                    with ui.card().classes('w-full'):
                        ui.label('Upcoming Assignments').classes('text-2xl font-bold mb-4')
                        assignments = {
                            'PHP Assignment': 'Due: Oct 30',
                            'Web Dev Project': 'Due: Nov 5',
                            'Data Analysis Report': 'Due: Nov 12',
                        }
                        for name, due_date in assignments.items():
                            with ui.row().classes('w-full justify-between'):
                                ui.label(name)
                                ui.label(due_date).classes('text-gray-500')
                    with ui.card().classes('w-full'):
                        ui.label('Recent Messages').classes('text-2xl font-bold mb-4')
                        messages = [
                            ('From: Gifty Eshun', 'Re: PHP Assignment'),
                            ('From: Micheal Luminous', 'Re: Web Dev Project'),
                        ]
                        for sender, subject in messages:
                            with ui.column().classes('w-full'):
                                ui.label(sender).classes('font-bold')
                                ui.label(subject).classes('text-gray-500')

                # Mark Attendance
                with ui.card().classes('w-1/3'):
                    ui.label('Mark Attendance').classes('text-2xl font-bold mb-4')
                    ui.select(['Present', 'Absent', 'Late'], label='Status').classes('w-full')
                    ui.textarea(label='Daily Summary').classes('w-full')
                    ui.upload(label='Upload Media', auto_upload=True, on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('w-full mt-4')
                    ui.button('Submit', on_click=lambda: ui.notify('Attendance marked!')).classes('w-full mt-4 bg-blue-500 text-white')
    show_footer()
