"""
It is required to have output of sanitized phone numbers in the following format (using decorator).
For example for numbers:
  "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",

    we received:
380501233234
0503451234
0508889900
380501112222
380501112211

and after decorating we should get:
+380501233234
+380503451234
+380508889900
+380501112222
+380501112211


Decorator should add to short numbers prefix +38, and for full international number (with 12-th symbol) only '+'
Implement decorator <format_phone_number> for function sanitize_phone_number> with the required functional

"""
def format_phone_number(func):
    def phone_output_formatting(phone):
        phone = func(phone)        
        if len(phone)==12 and phone.isdigit():
            return "+"+func(phone)
        elif len(phone)==10 and phone.isdigit():
            return "+38"+func(phone)
        elif len(phone)==13 and phone.startswith('+') and phone[1:].isdigit():
            return func(phone)
                
    return phone_output_formatting
        


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone



phones1 = ["380501233234","0503451234","0508889900","380501112222","380501112211"]
phones = ["    +38(050)123-32-34", "     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   "]

for phone in phones:  
    print(sanitize_phone_number(phone))

