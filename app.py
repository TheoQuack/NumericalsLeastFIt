#.venv\Scripts\activate.bat

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np  # Import numpy

st.write("LEAST SQUARE FITTING")

try:
    points = int(st.text_input("How many data points do you want? "))
    xcolumns = []
    ycolumns = []
    x_2columns = []
    xycolumns = []
    sum_of_x = 0
    sum_of_y = 0
    sum_of_x_2 = 0
    sum_of_xy = 0

    for number in range(0, points):
        xcolumns.append(number)  
        ycolumns.append(number)  

    st.write(f"{points} points will be given and placed in the graph")
    st.write("Please give the X and Y values, separated by spaces.")
    st.write("Example:  For 3 points:  1 2 3  for X, and 4 5 6 for Y")
    st.write("")

    xString = st.text_input("X values (space-separated):")
    yString = st.text_input("Y Values (space-separated):")

    x_values = xString.split(" ")
    y_values = yString.split(" ")

    if (len(x_values) != len(y_values)) or (len(x_values) != points) or (
            len(y_values) != points):
        st.write("Please add the appropriate number of values in the text box.")
    else:
        x = 0
        for p in x_values:
            x_2columns.append(float(p) ** 2)
            xycolumns.append(float(y_values[x]) * float(p))
            x += 1

        for p in x_values:
            sum_of_x += float(p)

        for p in y_values:
            sum_of_y += float(p)

        for p in x_2columns:
            sum_of_x_2 += p

        for p in xycolumns:
            sum_of_xy += p

        y_prime = sum_of_y / points
        x_prime = sum_of_x / points

        a = ((points * sum_of_xy) - (sum_of_x * sum_of_y)) / (
                points * (sum_of_x_2) - (sum_of_x) ** 2)

        b = y_prime - (a * x_prime)


        st.write(f"The equation of the line is: y = {a:.2f}x + {b:.2f}")

        df = pd.DataFrame({'X': [float(x) for x in x_values], 'Y': [float(y) for y in y_values]})

        x_min = min(df['X'])
        x_max = max(df['X'])
        x_range = np.linspace(x_min, x_max, 100)  
        y_fit = a * x_range + b
        df_fit = pd.DataFrame({'X': x_range, 'Y': y_fit})

        chart = alt.Chart(df).mark_circle(size=60).encode( 
                x='X',
                y='Y',
                color=alt.value('blue'),  
                tooltip=['X', 'Y']
            ).properties(
                title='Least Squares Fit'  
            ) + alt.Chart(df_fit).mark_line(color='red').encode(  
                x='X',
                y='Y',
                tooltip=['X', 'Y']
            ).interactive()

        st.altair_chart(chart, use_container_width=True) 

except Exception as e:
    pass
