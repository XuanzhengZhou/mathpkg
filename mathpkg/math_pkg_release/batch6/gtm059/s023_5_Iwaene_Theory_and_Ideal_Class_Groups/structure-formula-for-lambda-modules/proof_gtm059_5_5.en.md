---
role: proof
locale: en
of_concept: structure-formula-for-lambda-modules
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
\textbf{Case (i):} $V = \Lambda/(p^m)$. Here $\Lambda/(p^m)$ is a free $\mathbb{Z}/p^m\mathbb{Z}[[X]]$-module of rank 1 as a $\mathbb{Z}_p$-module. One computes that $|V_n| = p^{m p^n}$, so $s_n(V) = m p^n$.

\textbf{Case (ii):} $V = \Lambda/(f)$ with $f$ distinguished of degree $d$. The Weierstrass Preparation Theorem implies that $f$ differs from a monic polynomial of degree $d$ by a unit. Modulo $\gamma^{p^n}-1$, one obtains a module of size related to $p^{dn}$, giving $s_n(V) = dn + c$ for large $n$.

\textbf{Case (iii):} The general case follows from the structure theorem (Theorem 3.1), which gives a quasi-isomorphism of $V$ with a direct sum of modules of types (i) and (ii). The additivity of $s_n$ under direct sums (up to finite kernel/cokernel) yields the formula $s_n(V) = \mu p^n + \lambda n + \nu$, where $\mu = \sum m_i$ (sum of the $p$-power torsion exponents) and $\lambda = \sum \deg f_j$ (sum of the degrees of the distinguished polynomial factors).
