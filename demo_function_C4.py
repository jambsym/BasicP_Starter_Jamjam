# function ที่ return ค่าของเกรด
# ลองทำดู
# def grade(scoer):
#     if scoer >= 50:
#         print("pass")
#         if scoer >= 80:
#             print("Grade : A")
#         elif scoer >= 70:
#             print("Grade : B")
#         elif scoer >=60:
#             print("Grade : C")
#         else:
#             print("Grade : D")
#     else:
#         print("failed")
# grade(60)

# def function(x,y):
#     for i in range(y):
#         i = i+1
#         print(f" {x} * {i} = {x*i}")
# function(3,6)

# 1 เริ่มต้นยังไง
# 2 แก้ไขได้อย่างไร
# 3 ใช้งาน หรือ ดู มันได้อย่างไร
# 4 ลบมันได้อย่างไร
# 5 เพิ่มอย่างไร

# x =["jam" ,"pam" ,"bam "]
# for i in x:
#     print(f"i love {i}")

student = {
    "name" : "jamjam",
    "ID" : "41",
    "year" : "1"
}
print(f"my name is {student['name']}")
student['name'] = "jam"
print(f"my name is {student['name']}")

print(student)
student['grede'] = "A"
print(student)
student.pop("grede")
print(student)


student = [
    {"name" : "jam" , "ID" : "41" , "age" : 19 },
    {"name" : "pam" , "ID" : "39" , "age" : 19 }
]
print(student)
for s in student :
    print(s)
    print(f"your name is {s['name']}")