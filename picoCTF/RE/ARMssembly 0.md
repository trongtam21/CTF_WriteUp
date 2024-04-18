## Description 
> What integer does this program print with arguments 182476535 and 3742084308? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Link challenge 
> https://play.picoctf.org/practice/challenge/160?assigned=0&category=3&page=1&solved=1
## Solution 
- Sau khi tải file về và mở lên với notepad em được 1 đoạn mã arm như sau 
```
	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

```
- Để đọc được em dùng chatgpt để convert qua python
```
def func1(w0, w1):
    if w1 <= w0:
        return w0
    else:
        return w1

def main():
    # Giả lập bộ nhớ stack
    stack = [0] * 64
    sp = 0

    # Giả lập các đối số được truyền vào main
    stack[sp + 44] = int(input("Nhập số thứ nhất: "))
    stack[sp + 32] = int(input("Nhập số thứ hai: "))

    # Tương đương với: w19 = int(input("Nhập số thứ nhất: "))
    w19 = stack[sp + 44]

    # Tương đương với: w1 = int(input("Nhập số thứ hai: "))
    w1 = stack[sp + 32]

    # Tương đương với: kết_quả = func1(w19, w1)
    ket_qua = func1(w19, w1)

    # Tương đương với: printf("Kết quả: %ld\n", kết_quả)
    print("Kết quả:", ket_qua)

    return 0

if __name__ == "__main__":
    main()
```
- Nếu đối số là 182476535 và 3742084308 ta sẽ có kết quả là 3742084308 (chuyển qua hex là DF0BACD4)
> Flag : picoCTF{df0bacd4}