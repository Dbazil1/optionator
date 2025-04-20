# Optionator

Optionator is a simple web application that helps you make decisions by randomly selecting from a list of options you provide. It's perfect for when you can't decide between multiple choices!

## Features

- Add multiple options to your decision pool
- View all your options with their corresponding numbers
- Get a random selection from your options with a single click
- Clean and intuitive user interface
- Persistent option storage during your session

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run option_selector.py
   ```

2. The application will open in your default web browser

3. To use Optionator:
   - Enter your options in the text input field
   - Click "Add Option" to add each option to your list
   - View all your options in the numbered list
   - Click "Let Optionator Decide" to get a random selection
   - The selected option will be displayed with a success message

## Example

Let's say you can't decide what to have for dinner. You could:
1. Add options like "Pizza", "Sushi", "Burgers", "Tacos"
2. Click "Let Optionator Decide"
3. Get a random suggestion from your list

## Requirements

- Python 3.7+
- Streamlit 1.32.0

## License

This project is open source and available under the MIT License. 