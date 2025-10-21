from nicegui import ui


def dashboard() -> None:
    """Create the dashboard page."""
    with ui.column().classes('w-full p-8'):
        # Welcome Header
        with ui.row().classes('w-full justify-between items-center'):
            with ui.column():
                ui.label('Welcome back, Sophia').classes(
                    'text-4xl font-bold'
                )
                ui.label('Your BridgeLMS academic journey summary.').classes(
                    'text-lg text-gray-600'
                )

        # My Courses Section
        ui.label('My Courses').classes('text-3xl font-bold mt-8')
        with ui.grid(columns=3).classes('w-full gap-8 mt-4'):
            for title, instructor in [
                ('Introduction to Data Science', 'Dr. Evelyn Reed'),
                ('Advanced Spanish', 'Isabella Rossi'),
                ('Digital Marketing Fundamentals', 'Ethan Carter'),
            ]:
                with ui.card().classes('text-left'):
                    if title == 'Introduction to Data Science':
                        image_url = 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80'
                    elif title == 'Advanced Spanish':
                        image_url = 'https://images.unsplash.com/photo-1524678606370-a47625cb810c?auto=format&fit=crop&w=800&q=80'
                    else:
                        image_url = 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80'
                    ui.image(image_url).classes('w-full h-48 object-cover rounded-t-lg')
                    with ui.card_section():
                        ui.label(title).classes('text-xl font-bold')
                        ui.label(instructor).classes('text-gray-600')

        # Upcoming Events & Recent Announcements
        with ui.grid(columns=2).classes('w-full gap-16 mt-16'):
            # Upcoming Events
            with ui.column():
                ui.label('Upcoming Events').classes('text-2xl font-bold')
                with ui.column().classes('w-full mt-4 space-y-4'):
                    for event, time in [
                        ('Data Science Lecture', '10:00 AM - 11:00 AM'),
                        (
                            'Spanish Conversation Practice',
                            '2:00 PM - 3:00 PM',
                        ),
                        ('Marketing Workshop', '4:00 PM - 5:00 PM'),
                    ]:
                        with ui.card().classes('w-full p-4 flex items-center'):
                            ui.icon('event', size='lg').classes(
                                'text-blue-500 mr-4'
                            )
                            with ui.column():
                                ui.label(event).classes('font-bold')
                                ui.label(time).classes('text-gray-600')

            # Recent Announcements
            with ui.column():
                ui.label('Recent Announcements').classes('text-2xl font-bold')
                with ui.column().classes('w-full mt-4 space-y-4'):
                    for title, desc, date in [
                        (
                            'Data Science Lecture Rescheduled',
                            'Lecture moved to Monday at 10 AM.',
                            '2 days ago',
                        ),
                        (
                            'Spanish Project Deadline Extended',
                            'New deadline is next Friday.',
                            '1 week ago',
                        ),
                    ]:
                        with ui.card().classes('w-full p-4 flex items-center'):
                            ui.icon('campaign', size='lg').classes(
                                'text-blue-500 mr-4'
                            )
                            with ui.column():
                                ui.label(title).classes('font-bold')
                                ui.label(desc).classes('text-gray-600')
                                ui.label(date).classes(
                                    'text-sm text-gray-400'
                                )
