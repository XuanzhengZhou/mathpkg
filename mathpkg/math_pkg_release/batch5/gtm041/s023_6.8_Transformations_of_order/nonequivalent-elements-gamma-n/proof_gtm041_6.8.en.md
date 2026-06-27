---
role: proof
locale: en
of_concept: nonequivalent-elements-gamma-n
source_book: gtm041
source_chapter: "6"
source_section: "6.8"
---

Theorem 6.7 shows that every element in $\Gamma(n)$ is equivalent to one of the transformations in (18). Therefore we need only show that two such transformations, say
$$A_1 = \begin{pmatrix} a_1 & b_1 \\ 0 & d_1 \end{pmatrix} \quad \text{and} \quad A_2 = \begin{pmatrix} a_2 & b_2 \\ 0 & d_2 \end{pmatrix},$$
are equivalent if, and only if,
$$a_1 = a_2, \quad d_1 = d_2, \quad \text{and} \quad b_1 \equiv b_2 \pmod{d_1}.$$

If (19) holds then $b_2 = b_1 + q d_1$ for some integer $q$ and we can take
$$V = \begin{pmatrix} 1 & q \\ 0 & 1 \end{pmatrix} \in \Gamma,$$
so that $V A_1 = A_2$, proving $A_1 \sim A_2$.

Conversely, if $A_1 \sim A_2$, there exists $V = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \in \Gamma$ such that $A_1 = V A_2$. Then
$$\begin{pmatrix} a_1 & b_1 \\ 0 & d_1 \end{pmatrix} = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \begin{pmatrix} a_2 & b_2 \\ 0 & d_2 \end{pmatrix} = \begin{pmatrix} p a_2 & p b_2 + q d_2 \\ r a_2 & r b_2 + s d_2 \end{pmatrix}.$$
The bottom-left entry gives $r a_2 = 0$, and since $a_2 = n/d_2 \neq 0$, we have $r = 0$. Then $\det V = ps = 1$ implies $s = 1$ (identifying $V$ with $-V$). Hence $p = 1$, so $a_1 = a_2$ and $d_1 = d_2$. From the top-right entry, $b_1 = b_2 + q d_2 = b_2 + q d_1$, so $b_1 \equiv b_2 \pmod{d_1}$.
