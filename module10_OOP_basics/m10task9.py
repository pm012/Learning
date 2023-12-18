"""
Create class LookupKeyDict with parent class UserDict. 
Add function lookup_key as a method of LookUpKeyDict class.


"""

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return [key for key in self.data if self.data[key]==value]
    
my_dict = LookUpKeyDict()
my_dict.update( {
    1 : "Siam",
    2 : "Danilo",
    3 : "Kate",
    4 : "Serhii",
    5 : "Alex",
    6 : "Siam"
})

print(my_dict.lookup_key("Siam"))
        
        
            
                
        