import pandas as pd
import matplotlib.pyplot as plt

# Importing and Cleaning Data

data = pd.read_csv("./datasets/salary_data.csv")
data = data.drop(["Education Level", "Job Title"], axis=1)
data = data.dropna()

# Linear Regression Model

def gradient_descent(m_current, b_current, values, l):
    m_gradient = 0
    b_gradient = 0

    n = len(values)
    for i in range(n):
        x = values.iloc[i]["Years of Experience"]
        y = values.iloc[i]["Salary"]

        m_gradient += -(2/n) * x * (y - ((m_current * x) + b_current))
        b_gradient += -(2/n) * (y - ((m_current * x) + b_current))

    m = m_current - m_gradient * l
    b = b_current - b_gradient * l

    return m, b

m = 0
b = 0
learning_rate = 0.0001
epochs = 300

for i in range(epochs):
    m, b = gradient_descent(m, b, data, learning_rate)

# Visualizing Model

def draw_lr_model(x, y, scatter_color, line_color, m, b, start_range, end_range):
    plt.scatter(x, y, color=scatter_color, alpha=0.5)
    plt.plot(list(range(start_range, end_range)), [m * x + b for x in range(start_range, end_range)], color=line_color)
    plt.savefig("./visualizations/model.png")

draw_lr_model(data["Years of Experience"], data['Salary'], "blue", "#f2750f", m, b, 0, 26)
