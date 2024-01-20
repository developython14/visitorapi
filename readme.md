# Portfolio Visitor Statistics

This Django project allows you to count visitors and gather location statistics for your portfolio.

## Table of Contents:

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Counts and logs visitors to your portfolio.
- Gathers location statistics based on visitor IP addresses.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-portfolio.git
    cd your-portfolio
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Django project:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser  # Create an admin user
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the Django admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) to view visitor statistics.

## Usage

1. Embed the provided tracking code in your portfolio pages to start counting visitors:

    ```html
    <!-- Insert this code in your portfolio pages -->
    <script>
        // Your tracking code here
    </script>
    ```

2. Visit the Django admin interface to view visitor statistics and location data.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
