f = open("학생정보.csv", "r", encoding="utf-8")
text = f.readlines()

student = {}

for line in text:
    new_line = line.split(',')
    id = new_line[0]
    name = new_line[1].strip()
    grade = new_line[2].replace('\n', '').strip()

    info = {}
    info["이름"] = name
    info["성적"] = grade

    student[id] = info

while True:
    number = input("옵션->조회(1) 수정(2) 추가(3) 종료(4):")
    number = int(number)

    if number == 1:
        
        


        
        if id in student.keys():
            n = student[id]
            print(id + " 학번의 이름은 " + n["이름"] + " 성적은 " + n["성적"] + "입니다.")
        else:
            print(id + " 학번은 없습니다!")

    elif number == 2:
        id, update_list, comment = input("학번, 수정항목, 수정내용을 입력하세요: ").split()
        if id not in student.keys():
            print(id + " 학번은 없습니다!")
        else:
            if update_list == "이름":
                student[id][update_list] = comment
                print(id + " 학번의 이름이 " + comment + "로 바뀌었습니다.")
                print(id + " 학번의 이름은 " +
                      student[id]["이름"] + " 성적은 " + student[id]["성적"] + "입니다.")

            elif update_list == "성적":
                student[id][update_list] = comment
                print(id + " 학번의 성적이 " + comment + "로 바뀌었습니다.")
                print(id + " 학번의 이름은 " +
                      student[id]["이름"] + " 성적은 " + student[id]["성적"] + "입니다.")

            else:
                print('"'+update_list+'"' + " 항목은 존재하지 않습니다!")
    elif number == 3:
        l = list(input("추가할 학번, 이름, 성적을 입력하세요: ").split())
        if l[0] in student.keys():
            print(l[0] + " 학번은 이미 존재합니다.")
        else:
            id = l[0]
            if len(l) == 1:
                name = "홍길동"
                grade = "F"

            elif len(l) == 2:
                name = l[1]
                grade = "F"

            elif len(l) == 3:
                name = l[1]
                grade = l[2]

            student[id] = {"이름": name, "성적": grade}
            print(id + " 학번으로 " + student[id]["이름"] +
                  ", " + student[id]["성적"] + " 가 저장되었습니다.")

    elif number == 4:
        f = open("학생정보.csv", "w", encoding="utf-8")
        for key in student.keys():
            f.write(key + ", " + student[key]
                    ["이름"] + ", " + student[key]["성적"]+'\n')
        print("저장됐습니다.")
        f.close()
        break
