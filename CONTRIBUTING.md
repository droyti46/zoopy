<div align="center"><img src="img/logo.png"></div>

<h1 align="center"> Contributing to ZOOPY 🤗</h1>

<p align="center">Thank you for your interest in contributing to ZOOPY! We welcome contributions from the community to help improve this project.</p>

---

## Getting Started
1. **Fork the Repository**: Start by forking the [ZOOPY repository](https://github.com/droyti46/zoopy) to your GitHub account.
2. **Clone the Repository**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/droyti46/zoopy.git
   ```
3. **Set Up the Development Environment**:
   - Ensure you have Python 3.8 or higher installed.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
4. **Create a Branch**: Create a new branch for your contribution.
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Code Style and Guidelines
To maintain consistency across the codebase, please adhere to the following guidelines:

1. **Python Style**:
   - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
   - Use type hints for function arguments and return values (as seen in the provided code).
   - Use descriptive variable and function names.

2. **Docstrings**:
   - Include docstrings for all public classes, methods, and functions.
   - Follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstring formatting.
   - Example:
     ```python
     def get_all_by(attribute: str,
                    value: str,
                    lang: str,
                    return_dataframe: bool = False
        ) -> list[Animal] | pd.DataFrame:

         '''
         Returns all animals with same attribute.

         Parameters:
             attribute (str): attribute for filter (e.g. "kingdom", "class", "order")
             value (str): value of attribute
             lang (str): language of returned data
             return_dataframe (bool): returns pandas.Dataframe if True else list[Animal]

         Examples:
             >>> from zoopy import animal
             >>> chordates = animal.get_all_by('phylum', 'Хордовые')
             >>> chordates[0].display()
         '''
     ```

3. **Imports**:
   - Group imports in the following order:
     1. Standard library imports.
     2. Third-party library imports.
     3. Local application/library imports.
   - Example:
     ```python
     import os
     import time
     
     import pandas as pd
     from IPython.display import display, HTML
     from tqdm import tqdm

     from zoopy import data
     ```

4. **Error Handling**:
   - Include appropriate error handling to ensure robustness.

---

## Documentation
1. **Update Documentation**: If your contribution adds new features or changes existing behavior, update the relevant [documentation](docs/).
2. **Inline Comments**: Use inline comments to explain complex logic or decisions.
Example:
```python
# Load data
self.__data_loader = data.DataLoader()
self.__series: pd.Series = self.__data_loader.get_animal(
    animal_name,
    lang,
    accurate
)
```

---


## Submitting a Pull Request
1. **Commit Your Changes**: Commit your changes with clear and descriptive commit messages.
   ```bash
   git commit -m "your feature description"
   ```
2. **Push Your Changes**: Push your changes to your forked repository.
   ```bash
   git push origin feature/your-feature-name
   ```
3. **Create a Pull Request**:
   - Go to the [ZOOPY repository](https://github.com/droyti46/zoopy) and create a pull request from your branch.
   - Provide a detailed description of your changes, including the purpose and any relevant context.

---

## Reporting Issues
If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub Issues page](https://github.com/droyti46/zoopy/issues). Include the following information:
- A clear description of the issue.
- Steps to reproduce the issue.
- Expected vs. actual behavior.
- Screenshots or error logs (if applicable).

---

<p align="center">Thank you for contributing to ZOOPY! Your efforts help make this project better for everyone 💖</p>