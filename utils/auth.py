from typing import Optional, Tuple
import requests
from nicegui import app, ui
from .api import base_url

# --- Safe session helpers for BridgeLMS (Learners & Tutors) ---

def _ensure_session_storage():
    """Ensure user storage exists (no-op for NiceGUI built-in storage)."""
    pass


def set_session(token: Optional[str], role: Optional[str], user_id: Optional[str], username: Optional[str] = None) -> None:
    """Set session details for the logged-in learner or tutor."""
    try:
        app.storage.user['token'] = token
        app.storage.user['role'] = role
        app.storage.user['user_id'] = user_id
        app.storage.user['username'] = username
    except RuntimeError:
        pass


def clear_session() -> None:
    """Clears all user session data."""
    try:
        app.storage.user.clear()
    except RuntimeError:
        pass


def get_role() -> Optional[str]:
    """Retrieve current user’s role (learner or tutor)."""
    try:
        return app.storage.user.get('role')
    except RuntimeError:
        return None


def get_user_id() -> Optional[str]:
    """Retrieve the currently logged-in user’s ID."""
    try:
        return app.storage.user.get('user_id')
    except RuntimeError:
        return None


def get_token() -> Optional[str]:
    """Retrieve the current session token."""
    try:
        return app.storage.user.get('token')
    except RuntimeError:
        return None


def is_tutor() -> bool:
    """Check if current user is a tutor."""
    return get_role() == 'tutor'


def is_learner() -> bool:
    """Check if current user is a learner."""
    return get_role() == 'learner'


def require_tutor() -> bool:
    """Ensure only tutors can access certain pages."""
    if not is_tutor():
        ui.notify('Tutor access required. Please sign in as a tutor.', type='warning')
        ui.navigate.to('/login')
        return False
    return True


# --- Backend API auth helpers ---

def api_signup(username: str, email: str, password: str, role: str, phone: str, bio: str) -> Tuple[bool, str, Optional[str], Optional[str]]:
    """
    Attempts to register a new learner or tutor.
    Returns (success, message, token, user_id).
    """
    try:
        payload = {
            'username': username,
            'email': email,
            'password': password,
            'role': role,
            'phone': phone,
            'bio': bio,
        }
        r = requests.post(f"{base_url}/auth/signup", json=payload, timeout=15)

        if 200 <= r.status_code < 300:
            data = r.json()
            token = data.get('token') or data.get('access_token')
            user_id = (data.get('user') or {}).get('id') or data.get('user_id')
            return True, 'Account successfully created', token, user_id
        else:
            return _local_signup(username, email, password, role, phone, bio)
    except Exception:
        # Fallback to local mock
        return _local_signup(username, email, password, role, phone, bio)


def _local_signup(username: str, email: str, password: str, role: str, phone: str, bio: str) -> Tuple[bool, str, Optional[str], Optional[str]]:
    """Fallback local mock signup."""
    try:
        from .frontend_store import create_user, hash_password
        user = create_user(username, email, password, role, phone, bio)
        token = f"mock_token_{user['id']}"
        return True, 'Account created locally', token, user['id']
    except Exception as e:
        return False, f"Signup failed: {e}", None, None


def api_login(email: str, password: str) -> Tuple[bool, str, Optional[str], Optional[str], Optional[str], Optional[str]]:
    """
    Attempts to log in a learner or tutor.
    Returns (success, message, token, user_id, role, username).
    """
    try:
        payload = {'email': email, 'password': password}
        r = requests.post(f"{base_url}/auth/login", json=payload, timeout=15)

        if 200 <= r.status_code < 300:
            data = r.json()
            token = data.get('token') or data.get('access_token')
            user = data.get('user') or {}
            user_id = user.get('id') or data.get('user_id')
            role = user.get('role') or data.get('role')
            username = user.get('username') or data.get('username')
            return True, 'Login successful', token, user_id, role, username
        else:
            return _local_login(email, password)
    except Exception:
        return _local_login(email, password)


def _local_login(email: str, password: str) -> Tuple[bool, str, Optional[str], Optional[str], Optional[str], Optional[str]]:
    """Fallback local mock login."""
    try:
        from .frontend_store import authenticate_user
        user = authenticate_user(email, password)
        if user:
            token = f"mock_token_{user['id']}"
            return True, 'Login successful (local)', token, user['id'], user['role'], user['username']
        else:
            return False, 'Invalid email or password', None, None, None, None
    except Exception as e:
        return False, f"Login failed: {e}", None, None, None, None




# from typing import Optional, Tuple
# import requests
# from nicegui import app, ui
# from .api import base_url


# # --- Safe session helpers ---

# def _ensure_session_storage():
#     # This function is now a no-op, as the checks are done in each session function
#     pass

# def set_session(token: Optional[str], role: Optional[str], user_id: Optional[str], name: Optional[str] = None) -> None:
#     try:
#         app.storage.user['token'] = token
#         app.storage.user['role'] = role
#         app.storage.user['user_id'] = user_id
#         app.storage.user['name'] = name
#     except RuntimeError:
#         # Storage not initialized yet, ignore silently
#         pass

# def clear_session() -> None:
#     try:
#         app.storage.user.clear()
#     except RuntimeError:
#         # Storage not initialized yet, ignore silently
#         pass

# def get_role() -> Optional[str]:
#     if not hasattr(app, 'storage'):
#         return None
#     try:
#         return app.storage.user.get('role')
#     except RuntimeError:
#         return None

# def get_user_id() -> Optional[str]:
#     if not hasattr(app, 'storage'):
#         return None
#     try:
#         return app.storage.user.get('user_id')
#     except RuntimeError:
#         return None

# def get_token() -> Optional[str]:
#     if not hasattr(app, 'storage'):
#         return None
#     try:
#         return app.storage.user.get('token')
#     except RuntimeError:
#         return None

# def is_learner() -> bool:
#     return get_role() == 'learner'
# def is_tutor() -> bool:
#     return get_role() == 'tutor'

# def is_user() -> bool:
#     return get_role() == 'user'

# def require_learner() -> bool:
#     if not is_learner():
#         ui.notify('Vendor access required. Please sign in as a vendor.', type='warning')
#         ui.navigate.to('/sign-in')
#         return False
#     return True

# def require_tutor() -> bool:
#     if not is_tutor():
#         ui.notify('Vendor access required. Please sign in as a vendor.', type='warning')
#         ui.navigate.to('/sign-in')
#         return False
#     return True


# # --- Backend API auth helpers ---
# def api_signup(username: str, email: str, password: str, role: str, phone: str, bio: str) -> Tuple[bool, str, Optional[str], Optional[str]]:
#     """
#     Attempts to sign up a user. Falls back to local mock system if remote API fails.
#     Returns (success, message, token, user_id).
#     """
#     return _local_signup(username, email, password, role,phone,bio)


# def _local_signup(username: str, email: str, password: str, role: str, phone: str, bio: str) -> Tuple[bool, str, Optional[str], Optional[str]]:
#     """
#     Local mock signup implementation.
#     """
#     try:
#         from .frontend_store import create_user
#         user = create_user(username, email, password, role, phone, bio)
#         # Generate a mock token
#         token = f"mock_token_{user['id']}"
#         return True, 'Account created (local)', token, user['id']
#     except Exception as e:
#         return False, f"Signup failed: {e}", None, None


# def api_login(email: str, password: str) -> Tuple[bool, str, Optional[str], Optional[str], Optional[str], Optional[str]]:
#     """
#     Attempts to log in. Falls back to local mock system if remote API fails.
#     Returns (success, message, token, user_id, role, name).
#     """
#     try:
#         payload = {
#             'email': email,
#             'password': password,
#         }
#         r = requests.post(f"{base_url}/auth/login", json=payload, timeout=15)
#         if 200 <= r.status_code < 300:
#             data = r.json()
#             token = data.get('token') or data.get('access_token')
#             user = data.get('user') or {}
#             user_id = user.get('id') or data.get('user_id')
#             role = user.get('role') or data.get('role')
#             name = user.get('name') or data.get('name')
#             return True, 'Logged in', token, user_id, role, name
#         else:
#             # Fallback to local mock system if remote API fails
#             return _local_login(email, password)
#     except Exception as e:
#         # Fallback to local mock system if remote API fails
#         return _local_login(email, password)

