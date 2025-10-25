from nicegui import ui
import calendar
from datetime import datetime

def calendar_page():
    """Create the calendar page with a monthly view and events."""
    ui.add_css('''
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 1px;
        background-color: #e0e0e0;
        border: 1px solid #e0e0e0;
    }
    .calendar-day, .calendar-header-day {
        background-color: white;
        padding: 8px;
        min-height: 120px;
        position: relative;
    }
    .calendar-header-day {
        min-height: auto;
        text-align: center;
        font-weight: bold;
        background-color: #f5f5f5;
    }
    .day-number {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .today .day-number {
        background-color: #6C5CE7;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    .event {
        font-size: 0.75rem;
        padding: 2px 6px;
        border-radius: 4px;
        color: white;
        margin-top: 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .event-blue { background-color: #3b82f6; }
    .event-red { background-color: #ef4444; }
    .event-purple { background-color: #8b5cf6; }
    .event-green { background-color: #22c55e; }
    .tasks-container {
        width: 300px;
        padding-left: 2rem;
    }
    .task-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem 0;
    }
    ''')

    # Dummy data for events
    events = {
        3: [{'name': 'Volunteers Aid', 'color': 'blue'}, {'name': 'Python Fundamentals', 'color': 'purple'}],
        4: [{'name': '2nd Meeting', 'color': 'blue'}],
        5: [{'name': 'P&P', 'color': 'red'}, {'name': 'ENVIRONMENT', 'color': 'purple'}],
        6: [{'name': 'Gym', 'color': 'blue'}, {'name': 'AGILE Framework', 'color': 'red'}, {'name': 'IT LAW', 'color': 'purple'}],
        7: [{'name': 'Exams supervision', 'color': 'red'}, {'name': 'Assignment Grading', 'color': 'blue'}],
        10: [{'name': 'Project Management Fundamentals', 'color': 'red'}],
        11: [{'name': 'Seminar', 'color': 'blue'}, {'name': 'Gym', 'color': 'red'}],
        14: [{'name': 'Gym', 'color': 'red'}],
        25: [{'name': '3 pending tasks', 'color': 'green'}, {'name': 'Morning Aur', 'color': 'blue'}, {'name': 'Gym', 'color': 'red'}],
    }

    def build_month_view():
        with ui.element('div').classes('calendar-grid'):
            for day in ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']:
                with ui.element('div').classes('calendar-header-day'):
                    ui.label(day)
            
            cal = calendar.Calendar()
            month_days = cal.monthdayscalendar(2025, 10)
            
            for week in month_days:
                for day in week:
                    day_classes = 'calendar-day'
                    if day == 0:
                        with ui.element('div').classes(day_classes + ' bg-gray-50'):
                            pass
                    else:
                        if day == 25:
                            day_classes += ' today'
                        with ui.element('div').classes(day_classes):
                            ui.label(day).classes('day-number')
                            if day in events:
                                for event in events[day]:
                                    ui.label(event['name']).classes(f"event event-{event['color']}")

    def set_view(view_name: str):
        view_container.clear()
        with view_container:
            if view_name == 'month':
                build_month_view()
            else:
                ui.label(f'{view_name.capitalize()} View Placeholder').classes('text-2xl')

    with ui.column().classes('w-full items-center p-8'):
        # Header
        with ui.row().classes('w-full max-w-7xl justify-between items-center mb-4'):
            with ui.row().classes('items-center gap-2'):
                ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/tutor-dashboard')).props('flat round')
                ui.icon('calendar_today', size='lg').classes('text-gray-600')
                ui.label('Calendar').classes('text-2xl font-bold')
                ui.button('Today')
                ui.button(icon='chevron_left')
                ui.button(icon='chevron_right')
                ui.label('October 2025').classes('text-xl font-semibold')
            with ui.row().classes('items-center gap-2'):
                ui.button('Month', on_click=lambda: set_view('month')).props('color=primary')
                ui.button('Week', on_click=lambda: set_view('week'))
                ui.button('Day', on_click=lambda: set_view('day'))
                ui.button('List', on_click=lambda: set_view('list'))
        
        with ui.row().classes('w-full max-w-7xl'):
            view_container = ui.column().classes('w-2/3')
            set_view('month')

            # Weekly Tasks Sidebar
            with ui.column().classes('tasks-container w-1/3'):
                ui.label('Weekly Tasks').classes('text-xl font-bold mb-4')
                tasks = {
                    "8:30am": "Advanced Data Science",
                    "9am": "GIZ AGILE",
                    "11am": "Grade Assignments",
                    "2pm": "Lecture: Advanced Python",
                    "4pm": "Office Hours",
                    "5pm": "Business Analytics Essentials",
                    "7pm": "Prepare tomorrow's lesson",
                }
                for time, task in tasks.items():
                    with ui.row().classes('task-item'):
                        ui.label(time).classes('text-gray-500')
                        ui.label(task)
