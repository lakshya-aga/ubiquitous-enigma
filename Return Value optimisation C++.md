


Compiler generates code to directly construct item in return object rather than do a copy if the item returned is a local variable of the function
![[Screenshot 2026-06-30 at 5.54.45 AM.png]]
When forced to an rvalue, compiler cannot do elision and costs more. see extra ops after the s=string(temp);

![[Screenshot 2026-06-30 at 5.55.16 AM.png]]
