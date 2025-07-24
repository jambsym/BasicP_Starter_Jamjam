# student = [
#     {"name": "jam" , "id": "68130500041","age": 19},
#     {"name" : "pam" , "id": "68130500039","age": 20},
#     {"name" : "bam" , "id": "68130500039","age": 21}
# ]

# def check_age(age):
#     return age > 19

# def get_data(ds,index,key) :
#     return ds[index][key]

# print(get_data(student, 2 , "name"))

# print(type(student))


# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # นลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    print("รายชื่อหนังทั้งหมด : ")
    for i , movie in enumerate(movie_list,1):
        print(f"{i} {movie}")
# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    if age_restriction == 'G' :
        return True
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    else:
        return int(user_age) >= (age_restriction)
# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # ถ้า genre เป็น 'Action' บวกเพิ่ม 50 บาท
    if genre == 'Action' :
        return True
    # ถ้าไม่ใช่ คืนราคาเดิม
    else:
        return base_price
# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list): 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    print(show_movies)
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
x = int(input("หนังที่ต้องการ (1-5) : "))
    # 3. รับอายุผู้ใช้
age =int
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    # สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("เลือกเมนู: ")

    # ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# เรียก main เพื่อเริ่มโปรแกรม
main()