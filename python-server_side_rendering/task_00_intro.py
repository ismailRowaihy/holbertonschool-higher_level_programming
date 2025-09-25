

def generate_invitations(template, attendees):
    
    if not isinstance(template,str):
        print("template is not string")
        return
    if not isinstance(attendees,list):
        print("attendess is not a list")
        return
    for i in attendees:
        if not isinstance(i,dict):
            print (" list in not a list of dict")
            return

    if not template:
        print ("Template is empty, no output files generated.")
        return
    if not attendees:
        print ("No data provided, no output files generated.")
        return
    
    for i,atnd in enumerate(attendees,start=1):
        new_template = template
        for k,v in atnd.items():
            #print(str(k)+" : "+str(v))
            new_template = new_template.replace("{"+str(k)+"}",str(v)if v else "N/A")
        
        with open(f"output_{i}.txt", "w") as file:
            file.write(new_template)
            print(new_template)