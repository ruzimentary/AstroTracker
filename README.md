AstroTracker

Author: Andrew Wanyonyi Kipruto
Description

AstroTracker is a command-line interface (CLI) application designed to assist astronomers in planning and logging their observations. It allows users to manage celestial objects, events, observations, and weather conditions related to their stargazing activities.

The application provides functionalities such as:

    Adding, editing, and deleting users
    Managing celestial objects, including adding new objects and updating existing ones
    Creating and editing events, such as meteor showers or eclipses, with details on visibility location and dates
    Logging observations with notes and optional timestamps
    Planning observation nights by viewing celestial events and weather conditions

AstroTracker aims to simplify the process of organizing and documenting astronomical observations, making it easier for users to track their stargazing activities over time.
Project Setup Instructions

To set up the AstroTracker project, follow these steps:

    Clone the repository: git clone https://github.com/ruzimentary/astrotracker.git
    Navigate to the project directory: cd astrotracker
    Install the required dependencies: pip install -r requirements.txt
    Run the CLI: python astrotracker.py

Installation Requirements

    Python 3.x
    SQLite (optional, for local database)

Installation Instructions

To install AstroTracker, follow these steps:

    Clone the repository: git clone https://github.com/ruzimentary/astrotracker.git
    Navigate to the project directory: cd astrotracker
    Install the required dependencies: pip install -r requirements.txt

Deployment

AstroTracker can be deployed locally or on a server. To deploy locally, follow the installation instructions. For server deployment, ensure the server meets the installation requirements and deploy the application using your preferred method.
Usage

After setting up the project, you can use the CLI commands to interact with the application. For example, to add a new user, use the following command:

css

python astrotracker.py add_user --username JohnDoe --email johndoe@example.com --location New York

Bugs

If you encounter any bugs or issues while using AstroTracker, please report them on the project's GitHub issues page: GitHub Issues
License

This project is licensed under the MIT License. See the LICENSE file for details.