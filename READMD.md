# Real Estate Price Estimator 🚀

This project is a web-based **Real Estate Price Estimator** that uses FastAPI as the backend server and Gradio for the user interface. It predicts property prices based on user inputs like lot area, quality, condition, and other features.

---

## Features 🌟
- **Interactive UI**: Built using Gradio for easy interaction.
- **Fast API Server**: Powered by FastAPI to serve predictions.
- **Real-time Predictions**: Get instant price estimates.
- **Theme Switching**: Switch between Light and Dark themes dynamically.
- **Deployable with Uvicorn**: Easily run the project locally or deploy it to a cloud server.

---

## Tech Stack 🛠️
- **Backend**: FastAPI
- **Frontend/UI**: Gradio
- **Machine Learning**: `scikit-learn`, `torch`, `numpy`
- **Server**: Uvicorn

---

## Installation ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/allen-liu-598/real-estate-project
   cd real-estate-project

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    .\venv\Scripts\activate

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt

## Running the Project

1. **Start the FastAPI server with Gradio:**
    ```bash
    uvicorn app.main:app --reload --port 8000

2. **Access the app**: Open the following URL in your browser:
    ```bash
    uvicorn app.main:app --reload --port 8000
