from fastapi import FastAPI
from fastapi import HTTPException
import schemas
from database import *

app = FastAPI()

students_collection = database["students"]
teachers_collection = database["teacher"]
lessons_collection = database["lesson"]

@app.post("/RegStu", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate):
    # بررسی تکراری بودن رکورد دانشجو
    existing_student = await students_collection.find_one({"stid": student.stid})
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with the same STID already exists")

    # ایجاد رکورد دانشجو با استفاده از اطلاعات ارسال شده
    created_student = await students_collection.insert_one(student.dict())
    # بازگرداندن رکورد ایجاد شده
    return student


@app.get("/RegStu/{student_stid}", response_model=schemas.StudentRead)
async def read_student(student_stid: str):
    # جستجوی دانشجو بر اساس student_stid
    student = await students_collection.find_one({"stid": student_stid})
    # بررسی وجود دانشجو
    if student is None:
        raise HTTPException(status_code=404, detail='STUDENT NOT FOUND')
    return student


@app.delete("/DelStu/{student_stid}")
async def delete_student(student_stid: str):
    # بررسی وجود رکورد با student_stid
    existing_student = await students_collection.find_one({"stid": student_stid})
    if existing_student is None:
        raise HTTPException(status_code=404, detail='STUDENT NOT FOUND')

    # حذف رکورد دانشجو
    await students_collection.delete_one({"stid": student_stid})

    return {"message": "Student deleted successfully"}



@app.put("/UpStu/{student_stid}", response_model=schemas.Student)
async def update_student(student_stid: str, updated_student: schemas.StudentCreate):
    # جستجوی رکورد دانشجو با استفاده از شناسه
    existing_student = await students_collection.find_one({"stid": student_stid})
    # بررسی یافت شدن رکورد
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    # آپدیت رکورد دانشجو با استفاده از اطلاعات ارسال شده
    updated_student_data = updated_student.dict(exclude_unset=True)
    updated_student = {**existing_student, **updated_student_data}
    await students_collection.update_one({"stid": student_stid}, {"$set": updated_student})

    # بازگرداندن رکورد دانشجو آپدیت شده
    return updated_student



@app.post("/RegTeach", response_model=schemas.Teacher)
async def create_teacher(teacher: schemas.TeacherCreate):
    # بررسی تکراری بودن رکورد استاد
    existing_teacher = await teachers_collection.find_one({"lid": teacher.lid})
    if existing_teacher:
        raise HTTPException(status_code=400, detail="teacher with the same lID already exists")

    # ایجاد رکورد استاد با استفاده از اطلاعات ارسال شده
    created_teacher = await teachers_collection.insert_one(teacher.dict())
    # بازگرداندن رکورد ایجاد شده
    return teacher


@app.get("/RegTeach/{lid}", response_model=schemas.TeacherRead)
async def read_teacher(lid: str):
    # جستجوی استاد بر اساس lid
    teacher = await teachers_collection.find_one({"lid": lid})
    # بررسی وجود استاد
    if teacher is None:
        raise HTTPException(status_code=404, detail='TEACHER NOT FOUND')
    return teacher


@app.delete("/DelTeach/{teacher_lid}")
async def delete_teacher(teacher_lid: str):
    # جستجوی رکورد استاد با استفاده از شناسه
    existing_teacher = await teachers_collection.find_one({"lid": teacher_lid})

    # بررسی یافت شدن رکورد
    if not existing_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # حذف رکورد استاد
    await teachers_collection.delete_one({"lid": teacher_lid})

    # بازگرداندن پیام موفقیت حذف
    return {"message": "Teacher deleted successfully"}



@app.put("/UpTeach/{teacher_lid}", response_model=schemas.Teacher)
async def update_teacher(teacher_lid: str, updated_teacher: schemas.TeacherCreate):
    # جستجوی رکورد استاد با استفاده از شناسه
    existing_teacher = await teachers_collection.find_one({"lid": teacher_lid})

    # بررسی یافت شدن رکورد
    if not existing_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # آپدیت رکورد استاد با استفاده از اطلاعات ارسال شده
    updated_teacher_data = updated_teacher.dict(exclude_unset=True)
    updated_teacher = {**existing_teacher, **updated_teacher_data}
    await teachers_collection.update_one({"lid": teacher_lid}, {"$set": updated_teacher})

    # بازگرداندن رکورد استاد آپدیت شده
    return updated_teacher


@app.post("/RegLes", response_model=schemas.Lesson)
async def create_lesson(lessons: schemas.LessonCreate):
    # بررسی تکراری بودن رکورد درس
    existing_lessons = await lessons_collection.find_one({"cid": lessons.cid})
    if existing_lessons:
        raise HTTPException(status_code=400, detail="Lesson with the same CID already exists")

    # ایجاد رکورد درس با استفاده از اطلاعات ارسال شده
    created_lessons = await lessons_collection.insert_one(lessons.dict())

    # بازگرداندن رکورد ایجاد شده
    return lessons


@app.get("/RegLes/{lesson_cid}", response_model=schemas.LessonRead)
async def read_lesson(lesson_cid: str):
    # جستجوی رکورد درس با استفاده از شناسه
    existing_lesson = await lessons_collection.find_one({"cid": lesson_cid})
    # بررسی یافت شدن رکورد
    if not existing_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    # بازگرداندن رکورد درس
    return existing_lesson


@app.delete("/DelLes/{lesson_cid}")
async def delete_lesson(lesson_cid: str):
    # جستجوی رکورد درس با استفاده از شناسه
    deleted_lesson = await lessons_collection.find_one({"cid": lesson_cid})

    # بررسی یافت شدن رکورد
    if not deleted_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    # حذف رکورد
    await lessons_collection.delete_one({"cid": lesson_cid})

    # بازگرداندن پیام موفقیت حذف
    return {"message": "Lesson deleted successfully"}

@app.put("/UpLes/{lesson_cid}", response_model=schemas.Lesson)
async def update_lesson(lesson_cid: str, updated_lesson: schemas.LessonCreate):
    # جستجوی رکورد درس با استفاده از شناسه
    existing_lesson = await lessons_collection.find_one({"cid": lesson_cid})

    # بررسی یافت شدن رکورد
    if not existing_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    # آپدیت رکورد درس با استفاده از اطلاعات ارسال شده
    updated_lesson_data = updated_lesson.dict(exclude_unset=True)
    updated_lesson = {**existing_lesson, **updated_lesson_data}
    await lessons_collection.update_one({"cid": lesson_cid}, {"$set": updated_lesson})

    # بازگرداندن رکورد درس آپدیت شده
    return updated_lesson
