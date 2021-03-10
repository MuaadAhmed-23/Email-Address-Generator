def addressFunc(firstName, lastName, email):
    p = '.'
    a = '@'
    c = 'com'
    value_firstName = input("Please insert First Name: ")
    value_lastName = input("Please insert Last Name: ")
    value_domainName = input("Please insert Domain Name: ")
    con_cat = value_firstName + p + value_lastName + a + value_domainName + p + c
    print(con_cat)
addressFunc("Muaad", "Ahmed", "carleton")
