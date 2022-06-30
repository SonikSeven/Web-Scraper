# Web Scraper

This Python project allows users to download and save articles of a specified type from nature.com for the year 2020. The script navigates through the specified number of pages of article listings, filters based on the given article type, and saves the content of each matched article locally in a structured format.

## Features

- Downloads articles published in 2020 from nature.com based on the article type.
- Filters articles by specified type (e.g., News, Research, etc.).
- Saves articles in text format, naming files based on the article titles, stripped of punctuation and spaces replaced with underscores.
- Organizes saved articles into folders corresponding to each page of the search results.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/web-scraper.git
```

2. Navigate to the cloned repository:

```
cd web-scraper
```

3. Create and activate a virtual environment:

```
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies using pip and the requirements.txt file:

```
pip install -r requirements.txt
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

1. When prompted, enter the number of pages you want the script to process.
2. Next, input the type of articles you're interested in downloading (e.g., Research, News).
3. The script will begin processing. Once completed, you can find the saved articles organized in folders by the page number within the current directory.

## License

This project is licensed under the [MIT License](LICENSE.txt).
