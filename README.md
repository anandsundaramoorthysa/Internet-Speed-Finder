# Internet Speed Finder

This repository hosts a Flask-based Internet Speed Finder application that provides a simple user interface to test download speed, upload speed, and ping. The application is responsive, has loading animations, and allows users to retry the test without refreshing the page.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Demo

[Provide your hosted demo link if available or set up instructions below.]

## Features

- **Responsive Design**: Adaptable layout for various devices.
- **Test Speeds**: Measures download speed, upload speed, and ping.
- **Retry Option**: Allows users to rerun the test after results display.
- **Loading Animation**: Displays spinner and animations during speed test.

## Environment Setup

### Prerequisites

Make sure the following are installed:

1. **Python 3.10.6**: Required to run the Flask application. Download it from [Python's official website](https://www.python.org/downloads/release/python-3106/).
2. **Virtual Environment** (recommended): To keep dependencies isolated.
3. **Flask**: Flask is the Python web framework used to handle requests.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/a1n13a1n13d4/Internet-Speed-Finder.git
   ```

2. **Navigate to Project Directory**

   ```bash
   cd Internet-Speed-Finder
   ```

3. **Create a Virtual Environment**

   This step is recommended to isolate project dependencies. Python 3.10.6 provides a built-in way to create virtual environments.

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

   Make sure to have `Flask` installed. You can install it by using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: If `requirements.txt` isn’t available, manually install Flask:

   ```bash
   pip install flask
   ```

6. **Add Flask as a Dependency (if needed)**

   If you created the `requirements.txt` file, update it with:

   ```bash
   pip freeze > requirements.txt
   ```

## Installation

1. **Set up Static Files**

   Ensure that the required static files, such as `logo.png`, are located in the `static/images` folder. This image will appear as the logo on the application page.

2. **Run the Flask Application**

   Run the following command to start the Flask development server:

   ```bash
   python app.py
   ```

   By default, Flask will start on `http://127.0.0.1:5000`. Open this link in your browser to access the application.

## Usage

1. **Start the Test**: Click on "Start Test" to begin measuring download speed, upload speed, and ping.
2. **Retry the Test**: After the first results appear, use the "Retry" button to rerun the test.
3. **View Results**: The results will display download speed, upload speed, and ping once the test completes.

### Important Note

Ensure your application has a `/speedtest` endpoint or equivalent to simulate or fetch speed data. You may use mock data if real-time testing APIs aren’t available.

## Project Structure

```plaintext
Internet-Speed-Finder/
├── static/
│   ├── css/
│   │   └── style.css           # CSS for project styling
│   └── images/
│       └── logo.png            # Logo displayed on the application
├── templates/
│   └── index.html              # Main HTML template for the application
├── app.py                      # Main Flask application file
├── requirements.txt            # List of project dependencies
└── README.md                   # Project README with setup instructions
```

## Technologies Used

- **HTML5**: For structuring the web page.
- **CSS3**: For styling, including animations and responsiveness.
- **JavaScript**: Adds interactivity and handles front-end logic.
- **Flask**: A lightweight web framework to serve the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Troubleshooting

- **Error: `ModuleNotFoundError: No module named 'flask'`**: Ensure your virtual environment is activated and Flask is installed by running `pip install -r requirements.txt`.
- **Static Files Not Loading**: Verify that the static file paths in HTML are correct and that `logo.png` is in the `static/images` directory.

---

### Contribution

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for new features.
