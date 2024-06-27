def preprocess(txt_filepath):
    result = ""
    adding = True
    with open(txt_filepath, "+r") as file:
        lines = file.readlines()
        for line in lines:
            for i in range(len(line)):
                if line[i] == "%":
                    if i+1 != len(line):
                        if line[i + 1] == "*":
                            adding = False
                        else:
                            break
                elif line[i] == "*" and not adding:
                    if i+1 != len(line):
                        if line[i + 1] == "%":
                            adding = True

                elif adding:
                    if line[i] != "\t":
                        if line[i] == "\n":
                            result += " "
                        else:
                            result += line[i]

    return result.strip()