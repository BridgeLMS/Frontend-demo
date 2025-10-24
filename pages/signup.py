from nicegui import ui
from utils.auth import api_signup, set_session

# from utils.auth import api_login, api_signup, set_session

# Mock user database
USERS = {'user@example.com': 'password123', 'admin': 'adminpass'}



def signup() -> None:
    """Create the sign-up page."""

    async def handle_signup():
        """Handle the sign-up attempt."""
        if not username.value or not email.value or not password.value or not role.value or not phone.value or not bio.value:
            ui.notify('Please fill in all fields', color='negative')
            return
        
        success, message, token, user_id = api_signup(
            username.value,
            email.value,
            password.value,
            role.value,
            phone.value,
            bio.value
        )
        
        if success:
            set_session(token, role.value, user_id, username.value)
            ui.notify(message, color='positive')
            ui.navigate.to('/login')
        else:
            ui.notify(message, color='negative')

    with ui.column().classes('w-full min-h-screen flex items-center justify-center bg-gray-100'):
        with ui.card().classes('w-full max-w-md p-8 rounded-lg shadow-lg'):
            with ui.column().classes('w-full items-center space-y-4'):
                ui.label('Create an Account').classes('text-4xl font-bold text-gray-800')
                ui.label('Join BridgeLMS to start your learning journey.').classes('text-gray-600')

                username = ui.input(label='Username', placeholder='Enter your username').classes('w-full')
                email = ui.input(label='Email Address', placeholder='Enter your email address').classes('w-full')
                password = ui.input(
                    label='Password',
                    placeholder='Create a password',
                    password=True,
                    password_toggle_button=True,
                ).classes('w-full')
                role = ui.input (label='Role', placeholder='Are you a Learner or Tutor?').classes('w-full')
                phone = ui.input (label='Phone', placeholder='Enter your phone number').classes('w-full')
                bio = ui.input (label='Bio', placeholder='Tell us about yourself').classes('w-full')

                ui.button('Create Account', on_click=handle_signup).classes('w-full bg-blue-500 text-white')

                with ui.row().classes('items-center mt-4'):
                    ui.label('Already have an account?')
                    ui.link('Log in', '/login').classes('text-blue-500 font-semibold hover:underline')
