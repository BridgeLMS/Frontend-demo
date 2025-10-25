from nicegui import ui
from utils.auth import api_login, set_session
from components.footer import show_footer
from components.header import show_header


def login():
    """Login page for learners and tutors."""
    show_header()
    with ui.column().classes('items-center justify-center w-full p-6 flex-grow').style("background-image: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); background-size: cover; background-position: center;"):
        with ui.card().classes('w-[500px] max-w-[95%] p-8 shadow-lg rounded-2xl bg-white'):
            ui.label('Welcome to BridgeLMS').classes('text-3xl font-extrabold text-center mb-2 text-indigo-700')
            ui.label('Sign in to access your learning or teaching dashboard').classes(
                'text-base text-center text-gray-600 mb-6'
            )

            email = ui.input('Email').props('outlined dense').classes('w-full mb-4')
            password = ui.input('Password').props('outlined dense type=password').classes('w-full mb-6')

            def on_login():
                if not email.value or not password.value:
                    ui.notify('Please fill in both fields', type='warning')
                    return

                loading = ui.spinner(size='lg').classes('mt-4')
                try:
                    success, msg, token, user_id, role, username = api_login(email.value, password.value)
                    loading.visible = False

                    if not success:
                        ui.notify(msg, type='negative')
                        return

                    set_session(token=token, role=role, user_id=user_id, name=username)
                    ui.notify('Login successful', type='positive')

                    if role == 'tutor':
                        ui.navigate.to('/tutor/dashboard')
                    elif role == 'learner':
                        ui.navigate.to('/learner/dashboard')
                    else:
                        ui.navigate.to('/')
                except Exception as e:
                    loading.visible = False
                    ui.notify(f'Login failed: {str(e)}', type='negative')

            ui.button('Login', on_click=on_login).classes(
                'w-full text-white rounded-lg'
            ).style('background-color: #4f46e5 !important; hover:background-color: #4338ca !important;')

            ui.link('Don’t have an account? Sign up here', '/signup').classes(
                'block text-center mt-4 text-indigo-700'
            )
    show_footer()
