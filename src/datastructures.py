
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        id = member.get("id", None)
        if id != None:
           for person in self._members:
               if person.get("id") == id:
                  return {
                      "msg": "id repetido"
                  }
        else: 
            member["id"] = self._generateId()           
             
        self._members.append(member) 
        return True


    def delete_member(self, member_id):
        # fill this method and update the return
        id_exist = False

        for member in self._members:
          if member["id"] == member_id:
            self._members.remove(member)
            id_exist = True

        if id_exist is True:
            return True
        return False

    def get_member(self, member_id):
        # fill this method and update the return

        for member in self._members:
           if member["id"]  == member_id:
            return member
        return False
    
    def edit_member(self, member_id, last_name):
        # fill this method and update the return

        for member in self._members:
          if member["id"] == member_id:
            member["last_name"] = last_name
            return True
        return False
        


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
