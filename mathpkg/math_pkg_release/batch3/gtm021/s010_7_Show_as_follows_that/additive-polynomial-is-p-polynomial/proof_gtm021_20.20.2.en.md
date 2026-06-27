---
role: proof
locale: en
of_concept: additive-polynomial-is-p-polynomial
source_book: gtm021
source_chapter: "20"
source_section: "20.2"
---

Use induction on the degree of $f(T)$ and denote by $(D_i f)(T)$ the partial derivative of $f(T)$ with respect to $T_i$. From the assumed identity $f(T_1 + a_1, \ldots, T_n + a_n) = f(T) + f(a)$ for all $(a) \in K^n$, we obtain $(D_i f)(T + a) = (D_i f)(T)$. Therefore $(D_i f)(T)$ takes constant value $c_i$ on $K^n$, and all partial derivatives of $f(T) - (c_1 T_1 + \cdots + c_n T_n)$ are 0. Any polynomial with vanishing partial derivatives has the form $g(T_1^p, \ldots, T_n^p)$. Since $K$ is algebraically closed, $a_i = d_i^p$, $b_i = e_i^p$ for some $d_i, e_i \in K$. Then $g(a+b) = g((d_1+e_1)^p, \ldots) = f(d+e) - \sum c_i(d_i+e_i) = g(a) + g(b)$. Now $g(T)$ is additive but of smaller degree than $f(T)$, so by induction $g(T)$ (hence also $f(T)$) is a $p$-polynomial.
