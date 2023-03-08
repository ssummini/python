f = open("학생정보.csv", "r", encoding="utf-8")
text = f.readlines()


student = {}

for line in text:
    new_line = line.split(',')
    id = new_line[0]
    info = {}
    name = new_line[1].strip() 
    grade = new_line[2].replace("\n", "").strip()
    info["이름"] = name
    info["성적"] = grade

    student[id] = info

print(student.keys())

finding = input("정보를 확인하려는 학생의 학번을 입력하세요:")
if finding in student.keys():        
    print(finding, "학번의 이름은 ", 
    student[finding]["이름"], "성적은 ",
    student[finding]["성적"], "입니다.")
else :
    print(finding, "학번은 없습니다 !")