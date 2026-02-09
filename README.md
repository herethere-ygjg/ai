# HereThere AI

추천시스템 구현을 위한 HereThere AI 레포지토리입니다.


---


## 기술 스택

- Python 3.10+
- Scikit-Learn 
- FastAPI + Uvicorn
- Pydantic
- Airflow


---


## 프로젝트 실행 방법

### 1. 프로젝트 클론

```bash
git clone https://github.com/herethere-ygjg/ai.git
cd ai
```

### 2. 종속성(requirements.txt) 설치 (anaconda based)

```bash
conda create ygjg-ai
conda activate ygjg-ai

pip install -r requirements.txt
```


---


## 프로젝트 구조

```
ai/
├─ requirements.txt
├─ .env
├─ src/
│   └─ main/
│       ├─ config/           
│       ├─ domain/           
│       ├─ repository/      
│       ├─ service/          
│       ├─ pipeline/         
│       └─ airflow/
├─ docker/                
│   └─ Dockerfile                 
├─ tests/
├─ models/                   
└─ data/         

 ```