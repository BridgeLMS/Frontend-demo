from nicegui import ui, app
from components.footer import show_footer
from components.header import show_header
from pages.home import home
from pages.learner_dashboard import dashboard as learner_dashboard
from pages.courses import courses
from pages.contact import contact
from pages.calendar import calendar_page
from pages.login import login
from pages.tutor_dashboard import tutor_dashboard
from pages.signup import signup
from pages.create_course import create_course_page
from pages.mailbox import mailbox_page
from pages.calendar import calendar_page
# aboutfrom pages.about import about

# Force reload
def main_layout():
    """Create the main layout with header and necessary scripts."""
    ui.add_head_html('<link rel="stylesheet" href="https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css">')
    show_header()


@ui.page('/')
def main():
    """Main page layout."""
    from pages.home import home
    from components.footer import show_footer
    main_layout()
    home()
    show_footer()
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
    main_layout()
    calendar_page()
    show_footer()


@ui.page('/courses')
def courses_page():
    """Courses page layout."""
    from pages.courses import courses
    from components.footer import show_footer
    main_layout()
    courses()
    show_footer()


@ui.page('/contact')
def contact_page():
    """Contact page layout."""
    from pages.contact import contact
    from components.footer import show_footer
    main_layout()
    contact()
    show_footer()


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


@ui.page('/mailbox')
def mailbox():
    """Mailbox page layout."""
    main_layout()
    mailbox_page()
    show_footer()


@ui.page('/calendar')
def calendar():
    """Calendar page layout."""
    main_layout()
    calendar_page()
    show_footer()


@ui.page('/create_course')
def create_course():
    """Create course page layout."""
    main_layout()
    create_course_page()
    show_footer()
# @ui.page('/about')
# def about_page():
#     """About page layout."""
#     main_layout()
#     about()
#     show_footer()


app.add_static_files('/assets', 'assets')
ui.run()