---
role: proof
locale: en
of_concept: ufd-primitive-polynomial-irreducibility
source_book: gtm028
source_chapter: "II"
source_section: "§13. Separably generated fields of algebraic functions"
---

\begin{proof}
(1) Let $f(X) \in R[X]$ be primitive and irreducible in $R[X]$. Suppose $f(X) = f_1(X) f_2(X)$ in $K[X]$. By clearing denominators, we may assume $f_1, f_2 \in R[X]$ after multiplying by a suitable element of $R$. Since $f$ is irreducible in $R[X]$, one factor, say $f_1$, must have degree zero. Then $f_1(X) = a \in R$ is a constant. But $f$ is primitive and $f = a f_2$, so $a$ must divide the content of $f$ in $R$, hence $a$ is a unit in $R$. Thus $\partial f_2 = \partial f > 0$ and $f_2$ is not a unit in $K[X]$. Since $f$ has positive degree, it is not a unit in $K[X]$. Consequently $f(X)$ is an irreducible element in $K[X]$.

(2) Assume that $f(X) = f_1(X) f_2(X)$ where $f_1(X), f_2(X) \in R[X]$. Since $f(X)$ is irreducible in $K[X]$, one of the polynomials $f_i(X)$ must be of degree zero. Let, say, $\partial f_1 = 0$, whence $f_1(X) = a \in R$. From $f(X) = a f_2(X)$ it follows that $a$ divides, in $R$, the content of $f(X)$, and hence $a$ is a unit in $R$ since $f(X)$ is primitive. This shows that $f(X)$ is an irreducible element of $R[X]$.

(3) We have, by assumption: $f(X) = g(X) \cdot h(X)/a$, where $h(X) \in R[X]$ and $a \in R$. Thus $g(X)$ divides $a f(X)$ in $R[X]$. Since $g(X)$ is primitive, it follows from I, \S 17, Lemma 2, that $g(X)$ divides $f(X)$ in $R[X]$.
\end{proof}
