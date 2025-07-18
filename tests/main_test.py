import uuid
from unittest.mock import MagicMock, patch

import pytest

from pydk_wrapper.py_dk_generated_facade import PyDkGeneratedFacade
from pydk_wrapper.python_exercise_client.models import (
    OfferResponse,
    RegisterProductResponse,
)
from pydk_wrapper.python_exercise_client.models import AuthResponse
from pydk_wrapper.python_exercise_client.types import Response

BEARER_TOKEN = "dummy-token"
DUMMY_ACCESS_TOKEN = "dummy-access-token"
DUMMY_PRODUCT_ID = uuid.uuid4()

PATCH_PREFIX = "pydk_wrapper.py_dk_generated_facade"


def mock_auth_response(*args, **kwargs):
    return Response(
        status_code=201,
        parsed=AuthResponse(access_token=DUMMY_ACCESS_TOKEN),
        content=b"",
        headers={},
    )


def mock_register_response(*args, **kwargs):
    mock = MagicMock(spec=Response)
    mock.status_code = 201
    mock.parsed = RegisterProductResponse(id=DUMMY_PRODUCT_ID)
    return mock


def mock_offers_response(*args, **kwargs):
    mock = MagicMock(spec=Response)
    mock.status_code = 200
    mock.parsed = [OfferResponse(id=DUMMY_PRODUCT_ID, price=1000, items_in_stock=10)]
    return mock


@pytest.fixture
def facade():
    return PyDkGeneratedFacade(bearer_token=BEARER_TOKEN)


@patch(
    PATCH_PREFIX + ".auth_api_v1_auth_post.sync_detailed",
    side_effect=mock_auth_response,
)
def test_fetch_access_token(mock_auth, facade):
    token = facade._fetch_access_token()
    assert token == DUMMY_ACCESS_TOKEN
    mock_auth.assert_called_once()


@patch(
    PATCH_PREFIX + ".auth_api_v1_auth_post.sync_detailed",
    side_effect=mock_auth_response,
)
@patch(
    PATCH_PREFIX + ".register_product_api_v1_products_register_post.sync_detailed",
    side_effect=mock_register_response,
)
def test_register_product(mock_register, mock_auth, facade):
    response = facade.register_product(name="Test", description="Test Desc")
    assert response.status_code == 201
    assert response.parsed.id == DUMMY_PRODUCT_ID
    mock_register.assert_called_once()


@patch(
    PATCH_PREFIX + ".auth_api_v1_auth_post.sync_detailed",
    side_effect=mock_auth_response,
)
@patch(
    PATCH_PREFIX + ".get_offers_api_v1_products_product_id_offers_get.sync_detailed",
    side_effect=mock_offers_response,
)
def test_get_offers_for_product(mock_offers, mock_auth, facade):
    response = facade.get_offers_for_product(product_id=DUMMY_PRODUCT_ID)
    assert response.status_code == 200
    assert len(response.parsed) == 1
    assert response.parsed[0].price == 1000
    mock_offers.assert_called_once()
