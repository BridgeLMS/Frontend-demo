from nicegui import ui, app


@ui.page('/')
def main():
    """Main page layout."""
    from components.header import header
    from pages.home import home
    from components.footer import footer
    header()
    home()
    footer()
    # Back to top button
    ui.button(icon='arrow_upward', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"})')) \
        .props('fab-mini') \
        .classes('fixed bottom-8 right-8 z-50') \
        .style('background-color: #007bff; color: white;')


@ui.page('/dashboard')
def dashboard_page():
    """Dashboard page layout."""
    from pages.learner_dashboard import dashboard as learner_dashboard
    learner_dashboard()


@ui.page('/calendar')
def show_calendar_page():
    """Calendar page layout."""
    from components.header import header
    from pages.calendar import calendar_page
    from components.footer import footer
    header()
    calendar_page()
    footer()


@ui.page('/courses')
def courses_page():
    """Courses page layout."""
    from components.header import header
    from pages.courses import courses
    from components.footer import footer
    header()
    courses()
    footer()


@ui.page('/contact')
def contact_page():
    """Contact page layout."""
    from components.header import header
    from pages.contact import contact
    from components.footer import footer
    header()
    contact()
    footer()


@ui.page('/login')
def login_page():
    """Login page layout."""
    from pages.login import login
    login()


@ui.page('/tutor-dashboard')
def tutor_dashboard_page():
    """Tutor dashboard page layout."""
    from pages.tutor_dashboard import tutor_dashboard
    tutor_dashboard()


@ui.page('/signup')
def signup_page():
    """Sign up page layout."""
    from pages.signup import signup
    signup()


@ui.page('/inbox')
def inbox_page():
    """Inbox page layout."""
    from pages.inbox import mailbox_page
    mailbox_page()


app.add_static_files('/assets', 'assets')
ui.run()