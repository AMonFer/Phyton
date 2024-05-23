# % comentario una linea
# %**% comentario varias lineas

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
                    if line[i] != " " and line[i] != "\t" and line[i] != "\n":
                        result += line[i]

            #if len(result) > 0 and result[-1] != "\n":
            #    result += "\n"

    return result.strip()
