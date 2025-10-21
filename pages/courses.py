from nicegui import ui
from typing import Dict, Any


def courses() -> None:
    """Create the courses page."""

    all_courses = [
        {'title': 'Introduction to Programming', 'desc': 'Learn the basics of programming with Python.',
            'image_url': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80', 'category': 'Web Development', 'status': 'Active', 'tutor': 'Dr. Reed'},
        {'title': 'Advanced Data Science', 'desc': 'Dive deep into advanced data science techniques.',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80', 'category': 'Data Science', 'status': 'Active', 'tutor': 'Ms. Rossi'},
        {'title': 'Marketing Strategies', 'desc': 'Develop effective marketing strategies for your business.',
            'image_url': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80', 'category': 'Marketing', 'status': 'Completed', 'tutor': 'Dr. Reed'},
        {'title': 'Financial Accounting', 'desc': 'Master the principles of financial accounting.',
            'image_url': 'https://images.unsplash.com/photo-1554224154-22dec7ec8818?auto=format&fit=crop&w=800&q=80', 'category': 'Business', 'status': 'Active', 'tutor': 'Ms. Rossi'},
        {'title': 'Graphic Design Basics', 'desc': 'Get started with graphic design using industry-standard tools.',
            'image_url': 'https://images.unsplash.com/photo-1501555088652-021faa106b9b?auto=format&fit=crop&w=800&q=80', 'category': 'Design', 'status': 'Completed', 'tutor': 'Dr. Reed'},
        {'title': 'Project Management Fundamentals', 'desc': 'Learn the fundamentals of project management.',
            'image_url': 'https://images.unsplash.com/photo-1581091870639-47fdbbb0f15b?auto=format&fit=crop&w=800&q=80', 'category': 'Business', 'status': 'Active', 'tutor': 'Ms. Rossi'},
    ]

    filters: Dict[str, Any] = {
        'category': 'All',
        'status': 'All',
        'tutor': 'All',
    }

    def update_courses():
        course_grid.clear()
        with course_grid:
            filtered_courses = all_courses
            if filters['category'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['category'] == filters['category']]
            if filters['status'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['status'] == filters['status']]
            if filters['tutor'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['tutor'] == filters['tutor']]

            for course in filtered_courses:
                with ui.card().classes('text-left transition hover:scale-105 hover:shadow-lg duration-300'):
                    ui.image(course['image_url']).classes(
                        'w-full h-48 object-cover rounded-t-lg')
                    with ui.card_section():
                        ui.label(course['title']).classes('text-lg font-bold')
                        ui.label(course['desc']).classes('text-gray-600 mt-2')

    with ui.row().classes('w-full items-center'):
        # Hero Section
        with ui.row().classes(
            'w-full h-[70vh] bg-cover bg-center flex items-center justify-center text-center text-white'
        ).style(
            'background-image: url("https://images.unsplash.com/photo-1584697964193-40b0a4f1c95e?auto=format&fit=crop&w=1600&q=80")'
        ):
            with ui.row().classes('items-center bg-black bg-opacity-40 p-8 rounded-xl'):
                ui.label('Explore Courses').classes('text-5xl font-extrabold')
                ui.label(
                    'Find the perfect course to enhance your skills and knowledge. '
                    'Browse our catalog or use filters to narrow your search.'
                ).classes('text-xl mt-4 text-center max-w-3xl')
                with ui.row().classes('mt-8 w-full max-w-lg'):
                    ui.input(placeholder='Search for courses, e.g. "Web Development"').classes(
                        'w-full')
                    ui.button(
                        'Search', on_click=lambda: ui.notify('Searching...'))

        # Featured Courses Section
        with ui.column().classes('w-full items-center my-16 px-4'):
            ui.label('Featured Courses').classes(
                'text-4xl font-bold text-gray-800')
            with ui.grid(columns=3).classes('w-full max-w-6xl gap-8 mt-8'):
                featured_courses = [
                    (
                        'Digital Art Fundamentals',
                        'Learn the basics of digital art and create stunning visuals.',
                        'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80',
                    ),
                    (
                        'Business Analytics Essentials',
                        'Master the fundamentals of business analytics.',
                        'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80',
                    ),
                    (
                        'Creative Writing Workshop',
                        'Unleash your inner writer and craft compelling stories.',
                        'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=800&q=80',
                    ),
                ]

                for title, desc, image_url in featured_courses:
                    with ui.card().classes('text-left transition hover:scale-105 hover:shadow-lg duration-300'):
                        ui.image(image_url).classes(
                            'w-full h-48 object-cover rounded-t-lg')
                        with ui.card_section():
                            ui.label(title).classes('text-xl font-bold')
                            ui.label(desc).classes('text-gray-600 mt-2')

        # All Courses Section
        with ui.row().classes('w-full max-w-7xl my-16 px-4 gap-8'):
            # Filters
            with ui.column().classes('w-1/4'):
                ui.label('Filter Courses').classes('text-3xl font-bold')
                with ui.column().classes('mt-4 space-y-4'):
                    ui.select(['All', 'Web Development', 'Data Science', 'Marketing', 'Business', 'Design'],
                              label='Category', on_change=lambda e: filters.update({'category': e.value}) or update_courses())
                    ui.select(['All', 'Active', 'Completed'], label='Status', on_change=lambda e: filters.update(
                        {'status': e.value}) or update_courses())
                    ui.select(['All', 'Dr. Reed', 'Ms. Rossi'], label='Tutor', on_change=lambda e: filters.update(
                        {'tutor': e.value}) or update_courses())

            # Course Grid
            with ui.column().classes('w-3/4'):
                with ui.row().classes('w-full justify-end'):
                    ui.select(['Relevance', 'Popularity',
                              'Newest'], label='Sort')

                course_grid = ui.grid(columns=3).classes('w-full gap-8 mt-4')
                update_courses()

                # Pagination
                with ui.row().classes('w-full justify-center mt-8'):
                    ui.button(icon='chevron_left',
                              on_click=lambda: ui.notify('Prev'))
                    ui.button('1', on_click=lambda: ui.notify('1'))
                    ui.button('2', on_click=lambda: ui.notify('2'))
                    ui.button('3', on_click=lambda: ui.notify('3'))
                    ui.button(icon='chevron_right',
                              on_click=lambda: ui.notify('Next'))
