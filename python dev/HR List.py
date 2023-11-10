with open("hr_system.txt") as hr_list:
    for line in hr_list:
        line = line.strip()
        parts = line.split()
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        pay_check = salary / 24
        if job_title.lower() == "engineer":
            pay_check += 1000
        #print(line)
        print(f"{name} (ID: {id_number}), {job_title} - ${pay_check:.2f}")
