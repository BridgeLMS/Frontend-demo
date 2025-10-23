from nicegui import ui
from typing import Dict, Any


def courses() -> None:
    """Create the courses page."""
    ui.add_css('''
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    body {
        font-family: 'Montserrat', Times New Roman, serif;
    }
    ''')
    
    all_courses = [
        {'title': 'Introduction to Programming', 'desc': 'Learn the basics of programming with Python.',
            'image_url': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80', 'category': 'Web Development', 'status': 'Active', 'tutor': 'Dr. Reed', 'popularity': 8, 'date_added': '2023-10-01'},
        {'title': 'Advanced Data Science', 'desc': 'Dive deep into advanced data science techniques.',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80', 'category': 'Data Science', 'status': 'Active', 'tutor': 'Ms. Rossi', 'popularity': 10, 'date_added': '2023-09-15'},
        {'title': 'Marketing Strategies', 'desc': 'Develop effective marketing strategies for your business.',
            'image_url': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80', 'category': 'Marketing', 'status': 'Completed', 'tutor': 'Dr. Reed', 'popularity': 7, 'date_added': '2023-08-20'},
        {'title': 'Financial Accounting', 'desc': 'Master the principles of financial accounting.',
            'image_url': 'https://images.unsplash.com/photo-1554224154-22dec7ec8818?auto=format&fit=crop&w=800&q=80', 'category': 'Business', 'status': 'Active', 'tutor': 'Ms. Rossi', 'popularity': 9, 'date_added': '2023-10-05'},
        {'title': 'Graphic Design Basics', 'desc': 'Get started with graphic design using industry-standard tools.',
            'image_url': 'https://images.unsplash.com/photo-1501555088652-021faa106b9b?auto=format&fit=crop&w=800&q=80', 'category': 'Design', 'status': 'Completed', 'tutor': 'Dr. Reed', 'popularity': 6, 'date_added': '2023-07-11'},
        {'title': 'Project Management Fundamentals', 'desc': 'Learn the fundamentals of project management.',
            'image_url': 'https://hub.aipm.com.au/images/Events/Project%20Management%20Fundamentals%20Course4.jpg', 'category': 'Business', 'status': 'Active', 'tutor': 'Ms. Rossi', 'popularity': 8, 'date_added': '2023-09-01'},
    ]

    filters: Dict[str, Any] = {
        'category': 'All',
        'status': 'All',
        'tutor': 'All',
        'sort': 'Relevance',
        'search': '',
    }

    def update_courses():
        course_grid.clear()
        with course_grid:
            filtered_courses = all_courses
            if filters['search']:
                filtered_courses = [
                    c for c in filtered_courses if filters['search'].lower() in c['title'].lower()]
            if filters['category'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['category'] == filters['category']]
            if filters['status'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['status'] == filters['status']]
            if filters['tutor'] != 'All':
                filtered_courses = [
                    c for c in filtered_courses if c['tutor'] == filters['tutor']]

            if filters['sort'] == 'Popularity':
                filtered_courses = sorted(
                    filtered_courses, key=lambda c: c.get('popularity', 0), reverse=True)
            elif filters['sort'] == 'Newest':
                filtered_courses = sorted(
                    filtered_courses, key=lambda c: c.get('date_added', ''), reverse=True)

            for course in filtered_courses:
                with ui.card().classes('text-left transition hover:scale-105 hover:shadow-lg duration-300'):
                    ui.image(course['image_url']).classes(
                        'w-full h-48 object-cover rounded-t-lg')
                    with ui.card_section():
                        ui.label(course['title']).classes('text-lg font-bold')
                        ui.label(course['desc']).classes('text-gray-600 mt-2')

    with ui.column().classes('w-full items-center gap-8'):
        # Welcome/Header section
        with ui.element('div').classes('banner'):
         with ui.column().classes('w-full items-center'):
            
            ui.label('Welcome to BridgeLMS course panel !').classes(
                'text-small background italic')
            ui.label('Explore Our Courses').classes('text-4xl font-bold')
            ui.label(
                'Find the perfect course to advance your skills and knowledge.'
            ).classes('text-lg mt-2')
            with ui.row().classes('mt-8 items-center justify-center'):
                ui.button('All Categories', on_click=lambda: ui.notify('All')).style(
                    'background-color: var(--primary-brand); color: white;')
                ui.link(
                    'Cybersecurity',
                    'https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/',
                    new_tab=True
                ).classes('q-btn').style('background-color: var(--primary-brand); color: white; text-decoration: none;')
                ui.button(
                    'Web Development',
                    on_click=lambda: ui.notify('Web Development'),
                ).style('background-color: var(--primary-brand); color: white;')
                ui.button(
                    'Data Science', on_click=lambda: ui.notify('Data Science')
                ).style('background-color: var(--primary-brand); color: white;')
                ui.button('Marketing', on_click=lambda: ui.notify('Marketing')).style(
                    'background-color: var(--primary-brand); color: white;')

        # Filter section
        with ui.column().classes('w-full max-w-6xl px-4'):
            ui.label('Filter Courses').classes('text-3xl font-bold mb-4')
            with ui.row().classes('w-full gap-4 items-center'):
                search_input = ui.input(placeholder='Search for courses...').classes(
                    'flex-1').on('keydown.enter', lambda: filters.update({'search': search_input.value}) or update_courses())
                ui.button('Search', on_click=lambda: filters.update(
                    {'search': search_input.value}) or update_courses())
            with ui.row().classes('w-full gap-4 mt-4'):
                ui.select(['All', 'Web Development', 'Data Science', 'Marketing', 'Business', 'Design'],
                          label='Category', on_change=lambda e: filters.update({'category': e.value}) or update_courses()).classes('flex-1')
                ui.select(['All', 'Active', 'Completed'], label='Status', on_change=lambda e: filters.update(
                    {'status': e.value}) or update_courses()).classes('flex-1')
                ui.select(['All', 'Dr. Reed', 'Ms. Rossi'], label='Tutor', on_change=lambda e: filters.update(
                    {'tutor': e.value}) or update_courses()).classes('flex-1')
                ui.select(['Relevance', 'Popularity', 'Newest'], label='Sort', on_change=lambda e: filters.update(
                    {'sort': e.value}) or update_courses()).classes('flex-1')

        # Featured Courses Section
        with ui.column().classes('w-full max-w-6xl px-4'):
            ui.label('Featured Courses').classes(
                'text-4xl font-bold text-gray-800')
            with ui.grid(columns=3).classes('w-full gap-8 mt-8'):
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
        with ui.column().classes('w-full max-w-6xl px-4'):
            ui.label('All Courses').classes(
                'text-4xl font-bold text-gray-800')
            course_grid = ui.grid(columns=3).classes('w-full gap-8 mt-4')
            update_courses()
            # Pagination
            with ui.row().classes('w-full justify-center mt-8'):
                ui.button(icon='chevron_left',
                          on_click=lambda: ui.notify('Prev'))
                ui.button('1', on_click=lambda: ui.notify('1'))
                ui.button('2', on_click=lambda: ui.notify('2'))
                ui.button('3', on_click=lambda: ui.notify('3'))
