# codeclause_color-detection
```
# Color Detection using Pandas and OpenCV (cv2)

This is a simple Python program that allows you to detect the color of an image by extracting data from a dataset using pandas and OpenCV (cv2) libraries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/color-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd color-detection
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install pandas opencv-python
   ```

## Usage

1. Place your image in the project directory.

2. Update the image path in the code:

   ```python
   img_path = 'your-image.jpg'
   ```

3. Make sure you have a dataset file (CSV format) with color information (name, hex code, RGB values). Update the dataset file name and column names in the code:

   ```python
   data = pd.read_csv('color_dataset.csv', names=['Name', 'Hex', 'R', 'G', 'B'], header=None)
   ```

4. Run the program:

   ```bash
   python color_detection.py
   ```

5. The program will display the image with an interactive window. Double-click on any pixel to detect its color. The color name, RGB values, and a colored rectangle will be displayed on the image.

6. Press the `Esc` key to exit the program.

## Dataset Format

The dataset file should be in CSV format and contain the following columns:
used Data set: https://www.kaggle.com/datasets/nomaanahmeddd/color-codes
- Name: Color name
- Hex: Hex code for the color
- R: Red component value (0-255)
- G: Green component value (0-255)
- B: Blue component value (0-255)

Make sure the dataset file is properly formatted and contains valid color information.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
