'''1. Generates the field. So far it filled up with symbols "0".
2. change_field function defined, by changing it you can reassign values that will be printed in final.
(it will be useful for taking input from user, or view visual changes)
3. Numerate a columns in alphabetical
4. Numerate a rows in digital
5. Align first column.
6. Print the final look of the field.
Tips for future:
- can to add set_defualts function to put there symbols that will fill field, maybe var with dimension of field'''



def generate_field(x=10, y=10):
    '''Generate field
    at the moment it have const parameters,
    x = 10 (elements in nested list)
    y = 10 (element in list)
    but it could be easily changed just by typing var in function'''
    field = [[0 for i in range(x)] for j in range(y)]
    return field


def change_field(l):
    '''Function for making changes in field.
    It's created for future development. For now it's doing nothing.
    It just take the list and return it back without changes'''
    return l


def print_field():
    print(*add_first_element_to_list(create_list_alphabet()))
    '''It's print the field generated by generate_field'''
    for i in add_first_element_to_list(change_field(generate_field())):
        x = i
        print(*x)


def align_first_column(l):
    '''Function makes alignment of first column in field output
    It add spaces to element if needed'''
    l = generate_dig_list()
    l_new = []
    for i in l:
        if len(str(i)) <= len(str(max(l))):
            '''Count's number of spaces that we need to write before element,
            that they have the same length.'''
            global spaces_number
            spaces_number = len(str(max(l))) - len(str(i))
            i = " " * spaces_number + str(i)
            l_new.append(i)
    return l_new


def create_list_alphabet():
    '''Creates a list of letter in alphabetical.'''
    l = [chr(i) for i in range(65, 90)]
    '''List begins with " ", its align first symbol'''
    l.insert(0, "  " * (len(str(max(generate_dig_list()))) - len(l[0])))
    '''It\'s cut the list to appropriate size for print'''
    l = l[0: len(generate_field()[0]) + 1]
    return l


def generate_dig_list(x = 10):
    '''Generate list'''
    l = [i for i in range(1, x + 1)]
    return l


def add_first_element_to_list(l):
    ''' Adding a first element to the nested list.
     As a result we get numbered zero elements in nested lists'''
    count = 1
    for i in l:
        '''Separate ordinary lists (type will be != list) from nested lists'''
        if type(i) == list:
            for j in align_first_column(generate_dig_list()):
                if int(j) == count:
                    i.insert(0, j)
            count += 1
    return l


print_field()