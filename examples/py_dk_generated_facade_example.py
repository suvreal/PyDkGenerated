from pydk_wrapper.py_dk_generated_facade import (
    PyDkGeneratedFacade,
)  # checkout your import

"""
Example script demonstrating PyDkGeneratedFacade usage.
Not intended for production use. Replace BEARER_TOKEN with a valid token.
"""

# ADD YOUR BEARER TOKEN
BEARER_TOKEN = "YOUR_BEARER"  # Can be generated at https://python.exercise.applifting.cz/assignment/sdk/


def main():
    facade = PyDkGeneratedFacade(bearer_token=BEARER_TOKEN)

    # PRODUCT REGISTRATION
    product_name = "Test Product"
    product_description = "This is a test product"

    register_response = facade.register_product(
        name=product_name,
        description=product_description,
    )

    if register_response.status_code in [200, 201]:
        print(register_response.parsed)
    else:
        print(register_response)

    # GETTING OFFERS BY PRODUCT ID
    product_id = register_response.parsed.id

    offers_response = facade.get_offers_for_product(product_id=product_id)

    if offers_response.status_code == 200:
        print(offers_response.parsed)
    else:
        print(offers_response)


if __name__ == "__main__":
    main()
