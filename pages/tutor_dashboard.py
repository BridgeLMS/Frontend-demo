from nicegui import ui
from components.header import header as app_header


def tutor_dashboard() -> None:
    """Create the tutor dashboard page."""
    app_header()
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
    }
    .app {
        min-height: 100vh;
    }
    .container {
        width: 100%;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-right: 2rem;
    }
    .grid {
        display: grid;
        gap: 1.5rem;
        grid-template-columns: 1fr;
    }
    @media (min-width: 768px) {
        .grid {
            grid-template-columns: 240px 1fr;
        }
    }
    .card {
        border-radius: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        background: white;
        padding: 2rem;
    }
    .topbar {
        position: sticky;
        top: 0;
        z-index: 10;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--light);
    }
    .sidebar .q-btn {
        width: 100%;
        justify-content: flex-start;
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
    }
    .sidebar .q-btn:hover {
        background-color: var(--light);
    }
    ''')
    with ui.column().classes('app'):
        # Main grid
        with ui.element('main').classes('container'):
            with ui.element('div').classes('grid'):
                # ---------- LEFT SIDEBAR ----------
                with ui.column().classes('sidebar flex flex-col justify-between'):
                    with ui.column().classes('space-y-2 w-full'):
                        ui.label('MENU').classes('text-xs font-bold text-gray-500 uppercase tracking-wider px-4 text-center')
                        ui.button('Home', icon='home', on_click=lambda: ui.navigate.to('/')).props('flat no-caps').classes('w-full justify-start')
                        ui.button('My Courses', icon='book', on_click=lambda: ui.open('/courses')).props('flat no-caps').classes('w-full justify-start')
                        ui.button('Students', icon='group').props('flat no-caps').classes('w-full justify-start')
                        ui.button('Messages', icon='mail').props('flat no-caps').classes('w-full justify-start')
                    with ui.column().classes('space-y-2 w-full'):
                        ui.separator().classes('my-4')
                        ui.label('SETTINGS').classes('text-xs font-bold text-gray-500 uppercase tracking-wider px-4 text-center')
                        ui.button('Profile', icon='person').props('flat no-caps').classes('w-full justify-start')
                        ui.button('Logout', icon='logout').props('flat color=negative no-caps').classes('w-full justify-start')

                # ---------- CENTER COLUMN ----------
                with ui.column().classes('space-y-6').style('padding-left: 2rem'):
                    # Header
                    with ui.row().classes('w-full justify-between items-center'):
                        with ui.column():
                            ui.label('Tutor Dashboard').classes('text-4xl font-bold text-gray-800')
                            ui.label('Welcome back, Prof Ellen! Here’s your summary for this semester.').classes('text-lg text-gray-600')

                    # Stats
                    with ui.row().classes('w-full gap-4'):
                        for label, value, icon in [('Total Students', '249', 'group'), ('Courses', '3', 'book'), ('Pending Assignments', '12', 'assignment')]:
                            with ui.card().classes('flex-1'):
                                with ui.row().classes('items-center justify-between'):
                                    with ui.column():
                                        ui.label(label).classes('text-gray-500')
                                        ui.label(value).classes('text-3xl font-bold')
                                    ui.icon(icon, size='lg').classes('text-brand')

                    # My Courses & Management Tools
                    with ui.row().classes('w-full gap-6 items-stretch'):
                        with ui.card().classes('flex-1'):
                            ui.label('My Courses').classes('text-2xl font-bold text-gray-800 mb-4')
                            with ui.column().classes('w-full space-y-4'):
                                courses = [
                                    ('Digital Marketing Fundamentals', '124 Students', 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80'),
                                    ('Advanced Spanish', '88 Students', 'https://images.unsplash.com/photo-1524678606370-a47625cb810c?auto=format&fit=crop&w=800&q=80'),
                                    ('Creative Writing Workshop', '95 Students', 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=800&q=80'),
                                ]
                                for title, students, image_url in courses:
                                    with ui.row().classes('w-full items-center gap-4'):
                                        ui.image(image_url).classes('w-24 h-16 rounded-lg object-cover')
                                        with ui.column().classes('flex-1'):
                                            ui.label(title).classes('font-bold')
                                            ui.label(students).classes('text-gray-500 text-sm')
                                        ui.button('Manage', icon='arrow_forward').props('flat round')
                        with ui.card().classes('flex-1'):
                            ui.label('Management Tools').classes('text-2xl font-bold text-gray-800 mb-4')
                            with ui.column().classes('w-full space-y-4'):
                                tools = [
                                    ('book', 'Manage Resources', 'Upload and organize course materials.'),
                                    ('campaign', 'Post Announcements', 'Share updates with your students.'),
                                    ('checklist', 'Track Attendance', 'Monitor student attendance and engagement.'),
                                ]
                                for icon, name, desc in tools:
                                    with ui.row().classes('items-center gap-4'):
                                        ui.icon(icon, size='md').classes('text-brand')
                                        with ui.column():
                                            ui.label(name).classes('font-bold')
                                            ui.label(desc).classes('text-gray-500 text-sm')
                    # Recent Activity & Announcements Section
                    with ui.row().classes('w-full gap-6 items-stretch'):
                        with ui.card().classes('flex-1'):
                            ui.label('Recent Activity').classes('text-2xl font-bold text-gray-800 mb-4')
                            with ui.column().classes('w-full space-y-4'):
                                activities = [
                                    ('Sophia Carter submitted a new assignment.', '2 hours ago'),
                                    ('You posted a new announcement.', '1 day ago'),
                                    ('New student enrolled in your course.', '3 days ago'),
                                ]
                                for desc, time in activities:
                                    with ui.column():
                                        ui.label(desc).classes('font-semibold')
                                        ui.label(time).classes('text-sm text-gray-500')
                        with ui.card().classes('flex-1'):
                            ui.label('Post a New Announcement').classes('text-2xl font-bold text-gray-800 mb-4')
                            ui.input(placeholder='Announcement Title').classes('w-full')
                            ui.textarea(placeholder='Write your announcement...').classes('w-full')
                            ui.button('Post Announcement', on_click=lambda: ui.notify('Announcement Posted!')).classes('w-full mt-4 bg-brand text-white')
