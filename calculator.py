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
num1 = st.number_input("Enter first number:", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, step=0.1, format="%.2f")

# Operation selection
operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate result
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    # Display result
    st.success(f"The result is: {result}")
