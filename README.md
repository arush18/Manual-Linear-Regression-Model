# Manual Linear Regression Model

A simple implementation of **Linear Regression** using **Gradient Descent** in Python without using Scikit-Learn. The dataset used is taken from Kaggle.

## Features
- Reads and cleans salary dataset.
- Implements **Gradient Descent** from scratch.
- Trains the model to predict salary based on **Years of Experience**.
- Saves the visualization of the regression model.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/arush18/Manual-Linear-Regression-Model
   cd Manual-Linear-Regression-Model
   ```
2. Install dependencies:
   ```sh
   pip install pandas matplotlib.pyplot
   ```
3. Place the dataset in the `datasets` directory.

## Usage
Run the script to train the model and save the visualization:
```sh
python main.py
```
The output graph will be saved in the `visualizations` directory as `model.png`.

## Project Structure
```
/manual-linear-regression-model
│── /datasets/
│── ── salary_data.csv
│── /src/
│── ── main.py
│── /visualizations/
│── ── model.png
│── .gitignore
│── README.md
│── LICENSE.md
```

## Dataset
The dataset used in this project is taken from Kaggle. Ensure the CSV file is placed in the `datasets` directory.

## License
[MIT License](https://github.com/arush18/Manual-Linear-Regression-Model/blob/main/LICENSE.md)

