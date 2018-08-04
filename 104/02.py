u=input()
u.split(",")
class Manager:
	def Adduser(self,username,userpassword,usermail):
		for i in username:
			if i < A or i >z or (i >Z and i < a):
				raise nameerror('username error')
				Addusererror = true
				break		
		if len(userpassword)>8:
			raise passworderror('password error')
			Addusererror = true
		else:
			for i in userpassword:
				if not(i == "_" or i == "-" or i=="@" or i=="#" or i=="%" or ( i>=A and i<=Z) or ( i>=a and i<=z) or ( i>="0" and i<="9")):					
					raise passworderror('password error')
					Addusererror = true
					break 
		if Addusererror == true:
			print("Add user error")
		else:
			self.username = username
			self.userpassword = userpassword
			self.usermail = usermail
			print("Add user successful")
	def AddCandidate(self,candidatename,candidatepassword,candidatenumber,candidatelastname):
		

class user:
	def logein(self,username,userpassword,Voting):

	def search(self,username,userpassword,candidatenumber):
a= Manager
a.Adduser("a","b","n")
