
print("-"*30)
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("-"*30)

employees = []

while True:
    name = input("請輸入姓名:")

    if not name:
        break

    salary_str = input("請輸入薪資:")
    print("")
    try:
        salary = int(salary_str)
    except ValueError:
        print("薪資輸入錯誤，請輸入數字。")
        continue

    employee = {'eName': name, 'eSalary': salary}
    employees.append(employee)

print("-"*30)

total_salary = sum(employee['eSalary'] for employee in employees)
average_salary = total_salary / len(employees) if len(employees) > 0 else 0

for employee in employees:

    print(f"員工{employee['eName']:>5} 的薪資為 {employee['eSalary']:>5,}")
print("-"*30)
print(f"合計薪資：{total_salary:>15,}")
print(f"平均薪資：{average_salary:>18,.2f}")
print("="*30)
