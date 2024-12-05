# Test_Shape_Coordinates

#### Description
This program is an interactive application built using the **Tkinter** library in Python. It is designed to practice recognizing shapes (squares and rectangles) and their correct coordinates. The goal is to select the correct coordinates for the displayed shape from three given options.

---

#### Features
1. **Shape Display**:
   - The program randomly displays shapes (squares and rectangles) on a canvas.
   - Each shape has predefined coordinates.

2. **Answer Selection**:
   - For each shape, three coordinate options are provided. The user must select the correct one.

3. **Feedback**:
   - After each answer, feedback is displayed:
     - **Correct**: A success message appears for the correct answer.
     - **Incorrect**: An error message appears for the wrong answer.
   - At the end of the test, the program displays the total score:
     - Number of correct and incorrect answers.

4. **Restart Option**:
   - After completing the test, a **Restart** button allows the user to start a new test with a reshuffled set of examples.

---

#### Libraries Used
- **tkinter**: For creating the graphical user interface.
- **random**: For shuffling the examples randomly.

---

#### How to Use
1. **Running the Program**:
   - Ensure you have Python (version 3.x) installed.
   - Save the code to a file, e.g., `shape_coordinates_test.py`.
   - Run the program using the command:
     ```bash
     python shape_coordinates_test.py
     ```

2. **Instructions**:
   - Click on one of the buttons with the coordinate options.
   - After answering, proceed to the next example.
   - At the end of the test, view your score and restart the game if desired.

---

#### Code Structure
- **Global Variables**: Used to track the current example, the number of correct and incorrect answers.
- **Functions**:
  - `reset_game`: Resets the test to the beginning.
  - `draw_example`: Draws the current shape on the canvas.
  - `check_answer`: Validates the selected answer.
  - `update_options`: Updates the text of the answer buttons.

---

#### Examples
- **Square**:
  - Coordinates: (50, 50, 150, 150)
  - Options:
    - (60, 60, 160, 100) - Incorrect (rectangle)
    - (50, 50, 150, 150) - **Correct** (square)
    - (40, 40, 120, 80) - Incorrect (rectangle)

- **Rectangle**:
  - Coordinates: (50, 100, 150, 250)
  - Options:
    - (50, 50, 150, 150) - Incorrect (square)
    - (60, 60, 160, 160) - Incorrect (square)
    - (50, 100, 150, 250) - **Correct** (rectangle)

---

#### Future Improvements
- Support for additional shape types (e.g., circles, triangles).
- Audio feedback for answers.
- Ability to add custom examples via an external file (e.g., JSON).

---


This program is ideal for educational purposes, helping users practice visual recognition and spatial reasoning.
