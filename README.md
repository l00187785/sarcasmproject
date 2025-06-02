# Sarcasm Detector API

This project is a Flask-based sarcasm detection API using a trained scikit-learn model.

---

## Project Structure

/sarcasmproject
│├── app/
│├── main.py
│├── predictor.py
│├── templates/
││ └── index.html
│├── model/
││ ├── vectorizer.pkl
││ └── sarcasm_model.pkl
│└── init.py
│├── Dockerfile
├── docker-compose.yml # Docker Swarm stack definition
├── requirements.txt
├── retrain.py
└── README.md

---

## Prerequisites

- Docker (with Docker Swarm enabled)
- Python 3.9 (for local development/retraining)
- `docker-compose` (optional, for local multi-container testing)

---
## Branching Strategy

- `main`: Production-ready stable code.
- `dev`: Integration branch for tested features.
- `test`: Feature testing and validation occur here. New code and tests are pushed to the test branch, validated, merged to dev, then promoted to main.
- `feature/...`: Feature branches are created from `dev` and merged back into `dev` after testing.

---
## Testing Strategy

Tests are placed in the `tests/` folder and implemented using pytest.
Test Cases (4 Cases) :
<test_model.py> verifies model prediction correctness and handles edge cases such as empty input.
<test_api.py> tests API endpoints ensuring correct responses for valid and invalid inputs.
 <Test Conditions:>
test_model_prediction
test_model_empty_input
test_api_response
test_api_empty_input
Tests are automatically run on every push via GitHub Actions CI workflow to ensure code quality.

---
## Deployment Strategy

This strategy ensures stable main releases and flexible development.
--------

## Setup & Running with Docker Swarm

1. **Build your Docker image:**

docker build -t sarcasm-detector:latest .

2. **Initialize Docker Swarm (if not already):**

docker swarm init

3. **Deploy the service using the Docker Swarm stack file:**

docker stack deploy -c swarm-deploy.yml sarcasm-detector-stack

4. **Verify the service is running:**

docker service ls
5. **Access the app:**

Open your browser and go to:

http://<your-host-ip>:5000

**Notes**
1. The app uses scikit-learn 0.24.2 to avoid version incompatibility issues with the serialized models.

2. Make sure your requirements.txt pins the right versions:

** Requirements.txt file

flask
numpy==1.20.3
scikit-learn==0.24.2
joblib
pandas
pytest

Use retrain.py to retrain and update your model inside the Docker container to ensure environment consistency.

Cleanup
To remove the deployed stack:

docker stack rm sarcasm-detector-stack

Troubleshooting
If you see warnings about model unpickling version mismatch, ensure you are using the same scikit-learn version that was used to create the model (0.24.2).

License
MIT License

