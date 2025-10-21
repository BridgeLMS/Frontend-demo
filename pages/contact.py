from nicegui import ui


def contact() -> None:
    """Create the contact page."""
    with ui.row().classes(
        'w-full max-w-7xl mx-auto p-8 items-center justify-center'
    ):
        # Contact Information
        with ui.column().classes('w-1/2 space-y-8'):
            ui.label('Get in Touch').classes('text-5xl font-bold')
            ui.label(
                'We’re here to help and answer any question you might have. We look forward to hearing from you.'
            ).classes('text-lg text-gray-600')

            with ui.row().classes('items-center'):
                ui.icon('email', size='lg').classes('text-blue-500 mr-4')
                with ui.column():
                    ui.label('Email').classes('text-xl font-bold')
                    ui.label(
                        'Our support team will get back to you within 24 hours.'
                    ).classes('text-gray-600')
                    ui.link(
                        'support@bridgelms.com', 'mailto:support@bridgelms.com'
                    ).classes('text-blue-500')

            with ui.row().classes('items-center'):
                ui.icon('phone', size='lg').classes('text-blue-500 mr-4')
                with ui.column():
                    ui.label('Phone').classes('text-xl font-bold')
                    ui.label('Mon-Fri from 8am to 5pm.').classes(
                        'text-gray-600'
                    )
                    ui.link('+1 (555) 123-4567', 'tel:+15551234567').classes(
                        'text-blue-500'
                    )

            with ui.row().classes('items-center'):
                ui.icon('group', size='lg').classes('text-blue-500 mr-4')
                with ui.column():
                    ui.label('Follow Us').classes('text-xl font-bold')
                    ui.label('Join our community on social media.').classes(
                        'text-gray-600'
                    )
                    with ui.row():
                        ui.icon('twitter').classes('text-gray-500 mx-1')
                        ui.icon('facebook').classes('text-gray-500 mx-1')
                        ui.icon('instagram').classes('text-gray-500 mx-1')

        # Contact Form
        with ui.card().classes('w-1/2 p-8'):
            with ui.column().classes('w-full space-y-4'):
                ui.input(label='Your Name', placeholder='Enter your name')
                ui.input(
                    label='Your Email', placeholder='Enter your email'
                )
                ui.input(label='Subject', placeholder='Enter the subject')
                ui.textarea(
                    label='Message', placeholder='Enter your message'
                )
                ui.button(
                    'Send Message', on_click=lambda: ui.notify('Message sent!')
                ).classes('w-full')
