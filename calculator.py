import streamlit as st

# Function definitions for calculations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Streamlit app
st.title("Simple Calculator App")

# Instructions
st.write("### Perform basic calculations (Addition, Subtraction, Multiplication, Division)")

# User input for two numbers
num1 = st.number_input("Enter first number:", value=0.0, step=0.
