# InkLink

InkLink is a modern and intuitive web application designed to provide a transparent platform to showcase your desired links. This repository contains the complete source code, documentation, and resources for the InkLink project.

## Future Features

*   **User Authentication:** Secure user registration and login system.
*   **Dashboard:** A personalized dashboard for every user to manage their content.

## Tech Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, Jinja2
*   **Database:** PostgreSQL
*   **Deployment:** Docker

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.10+
*   pip (Python package installer)
*   Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/DropBombs/inklink.git
    cd inklink
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory by copying the example:
    ```sh
    # You can use 'cp .env.example .env' if you create an example file
    ```
    Then, populate the `.env` file with the necessary configuration, such as:
    ```
    SECRET_KEY='your_super_secret_key'
    DATABASE_URL='your_database_connection_string'
    ```

5.  **Run the application:**
    ```sh
    python run.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Usage

Create your account, use a dashboard to manage your links and display them publicly.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Antonio Pauulo - antoniopauloam@gmail.com

Project Link: [https://github.com/DropBombs/inklink](https://github.com/DropBombs/inklink)
