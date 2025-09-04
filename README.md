# Intro To Devops Assignment 1
## Steps to be followed to run the app

## (A) Getting Started Locally

### 1. Clone the Repository
```
git clone git@github.com:code-arpit/intro-to-devops-ACEest-Fitness-and-gym-assignment.git
cd intro-to-devops-ACEest-Fitness-and-gym-assignment/src
```

### 2. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Flask Application
```
python app.py
```

## Open http://localhost:5000 in your browser to use the app.

### 5. Running Tests Locally

### All unit tests reside in the `tests/` directory and use Pytest.
```
pytest tests/test.py
```

---

## (B) Docker Usage

### Run the app inside a Docker container for portability and consistency across environments.

### 1. Build the Docker Image
```
docker build -t fitness_test .
```

### 2. Run the Container
```
docker run -p 5000:5000 fitness_test
```

## Open http://localhost:5000 in your browser to use the app.
