# Student Performance Predictor

A simple Machine Learning based web application developed using **Flask** and **Scikit-learn** to predict whether a student will **PASS** or **FAIL** based on their **CGPA** and **Attendance**.

---

## Project Overview

The Student Performance Predictor is a beginner-friendly machine learning project that uses a **Decision Tree Classifier** to predict student eligibility. The application provides a simple web interface where users enter student details and receive an instant prediction.

---

## Features

- Simple and user-friendly interface
- Predicts PASS or FAIL
- Decision Tree Machine Learning model
- Flask-based web application
- Model saved as `.pth` file
- Easy to understand and modify

---

## Technologies Used

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS

---

## Project Structure

```
StudentPerformancePredictor/
│
├── student_eligibility.csv
├── model.py
├── app.py
├── student_model.pth
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
├── static/
│     ├── style.css
│     └── images/
│
└── screenshots/
```

---

## Dataset

The dataset contains the following columns:

| Column | Description |
|---------|-------------|
| CGPA | Student CGPA |
| Attendance | Attendance Percentage |
| Eligibility | Yes / No |

Example:

| CGPA | Attendance | Eligibility |
|------|------------|-------------|
| 8.2 | 90 | Yes |
| 5.8 | 62 | No |
| 7.5 | 82 | Yes |

---

## Installation

Clone the repository or download the project.

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Train the Model

Run:

```bash
python model.py
```

After successful training, a file named

```
student_model.pth
```

will be generated.

---

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Input

The application accepts:

- CGPA
- Attendance Percentage

Example:

```
CGPA : 8.5
Attendance : 90
```

---

## Output

The model predicts one of the following:

```
PASS
```

or

```
FAIL
```

---

## Machine Learning Algorithm

This project uses:

- Decision Tree Classifier

Reason for choosing Decision Tree:

- Easy to understand
- Fast training
- Suitable for small datasets
- Good accuracy for simple classification problems

---

## Requirements

```
Flask
pandas
scikit-learn
joblib
```

or install using

```bash
pip install -r requirements.txt
```

---

## Screenshots

Place screenshots of the application inside the `screenshots` folder.

Example:

```
screenshots/
    home.png
    prediction.png
```

---

## Future Enhancements

- Student Login System
- Database Integration
- Multiple Machine Learning Algorithms
- Performance Analytics Dashboard
- Export Prediction Reports
- Improved User Interface

---

## Author

**Kiran K M**

Final Year B.E. (Computer Science)

---

## License

This project is developed for educational purposes.