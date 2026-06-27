---
role: proof
locale: en
of_concept: jordan-canonical-form
source_book: gtm049
source_chapter: "7"
source_section: "7.5"
---

Suppose first that $V_f$ is cyclic with $m_a(X) = (X - x)^n$. It follows from the definition of $m_a(X)$ that
$$a, (X - x)a, \ldots, (X - x)^{n-1}a$$
are linearly independent. Set $v_i = (X - x)^{i-1}a$ for $i = 1, \ldots, n$. Then
$$(X - x)v_i = v_{i+1}, \quad i = 1, \ldots, n-1,$$
and
$$(X - x)v_n = 0.$$
Writing these relations in terms of $f$, we obtain
\begin{align*}
v_1 f &= x v_1 + v_2, \\
v_2 f &= x v_2 + v_3, \\
&\;\;\vdots \\
v_{n-1} f &= x v_{n-1} + v_n, \\
v_n f &= x v_n.
\end{align*}
Therefore, with respect to the ordered basis $(v_1, \ldots, v_n)$, the matrix of $f$ is the $n \times n$ Jordan block $C$ with eigenvalue $x$.

Now for the general case, the elementary divisor decomposition (Theorem 2) expresses $V_f$ as a direct sum of cyclic submodules whose annihilators are powers of linear factors $(X - x_i)^{n_{ij}}$. Applying the above construction to each cyclic summand yields a basis for which the matrix of $f$ restricted to that summand is the Jordan block $C_{ij}$. Concatenating these bases produces the full Jordan canonical form.
