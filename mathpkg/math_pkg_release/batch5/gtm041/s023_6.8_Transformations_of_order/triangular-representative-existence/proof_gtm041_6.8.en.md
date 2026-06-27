---
role: proof
locale: en
of_concept: triangular-representative-existence
source_book: gtm041
source_chapter: "6"
source_section: "6.8"
---

Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma(n)$. Since $\gcd(a, c)$ divides $\det(A) = n$, we can find integers $r$ and $s$ such that $ra + sc = 0$ and $\gcd(r, s) = 1$. Next we choose two integers $p$ and $q$ such that $ps - qr = 1$ and let
$$V = \begin{pmatrix} p & q \\ r & s \end{pmatrix}.$$
Then $V \in \Gamma$ and
$$VA = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} pa + qc & pb + qd \\ ra + sc & rb + sd \end{pmatrix}.$$
Since $ra + sc = 0$ and $\det(VA) = \det V \det A = n$, we see that $VA \in \Gamma(n)$ so $VA \sim A$. Hence $VA$ or its negative is the required representative.
