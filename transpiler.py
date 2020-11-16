c_file_str = input("Enter c file location: ");
python_file_str = input("Enter target python file: ");

indent = 0

c_datatypes = {"int ","float ","double ","bool ","short ","long ","char "}

analagous_func = {
    "printf(" : "print("
}

with open(c_file_str, "r") as f:
    lines = f.readlines()
    for l in lines:
        if "main(" in l:
            indent -= 1
        if "{" in l:
            indent += 1
        if "}" in l:
            indent -= 1
        l_out = ""
        for datatype in c_datatypes:
            if datatype in l:
                l_out = l.replace(datatype, "").replace(";", "").strip() + "\n"
            
                if "(" in l and not "main(" in l and not "=" in l:
                    l_out = "def {}:\n".format(l_out.strip())
                else:
                    l_out = "{indents}{statement}".format(indents="    " * indent, statement=l_out)

                if not "main(" in l:
                    with open(python_file_str,"a+") as f1:
                        f1.write(l_out)
                        
        for func in analagous_func:
            if func in l:
                #converts function to python function
                l_out = l.replace(func, analagous_func[func]).replace(";", "").strip() + "\n"
                first_slice = l_out[:l_out.find("\"", l_out.find("\"") + 1) + 1]
                second_slice = l_out[l_out.find("\"", l_out.find("\"") + 1) + 1:]
                if "," in second_slice:
                  second_slice = second_slice.replace(",", "%", 1).strip()
                  second_slice = "{}({}){}".format(second_slice[0], second_slice[1:second_slice.find(")")], second_slice[second_slice.find(")"):])       
                  l_out = first_slice + second_slice

                    
                with open(python_file_str,"a+") as f1:
                        f1.write(l_out)

        

