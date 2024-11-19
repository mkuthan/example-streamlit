# Streamlit Non-Trivial App

Non-trivial Streamlit application skeleton implemented in a "Streamlit way".
Streamlit is not a typical web framework, so don't try to apply typical web frameworks patterns here.

* No typical request/response cycle
* Very limited routing capabilities
* HTML/CSS/JS abstracted away
* All the code runs on the server side
* Streamlit specific state management

## Implemented features

* Web routing within Streamlit built-in multi-page capabilities for navigation
* Authentication skeleton, unauthenticated user gets login page, authenticated user is able to log out
* Application state can be shared via URL
* Modularity of technical layers within a single domain
* Tests execution from IDE without additional configuration
* UI components with shared state management
* Minimal toolbar menu

TODO:

* Redirect to the original page after login

## Modules

## `example.api`

* API layer, business logic only
* Tested withing Pytest (TODO: how to avoid mocking infrastructure?) 
* Shouldn't import Streamlit API

## `example.infrastructure`

* Infrastructure code only, no application logic
* Tested in realistic environment (Cloud, Test Containers, etc.)
* Shouldn't import Streamlit API
* Acts as anti-corruption layer, for example - expose Pandas DataFrame instead of underlaying database API

## `example.ui`

* Application pages
* Tested with Streamlit testing framework (TODO: how to avoid mocking api/infrastructure?)
* Delegate shared UI components to `example.ui.components`

## `example.ui.components`

* Shared UI components
* Encapsulates Streamlit state management
* Tested with Streamlit testing framework (TODO: how to do it?)

## `example.utils`

* Utility functions
* Shouldn't import Streamlit API
* Tested within Pytest, no mocking

## Python guides

* Define type hints for all functions
* Skip docstrings, it's better to write small and easy to understand functions
