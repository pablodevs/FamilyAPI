
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
        if member["age"] <= 0: return "Not valid age"

        new_member = {
            "id": member.get("id", self._generateId()),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member)

    def delete_member(self, id):
        for idx, member in enumerate(self._members):
            if member["id"] == id:
                deleted_member = self._members.pop(idx)
                return "Member: {}, with id {} was deleted".format(deleted_member["first_name"], deleted_member["id"])
        return "Member not found"

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return {"id": member["id"], "first_name": member["first_name"], "age": member["age"], "lucky_numbers": member["lucky_numbers"]}
        return "Member not found"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members