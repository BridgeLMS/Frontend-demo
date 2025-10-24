from typing import Dict, List, Optional, Any
from nicegui import app
import hashlib
import uuid

LEARNERS_KEY = 'mock_learners'
TUTORS_KEY = 'mock_tutors'
# COURSES_KEY = 'mock_courses'


def _ensure_init():
    store = app.storage.general

    # Initialize mock learners and tutors if they don't exist
    if LEARNERS_KEY not in store or TUTORS_KEY not in store:
        pwd = hashlib.sha256('123456'.encode()).hexdigest()

        store[LEARNERS_KEY] = [
            {
                'id': 'l1',
                'name': 'Demo Learner',
                'email': 'learner@example.com',
                'password': pwd,
                'role': 'learner',
                'phone': '+233540000001',
                'bio': 'A sample learner exploring online courses.'
            }
        ]

        store[TUTORS_KEY] = [
            {
                'id': 't1',
                'name': 'Demo Tutor',
                'email': 'tutor@example.com',
                'password': pwd,
                'role': 'tutor',
                'phone': '+233540000002',
                'bio': 'A professional tutor specializing in Python programming.'
            }
        ]

    # Seed example courses
    # if COURSES_KEY not in store:
    #     store[COURSES_KEY] = [
    #         {
    #             'id': 'c1',
    #             'title': 'Introduction to Web Development',
    #             'description': 'Learn HTML, CSS, and JavaScript from scratch.',
    #             'tutor_id': 't1',
    #             'price': 120.00,
    #             'enrolled_learners': [],
    #             'image': ''
    #         },
    #         {
    #             'id': 'c2',
    #             'title': 'Data Analysis with Python',
    #             'description': 'A hands-on course for data cleaning, analysis, and visualization.',
    #             'tutor_id': 't1',
    #             'price': 150.00,
    #             'enrolled_learners': [],
    #             'image': ''
    #         },
    #     ]


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------- USERS --------------------

def create_user(name: str, email: str, password: str, role: str, phone: str, bio: str) -> Dict[str, Any]:
    """Register a new learner or tutor."""
    _ensure_init()

    key = LEARNERS_KEY if role == 'learner' else TUTORS_KEY
    users: List[Dict[str, Any]] = app.storage.general[key]

    if any(u['email'].lower() == email.lower() for u in users):
        raise ValueError('Email already registered')

    new_user = {
        'id': str(uuid.uuid4()),
        'name': name,
        'email': email,
        'password': hash_password(password),
        'role': role,
        'phone': phone,
        'bio': bio,
    }

    users.append(new_user)
    app.storage.general[key] = users
    return new_user


def authenticate_user(email: str, password: str) -> Optional[Dict[str, Any]]:
    """Authenticate either a learner or a tutor."""
    _ensure_init()
    h = hash_password(password)

    for key in [LEARNERS_KEY, TUTORS_KEY]:
        users: List[Dict[str, Any]] = app.storage.general[key]
        for u in users:
            if u['email'].lower() == email.lower() and u['password'] == h:
                return u
    return None


# # -------------------- COURSES --------------------

# def list_courses() -> List[Dict[str, Any]]:
#     """Return all available courses."""
#     _ensure_init()
#     return list(app.storage.general[COURSES_KEY])


# def get_course(course_id: str) -> Optional[Dict[str, Any]]:
#     """Retrieve a single course by its ID."""
#     _ensure_init()
#     for course in app.storage.general[COURSES_KEY]:
#         if str(course['id']) == str(course_id):
#             return course
#     return None


# def create_course(title: str, description: str, tutor_id: str, price: float, image: str = '') -> Dict[str, Any]:
#     """Create a new course by a tutor."""
#     _ensure_init()
#     courses: List[Dict[str, Any]] = app.storage.general[COURSES_KEY]

#     new_course = {
#         'id': str(uuid.uuid4()),
#         'title': title,
#         'description': description,
#         'tutor_id': tutor_id,
#         'price': price,
#         'enrolled_learners': [],
#         'image': image,
#     }

   