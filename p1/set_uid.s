/* set_uid.s */
.globl main
main:
	xorl %ebx, %ebx           /* set ebx to 0 */
	leal 0x17(%ebx), %eax     /* set eax to 0x17 */
	int $0x080                /* sofware interrupt 0x80 */
	
