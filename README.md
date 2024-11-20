# Streamlit Non-Trivial App

Non-trivial Streamlit application skeleton implemented in a "Streamlit way".
Streamlit is not a typical web framework, so don't try to apply typical web frameworks patterns here.

* No typical request/response cycle
* Very limited routing capabilities
* HTML/CSS/JS abstracted away
* All the code runs on the server side
* Streamlit specific state management

## Implemented features

* Web routing using Streamlit's built-in multi-page navigation capabilities
* Authentication skeleton: unauthenticated users see the login page, authenticated users can log out
* Integration with BigQuery
* Share application state via URL
* Vega-Altair for visualizations
* Modular technical layers within a single domain
* Execute tests from the IDE without additional configuration
* Modern Python build tools: uv, ruff
* Minimal external dependencies
* UI components with shared state management
* Minimal toolbar menu

TODO:

* Redirect to the original page after login
* Integration tests for BigQuery
* Verify load balancer strategies (sticky session)
* Dependabot [dependabot#10039](https://github.com/dependabot/dependabot-core/issues/10039)
* Type checking with [mypy](https://mypy.readthedocs.io/)

## Modules

### `example.services`

* Service layer, business logic only
* Tested with Pytest and mocked infrastructure layer
* Shouldn't import Streamlit API besides `@st.cache`

### `example.infrastructure`

* Infrastructure code only, no application logic
* Tested in realistic environment (Cloud, Test Containers, etc.)
* Shouldn't import Streamlit API
* Acts as anti-corruption layer, for example - expose Pandas DataFrame instead of underlying database API

### `example.ui.pages`

* Application pages
* Tested with Streamlit testing framework and mocked API layer
* Delegate shared UI components to `example.ui.components`
* Delegate logic to `example.service`

### `example.ui.components`

* Shared UI components
* Encapsulates Streamlit state management
* Tested with Streamlit testing framework with small helper wrappers

### `example.utils`

* Utility functions
* Shouldn't import Streamlit API
* Tested within Pytest, no mocking

## Local development

Use VS Code with the following extensions:

* Python
* Ruff

Update environment:

```shell
uv sync
```

Execute the following commands to run the application locally:

```shell
streamlit run app.py
```

Check formatting:

```shell
ruff check
```

Execute tests:

```shell
pytest
```

Show outdated dependencies:

```shell
uv pip list --outdated
```

## Python guides

* Define type hints for all functions
* Skip docstrings, it's better to write small and easy to understand functions
