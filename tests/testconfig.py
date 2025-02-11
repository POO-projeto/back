import pytest

from testapp import create_app, db


@pytest.fixture(scope="module")
def app():
    app = create_app("sqlite://")
    app.config.update({"TEST": True, "DEBUG": False})

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
