---
role: proof
locale: en
of_concept: properties-of-r-homomorphisms
source_book: gtm028
source_chapter: "III"
source_section: "3"
---

Let $T$ be an $R$-homomorphism of $M$ into $M'$.

For (2): Let $A$ be an ideal of $R$ and $L$ an $R$-submodule of $M$. If $a_i \in A$ and $x_i \in L$, $i = 1, 2, \dots, n$, then
$$
\Bigl(\sum a_i x_i\Bigr) T = \sum (a_i x_i) T = \sum a_i (x_i T) \in A(LT),
$$
which shows $(AL)T \subset A(LT)$. Conversely, any element of $A(LT)$ is of the form $\sum a_i y_i$ with $y_i \in LT$, so $y_i = x_i T$ for some $x_i \in L$. Then $\sum a_i y_i = \sum a_i (x_i T) = (\sum a_i x_i) T \in (AL)T$, whence $A(LT) \subset (AL)T$. Thus $(AL)T = A(LT)$.

For (3): Let $N$ denote the kernel of $T$; $N$ consists of all $x \in M$ such that $xT = 0$. By Theorem 1 of I, \S 11, $N$ is a subgroup of $M$; it is a submodule since
$$
(RN)T \subset R(NT) \subset R \cdot 0 = (0),
$$
hence $RN \subset N$. For the second part, let $L'$ be an $R$-submodule of $M'$. If $x, y \in L'T^{-1}$, then $xT, yT \in L'$, hence $(x - y)T = xT - yT \in L'$, so $x - y \in L'T^{-1}$. If $a \in R$, then $(ax)T = a(xT) \in L'$, hence $ax \in L'T^{-1}$. Thus $L'T^{-1}$ is an $R$-submodule of $M$. Similarly, if $L$ is an $R$-submodule of $M$, then $LT$ is an $R$-submodule of $M'$, which is statement (1).
