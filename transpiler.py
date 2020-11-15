c_file_str = input("Enter c file location: ");
python_file_str = input("Enter target python file: ");

indent = 0

c_datatypes = {"int ","float ","double ","bool ","short ","long ","char "}
with open(c_file_str, "r") as f:
    lines = f.readlines()
    for l in lines:
        if "main(" in l:
            indent -= 1
        if "{" in l:
            indent += 1
        if "}" in l:
            indent -= 1

        for datatype in c_datatypes:
            if datatype in l:
                l_out = l.replace(datatype, "").replace(";", "").strip() + "\n"
            
                if "(" in l and not "main(" in l:
                    l_out = "def {}:\n".format(l_out.strip())
                else:
                    l_out = "{indents}{statement}".format(indents="    " * indent, statement=l_out)

                if not "main(" in l:
                    with open(python_file_str,"a+") as f1:
                        f1.write(l_out)
                    
                print(l)

        
