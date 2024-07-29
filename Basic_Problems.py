# 1. Question: Write a function that takes a list of numbers and returns the sum.
def sum_of_list(list_num):
    return sum(list_num)


# 2.How do you reverse a string in Python?
def reverse_str(string):
    return string[::-1]


# 3.Question: Write a function that checks if a given word is a palindrome.
def palindrome(string):
    return string == string[::-1]


# 4. Question: How can you remove duplicates from a list?
def duplicate_removal(list_to_chk):
    return set(list_to_chk)


# 5 Question: How do you handle exceptions in Python?
def get_integer_id(prompt):
    try:
        user_input = input(prompt)
        user_id = int(user_input)
        return user_id
    except ValueError:
        print('Invalid Input')


# 6 Question: What is a lambda function? Provide an example.

# 7 Question: Write a function that returns the n-th Fibonacci number using recursion.

# 8 Question: What are decorators in Python and how are they used?
# Answer - add extra features on an exsitimg function by not changing it


# Example 1 : div function always diving larger_valye/smaller_value
def smart_dev(div_func):
    def inner_fun(first, second):
        if first < second:
            first, second = second, first
        return div_func(first, second)

    return inner_fun


def div(a, b):
    return a / b


# Example 2 : password access to only admin
user = {'name': 'Rezwan', "access_level": "admin"}
import functools
def secure_admin_password(get_admin_pass_funct):
    @functools.wraps(get_admin_pass_funct) # this does not allow get_admin_the_password name change to secure_admin_password
    def securing_admmin_password():
        if user['access_level'] == 'admin':
            return get_admin_pass_funct()

    return securing_admmin_password


@secure_admin_password # this element the need of this line 'get_admin_the_password = secure_admin_password(get_admin_the_password)'
def get_admin_the_password():
    return "1234"


if __name__ == "__main__":
    print('***Answer1****')
    print('Sum of List->', sum_of_list([1, 5, 6]))

    print('***Answer2****')
    print('Reverse String->', reverse_str('abc'))

    print('***Answer3****')
    print('Panlindrome->', palindrome('raccar'))

    print('***Answer4****')
    print('Remove Dulipcate Element from List->', duplicate_removal([1,1,1,1,3,3,3,3,]))

    print('***Answer5****')
    user_id = get_integer_id("Enter your Integer id")
    print(f"Your Id is: {user_id}")

    print('***Answer8a****')
    div = smart_dev(div)
    print(f"Example 1 -> adding decorater to the divison function, The answer is {div(2,4)}")

    print('***Answer8b****')
    # get_admin_the_password = secure_admin_password(get_admin_the_password)
    if get_admin_the_password() == None:
        print('Hey you are not admin, dont ask for password!!!')
    else:
        print(f"Example 2 -> The password is '{get_admin_the_password()}' "
              f"which is given to {user['access_level']}")
