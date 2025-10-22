from nicegui import ui
from components.footer import footer
from components.header import header
from pages.home import home
from pages.learner_dashboard import dashboard as learner_dashboard
from pages.courses import courses
from pages.contact import contact
from pages.login import login
from pages.tutor_dashboard import tutor_dashboard
from pages.signup import signup


@ui.page('/')
def main():
    """Main page layout."""
    header()
    home()
    footer()


@ui.page('/dashboard')
def dashboard_page():
    """Dashboard page layout."""
    learner_dashboard()


# @ui.page('/about')
# def about_page():
#     """About page layout."""
#     header()
#     about()
#     footer()


@ui.page('/courses')
def courses_page():
    """Courses page layout."""
    header()
    courses()
    footer()


@ui.page('/contact')
def contact_page():
    """Contact page layout."""
    header()
    contact()
    footer()


@ui.page('/login')
def login_page():
    """Login page layout."""
    login()


@ui.page('/tutor-dashboard')
def tutor_dashboard_page():
    """Tutor dashboard page layout."""
    header()
    tutor_dashboard()
    footer()


@ui.page('/signup')
def signup_page():
    """Sign up page layout."""
    signup()


ui.run()
