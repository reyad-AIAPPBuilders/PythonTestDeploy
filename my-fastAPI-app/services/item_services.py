def get_available_doctors(x: int):
    print(x,type(x))
    doctors = []

    for i in range(x):
        name = "doctors_" + str(i)

        doctors.append(name)

    print(doctors)
    return doctors