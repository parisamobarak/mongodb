from pydantic import BaseModel, validator
import re
class StudentBase(BaseModel):
    fname: str
    lname: str
    father: str
    birth: str
    ids: str
    borncity: str
    addres: str
    postalcode: int
    cphone: int
    hphone: int
    department: str
    major: str
    married: str
    id: int
    scourseids: int
    lids: int

    @validator('fname', 'lname', 'father')
    def validate_name(cls, name):
        if len(name) > 10:
            raise ValueError("نام نامعتبر است. حداکثر طول نام ۱۰ کاراکتر است.")
        if not re.match(r'^[آ-ی\s]+$', name):
            raise ValueError("نام نامعتبر است. نام باید فقط شامل حروف فارسی باشد.")
        if re.search(r'\d', name) or re.search(r'[!@#$%^&*(),.?":{}|<>]', name):
            raise ValueError("نام نامعتبر است. نام نباید شامل اعداد یا علائم خاص باشد.")
        return name

    @validator('birth')
    def validate_birth(cls, birth):
        date_pattern = "^1[3-4][0-9]{2}/((0[0-9])|(1[0-2]))/(([0-2][0-9])|3[0-1])$"
        match = re.match(date_pattern, birth)
        if not match:
            raise ValueError("تاریخ تولد نامعتبر است.")
        return birth

    @validator('ids')
    def validate_ids(cls, ids):
        if not re.match(r'^\d{6}[آ-ی]\d{2}$', ids):
            raise ValueError("شماره شناسایی نامعتبر است. باید شامل یک عدد 6 رقمی، یک حرف فارسی و یک عدد 2 رقمی باشد.")
        return ids

    @validator('borncity')
    def validate_borncity(cls, borncity):
        valid_cities = ['تهران', 'مشهد', 'اصفهان', 'شیراز', 'تبریز', 'اهواز', 'کرج', 'قم', 'کرمانشاه', 'ارومیه']
        if borncity not in valid_cities:
            raise ValueError("شهر محل تولد نامعتبر است. باید یکی از مراکز استان‌های کشور باشد.")
        return borncity

    @validator('addres')
    def validate_addres(cls, addres):
        if len(addres) > 100:
            raise ValueError("آدرس نمی‌تواند بیشتر از 100 کاراکتر باشد.")
        return addres

    @validator('postalcode')
    def validate_postalcode(cls, postalcode):
        if not re.match(r'^\d{10}$', str(postalcode)):
            raise ValueError("کد پستی نامعتبر است. باید شامل یک عدد 10 رقمی باشد.")
        return postalcode


    #@validator('cphone')
    #def validate_cphone(cls, cphone):
        #str_cphone = str(cphone)
        #if not re.match(r'^09\d{9}$', str_cphone):
            #raise ValueError("شماره تلفن همراه نامعتبر است. باید شامل یک عدد 11 رقمی باشد و با 09 شروع شود.")
        #return cphone

    #@validator('hphone')
    #def validate_hphone(cls, hphone):
        #if not re.match(r'^0\d{2}\d{8}$', str(hphone)):
            #raise ValueError("شماره تلفن ثابت نامعتبر است. باید به صورت استاندارد در ایران باشد.")
        #return hphone

    @validator('department')
    def validate_department(cls, department):
        valid_department = ['فنی و مهتدسی', 'هنر', 'علوم اقتصادی', 'علوم پایه', 'پزشکی', 'علوم کامپیوتر', 'مدیریت', 'علوم انسانی', 'حقوق ', 'زبان و ادبیات']
        if department not in valid_department:
            raise ValueError("نام دانشکده نامعتبر است. باید یکی از دانشکده های مجاز باشد.")
        return department

    @validator('major')
    def validate_major(cls, value):
        allowed_majors = ["مهندسی برق", "مهندسی مکانیک", "مهندسی عمران", "مهندسی کامپیوتر"]
        if value not in allowed_majors:
            raise ValueError('رشته تحصیلی نامعتبر است.')
        return value

    @validator('married')
    def validate_marital_status(cls, value):
        allowed_marital_status = ["مجرد", "متاهل"]
        if value not in allowed_marital_status:
            raise ValueError('وضعیت تاهل نامعتبر است')
        return value






class StudentCreate(StudentBase):
    id:int
    stid: int


    @validator('stid')
    def validate_stid(cls, stid):
        str_id = str(stid)  # تبدیل ورودی به نوع رشته
        if not re.match(r'^[3-4][0-9]{2}114150[0-9]{2}$', str_id):
            raise ValueError("کد دانشجویی نامعتبر است.")
        return str_id

    @validator('id')
    def validate_id(cls, id):
        str_id = str(id)  # تبدیل ورودی به نوع رشته
        if not re.match(r'^\d{10}$', str_id):
            raise ValueError("شماره شناسنامه نامعتبر است. باید شامل یک عدد 10 رقمی باشد.")
        return str_id

class Student(StudentBase):
    stid: int
    class Config:
        orm_mode=True

class StudentRead(BaseModel):
    stid: int
    fname: str
    lname: str
    father: str

class TeacherBase(BaseModel):
    fname :str
    lname :str
    department :str
    major :str
    birth :str
    borncity :str
    addres :str
    postalcode :int
    cphone: int
    hphone: int
    lcourseid: int

    @validator('fname', 'lname')
    def validate_name(cls, name):
        if len(name) > 10:
            raise ValueError("نام نامعتبر است. حداکثر طول نام ۱۰ کاراکتر است.")
        if not re.match(r'^[آ-ی\s]+$', name):
            raise ValueError("نام نامعتبر است. نام باید فقط شامل حروف فارسی باشد.")
        if re.search(r'\d', name) or re.search(r'[!@#$%^&*(),.?":{}|<>]', name):
            raise ValueError("نام نامعتبر است. نام نباید شامل اعداد یا علائم خاص باشد.")
        return name

    @validator('department')
    def validate_department(cls, department):
        valid_department = ['فنی و مهتدسی', 'هنر', 'علوم اقتصادی', 'علوم پایه', 'پزشکی', 'علوم کامپیوتر', 'مدیریت',
                            'علوم انسانی', 'حقوق ', 'زبان و ادبیات']
        if department not in valid_department:
            raise ValueError("نام دانشکده نامعتبر است. باید یکی از دانشکده های مجاز باشد.")
        return department

    @validator('major')
    def validate_major(cls, value):
        allowed_majors = ["مهندسی برق", "مهندسی مکانیک", "مهندسی عمران", "مهندسی کامپیوتر"]
        if value not in allowed_majors:
            raise ValueError('رشته تحصیلی نامعتبر است.')
        return value

    @validator('birth')
    def validate_birth(cls, birth):
        date_pattern = "^1[3-4][0-9]{2}/((0[0-9])|(1[0-2]))/(([0-2][0-9])|3[0-1])$"
        match = re.match(date_pattern, birth)
        if not match:
            raise ValueError("تاریخ تولد نامعتبر است.")
        return birth


    @validator('borncity')
    def validate_borncity(cls, borncity):
        valid_cities = ['تهران', 'مشهد', 'اصفهان', 'شیراز', 'تبریز', 'اهواز', 'کرج', 'قم', 'کرمانشاه', 'ارومیه']
        if borncity not in valid_cities:
            raise ValueError("شهر محل تولد نامعتبر است. باید یکی از مراکز استان‌های کشور باشد.")
        return borncity

    @validator('addres')
    def validate_addres(cls, addres):
        if len(addres) > 100:
            raise ValueError("آدرس نمی‌تواند بیشتر از 100 کاراکتر باشد.")
        return addres

    @validator('postalcode')
    def validate_postalcode(cls, postalcode):
        if not re.match(r'^\d{10}$', str(postalcode)):
            raise ValueError("کد پستی نامعتبر است. باید شامل یک عدد 10 رقمی باشد.")
        return postalcode


class TeacherCreate(TeacherBase):
    id:int
    lid: int

    @validator('lid')
    def validate_id_number(cls, lid):
        lid = str(lid)  # تبدیل ورودی به نوع رشته
        if not re.match("^\d{6}$", lid):
            raise ValueError("شماره LID باید شامل یک عدد 6 رقمی باشد.")
        return lid

    @validator('id')
    def validate_id(cls, id):
        str_id = str(id)  # تبدیل ورودی به نوع رشته
        if not re.match(r'^\d{10}$', str_id):
            raise ValueError("شماره شناسنامه نامعتبر است. باید شامل یک عدد 10 رقمی باشد.")
        return str_id

class Teacher(TeacherBase):
    lid: int


    class Config:
        orm_mode=True


class TeacherRead(BaseModel):
    lid: int
    fname: str
    lname: str
    id: int


class LessonBase(BaseModel):
    cname: str
    part: str
    credit: int

    @validator('cname')
    def validate_name(cls, name):
        if len(name) > 25:
            raise ValueError("نام کلاس نامعتبر است. حداکثر طول نام ۱۰ کاراکتر است.")
        if not re.match(r'^[آ-ی\s]+$', name):
            raise ValueError("نام کلاس نامعتبر است. نام باید فقط شامل حروف فارسی باشد.")
        if re.search(r'\d', name) or re.search(r'[!@#$%^&*(),.?":{}|<>]', name):
            raise ValueError("نام کلاس نامعتبر است. نام نباید شامل اعداد یا علائم خاص باشد.")
        return name


    @validator('part')
    def validate_department(cls, department):
        valid_department = ['فنی و مهتدسی', 'هنر', 'علوم اقتصادی', 'علوم پایه', 'پزشکی', 'علوم کامپیوتر', 'مدیریت',
                            'علوم انسانی', 'حقوق ', 'زبان و ادبیات']
        if department not in valid_department:
            raise ValueError("نام دانشکده نامعتبر است. باید یکی از دانشکده های مجاز باشد.")
        return department

    @validator('credit')
    def validate_id_range(cls, id_value):
        if not (1 <= id_value <= 4):
            raise ValueError("تعداد واحد باید بین 1 تا 4 باشد.")
        return id_value

class LessonCreate(LessonBase):
    cid: int

    @validator('cid')
    def validate_id(cls, id):
        str_id = str(id)  # تبدیل ورودی به نوع رشته
        if not re.match(r'^\d{5}$', str_id):
            raise ValueError("کد درس  نامعتبر است. باید شامل یک عدد 5 رقمی باشد.")
        return str_id

class Lesson(LessonBase):
    cid: int
    class Config:
        orm_mode=True

class LessonRead(BaseModel):
    cid: int
    cname: str
    part: str
    credit: int