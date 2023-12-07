#  :chart_with_upwards_trend: Analyzing real estate properties using Streamlit

**1. Overview**

:small_blue_diamond:  Analyzing residential properties for sale in Brazil (or any country) can be time-consuming. Usually, there are public reports that track real estate prices but no interactive data visualizations to compare assets across cities. That can be solved by creating an "appreciation of residential properties" app which combine Python programming, statistics and storytelling techniques to make data analysis more accessible!

**1.2 Prerequisites**

:small_blue_diamond:  Familiarity with Python

**1.3 What You'll Learn**

:small_blue_diamond: How to combine Data Visualization and Storytelling to analyze residential properties via stripplots

:small_blue_diamond: How to create a stripplot for analyzing residential properties annual appreciation (over locations)

:small_blue_diamond: How to create a stripplot for analyzing price by squared meter (over locations)

:small_blue_diamond: How to structure and theme your solution into a Streamlit app

**1.4 What You'll Need**

:small_blue_diamond:  A GitHub Account

:small_blue_diamond:  An Python IDE installed, such as VSCode

:small_blue_diamond:  A sample dataset (Brazilian Real Estate Properties Appreciation over 50 cities - data from the first quarter of 2023)

**1.5 What You'll Build**

:small_blue_diamond:  An "appreciation of residential properties" Streamlit app

# 2. Working Principle

For this guide, we turn the audience into the center of attention. To do that, we allow it to select a location from our dataset, which is highlighted during the app's usage. Besides, the app uses a single visual type—the stripplot.

![image](https://github.com/SRUSHTI2493/Analyzing-_properties_using_Streamlit/assets/87080882/1c9c40a0-7269-46cc-ac61-63ff133d1841)

In our scenario, each white dot represents a city. The lowest values are at the bottom, and the highest are at the top. Once the user selects a location, it is highlighted in green, and that allows comparing it with the other cities. Note that you can also provide context by using statistical measures such as:

**The first quartile (Q1):** represents 25% of the data.

**Median:** the middle value that splits the data in half (can also provide a central tendency sense).

**Third quartile (Q3):** represents 75% of the data.

These statistical measures allow the user to compare the situation of the chosen location with the national average and data distribution. Summing up, the user can extract insights from the data, such as identifying opportunities when an appreciation rate is above the national average and the price per square meter is below average. Hence, we will create two stripplots: one for analyzing residential properties annual appreciation and another for analyzing the cost per square meter. This is how the solution will look:

![image](https://github.com/SRUSHTI2493/Analyzing-_properties_using_Streamlit/assets/87080882/830aba6c-29db-4573-93b7-83928084d072)

# 3. Initial Set-Up
In this step, we need to import the required Python modules and set up the Matplotlib layout for storytelling.

Importing Streamlit, Numpy, and Pandas (for arrays and data manipulation) and Matplotlib and Seaborn (for data visualization):


# Modules:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
```

 ### To install the required libraries (numpy, pandas, matplotlib, seaborn, and streamlit), you can use the following commands in your command prompt or terminal:

```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install streamlit

```

**Creating a unique design for your Matplotlib figures and defining the color palette:**

```
# Setup for Storytelling (matplotlib):
plt.rcParams['font.family'] = 'monospace'
plt.rcParams['font.size'] = 8
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['figure.facecolor'] = '#464545' 
plt.rcParams['axes.facecolor'] = '#464545' 
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlecolor'] = 'black'
plt.rcParams['axes.titlesize'] = 9
plt.rcParams['axes.labelcolor'] = 'darkgray'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.edgecolor'] = 'darkgray'
plt.rcParams['axes.linewidth'] = 0.2
plt.rcParams['ytick.color'] = 'darkgray'
plt.rcParams['xtick.color'] = 'darkgray'
plt.rcParams['axes.titlecolor'] = '#FFFFFF'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'darkgray'
plt.rcParams['axes.linewidth'] = 0.85
plt.rcParams['ytick.major.size'] = 0
```

