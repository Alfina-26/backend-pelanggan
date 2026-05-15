from database import SessionLocal
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

db = SessionLocal()

existing = db.query(User).filter(User.username == "admin").first()
if existing:
    print("Admin sudah ada!")
else:
    admin = User(
        username="admin",
        hashed_password=pwd_context.hash("admin123"),
        role="admin"
    )
    db.add(admin)
    db.commit()
    print("Admin berhasil dibuat! Login dengan: admin / admin123")

db.close()