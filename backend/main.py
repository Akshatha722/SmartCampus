from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI(title="SmartCampus API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

create_table()


class Complaint(BaseModel):
    student_name: str
    category: str
    description: str


@app.get("/")
def home():
    return {"message": "SmartCampus Backend is running!"}


@app.post("/complaints")
def submit_complaint(complaint: Complaint):

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO complaints (student_name, category, description)
        VALUES (?, ?, ?)
        """,
        (
            complaint.student_name,
            complaint.category,
            complaint.description
        )
    )

    connection.commit()

    complaint_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Complaint submitted successfully",
        "complaint_id": complaint_id
    }


@app.get("/complaints")
def get_complaints():

    connection = get_connection()

    complaints = connection.execute(
        "SELECT * FROM complaints ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return [dict(complaint) for complaint in complaints]