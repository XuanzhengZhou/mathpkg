---
role: proof
locale: en
of_concept: periodic-points-near-invariant-tori
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "E"
---

Since $A$ is homologous to the identity, $A^N_0$ has a single-valued global generating function of the form $Xy + S(X, y)$, where $S$ has period $2\pi$ in the variable $y$.

By the implicit function theorem, near the torus $x = x_0$, the mapping $A^N_0$ has a torus given by an equation $x = f(y)$ whose image is given by $x = g(y)$, with

$$X(f(y), y) = g(y), \quad Y(f(y), y) = y.$$

Consider the function $F(y) = S(X(f(y), y), y)$ on the $n$-dimensional torus parameterized by $y$. The fixed points of $A^N_0$ are exactly the critical points of $F$, because at a critical point we have $dF = 0$, and using the generating function relation

$$dS = (x - X)dy + (Y - y)dX,$$

the condition $dF(y) = 0$ implies $X(f(y), y) = f(y)$ and $Y(f(y), y) = y$, i.e., $(f(y), y)$ is a fixed point of $A^N_0$.

A smooth function on an $n$-dimensional torus has at least $2^n$ critical points, counting multiplicities (this follows from Morse theory or Lusternik-Schnirelman category). Therefore $A^N_0$ has at least $2^n$ fixed points, counting multiplicity, near the torus $x = x_0$. Since $A$ is sufficiently close to $A_0$, these fixed points persist as periodic points of period $N$ for $A$.

The proof could alternatively be reduced to investigating the intersection of two Lagrangian submanifolds of a $4n$-dimensional phase space $(\mathbb{R}^n \times \mathbb{T}^n \times \mathbb{R}^n \times \mathbb{T}^n)$ with symplectic form $\Omega = dx \wedge dy - dX \wedge dY$, one being the diagonal $(X = x, Y = y)$ and the other the graph of $A^N$.
