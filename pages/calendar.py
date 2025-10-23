from nicegui import ui
from datetime import datetime

def calendar_content():
    """Creates the calendar content."""

    # Main container
    with ui.column().classes('w-full p-8 gap-8'):
        # Header
        with ui.row().classes('w-full justify-between items-center'):
            ui.label('Calendar').classes('text-4xl font-bold')
            ui.button('New Event', on_click=lambda: ui.notify('New Event clicked!')).props('color=primary')

        # Tabs for Week/Month
        with ui.tabs().classes('w-full') as tabs:
            week_tab = ui.tab('Week')
            month_tab = ui.tab('Month')

        with ui.tab_panels(tabs, value=week_tab).classes('w-full'):
            with ui.tab_panel(week_tab):
                # Week navigation
                with ui.row().classes('w-full justify-between items-center my-4'):
                    ui.button(icon='chevron_left')
                    ui.label('October 23 - 29, 2024').classes('text-xl')
                    ui.button(icon='chevron_right')

                # Weekly grid
                days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
                with ui.grid(columns=7).classes('w-full border-t border-l border-gray-200'):
                    for day in days:
                        with ui.column().classes('border-r border-b border-gray-200 p-2 text-center'):
                            ui.label(day).classes('font-semibold text-gray-600')
                            if day == 'THU':
                                ui.label('25').classes('mt-1 bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center')
                    
                    # Dummy grid cells for events
                    for i in range(7 * 1): # 1 row for the week view
                        with ui.column().classes('h-96 border-r border-b border-gray-200 p-1'):
                            # Thursday events
                            if i % 7 == 4: # Corresponds to Thursday
                                with ui.card().classes('w-full bg-blue-100 p-2 mt-8'):
                                    ui.label('Calculus 101').classes('font-semibold text-xs')
                                    ui.label('10am - 11am').classes('text-xs text-gray-500')
                                with ui.card().classes('w-full bg-blue-100 p-2 mt-12'):
                                    ui.label('Office Hours').classes('font-semibold text-xs')
                                    ui.label('1pm - 2pm').classes('text-xs text-gray-500')
                                with ui.card().classes('w-full bg-blue-100 p-2 mt-8'):
                                    ui.label('Linear Algebra').classes('font-semibold text-xs')
                                    ui.label('3pm - 4pm').classes('text-xs text-gray-500')
                                with ui.card().classes('w-full bg-blue-100 p-2 mt-8'):
                                    ui.label('Study Group').classes('font-semibold text-xs')
                                    ui.label('5pm - 6pm').classes('text-xs text-gray-500')


            with ui.tab_panel(month_tab):
                ui.label('Month view coming soon!')

def calendar_page():
    """The main calendar page layout."""
    with ui.row().classes('w-full no-wrap'):
        # Left side (main calendar)
        with ui.column().classes('w-2/3'):
            calendar_content()

        # Right side (monthly calendar and events)
        with ui.column().classes('w-1/3 p-8 gap-8'):
            # Monthly calendar
            with ui.card().classes('w-full'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.button(icon='chevron_left')
                    ui.label('October 2024').classes('text-lg font-semibold')
                    ui.button(icon='chevron_right')
                
                days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
                with ui.grid(columns=7).classes('w-full text-center gap-2 mt-4'):
                    for day in days:
                        ui.label(day).classes('font-semibold text-gray-500')
                    for i in range(31):
                        day_num = i + 1
                        if day_num in [5, 12, 25]:
                            ui.button(f'{day_num}', on_click=lambda d=day_num: ui.notify(f'Day {d}')) \
                                .props(f'round color={"blue" if day_num == 25 else "light-blue"} text-white')
                        else:
                            ui.label(f'{day_num}')

            # Today's Events
            ui.label("Today's Events").classes('text-2xl font-bold mt-8')
            events = [
                ("Calculus 101", "10:00 AM - 11:00 AM"),
                ("Office Hours with Dr. Ramirez", "1:00 PM - 2:00 PM"),
                ("Linear Algebra", "3:00 PM - 4:00 PM"),
                ("Study Group - Physics", "5:00 PM - 6:00 PM"),
            ]
            for title, time in events:
                with ui.card().classes('w-full'):
                    with ui.row().classes('w-full items-center no-wrap'):
                        ui.html('<div class="w-1 h-12 bg-blue-500 rounded-full mr-4"></div>')
                        with ui.column().classes('gap-0'):
                            ui.label(title).classes('font-semibold')
                            ui.label(time).classes('text-sm text-gray-500')