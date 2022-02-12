Error = False
def make_string(line,open_position,string):
	for i in range(len(line)):
		if i < open_position+4:
			continue
		while line[i] != ")":
			string += line[i]
			i += 1
		
		if string[0] == '"' and string[-1] == '"':
			string = check_string(string)
			return string
		else: 
			#if is_in_var(string):#well not variables, the first variable in each	
			return -1

def run_prints(line,line_count):	#A: good candidate for some inversion b: yup
	
	open_position = line.find("say(")	
	if open_position == -1: # if the line has a "say("
		return
	close_position = line.find(")",open_position)		
	if close_position == -1:#if there is a close somewhere after the open one	
		return
	string = ""
	output_string = make_string(line,open_position,string)
	if output_string == -1:
		print("///Line",str(line_count+1)+".","Syntax Error. All errors in this program for now end up as execution (ish) or logic, no prerun checks expected quotes after 'say(''")
		global Error
		Error = True
	else:
		print(output_string)
	

def check_string(string):
	characters = []

	for i in string:
		characters.append(i)
	characters.pop(0)
	characters.pop(-1)
	string = ""
	for i in characters:
		string+=i
	return string


def make_var(string,value):
	#https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/ 
	if value[0] == '"' and value[-1] == '"':
		value = check_string(value) 
		#A: you dont need this function, just do:
		#value = value[1:-1]
	else:
		try:
			value = int(value)
		except ValueError:
			try:
				value = float(value)
			except:
				pass
		else:
			pass
	globals()[string] = value
	
	global variables
	variables.append([string,value])
	return string,value#to return the name of the variable?

def find_var(line,open_position,comma_position,close_position):
	string = ""
	value = ""
	
	for i in range(len(line)):
		if i < open_position+4:
			continue
		
		if i < comma_position:
			string += line[i]
			continue

		if i < close_position-1:
			i+=1
			value += line[i]
			continue
	return string, value	

def run_vars(line):
	open_position = line.find("var(")
	if open_position == -1:# oh yeah "==" forgot abt that
		return
	comma_position = line.find(",",open_position)
	if comma_position == -1:
		return
	close_position = line.find(")",comma_position)
	if close_position == -1:
		return
	string,value = find_var(line,open_position,comma_position,close_position)
	#print(make_var(string,value))
	make_var(string,value)
				

def is_var(line):
	open_position = line.find("var(")
	comma_position = line.find(",",open_position)
	close_position = line.find(")",comma_position)
	#alex is there a point doing that here?
	if open_position == -1 or comma_position == -1 or close_position == -1:
		return False,open_position
	
	return True,open_position
 # no nead for this else, as when it returns, the function ends
	# also makes it look better imo cause you have a return at the end so even if everything else fails it wond return null
	# also allows you to quickly look at the bottom of a function to see what it returns
		#ok yeah yeah thats wow yeah ok u kep giving me more reasons to love these ideas like a salesperson or somethin
		# thankss

def is_say(line):
	open_position = line.find("say(")
	close_position = line.find(")",open_position)
	if open_position != -1 and close_position != -1:
		return True,open_position
	else:
		return False,open_position
variables = [] 

def prerun(file):
	with open(file,"r") as f:
		line_count = 0
		for line in f:
			#check if legal	
			return

def run(file):#A: Make sure you've got whitespaces between functions b: gahhh
	with open(file,"r") as f:
		line_count = 0
		for line in f:
			#print(variables)
			if Error == True: 
				return
			var_bool,var_position = is_var(line)
			say_bool,say_position = is_say(line)
			if var_bool and say_bool:
				if say_position > var_position:
					run_vars(line)
				if say_position < var_position:
					run_prints(line,line_count)
			elif var_bool:
				run_vars(line)
			elif say_bool:
				run_prints(line,line_count)
			line_count += 1
run("code.ben")
