#!pip install streamlit
import streamlit as st

# Display an image from a file
st.image("GHFE1.JPG", caption="This image is not related to BMI. It is a Grey Headed Fish Eagle by the way", use_column_width=True)

def calculate_bmi(weight, height):
    """Calculate BMI given weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=0.0)
    height = st.number_input("Enter your height (m)", min_value=0.0)

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")
            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.error("Height must be greater than 0.")

if __name__ == "__main__":
    main()
