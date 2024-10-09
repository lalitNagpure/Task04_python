
# 1.
def emp(empName,empAge,empMob,empAddress):
    print(f'empname = {empName}')
    print(f'empAge = {empAge}')
    print(f'empMob = {empMob}')
    print(f'empAddress = {empAddress}')



    return{
    'emp-name' : 'empName',
    'emp-age' : 'empAge',
    'emp-mob': 'empMob',
    'emp-address' : empAddress
    }


emp1 = emp('emp1',23,123123,'mum')
print()

print(f'emp1 = {emp1}')

print()


# 2.

def Student(studentId,studentName,studentMob,studentAddress):
    print(f'studentId = {studentId}')
    print(f'studentname = {studentName}')
    print(f'studentMob = {studentMob}')
    print(f'studentAddress = {studentAddress}')



    return{
    'stud-id' : 'studentId',
    'stud-name' : 'studentName',
    'stud-mob': 'studentMob',
    'stud-address' : studentAddress
    }


Student1 = Student(101,'Student',123123,'mum')
print()

print(f'Student1 = {Student1}')