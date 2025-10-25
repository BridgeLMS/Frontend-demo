from nicegui import ui
from datetime import datetime

def mailbox_page():
    """Create the mailbox page with a messaging interface."""
    ui.add_css('''
    .chat-container {
        display: flex;
        height: 80vh;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        border: 1px solid #e0e0e0;
        border-radius: 1rem;
        background: white;
    }
    .conversations {
        width: 30%;
        border-right: 1px solid #e0e0e0;
        overflow-y: auto;
    }
    .chat-window {
        width: 70%;
        display: flex;
        flex-direction: column;
    }
    .messages {
        flex-grow: 1;
        padding: 2rem;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    .message-input {
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
    }
    .conversation-item {
        padding: 1rem;
        cursor: pointer;
    }
    .conversation-item:hover {
        background-color: #f5f5f5;
    }
    .message {
        padding: 0.5rem 1rem;
        border-radius: 1rem;
        max-width: 70%;
    }
    .sent {
        background-color: #6C5CE7;
        color: white;
        align-self: flex-end;
    }
    .received {
        background-color: #f0f0f0;
        color: #333;
        align-self: flex-start;
    }
    ''')

    with ui.column().classes('w-full items-center p-8'):
        ui.label('Mailbox').classes('text-3xl font-bold mb-4')
        
        with ui.element('div').classes('chat-container'):
            # Conversations List
            with ui.column().classes('conversations'):
                conversations = [
                    {'name': 'John Doe', 'last_message': 'See you tomorrow!'},
                    {'name': 'Jane Smith', 'last_message': 'Thanks for the help.'},
                    {'name': 'Peter Jones', 'last_message': 'I have a question.'},
                ]
                for conv in conversations:
                    with ui.element('div').classes('conversation-item'):
                        ui.label(conv['name']).classes('font-bold')
                        ui.label(conv['last_message']).classes('text-sm text-gray-500')

            # Chat Window
            with ui.column().classes('chat-window'):
                # Messages Display
                with ui.column().classes('messages') as messages_container:
                    ui.chat_message('Hello! How can I help you today?', name='John Doe', sent=False)
                    ui.chat_message('I have a question about the assignment.', name='You', sent=True)

                # Message Input
                with ui.row().classes('message-input w-full items-center'):
                    message_input = ui.input(placeholder='Type a message...').classes('flex-grow')
                    ui.button('Send', on_click=lambda: ui.notify('Message sent!')).props('flat round icon=send')
