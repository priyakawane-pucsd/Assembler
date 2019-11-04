section .data
s dd lit0
y dd lit1
	str1 db "lit2",10,0
	str2 db "lit3",0
	msg db "lit4",0
q dd lit0
e dd lit1
	t db "lit2",10,0
	o db "lit3",0
	1 db "lit4",0
section .bss
	str resd 1
section .text
	global main
main:	
	mov R0 R3
	mov R3 R2
	mov R2 R1
	mov R4 R5
	mov R5 R6
	xor R0 lit10
	xor R0 lit11
	xor R0 str1
abc: 	
	xor R3 R3
jmp abc	
bcf:	
	
	
	
	
