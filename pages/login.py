from nicegui import ui

# Mock user database
USERS = {'user@example.com': 'password123', 'admin': 'adminpass'}


def login() -> None:
    """Create the login page."""

    def handle_login():
        """Handle the login attempt."""
        username = username_input.value
        password = password_input.value
        if USERS.get(username) == password:
            ui.notify('Login successful!', color='positive')
            ui.navigate.to('/dashboard')
        else:
            ui.notify('Invalid email/username or password', color='negative')

    with ui.column().classes('w-full h-screen flex items-center justify-center bg-gray-100'):
        with ui.card().classes('w-full max-w-md p-8 rounded-lg shadow-lg'):
            with ui.column().classes('w-full items-center space-y-4'):
                ui.label('BridgeLMS').classes('text-4xl font-bold text-gray-800')
                ui.label('Welcome back! Please enter your details.').classes('text-gray-600')

                username_input = ui.input(
                    label='Email or Username',
                    placeholder='Enter your email or username',
                ).classes('w-full')
                password_input = ui.input(
                    label='Password',
                    placeholder='Enter your password',
                    password=True,
                    password_toggle_button=True,
                ).classes('w-full')

                with ui.row().classes('w-full justify-between items-center mt-2'):
                    ui.checkbox('Remember Me')
                    ui.link('Forgot Password?', '#').classes('text-blue-500 hover:underline')

                ui.button('Login', on_click=handle_login).classes('w-full bg-blue-500 text-white')

                with ui.row().classes('items-center mt-4'):
                    ui.label('New to BridgeLMS?')
                    ui.link('Sign up for free', '/signup').classes('text-blue-500 font-semibold hover:underline')
