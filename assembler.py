from sys import argv
import os
import fnmatch


from table import *

def generate_sym(filename):
	
	with open(filename,'r') as file:
		li=0
		for line in file:
			li=li+1
			if ":" in line:
				lab4=line.split(":")
				lable.append(lab4[0].strip())
				
						
			if "dd" in line:
				count=0
				val=[]
				d1=line.replace(' ',',')
				d2=d1.split(',')
				if d2[0] not in sym_name:
					sym_name.append(d2[0])
					for i in range(2,len(d2)):
						count=count+1
						val.append(d2[i])
					s=",".join(val)
					sym_size.append((4*count))
					sym_value.append(s)
					sym_type.append("S")
					sym_DU.append("D")
					section.append("data")
					line_no.append(li)
					sym_type1.append("dd")
				else:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(110)
					er_speci.append(d2[0])
				
			elif "db" in line:
				b1=line.replace(' ',',')
				b2=b1.split('"')
				#print(b2)
				sym_value.append(b2[1].replace(',',' '))
				#print(sym_value)
				sym_size.append(len(b2[1]))
				b3=b2[0].replace(',',' ')
				b4=b3.split()
				sym_name.append(b4[0])	
				sym_type.append("S")
				sym_DU.append("D")
				section.append("data")
				line_no.append(li)
				sym_type1.append("db")
			elif "resb" in line:
				rb1=line.split()
				if rb1[0] in sym_name:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(101)
					er_speci.append(rb[0])
					
				else:
					
					sym_name.append(rb1[0])
					sym_size.append(1*int(rb1[2]))
					sym_value.append(rb1[2])
					sym_type.append("L")
					sym_DU.append("D")
					section.append("bss")
					line_no.append(li)
					sym_type1.append("resb")
				
			elif "resd" in line:
				rd1=line.split()
				if rd1[0] in sym_name:
					er_li.append(li)
					er_name.append("Error:already defined")
					er.append(102)
					er_speci.append(rd1[0])
				else:
					
					sym_name.append(rd1[0])
					sym_size.append(4*int(rd1[2]))
					sym_value.append(rd1[2])
					sym_type.append("L")
					sym_DU.append("D")
					section.append("bss")
					line_no.append(li)
					sym_type1.append("resd")
			elif "global" in line:
				lab=line.split()
				#print(len(lab))
				if len(lab)>1:
					store_lable.append(lab[1])
					lab_line.append(li)
				else:
					er_li.append(li)
					er_name.append("Error:main function not defined")
					er.append(103)
					er_speci.append("-")
					
				
					
					
			elif "jmp" in line:
				lab1=line.split()
				if len(lab1)>1:
					store_lable.append(lab1[1])
					lab_line.append(li)
					
			elif "jz" in line:
				lab2=line.split()
				if len(lab2)>1:
					store_lable.append(lab2[1])
					lab_line.append(li)					
					
		if len(lable)>len(store_lable):
			for i in range(len(lable)):
				if lable[i] in store_lable:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
			for i in range(len(store_lable)):
				if store_lable[i] not in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		elif len(lable)<len(store_lable):
			for i in range(len(store_lable)):
				if store_lable[i] in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")				
				else:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		elif len(lable)==len(store_lable):
			for i in range(len(store_lable)):
				if lable[i] not in store_lable:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no.append("-")
					sym_type1.append("-")		
				else:
					sym_name.append(lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("D")
					section.append("text")
					line_no1.append("-")
					sym_type.append("-")				
				if store_lable[i] not in lable:
					sym_name.append(store_lable[i])
					sym_size.append("-")
					sym_value.append("-")
					sym_type.append("S")
					sym_DU.append("U")
					section.append("text")
					line_no.append(lab_line[i])
					sym_type1.append("-")		
		
	for i in range(len(sym_DU)):
		if 'U'==sym_DU[i]:
			er_li.append(li)
			er_name.append("error: symbol undefined")
			er.append(i)
			er_speci.append(sym_name[i])					
	
	file.close()
	#print(lable,store_lable)
def check_inst(filename):
	with open(filename,'r') as file:
		li=0
		for line in file:
			li=li+1
			if "main" in line:
				after_main(line,li,file)
				break
			
def after_main(line,li,file):
	for line in file:
		li=li+1
		s=line.replace(","," ")
		p1=s.split()	
		li_len=len(p1)
		#print(li_len)
		if li_len==1:
			zero_byte_inst(p1,li)				
		elif li_len==2:
			one_byte_inst(p1,li)
		elif li_len==3:
			two_byte_inst(p1,li)
		elif li_len==4:
			del(p1[0])
			two_byte_inst(p1,li)
		elif li_len==5:
			er_li.append(li)
			er_name.append("Error:Invalid instruction")
			er.append(104)
			er_speci.append(line)
			break
	file.close()
				    
def zero_byte_inst(p1,li):
	l="".join(p1)
	if ':' not in l:
		er_li.append(li)
		er_name.append("Error:Near")
		er.append(105)
		er_speci.append(l)
def one_byte_inst(p1,li):
	if p1[0] not in inst1:
		er_li.append(li)
		er_name.append("Error:Near")
		er.append(106)
		er_speci.append(p1[0])
	
def two_byte_inst(p1,li):
	
	if p1[0] not in inst2:
		er_li.append(li)
		er_name.append("Error:Syntax Error Near")
		er.append(107)
		er_speci.append(p1[0])		
	elif p1[1] not in reg:
		er_li.append(li)
		er_name.append("Error:undefined register")
		er.append(108)
		er_speci.append(p1[1])		
	elif p1[2] in reg:
		pass
	elif p1[2] not in sym_name:
		try:
			k=int(p1[2])
			#lit_name.append("lit")
			hexint='%.2X' % k
			lit_hexval.append(hexint)
			lit_actualval.append(p1[2])
		except ValueError:
			er_li.append(li)
			er_name.append("Error:undefined")
			er.append(109)
			er_speci.append(p1[2])		
			
	
def gen_lit(filename):
	for i in range(len(sym_type1)):
		if sym_type1[i]=="db":
			hexnum="".join(sym_value[i])
			lit_actualval.append(sym_value[i])
			temp=[]
			for i in range(len(hexnum)):
				mychr=ord(hexnum[i])
				hexstr='%.2X' % mychr
				temp.append(hexstr)
			g="".join(temp)
			lit_hexval.append(g)
		elif sym_type1[i]=="dd":
			lit_actualval.append(sym_value[i])
			t=sym_value[i].split(',')
			temp=[]
			for j in range(len(t)):
				lv=int(t[j])
				hexint='%.2X' % lv
				temp.append(hexint)
			o="".join(temp)
			lit_hexval.append(o)
				
				
def inter_code(filenmae):
	with open(filename,"r") as file:
		s=[]
		if fnmatch.fnmatch(filename, '*.asm'):
			inter_file=os.path.splitext(filename)[0]
			li=[inter_file,'i']
			inter_file=".".join(li)
			f=1
			with open(inter_file,"w") as fd:
				for line in file:
					if "dd" in line:
						l1=line.split()
						for i in range(len(lit_name)):
							if l1[2] in lit_actualval[i]:	
								l1[2]=lit_name[i]
								l2=str(" ".join(l1))
								fd.write(l2)
								fd.write('\n')
								break
					elif "db" in line:
						l1=line.split('"')
						#print(l1)
						for i in range(len(lit_name)):
							if l1[1] in lit_actualval[i]:	
								l1[1]=lit_name[i]
								fd.write('"'.join(l1))
								break
					elif "main" in line:
						fd.write(line)
						after_main1(line,file,fd)
						break
				
					else:
						fd.write(line)
			
def after_main1(line,file,fd):
	for line in file:
		temp=[]
		line1=line.replace("\t","")
		line2=line1.replace("\n","")
		l1=line2.replace(","," ")
		l2=l1.split(" ")
		#print(l2)
		len_l2=len(l2)
		if len_l2==1:
			fd.write("".join(l2))
		elif len_l2==2:
			fd.write(" ".join(l2))
		elif len_l2==3:
			if l2[0] in inst2:
				temp.append(l2[0])
				if l2[1] in myreg.keys():
					k=l2[1]
					temp.append(myreg[k])
				if l2[2] in myreg.keys():
					k1=l2[2]
					temp.append(myreg[k1])
				if l2[2] in lit_actualval:
					for i in range(len(lit_actualval)):
						if l2[2]==lit_actualval[i]:
							temp.append(lit_name[i])
				if l2[2] in sym_name:
					for i in range(len(sym_name)):
						if l2[2]==sym_name[i]:
							temp.append(sym_name[i])
		elif len_l2==4:
			temp.append(l2[0])
			if l2[1] in inst2:
				temp.append(l2[1])
				if l2[2] in myreg.keys():
					k=l2[2]
					temp.append(myreg[k])
				if l2[3] in myreg.keys():
					k1=l2[3]
					temp.append(myreg[k1])
				if l2[3] in lit_actualval:
					for i in range(len(lit_actualval)):
						if l2[3]==lit_actualval[i]:
							temp.append(lit_name[i])
				if l2[3] in sym_name:
					for i in range(len(sym_name)):
						if l2[3]==sym_name[i]:
							temp.append(sym_name[i])



		fd.write('\t')
		fd.write(" ".join(temp))
		fd.write("\n")
				
		#print(l2)
					
				
					
if __name__=='__main__':
	if len(argv)<2:
		print("Error:Specify file name")
	else:
		filename=argv[1]
		if fnmatch.fnmatch(filename, '*.asm'):
			generate_sym(filename)
			gen_lit(filename)
			check_inst(filename)
			if len(er)==0:
				print("\n\n\t\t-----------******Symbol Table******--------------\n\n")		
				print("sym_name","sym_size","sym_DU","sym_type","line_no","section","sym_value")			
				for i in range(len(sym_name)):
					print(sym_name[i],'\t',sym_size[i],'\t',sym_DU[i],'\t',sym_type[i],'\t',line_no[i],'\t',section[i],'\t',sym_type1[i],'\t',sym_value[i])
		
				temp=[]
				print("\n\n\t\t-----------******Literal Table******--------------\n\n")
				for i in range(len(lit_name)):
					temp.append(lit_name[i])
					temp.append('{}'.format(i))
					d="".join(temp)
					lit_name[i]=d
					temp=[]
				for i in range(len(lit_hexval)):
					lname=['lit']
					lname.append(str(i))
					lname="".join(lname)
					lit_name.append(lname)	
					print(lit_name[i],'\t',lit_actualval[i],'\t',lit_hexval[i])
				inter_code(filename)		
			else:
				for i in range(len(er)):
					print(filename,':',er_li[i],':',er_name[i],'"',er_speci[i],'"')	
		else:
			print("Warrning:Please Specify only .asm file")	


