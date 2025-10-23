from nicegui import ui


def home() -> None:
    """Create the home page."""
    ui.add_css('''
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    ''')
    with ui.column().classes('w-full items-center'):
        # Hero Section
        with ui.row().classes(
            'w-full h-[70vh] bg-cover bg-center flex items-center justify-center'
        ).style(
            'background-image: url("assets/Images/Team2.jpeg")'
        ):
            
            
            with ui.column().classes('items-center px-16 py-1 rounded-xl w-full max-w-3xl mx-auto mt-64').style("font-family: 'Montserrat', sans-serif; background-color: #965c40;"):
                ui.label('Welcome to BridgeLMS!').classes('text-4xl font-bold text-1E3A8A')
                with ui.column().classes('items-center gap-0'):
                    ui.label('Bridging Gaps, Building Futures').classes(
                        'text-4xl font-bold'
                    ).style('color: var(--primary-brand)')
                    ui.label(
                        'BridgeLMS is your all-in-one platform for seamless learning and teaching.'
                    ).classes('text-base text-center text-white italic')
                with ui.row().classes('mt-2'):
                    
                    ui.button(
                        "I am a Learner",
                        on_click=lambda: ui.navigate.to('/login'),
                    ).classes('m-2').style('background-color: var(--primary-brand); color: white;')
                    ui.button(
                        "I am a Tutor", on_click=lambda: ui.navigate.to('/login')
                    ).classes('m-2').style('background-color: var(--primary-brand); color: white;')
                    

        # # Explore Our Courses Section
        # with ui.column().classes('w-full items-center my-16'):
        #     ui.label('Explore Our Courses').classes('text-4xl font-bold')
        #     ui.label(
        #         'Find the perfect course to advance your skills and knowledge.'
        #     ).classes('text-lg mt-2').style('color: var(--text-titles)')

        #     with ui.row().classes('mt-8'):
        #         ui.button('All Categories', on_click=lambda: ui.notify('All')).style('background-color: var(--primary-brand); color: white;')
        #         # ui.button('Web Design', on_click=lambda: ui.notify('Web Design'))
        #         ui.button(
        #             'Cybersecurity', on_click=lambda: ui.notify('Cybersecurity')
        #         ).style('background-color: var(--primary-brand); color: white;')
        #         ui.button(
        #             'Web Development',
        #             on_click=lambda: ui.notify('Web Development'),
        #         ).style('background-color: var(--primary-brand); color: white;')
        #         ui.button(
        #             'Data Science', on_click=lambda: ui.notify('Data Science')
        #         ).style('background-color: var(--primary-brand); color: white;')
        #         ui.button('Marketing', on_click=lambda: ui.notify('Marketing')).style('background-color: var(--primary-brand); color: white;')

        #     with ui.grid(columns=3).classes('w-full max-w-5xl gap-8 mt-8'):
        #         for title, desc, price in [
        #             (
        #                 'Introduction to Web Design',
        #                 'Learn the fundamentals of web design, including HTML, CSS, and responsive design principles.',
        #                 '₵49.99',
        #             ),
        #             (
        #                 'Cybersecurity Essentials',
        #                 'Protect systems and networks from digital attacks with this comprehensive cybersecurity course.',
        #                 '₵89.99',
        #             ),
        #             (
        #                 'Full-Stack Web Development',
        #                 'Master both front-end and back-end technologies to build complete web applications.',
        #                 '₵129.99',
        #             ),
        #         ]:
            # with ui.grid(columns=3).classes('w-full max-w-5xl gap-8 mt-8'):
            #     for title, desc, price in [
            #         (
            #             'Introduction to Web Design',
            #             'Learn the fundamentals of web design, including HTML, CSS, and responsive design principles.',
            #             '₵49.99',
            #         ),
            #         (
            #             'Cybersecurity Essentials',
            #             'Protect systems and networks from digital attacks with this comprehensive cybersecurity course.',
            #             '₵89.99',
            #         ),
            #         (
            #             'Full-Stack Web Development',
            #             'Master both front-end and back-end technologies to build complete web applications.',
            #             '₵129.99',
            #         ),
            #     ]:
            #         with ui.card().classes('text-left').style('background-color: var(--card-surface-light);'):
            #             if title == 'Introduction to Web Design':
            #                 image_url = 'assets/Images/web_dev.jpg'
            #             elif title == 'Cybersecurity Essentials':
            #                 image_url = 'assets/Images/cyber_ess.jpg'
            #             else:
            #                 image_url = 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=800&q=80'
            #             ui.image(image_url).classes('w-full h-48 object-cover rounded-t-lg')
            #             with ui.card_section():
            #                 ui.label(title).classes('text-xl font-bold')
            #                 ui.label(desc).classes('mt-2').style('color: var(--text-titles)')
            #                 with ui.row().classes(
            #                     'w-full justify-between items-center mt-4'
            #                 ):
            #                     ui.label(price).classes(
            #                         'text-lg font-bold'
            #                     ).style('color: var(--accent)')
            #                     ui.link('Learn More', '#').style(
            #                         'color: var(--accent)'
            #                     )
        # Why BridgeLMS? Section
        with ui.column().classes('w-full items-center my-16 p-16').style('background-color: var(--background-light)'):
            ui.label('Why BridgeLMS?').classes('text-4xl font-bold')
            ui.label(
                'BridgeLMS simplifies the learning process, offering a comprehensive suite of tools to enhance your educational journey.'
            ).classes('text-lg mt-2 text-center max-w-2xl').style('color: var(--text-titles)')

            with ui.grid(columns=4).classes('w-full max-w-5xl gap-8 mt-8'):
                for icon, title, desc in [
                    (
                        'groups',
                        'Connect with Tutors',
                        'Find and connect with experienced tutors in various subjects.',
                    ),
                    (
                        'calendar_month',
                        'Unified Calendar',
                        'Manage your schedule with a centralized calendar for all your courses and sessions.',
                    ),
                    (
                        'folder',
                        'Course Resources',
                        'Access a wealth of course materials, notes, and assignments.',
                    ),
                    (
                        'verified_user',
                        'Attendance Tracking',
                        'Track attendance with our innovative facial verification system.',
                    ),
                ]:
                    with ui.card().classes('items-center text-center').style('background-color: var(--card-surface-light);'):
                        ui.icon(icon).classes('text-5xl').style('color: var(--primary-brand)')
                        ui.label(title).classes('text-xl font-bold mt-4')
                        ui.label(desc).classes('mt-2').style('color: var(--text-titles)')

        # How BridgeLMS Works Section
        with ui.column().classes('w-full items-center my-16'):
            ui.label('How BridgeLMS Works').classes('text-4xl font-bold')
            with ui.column().classes('w-full max-w-3xl mt-8 space-y-8'):
                for number, title, desc in [
                    (
                        '1',
                        'Find Your Perfect Tutor',
                        'Browse our extensive tutor directory and select the best fit for your learning needs.',
                    ),
                    (
                        '2',
                        'Engage in Interactive Learning',
                        'Participate in live sessions, access resources, and collaborate with peers.',
                    ),
                    (
                        '3',
                        'Track Your Progress',
                        'Monitor your attendance, grades, and overall progress with our intuitive dashboard.',
                    ),
                ]:
                    with ui.row().classes('items-start'):
                        ui.label(number).classes(
                            'text-4xl font-bold mr-8'
                        ).style('color: var(--primary-brand)')
                        with ui.column():
                            ui.label(title).classes('text-2xl font-bold')
                            ui.label(desc).classes('mt-2').style('color: var(--text-titles)')

        # Community & Trust Section
        with ui.column().classes('w-full items-center my-16 p-16').style('background-color: var(--background-light)'):
            ui.label('Community & Trust').classes('text-4xl font-bold')
            with ui.grid(columns=3).classes('w-full max-w-6xl gap-8 mt-8'):
                for quote, author, role in [
                    (
                        '"BridgeLMS has transformed my learning experience. The tutors are knowledgeable, and the platform is incredibly user-friendly."',
                        'Sophia Carter',
                        'Student',
                    ),
                    (
                        '"I love the flexibility and convenience of BridgeLMS. It\'s made learning so much more accessible and enjoyable."',
                        'Ethan Walker',
                        'Student',
                    ),
                    (
                        '"As a tutor, BridgeLMS has helped me connect with students from all over the world. The platform\'s features are top-notch."',
                        'Olivia Bennett',
                        'Tutor',
                    ),
                ]:
                    with ui.card().classes('p-6'):
                        ui.label(quote).classes('text-lg italic')
                        ui.label(f'- {author}, {role}').classes(
                            'mt-4 font-bold'
                        )
            ui.label('Trusted by world-class companies').classes(
                'text-2xl font-bold mt-16'
            )
            with ui.row().classes('w-full max-w-4xl justify-around mt-8'):
                for _ in range(4):
                    ui.icon('business', size='xl').classes('text-gray-400')

        # Final CTA Section
        with ui.column().classes('w-full items-center my-16'):
            ui.label('Ready to Elevate Your Learning Journey?').classes(
                'text-4xl font-bold text-center'
            )
            ui.label(
                'Join BridgeLMS today and unlock a world of educational opportunities.'
            ).classes('text-lg mt-2').style('color: var(--text-titles)')
            ui.button(
                'Get Started Now', on_click=lambda: ui.navigate.to('/login')
            ).classes('mt-8').style('background-color: var(--accent); color: white;')
