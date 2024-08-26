import streamlit as st

# Set up the title and description
st.title("🎈 My New App")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Create a simple UI with a text input and a button
st.header("User Input Section")

# Text input for the user's name
name = st.text_input("Enter your name:")

# Button to submit the input
if st.button("Say Hello"):
    if name:
        st.write(f"Hello, {name}! 🎉")
    else:
        st.write("Please enter your name to receive a greeting.")

# You can add more UI elements below as needed
st.sidebar.header("Sidebar Section")
st.sidebar.write("This is the sidebar where you can add additional information or controls.")

# Example of a slider in the sidebar
age = st.sidebar.slider("Select your age", 0, 100, 25)
st.sidebar.write(f"You selected age: {age}")

# Example of displaying a chart
import numpy as np
import matplotlib.pyplot as plt

st.header("Sample Chart")

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sine Wave")

# Display the plot in Streamlit
st.pyplot(fig)
