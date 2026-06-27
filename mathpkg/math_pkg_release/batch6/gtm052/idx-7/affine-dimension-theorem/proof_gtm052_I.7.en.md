---
role: proof
locale: en
of_concept: affine-dimension-theorem
source_book: gtm052
source_chapter: "I"
source_section: "7"
---
We proceed in several steps. First, suppose that $Z$ is a hypersurface, defined by an equation $f = 0$. If $Y \subseteq Z$, there is nothing to prove. If $Y \not\subseteq Z$, we must show that each irreducible component $W$ of $Y \cap Z$ has dimension $r - 1$. Let $A(Y)$ be the affine coordinate ring of $Y$. Then the irreducible components of $Y \cap Z$ correspond to the minimal prime ideals $\mathfrak{p}$ of the principal ideal $(\bar{f})$ in $A(Y)$. Now by Krull's Hauptidealsatz (1.11A), each such $\mathfrak{p}$ has height one, so by the dimension theorem, $\dim A(Y)/\mathfrak{p} = \dim A(Y) - 1 = r - 1$, as required.

For the general case, consider the affine cones $C(Y), C(Z)$ in $\mathbf{A}^{n+1}$. Then $C(Y), C(Z)$ have dimensions $r+1, s+1$, respectively. The intersection $C(Y) \cap C(Z)$ contains the origin, so by the hypersurface case applied repeatedly, each irreducible component has dimension $\geq (r+1) + (s+1) - (n+1) = r + s - n + 1$. Projecting back to $\mathbf{A}^n$ gives the result for $Y \cap Z$.
