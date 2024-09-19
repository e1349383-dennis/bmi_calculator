{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "Streamlit Tryout"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {},
      "outputs": [],
      "source": [
        "#!pip install streamlit\n",
        "import streamlit as st\n",
        "\n",
        "def calculate_bmi(weight, height):\n",
        "    \"\"\"Calculate BMI given weight and height.\"\"\"\n",
        "    bmi = weight / (height ** 2)\n",
        "    return bmi\n",
        "\n",
        "def main():\n",
        "    st.title(\"BMI Calculator\")\n",
        "\n",
        "    weight = st.number_input(\"Enter your weight (kg)\", min_value=0.0)\n",
        "    height = st.number_input(\"Enter your height (m)\", min_value=0.0)\n",
        "\n",
        "    if st.button(\"Calculate BMI\"):\n",
        "        if height > 0:\n",
        "            bmi = calculate_bmi(weight, height)\n",
        "            st.write(f\"Your BMI is: {bmi:.2f}\")\n",
        "            if bmi < 18.5:\n",
        "                st.write(\"You are underweight.\")\n",
        "            elif 18.5 <= bmi < 24.9:\n",
        "                st.write(\"You have a normal weight.\")\n",
        "            elif 25 <= bmi < 29.9:\n",
        "                st.write(\"You are overweight.\")\n",
        "            else:\n",
        "                st.write(\"You are obese.\")\n",
        "        else:\n",
        "            st.error(\"Height must be greater than 0.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.12.2"
    },
    "nav_menu": {},
    "toc": {
      "navigate_menu": True,
      "number_sections": True,
      "sideBar": True,
      "threshold": 6,
      "toc_cell": False,
      "toc_section_display": "block",
      "toc_window_display": False
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
