# Streamlit Non-Trivial Application Skeleton

This project demonstrates how to leverage the built-in power of Streamlit using best software engineering practices and tools. It provides a non-trivial Streamlit application skeleton, showcasing how to effectively utilize Streamlit's capabilities and address its limitations.

![Screenshot](screenshot.png)

## Key Features and Benefits

### Architecture & Build

* Modular, layered architecture for better maintainability
* Separation of concerns for improved testability
* Modern build tools to complete full CI builds in under 30 seconds
* Automated formatter and linter
* Test execution and debugging available directly from VS Code
* Minimal number of external dependencies

### Streamlit Features

* Web routing using built-in multi-page navigation capabilities
* Sample reusable, stateful components
* All pages and components tested with `AppTest`
* Vega-Altair example visualization
* BigQuery integration using the New York Taxi public dataset
* Authentication skeleton, easily replaceable with OAuth
* Application state sharing via URL

### TODO

* Test coverage and integration with [Codecov](https://about.codecov.io)
* Docker image
* Implement BigQuery integration tests
* More visualizations for integrated public dataset
* Integration with external OAuth provider
* Redirect to the original page after login
* Describe load balancer strategies (sticky sessions)
* Automated dependency updates with Dependabot, see [dependabot#10039](https://github.com/dependabot/dependabot-core/issues/10039)
* More sophisticated type checking, see [mypy](https://mypy.readthedocs.io/)

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
