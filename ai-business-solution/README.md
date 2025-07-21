# AI Business Solution Deployment

This project demonstrates an end-to-end AI workflow including EDA, training, model comparison, unit testing, API deployment, monitoring, and Docker containerization.

## 📦 Setup

```bash
pip install -r requirements.txt
```

## 🚀 Run API
```bash
uvicorn api.app:app --reload
```

## ✅ Run Tests
```bash
python tests/run_tests.py
```

## 🐳 Docker
```bash
docker build -t ai-solution .
docker run -p 8080:8080 ai-solution
```
