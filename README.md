# Internet Speed Finder

This repository hosts a Flask-based Internet Speed Finder application that provides a simple user interface to test download speed, upload speed, and ping. The application is responsive, has loading animations, and allows users to retry the test without refreshing the page.

## Table of Contents

- [About Project](#about-project)
- [Installation](#installation)
- [Use/Run the Project](#userun-the-project)
- [Features](#features)
- [Contribution](#contribution)
- [License](#license)
- [Contact Me](#contact-me)

## About Project

The Internet Speed Finder is a Flask web application that helps users measure their internet speed, including download speed, upload speed, and ping. It uses the `speedtest-cli` Python library to run the speed tests and displays results on a user-friendly web interface.

## Installation

### Prerequisites

Make sure the following are installed:

1. **Python 3.10.6**: Required to run the Flask application. Download it from [Python's official website](https://www.python.org/downloads/release/python-3106/).
2. **Virtual Environment** (recommended): To keep dependencies isolated.
3. **Flask**: Flask is the Python web framework used to handle requests.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/anandsundaramoorthysa/Internet-Speed-Finder.git
   ```

2. **Navigate to Project Directory**

   ```bash
   cd Internet-Speed-Finder
   ```

3. **Create a Virtual Environment**

   This step is recommended to isolate project dependencies.

   ```bash
   python3 -m venv venv  # On Windows, use `python -m venv venv`
   ```

4. **Activate the Virtual Environment**

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On MacOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages**

   Run the following command to install the necessary dependencies for the project:

   ```bash
   pip install flask speedtest-cli
   ```

6. **Run the Application**

   Start the Flask application by executing the following command in the terminal:

   ```bash
   python app.py
   ```

   After running this command, you can access the application by navigating to `http://127.0.0.1:5000` in your web browser.

## Use/Run the Project

1. **Start the Test**: Click on "Start Test" to begin measuring download speed, upload speed, and ping.
2. **Retry the Test**: After the first results appear, use the "Retry" button to rerun the test.
3. **View Results**: The results will display download speed, upload speed, and ping once the test completes.

### Important Note

Ensure your application has a `/speedtest` endpoint or equivalent to simulate or fetch speed data. You may use mock data if real-time testing APIs aren’t available.

## Features

- **Responsive Design**: Adaptable layout for various devices.
- **Test Speeds**: Measures download speed, upload speed, and ping.
- **Retry Option**: Allows users to rerun the test after results display.
- **Loading Animation**: Displays spinner and animations during the speed test.

## Contribution

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Me

If you have any questions or would like to collaborate, feel free to reach out:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Internet%20Speed%20Finder%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Internet%20Speed%20Finder%20project%20you%20developed.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])
- **LinkedIn**: [Anand's LinkedIn Profile](https://www.linkedin.com/in/anandsundaramoorthysa/)
