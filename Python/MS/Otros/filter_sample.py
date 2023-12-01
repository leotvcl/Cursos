with open("sample1.txt") as f:
    for line in f:
        line = line.strip()
        if line.lower().endswith(",f"):
            test = line.split(",")
            if len(test) >= 3:  # Asegurarse de que haya al menos 3 campos
                campo1 = test[0].strip()
                campo3 = test[2].strip()
                print(campo1 + "," + campo3)
