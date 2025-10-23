# learner_dashboard_nicegui.py
# pip install nicegui==1.*

from nicegui import ui
from components.header import header

# ---------- Helpers ----------
def toggle_theme():
    ui.dark_mode().toggle()

def course_chip(title: str, teacher: str, avatar_url: str):
    with ui.card().classes('card shadow-soft chip items-center').style('flex: 1 1 calc(50% - 0.5rem);'):
        ui.image(avatar_url).classes('rounded-borders').style('width:36px;height:36px;object-fit:cover')
        with ui.column().classes('gap-0 flex-grow'):
            ui.label(title).classes('text-weight-medium')
            ui.label(teacher).classes('tiny')

def mentor_row(name: str, topic: str, avatar_url: str):
    with ui.row().classes('kv'):
        with ui.row().classes('items-center').style('gap:10px'):
            ui.image(avatar_url).style('width:36px;height:36px;border-radius:50%;object-fit:cover')
            with ui.column().classes('gap-0'):
                ui.label(name).classes('small text-weight-medium')
                ui.label('Senior Mentor').classes('tiny')
        ui.label(topic).classes('tiny')

def progress_card(title: str, by: str, pct: int, duration: str):
    with ui.card().classes('card shadow-soft').style('padding:16px'):
        with ui.row().classes('w-full items-center justify-between'):
            with ui.column().classes('gap-0'):
                ui.label(title).classes('small text-weight-medium')
                ui.label(f'By {by} • Duration {duration}').classes('tiny')
            ui.button('Continue', color='primary', on_click=lambda: ui.open('/courses')).props('unelevated size=sm')

        ui.linear_progress(value=pct/100).classes('q-mt-md').props('rounded color=primary')

def right_card(title: str):
    with ui.card().classes('card shadow-soft').style('padding:16px'):
        ui.label(title).classes('text-weight-medium small')
        return ui.column().classes('q-mt-sm')

# ---------- App ----------
def dashboard():
    # ---------- Minimal CSS (no Tailwind) ----------
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
    @media (min-width: 1024px) {
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
    .banner {
        background: linear-gradient(to right, #A29BFE, #A0C4FF);
        color: white;
        border-radius: 1rem;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        border: none;
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
    header()
    with ui.column().classes('app'):
        # Main grid
        with ui.element('main').classes('container'):
            with ui.element('div').classes('grid'):
                # ---------- LEFT SIDEBAR ----------
                with ui.column().classes('sidebar space-y-2'):
                    ui.label('OVERVIEW').classes('text-xs font-bold text-gray-500 uppercase tracking-wider px-4')
                    ui.button('Home', icon='home', on_click=lambda: ui.navigate.to('/')).props('flat no-caps')
                    ui.button('Inbox', icon='mail').props('flat no-caps')
                    ui.button('Lesson', icon='menu_book', on_click=lambda: ui.open('/courses')).props('flat no-caps')
                    ui.button('Task', icon='check_circle', on_click=lambda: ui.navigate.to('/calendar')).props('flat no-caps')
                    ui.button('Group', icon='group').props('flat no-caps')
                    ui.separator().classes('my-8')
                    ui.label('SETTINGS').classes('text-xs font-bold text-gray-500 uppercase tracking-wider px-4')
                    ui.button('Settings', icon='settings').props('flat no-caps')
                    ui.button('Logout', icon='logout').props('flat color=negative no-caps')

                # ---------- CENTER COLUMN ----------
                with ui.column().classes('space-y-6 items-stretch').style('padding-left: 2rem'):
                    # Banner
                    with ui.element('div').classes('banner').style('margin-top: 2rem;'):
                        ui.label('Learn at your own pace, anytime, anywhere.').classes('text-3xl font-bold')
                        # ui.button('Join Now', icon='arrow_forward', on_click=lambda: ui.navigate.to('/signup')).props('unelevated').classes('mt-4 bg-white text-dark')

                    # Your Course
                    ui.label('Your Course').classes('text-xl font-bold text-center')
                    with ui.row().classes('w-full flex-wrap mt-4').style('gap: 1rem;'):
                        course_chip('Physics', 'Ms. Carter', 'https://i.pravatar.cc/64?img=68')
                        course_chip('Math', 'Mr. Stone', 'https://i.pravatar.cc/64?img=5')
                        course_chip('ES', 'Dr. Lee', 'https://i.pravatar.cc/64?img=22')
                        course_chip('Geo.', 'Dr. Zhang', 'https://i.pravatar.cc/64?img=33')
                        course_chip('Chem', 'Dr. Vega', 'https://i.pravatar.cc/64?img=41')
                        course_chip('DT', 'Mentor Addy', 'https://i.pravatar.cc/64?img=58')

                    # Your Mentor
                    with ui.card():
                        with ui.row().classes('w-full items-center justify-between'):
                            ui.label('Your Mentor').classes('text-xl font-bold')
                            ui.button('See all', on_click=lambda: ui.notify('Opening all mentors...')).props('flat dense color=primary')
                        ui.separator().classes('my-4')
                        mentor_row('Prashant Kumar Singh', 'Understanding Concept of React', 'https://i.pravatar.cc/64?img=12')
                        ui.separator().classes('my-2')
                        mentor_row('Ravi Kumar', 'Understanding Concept of React', 'https://i.pravatar.cc/64?img=57')

                    # Ongoing Courses
                    ui.label('Ongoing Courses').classes('text-xl font-bold')
                    progress_card('Android Developer', 'Tima Mustafa', pct=81, duration='12h 36mins')
                    progress_card('Android Developer', 'Tima Mustafa', pct=37, duration='7h 20mins')

                    # Today timeline & Upcoming Events
                    with ui.row().classes('w-full no-wrap items-stretch').style('gap: 1rem;'):
                        with ui.card().classes('w-1/2 h-full flex flex-col'):
                            ui.label('Today').classes('text-xl font-bold')
                            with ui.column().classes('flex-grow justify-around'):
                                for t in ['06:30 pm','07:00 pm','07:30 pm','08:00 pm','08:30 pm','09:00 pm','09:30 pm']:
                                    with ui.row().classes('items-center justify-between w-full'):
                                        ui.label(t).classes('text-sm text-gray-500')
                                        ui.separator().props('vertical').classes('mx-2')
                                        ui.label('•').classes('text-xs text-gray-400')

                        with ui.card().classes('w-1/2 h-full flex flex-col'):
                            ui.label('Upcoming Events').classes('text-xl font-bold')
                            with ui.column().classes('flex-grow justify-around'):
                                def event(title: str):
                                    with ui.column().classes('py-2'):
                                        ui.label(title).classes('font-semibold')
                                        ui.label('By Tima Mustafa').classes('text-sm text-gray-500')
                                event('3-Day JavaScript BootCamp')
                                event('Flutter Workshop')
                                event('2-Day GameDev BootCamp')
                                event('GameDevelopment Competition')
