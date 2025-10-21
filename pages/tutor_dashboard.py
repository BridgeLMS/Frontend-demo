from nicegui import ui

def tutor_dashboard() -> None:
    """Create the tutor dashboard page."""
    with ui.column().classes('w-full p-8 bg-gray-100'):
        # Header
        with ui.row().classes('w-full justify-between items-center mb-8'):
            with ui.column():
                ui.label('Tutor Dashboard').classes('text-4xl font-bold text-gray-800')
                ui.label('Welcome back, Ethan! Here’s your summary.').classes('text-lg text-gray-600')

        # My Courses Section
        with ui.column().classes('w-full mb-8'):
            ui.label('My Courses').classes('text-3xl font-bold text-gray-800 mb-4')
            with ui.grid(columns=3).classes('w-full gap-8'):
                courses = [
                    ('Digital Marketing Fundamentals', '124 Students', 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80'),
                    ('Advanced Spanish', '88 Students', 'https://images.unsplash.com/photo-1524678606370-a47625cb810c?auto=format&fit=crop&w=800&q=80'),
                    ('Creative Writing Workshop', '95 Students', 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=800&q=80'),
                ]
                for title, students, image_url in courses:
                    with ui.card().classes('text-left transition hover:scale-105 hover:shadow-lg duration-300'):
                        ui.image(image_url).classes('w-full h-48 object-cover rounded-t-lg')
                        with ui.card_section():
                            ui.label(title).classes('text-xl font-bold')
                            ui.label(students).classes('text-gray-600')

        # Management Tools & Recent Activity
        with ui.grid(columns=2).classes('w-full gap-8 mb-8'):
            # Management Tools
            with ui.column():
                ui.label('Management Tools').classes('text-2xl font-bold text-gray-800 mb-4')
                with ui.column().classes('w-full space-y-4'):
                    tools = [
                        ('book', 'Manage Resources', 'Upload and organize course materials.'),
                        ('campaign', 'Post Announcements', 'Share updates with your students.'),
                        ('checklist', 'Track Attendance', 'Monitor student attendance and engagement.'),
                    ]
                    for icon, name, desc in tools:
                        with ui.card().classes('w-full p-4 flex items-center'):
                            ui.icon(icon, size='lg').classes('text-blue-500 mr-4')
                            with ui.column():
                                ui.label(name).classes('font-bold')
                                ui.label(desc).classes('text-gray-600')

            # Recent Activity
            with ui.column():
                ui.label('Recent Activity').classes('text-2xl font-bold text-gray-800 mb-4')
                with ui.column().classes('w-full space-y-4'):
                    activities = [
                        ('Sophia Carter submitted a new assignment.', '2 hours ago'),
                        ('You posted a new announcement.', '1 day ago'),
                        ('New student enrolled in your course.', '3 days ago'),
                    ]
                    for desc, time in activities:
                        with ui.card().classes('w-full p-4'):
                            ui.label(desc).classes('font-semibold')
                            ui.label(time).classes('text-sm text-gray-500')

        # Announcements Section
        with ui.column().classes('w-full'):
            ui.label('Post a New Announcement').classes('text-2xl font-bold text-gray-800 mb-4')
            with ui.card().classes('w-full p-6'):
                ui.input(placeholder='Announcement Title').classes('w-full')
                ui.textarea(placeholder='Write your announcement...').classes('w-full')
                ui.button('Post Announcement', on_click=lambda: ui.notify('Announcement Posted!')).classes('w-full mt-4 bg-blue-500 text-white')
