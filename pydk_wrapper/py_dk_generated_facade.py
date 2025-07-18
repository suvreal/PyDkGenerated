# py_dk_generated_facade.py

import uuid
from typing import Any, Optional, Union

from cachetools.func import ttl_cache
from pydk_wrapper.python_exercise_client.models.auth_response import AuthResponse

from pydk_wrapper.python_exercise_client.models import HTTPValidationError
from pydk_wrapper.python_exercise_client import AuthenticatedClient, Client
from pydk_wrapper.python_exercise_client.api.default import (
    auth_api_v1_auth_post,
    get_offers_api_v1_products_product_id_offers_get,
    register_product_api_v1_products_register_post,
)
from pydk_wrapper.python_exercise_client.models import (
    OfferResponse,
    RegisterProductRequest,
    RegisterProductResponse,
)
from pydk_wrapper.python_exercise_client.types import Response

BASE_URL: str = "https://python.exercise.applifting.cz"
TTL_SECONDS: int = 295
ACCEPTED_STATUS_CODES: set[int] = {200, 201}


class PyDkGeneratedFacade:
    """Minimalistic facade wrapping python_exercise_client SDK."""

    def __init__(
        self,
        bearer_token: str,
        base_url: str = BASE_URL,
    ) -> None:
        self._bearer_token: str = bearer_token
        self._base_url: str = base_url

    @ttl_cache(maxsize=1, ttl=TTL_SECONDS)
    def _fetch_access_token(self) -> str:
        client = Client(self._base_url)
        response: Response[Any | AuthResponse | HTTPValidationError] = (
            auth_api_v1_auth_post.sync_detailed(
                client=client,
                bearer=self._bearer_token,
            )
        )

        if response.status_code not in ACCEPTED_STATUS_CODES or not response.parsed:
            raise ValueError(
                f"Auth failed: {response.status_code} {response.content.decode(errors='replace')}"
            )

        if isinstance(response.parsed, AuthResponse):
            return response.parsed.access_token
        else:
            raise ValueError(f"Auth response invalid: {response.parsed!r}")

    def _create_authenticated_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(
            base_url=self._base_url,
            token=self._fetch_access_token(),
        )

    def register_product(
        self,
        name: str,
        description: str,
        product_id: Optional[uuid.UUID] = None,
    ) -> Response[Union[Any, RegisterProductResponse]]:
        if not product_id:
            product_id = uuid.uuid4()

        product_request = RegisterProductRequest(
            id=product_id,
            name=name,
            description=description,
        )

        with self._create_authenticated_client() as client:
            response = register_product_api_v1_products_register_post.sync_detailed(
                client=client,
                body=product_request,
                bearer=self._fetch_access_token(),
            )

            return response

    def get_offers_for_product(
        self,
        product_id: uuid.UUID,
    ) -> Response[Union[Any, list["OfferResponse"]]]:
        with self._create_authenticated_client() as client:
            response = get_offers_api_v1_products_product_id_offers_get.sync_detailed(
                client=client,
                product_id=product_id,
                bearer=self._fetch_access_token(),
            )

            return response
