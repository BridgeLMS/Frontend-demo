from nicegui import ui
from dataclasses import dataclass
from typing import List

@dataclass
class Email:
    id: int
    sender: str
    subject: str
    body: str
    read: bool = False

# Sample emails
emails: List[Email] = [
    Email(id=1, sender='tutor@example.com', subject='Your assignment feedback', body='Great work on the last assignment!'),
    Email(id=2, sender='admin@example.com', subject='Important Announcement', body='Please note the upcoming holiday schedule.'),
    Email(id=3, sender='student-services@example.com', subject='Upcoming Events', body='Join us for the student mixer next week!'),
]

def mailbox_page():
    """Creates a simple functional mailbox page."""

    def show_email(email: Email):
        email.read = True
        email_list.refresh()
        with ui.dialog() as dialog, ui.card():
            ui.label(f"From: {email.sender}").classes('text-lg font-bold')
            ui.label(f"Subject: {email.subject}").classes('text-md font-semibold')
            ui.separator()
            ui.label(email.body).classes('mt-4')
            with ui.card_actions():
                ui.button('Close', on_click=dialog.close)
        dialog.open()

    @ui.refreshable
    def email_list():
        for email in emails:
            with ui.row().classes('w-full p-2 items-center border-b hover:bg-gray-100 cursor-pointer') as row:
                row.on('click', lambda e=email: show_email(e))
                with ui.column().classes('flex-grow'):
                    sender_class = 'font-bold' if not email.read else 'font-normal'
                    ui.label(email.sender).classes(f'text-md {sender_class}')
                    ui.label(email.subject).classes('text-sm text-gray-600')

    ui.label('Inbox').classes('text-2xl font-bold p-4')
    email_list()
