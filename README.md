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
* Modular technical layers within a single domain
* Execute tests from the IDE without additional configuration
* Minimal external dependencies
* UI components with shared state management
* Minimal toolbar menu

TODO:

* Redirect to the original page after login
* Integration tests for BigQuery
* Put tests in separate directory
* Configure Ruff linter
* Verify load balancer strategies (sticky session)

## Modules

## `example.api`

* API layer, business logic only
* Tested with Pytest and mocked infrastructure layer
* Shouldn't import Streamlit API besides `@st.cache`

## `example.infrastructure`

* Infrastructure code only, no application logic
* Tested in realistic environment (Cloud, Test Containers, etc.)
* Shouldn't import Streamlit API
* Acts as anti-corruption layer, for example - expose Pandas DataFrame instead of underlying database API

## `example.ui.pages`

* Application pages
* Tested with Streamlit testing framework and mocked API layer
* Delegate shared UI components to `example.ui.components`

## `example.ui.components`

* Shared UI components
* Encapsulates Streamlit state management
* Tested with Streamlit testing framework with small helper wrappers

## `example.utils`

* Utility functions
* Shouldn't import Streamlit API
* Tested within Pytest, no mocking

## Python guides

* Define type hints for all functions
* Skip docstrings, it's better to write small and easy to understand functions
