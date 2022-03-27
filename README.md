# .env

```
SECRET_KEY=fb0c812aa3cf11b55357eae4142f3ae348d48074ca2c5a0c1616ea43f76039c9
ALGORITHM=HS256
DATABASE_URL=mysql+mysqlconnector://root:@localhost:3306/echamber
URL_ONE=http://localhost:8000
URL_TWO=https://localhost:8000
```

# installation

```
pip3 install -r requirements.txt
```

# migration

```
cd src/
alembic upgrade head
```

# Run application

```
cd src/
python3 main.py
```