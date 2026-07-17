import json;
#Create a list of five AWS services and print them using a loop.
aws_Services =["EC2", "S3", "Lambda", "VPC", "ECS", "EKS"]
print(aws_Services)
for aws_service in aws_Services:
    print(aws_service)

#Create a dictionary for yourself with name, role, experience, and location, then print each key and value.
student_dic = {
    "name": "John",
    "role": "Student",
    "experience": "2",
    "location": "New York"
}
print(student_dic)
for key, value in student_dic.items():
    print(f"{key}: {value}")


employees = [
    {
        "name":"Sudhir",
        "role":"PM"
    },
    {
        "name":"Rahul",
        "role":"Developer"
    },
    {
        "name":"Amit",
        "role":"QA"
    }
]

for employee in employees:
    for key,value in employee.items():
        print(f"{key}: {value}")
       

with open("./Day01/employees.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("./Day01/employees.json", "r") as file:
    data = json.load(file)
    print(data)



