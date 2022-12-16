
import pytest
from fastapi import HTTPException
from routes.user import user_routes
from fastapi.testclient import TestClient

client = TestClient(user_routes)


def test_get_user_not_header():
    with pytest.raises(HTTPException) as excinfo:
        client.get("/users/754c776d-d869-4c7a-874d-04afccd9d317")
    assert excinfo.value.status_code == 401
