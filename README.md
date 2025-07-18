# PyDkGenerated

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

A generated Python SDK for Applifting test API with an added minimalistic facade.

* SDK generated using [OpenAPI Python Client Generator](https://github.com/openapi-generators/openapi-python-client)
* Facade class `PyDkGeneratedFacade` encapsulates and simplifies the generated SDK usage

---

## 📁 Table of Contents

* [⚙️ Requirements](#-requirements)
* [🚀 Installation & Usage](#-installation--usage)
* [✅ Running Tests](#-running-tests)
* [🔄 SDK Regeneration](#-sdk-regeneration)
* [📄 License](#-license)

---

## ⚙️ Requirements

* Python 3.10+
* cachetools >= 5.3.3

---

## 🚀 Installation & Usage

### Installation

#### From Local Wheel

```bash
  pip install dist/pydk_generated-0.1.0-py3-none-any.whl
```

#### From GitHub Repository

```bash
  pip install git+https://github.com/suvreal/PyDkGenerated.git
```

### Validate Installation

```bash
  pip list
  pip show pydk-generated
  pip show -f pydk-generated
```

### Import Example

```python
  from pydk_wrapper.py_dk_generated_facade import PyDkGeneratedFacade
  from pydk_wrapper.python_exercise_client.api.default import auth_api_v1_auth_post
```

### Basic Usage Example

```python
  from pydk_wrapper.py_dk_generated_facade import PyDkGeneratedFacade
  
  facade = PyDkGeneratedFacade(bearer_token="YOUR_TOKEN")
  
  product_response = facade.register_product(name="Test", description="Example")
  print(product_response.parsed)
  
  offers_response = facade.get_offers_for_product(product_id=product_response.parsed.id)
  print(offers_response.parsed)
```

> See also: `examples/py_dk_generated_facade_example.py`

---

## ✅ Running Tests

### Install Development Dependencies

```bash
  make install-dev
```

### Move to venv

```bash
  # access venv
   source .venv/bin/activate
   # or to leave 
   deactivate 
```

### Run Tests

```bash
  make test
```

### Run Type Checking

```bash
  make type-check
```

### Run Lint

```bash
  make lint
```

---

## 🔄 SDK Regeneration

Regenerate the SDK if the API specification changes:

```bash
  openapi-python-client generate --url https://python.exercise.applifting.cz/openapi.json
```

For more details, refer to [OpenAPI Python Client: Usage](https://github.com/openapi-generators/openapi-python-client?tab=readme-ov-file#usage)

---

## 📄 License

MIT License © Bartolomej Elias
