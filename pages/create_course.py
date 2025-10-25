from nicegui import ui

def create_course_page():
    """Create the page for creating and managing courses."""
    with ui.column().classes('w-full items-center'):
        ui.label('Create a New Course').classes('text-4xl font-bold text-white mb-8')
        
        with ui.card().classes('w-full max-w-2xl'):
            ui.input(label='Course Title').classes('w-full')
            ui.textarea(label='Course Description').classes('w-full')
            ui.button('Create Course', on_click=lambda: ui.notify('Course Created!')).classes('w-full bg-blue-500 text-white')

        ui.separator().classes('my-8')

        ui.label('Your Courses').classes('text-4xl font-bold text-white mb-8')
        
        with ui.column().classes('w-full max-w-2xl gap-4'):
            courses = [
                {'title': 'Digital Marketing Fundamentals', 'progress': 80},
                {'title': 'Advanced Spanish', 'progress': 55},
                {'title': 'Creative Writing Workshop', 'progress': 30},
            ]
            for course in courses:
                with ui.card().classes('w-full'):
                    with ui.row().classes('w-full items-center'):
                        ui.label(course['title']).classes('text-lg font-bold text-gray-800')
                        ui.space()
                        ui.label(f"{course['progress']}% Complete").classes('text-gray-600')
                    ui.linear_progress(value=course['progress']/100).classes('w-full mt-2')
