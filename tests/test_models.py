import pytest
from app.models import User, Link

# User tests
# Username tests
def test_create_user_with_long_username():
    """Test for user creation with long username"""
    user = User()
    invalid_username = 'a' * 81
    with pytest.raises(ValueError, match="Username cannot exceed 80 characters."):
        user.set_username(invalid_username)

def test_create_user_with_short_username():
    """Test for user creation with short username"""
    user = User()
    invalid_username = ''
    with pytest.raises(ValueError, match="Username must be at least 3 characters long."):
        user.set_username(invalid_username)

def test_create_user_with_int_username():
    """Test for user creation where username is an integer"""
    user = User()
    invalid_username = -1
    with pytest.raises(ValueError, match="Username must be a string."):
        user.set_username(invalid_username)

def test_create_user_with_bool_username():
    user = User()
    invalid_username = True
    with pytest.raises(ValueError, match="Username must be a string."):
        user.set_username(invalid_username)

# Email tests

def test_create_user_with_long_email():
    """Test for user creation with long email"""
    user = User()
    invalid_email = 'a' * 121
    with pytest.raises(ValueError, match="Email cannot exceed 120 characters."):
        user.set_email(invalid_email)

def test_create_user_with_short_email():
    """Test for user creation with short email"""
    user = User()
    invalid_email = ''
    with pytest.raises(ValueError, match="Email must be at least 3 characters long."):
        user.set_email(invalid_email)

def test_create_user_with_invalid_email_format():
    """Test for user creation with wrong email formatting"""
    user = User()
    invalid_email = 'invalid_email.com'
    with pytest.raises(ValueError, match="Invalid email address format."):
        user.set_email(invalid_email)

def test_create_user_with_valid_data():
    """Test for a valid user creation with name, email and password"""
    user = User()
    user.set_username("Stratego")
    user.set_email("stratego@email.com")
    user.set_password("a_strong_password")
    assert user.username == "Stratego"
    assert user.email == "stratego@email.com"
    assert user.password_hash != "a_strong_password" # Never store plain text passwords

# Link tests
# Title tests

def test_create_link_with_long_title():
    """Test for link creation wth long title"""
    link = Link()
    invalid_title = 'a' * 201
    with pytest.raises(ValueError, match="Title cannot exceed 200 characters."):
        link.set_title(invalid_title)

def test_create_link_with_short_title():
    """Test for link creation with short title"""
    link = Link()
    invalid_title = ''
    with pytest.raises(ValueError, match="Title must be at least 2 characters long."):
        link.set_title(invalid_title)

def test_create_link_with_int_title():
    """Test for link creation where title is an integer"""
    link = Link()
    invalid_title = -1
    with pytest.raises(ValueError, match="Title must be a string."):
        link.set_title(invalid_title)

def test_create_link_with_bool_title():
    """Test for link creation where title is a boolean"""
    link = Link()
    invalid_title = True
    with pytest.raises(ValueError, match="Title must be a string."):
        link.set_title(invalid_title)

# URL tests

def test_create_link_with_long_url():
    """Test for link creation with long url"""
    link = Link()
    invalid_url = 'a' * 501
    with pytest.raises(ValueError, match="URL cannot exceed 500 characters."):
        link.set_url(invalid_url)

def test_create_link_with_short_url():
    """Test for link creation with short url"""
    link = Link()
    invalid_url = ''
    with pytest.raises(ValueError, match="URL must be at least 2 characters long."):
        link.set_url(invalid_url)

def test_create_link_with_invalid_url_format():
    """Test for link creation with invalid url formatting"""
    link = Link()
    invalid_url = 'htps://google.com'
    with pytest.raises(ValueError, match="Invalid URL format."):
        link.set_url(invalid_url)

def test_create_link_with_int_url():
    """Test for link creation where url is an integer"""
    link = Link()
    invalid_url = -1
    with pytest.raises(ValueError, match="URL must be a string."):
        link.set_url(invalid_url)

def test_create_link_with_bool_url():
    """Test for link creation where url is a boolean"""
    link = Link()
    invalid_url = True
    with pytest.raises(ValueError, match="URL must be a string."):
        link.set_url(invalid_url)
    
def test_create_link_with_valid_data():
    """Test for a valid link creation with title and url"""
    link = Link()
    link.set_title("Stratego")
    link.set_url("https://google.com")
    assert link.title == "Stratego"
    assert link.url == "https://google.com"
