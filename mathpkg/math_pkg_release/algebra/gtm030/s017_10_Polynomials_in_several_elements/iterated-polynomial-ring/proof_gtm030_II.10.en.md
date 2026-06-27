---
role: proof
locale: en
of_concept: iterated-polynomial-ring
source_book: gtm030
source_chapter: "II"
source_section: "10"
---

By induction on $r$. The case $r = 1$ is trivial. Assume the statement holds for $s-1$ and consider $A[u_1, \cdots, u_s]$. This ring contains $A[u_1, \cdots, u_{s-1}]$ and $u_s$, hence it contains $A[u_1, \cdots, u_{s-1}][u_s]$. Conversely, $A[u_1, \cdots, u_{s-1}][u_s]$ is a subring containing $u_1, \cdots, u_s$, hence it contains $A[u_1, \cdots, u_s]$. Thus $A[u_1, \cdots, u_s] = A[u_1, \cdots, u_{s-1}][u_s] = A[u_1] \cdots [u_{s-1}][u_s]$ by the induction hypothesis.
