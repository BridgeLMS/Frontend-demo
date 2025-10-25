from nicegui import ui

def course_details_page():
    """Create the page for displaying course details."""
    ui.add_css('''
    .course-container {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .materials-list, .classmates-list {
        list-style-type: none;
        padding: 0;
    }
    .materials-list li, .classmates-list li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #e0e0e0;
    }
    ''')

    with ui.column().classes('course-container'):
        ui.label('Become a PHP Master and Make Money').classes('text-3xl font-bold mb-4')
        
        # Course Materials
        with ui.column().classes('w-full mb-8'):
            ui.label('Course Materials').classes('section-title')
            with ui.element('ul').classes('materials-list w-full'):
                for item in ['Introduction to PHP', 'Variables and Data Types', 'Control Structures', 'Functions']:
                    with ui.element('li'):
                        ui.label(item)

        # Classmates
        with ui.column().classes('w-full'):
            ui.label('Classmates').classes('section-title')
            with ui.element('ul').classes('classmates-list w-full'):
                for name in ['Alice', 'Bob', 'Charlie']:
                    with ui.element('li'):
                        ui.label(name)
