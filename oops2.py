# class account:
#      def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#         #private declaration

#      def reset_pass(self):
#           print(self.__acc_pass)

# s1=account("121113","Aman@@123")


# print(s1.acc_no)
# print(s1.reset_pass())







# ----------------multiple inheritance-----------------

class A:
        varA="welcome to A"
class B:
     varB="welcome to B"
class C(A,B):
     varC="welcome to C"


c1=C()
print(c1.varC)
print(c1.varB)

