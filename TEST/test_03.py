
str_dict = dict()
def solution(tstring, variables):
    answer = ""

    for name, value in variables:
        name = '{' + name + '}'
        str_dict[name] = value
    print(str_dict)
    change_list = []

    for key, value in str_dict.items():
        tstring = tstring.replace(key, value)


        print(tstring)







    # name = 'Elon'
    # exec("%s = %d" % (name, 100))
    # print(Elon)




    return answer

tstring = "this is {template} {template} is {state}"
variables = [["template", "string"], ["state", "changed"]]

solution(tstring, variables)