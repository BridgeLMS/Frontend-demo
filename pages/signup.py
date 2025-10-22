from nicegui import ui

def signup() -> None:
    """Create the sign-up page."""

    def handle_signup():
        """Handle the sign-up attempt."""
        # Add your sign-up logic here
        ui.notify('Account created successfully!', color='positive')
        ui.navigate.to('/login')

    with ui.column().classes('w-full min-h-screen flex items-center justify-center bg-gray-100'):
        with ui.card().classes('w-full max-w-md p-8 rounded-lg shadow-lg'):
            with ui.column().classes('w-full items-center space-y-4'):
                ui.label('Create an Account').classes('text-4xl font-bold text-gray-800')
                ui.label('Join BridgeLMS to start your learning journey.').classes('text-gray-600')

                ui.input(label='Full Name', placeholder='Enter your full name').classes('w-full')
                ui.input(label='Email Address', placeholder='Enter your email address').classes('w-full')
                ui.input(
                    label='Password',
                    placeholder='Create a password',
                    password=True,
                    password_toggle_button=True,
                ).classes('w-full')
                ui.input(
                    label='Confirm Password',
                    placeholder='Confirm your password',
                    password=True,
                    password_toggle_button=True,
                ).classes('w-full')
                ui.input (label='Role', placeholder='Are you a Learner or Tutor?').classes('w-full')
                ui.input (label='Bio', placeholder='Tell us about yourself').classes('w-full')

                ui.button('Create Account', on_click=handle_signup).classes('w-full bg-blue-500 text-white')

                with ui.row().classes('items-center mt-4'):
                    ui.label('Already have an account?')
                    ui.link('Log in', '/login').classes('text-blue-500 font-semibold hover:underline')
