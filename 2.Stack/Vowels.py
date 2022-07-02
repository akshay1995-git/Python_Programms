def removeVowels(name):
    new_str=''
    for i in range(0,len(name)):
        if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
            pass
        else:
            new_str+=name[i]
            print(new_str)
            
    print("Final string :",new_str)
    
removeVowels("kshirsagar")