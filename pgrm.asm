section .data
	s dd 10,20,30,40
	y dd 50,60,70,80
	str1 db "abcdef ghijklmn",10,0
	str2 db "hello sid",0
	msg db "sid pucsd",0
	q dd 10,20,30,40
	e dd 50,60,70,80
	t db "abcdef ghijklmn",10,0
	o db "hello sid",0
	1 db "sid pucsd",0
section .bss
	str resd 1
section .text
	global main
main:
	mov eax,ebx
	mov ebx,ecx
	mov ecx,edx
	mov esi,edi
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
abc: 	
	xor ebx,ebx
	jmp abc
bcf:



	
