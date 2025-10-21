from nicegui import ui


def about() -> None:
    """Create the about page."""
    with ui.column().classes('w-full items-center'):
        # Hero Section
        with ui.row().classes(
            'w-full h-screen bg-cover bg-center flex items-center justify-center'
        ).style(
            'background-image: url("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1600&q=80")'
        ):
            with ui.column().classes('items-center text-white bg-black bg-opacity-40 p-8 rounded-xl'):
                ui.label('About BridgeLMS').classes('text-5xl font-bold')
                ui.label(
                    'Bridging the gap between learners and tutors for a seamless educational experience.'
                ).classes('text-xl mt-4 text-center max-w-2xl')
                ui.button(
                    'Explore Courses',
                    on_click=lambda: ui.open('/courses'),
                ).classes('mt-8')

        # Our Story Section
        with ui.column().classes('w-full items-center my-16 px-4'):
            ui.label('Our Story').classes('text-4xl font-bold')
            ui.label(
                'BridgeLMS was born from a simple idea: to make learning more accessible and personalized. '
                'Founded in 2020 by a team of educators and tech enthusiasts, we saw a gap in the market for a '
                'platform that truly connects learners with the right tutors. Our journey began with a small pilot '
                'program, and today, we’re proud to serve thousands of students and tutors worldwide.'
            ).classes('text-lg mt-4 text-gray-600 text-center max-w-3xl')

        # Our Mission & Vision Section
        with ui.column().classes('w-full items-center my-16 px-4'):
            ui.label('Our Mission & Vision').classes('text-4xl font-bold')
            ui.label(
                'Our mission is to empower learners to achieve their educational goals by providing a comprehensive '
                'and user-friendly platform that facilitates seamless connections with qualified tutors. Our vision is to '
                'become the leading online learning platform, recognized for its innovative features, quality '
                'resources, and commitment to student success.'
            ).classes('text-lg mt-4 text-gray-600 text-center max-w-3xl')

        # Our Core Values Section
        with ui.column().classes('w-full items-center my-16 bg-gray-100 p-16'):
            ui.label('Our Core Values').classes('text-4xl font-bold')
            ui.label(
                'The principles that guide our work and our community.'
            ).classes('text-lg mt-2 text-gray-600')
            with ui.grid(columns=4).classes('w-full max-w-6xl gap-8 mt-8'):
                for icon, title, desc in [
                    (
                        'groups',
                        'Community',
                        'We foster a supportive and inclusive community of learners and tutors.',
                    ),
                    (
                        'school',
                        'Learning',
                        'We are committed to providing high-quality learning resources and experiences.',
                    ),
                    (
                        'verified',
                        'Integrity',
                        'We uphold the highest standards of honesty and transparency in all our interactions.',
                    ),
                    (
                        'handshake',
                        'Collaboration',
                        'We believe in the power of collaboration to enhance the learning process.',
                    ),
                ]:
                    with ui.card().classes('items-center text-center p-6'):
                        ui.icon(icon).classes('text-5xl text-blue-600')
                        ui.label(title).classes('text-xl font-bold mt-4')
                        ui.label(desc).classes('text-gray-600 mt-2')

        # What Sets BridgeLMS Apart Section
        with ui.column().classes('w-full items-center my-16 px-4'):
            ui.label('What Sets BridgeLMS Apart').classes(
                'text-4xl font-bold'
            )
            with ui.column().classes('w-full max-w-3xl mt-8 space-y-6'):
                for title, desc in [
                    (
                        'Comprehensive Features',
                        'Our platform offers a unified calendar, tutor contact access, and attendance tracking with facial verification.',
                    ),
                    (
                        'Quality Tutors',
                        'We carefully vet all tutors to ensure they meet our high standards of expertise and professionalism.',
                    ),
                    (
                        'User-Friendly Design',
                        'Our user-friendly interface makes it easy for learners and tutors to connect and manage their learning activities.',
                    ),
                    (
                        'Continuous Innovation',
                        'We are constantly innovating and adding new features to enhance the learning experience.',
                    ),
                ]:
                    with ui.row().classes('items-start'):
                        ui.icon('check_circle', color='blue').classes('mr-4 mt-1')
                        with ui.column():
                            ui.label(title).classes('text-xl font-bold')
                            ui.label(desc).classes('text-gray-600')

        # Join BridgeLMS Today Section
        with ui.column().classes('w-full items-center my-16 bg-gray-100 p-16'):
            ui.label('Join BridgeLMS Today').classes('text-4xl font-bold')
            ui.label(
                'Start your learning journey with us and experience the difference.'
            ).classes('text-lg mt-2 text-gray-600')
            ui.button(
                'Get Started', on_click=lambda: ui.notify('Get Started')
            ).classes('mt-8')
