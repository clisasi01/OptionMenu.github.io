

exitprogram =False
while exitprogram==False:
    print " +--------------------------+"
    print " + Select an option         +"
    print " +--------------------------+"
    print " + 1. Option 1              +"           
    print " + 2. UPload Option 2       +"
    print " +--------------------------+"

    Option=raw_input("Enter Choice ")
    if Option=="1":

        Project=raw_input("Enter (Options : ")

        print "You Invited this %s"%(Project)

        if Project.upper() =="UC CORE":
            print "+-------------------------------+"
            print "20/01/2017                       "
            print " In Process............"
            print "\n\nBy  ,  "
            print "---------------------------------"
            print ""
            print "+--------------------------------+"

        elif Project.upper() =="BPM":
            print "+-------------------------------+"
            print "        "
            print "\n\n,              "
            print "---------------------------------"
            print ""
            print "+--------------------------------+"

        elif Project.upper() =="PMX":
            print "+-------------------------------+"
            print "         "
            print "\n\,              "
            print "---------------------------------"
            print "                                  "
            print "+--------------------------------+"

        elif Project.upper()=="EXIT":
            exitprogram=True    

        else :
            print "NON CATEGORY"
    if Option=="2":
        
        file= open("test.txt", "r")
        Test=file.read()
        print Test
            
    elif Option.upper()=="EXIT":
            exitprogram=True
    else :
        print "ERROR MESSAGE"        
      
            
