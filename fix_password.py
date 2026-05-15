from database import SessionLocal
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

db = SessionLocal()

for username, password in [("admin", "admin123"), ("developer", "developer123")]:
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.hashed_password = pwd_context.hash(password)
        db.commit()
        print(f"Password {username} berhasil diupdate!")
    else:
        print(f"{username} tidak ditemukan!")

db.close()