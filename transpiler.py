c_file_str = input("Enter c file location: ");
python_file_str = input("Enter target python file: ");

indent = 0

c_datatypes = {"int ","float ","double ","bool ","short ","long ","char "}
with open(c_file_str, "r") as f:
    lines = f.readlines()
    for l in lines:
        if "{" in l:
            indent += 1
        if "}" in l:
            indent -= 1

        for datatype in c_datatypes:
            if datatype in l:
                with open(python_file_str, "a+") as output_f:
                    output_f.write(l[l.find(datatype)+ len(datatype):].replace(";", ""))
                
        print(l)
