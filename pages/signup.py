from nicegui import ui
from utils.auth import api_signup, set_session
from components.footer import show_footer
from components.header import show_header


def signup():
    """Signup page for learners and tutors."""
    show_header()
    with ui.column().classes('items-center justify-center w-full p-6 flex-grow').style("background-image: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); background-size: cover; background-position: center;"):
        with ui.card().classes('w-[600px] max-w-[95%] p-8 shadow-lg rounded-2xl bg-white'):
            ui.label('Join BridgeLMS').classes('text-3xl font-extrabold text-center mb-2 text-indigo-700')
            ui.label('Create your account to start learning or teaching online').classes(
                'text-base text-center text-gray-600 mb-6'
            )

            username = ui.input('Username').props('outlined dense').classes('w-full mb-4')
            email = ui.input('Email').props('outlined dense type=email').classes('w-full mb-4')
            password = ui.input('Password').props('outlined dense type=password').classes('w-full mb-4')
            role = ui.select(['learner', 'tutor'], value='learner', label='Role').props('outlined dense').classes('w-full mb-4')
            phone = ui.input('Phone Number').props('outlined dense type=tel').classes('w-full mb-4')
            bio = ui.textarea('Short Bio').props('outlined dense autogrow').classes('w-full mb-6')

            def on_signup():
                if not all([username.value, email.value, password.value, role.value, phone.value, bio.value]):
                    ui.notify('All fields are required', type='warning')
                    return

                loading = ui.spinner(size='lg').classes('mt-4')
                try:
                    success, msg, token, user_id = api_signup(
                        username.value, email.value, password.value, role.value, phone.value, bio.value
                    )
                    loading.visible = False

                    if not success:
                        ui.notify(msg, type='negative')
                        return

                    set_session(token=token, role=role.value, user_id=user_id, name=username.value)
                    ui.notify('Account created successfully!', type='positive')

                    if role.value == 'tutor':
                        ui.navigate.to('/tutor/dashboard')
                    else:
                        ui.navigate.to('/learner/dashboard')
                except Exception as e:
                    loading.visible = False
                    ui.notify(f'Signup failed: {str(e)}', type='negative')

            ui.button('Create Account', on_click=on_signup).classes(
                'w-full text-white rounded-lg'
            ).style('background-color: #4f46e5 !important; hover:background-color: #4338ca !important;')

            ui.link('Already have an account? Login here', '/login').classes(
                'block text-center mt-4 text-indigo-700'
            )
    show_footer()
