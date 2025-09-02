from app.models import User

# Change this test
def test_create_user_with_valid_data():
    """Test for a valid user creation with name, email and password"""
    user = User()
    user.set_username("Stratego")
    user.set_email("stratego@email.com")
    user.set_password("a_strong_password")
    assert user.username == "Stratego"
    assert user.email == "stratego@email.com"
    assert user.password_hash != "a_strong_password" # Never store plain text passwords
