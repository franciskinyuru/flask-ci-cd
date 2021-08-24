from app import index


def test_index():
    assert index() == "Flask CI/CD"
