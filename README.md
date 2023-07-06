# Color Detection using Pandas and OpenCV (cv2)

This simple Python program allows you to detect the color of an image by extracting data from a dataset using pandas and OpenCV (cv2) libraries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nomaanahmedd/codeclause_color-detection.git
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

5. The program will display the image with an interactive window—Double-click on any pixel to detect its color. The color name, RGB values, and a colored rectangle will be displayed on the image.

6. Press the `Esc` key to exit the program.

## Dataset
Dataset: https://www.kaggle.com/datasets/nomaanahmeddd/color-codes

The dataset file is in CSV format and contains the following columns containing more than 1000 color codes and their names:
- Name: Color name
- Hex: Hex code for the color
- R: Red component value 
- G: Green component value 
- B: Blue component value

while creating your own dataset make sure the dataset file is formatted correctly and contains valid color information.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
