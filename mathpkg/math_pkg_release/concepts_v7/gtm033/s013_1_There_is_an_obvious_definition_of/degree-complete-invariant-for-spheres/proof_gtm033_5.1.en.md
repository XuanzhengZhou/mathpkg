---
role: proof
locale: en
of_concept: degree-complete-invariant-for-spheres
source_book: gtm033
source_chapter: "5"
source_section: "1"
---

# Proof of Degree as Complete Homotopy Invariant for Maps into Spheres

**Theorem 5.1.10.** Let $M$ be a compact connected $n$-manifold, $n \geqslant 1$. Let $f, g: M \to S^n$ be continuous maps.

(a) If $M$ is oriented and $\partial M = \varnothing$, then $f \simeq g$ if and only if $\deg f = \deg g$; and there are maps of every degree $m \in \mathbb{Z}$.

(b) If $M$ is nonorientable and $\partial M = \varnothing$, then $f \simeq g$ if and only if $\deg_2 f = \deg_2 g$.

(c) If $\partial M \neq \varnothing$, then every map $f: M \to S^n$ is homotopic to a constant map; i.e., all maps $M \to S^n$ are null-homotopic.

*Proof of (a).* One direction follows immediately from Theorem 5.1.6(a): if $f \simeq g$, then homotopy invariance of the degree implies $\deg f = \deg g$.

For the converse, suppose $\deg f = \deg g$. We must construct a homotopy between $f$ and $g$. Consider the cylinder $M \times I$. Its boundary is
$$\partial(M \times I) = M \times \{0\} \cup M \times \{1\},$$
since $\partial M = \varnothing$. Define a map $H_0: \partial(M \times I) \to S^n$ by
$$H_0(x, 0) = f(x), \quad H_0(x, 1) = g(x).$$

The boundary $M \times \{1\}$ carries the opposite orientation to $M$ (by the product orientation convention for $\partial$-manifolds). Therefore the degree of $H_0$ on the boundary is
$$\deg(H_0) = \deg f - \deg g = 0.$$

By Theorem 5.1.8 (the Extension Theorem for oriented manifolds), a map $\partial W \to S^n$ extends to $W$ if and only if its degree is zero. Applying this to $W = M \times I$ and the boundary map $H_0$, we obtain an extension $H: M \times I \to S^n$ with $H|_{\partial(M \times I)} = H_0$. This extension is precisely a homotopy between $f$ and $g$.

The existence of maps of every degree follows from the construction of "winding maps." For $m \in \mathbb{Z}$, one can construct a map $S^n \to S^n$ of degree $m$ (e.g., the suspension of a map $S^{n-1} \to S^{n-1}$ of degree $m$, or by using $m$ "folds"). Composing with a degree-1 collapse map $M \to S^n$ (which exists since $M$ is compact and connected) yields a map $M \to S^n$ of degree $m$.

*Proof of (b).* The same argument applies using the mod 2 degree $\deg_2$ and the nonorientable analogue, Theorem 5.1.9: a map $\partial W \to S^n$ extends to a nonorientable $W$ if and only if $\deg_2 f = 0$.

*Proof of (c).* When $\partial M \neq \varnothing$, we can use a collar neighborhood of the boundary. Every map $f: M \to S^n$ can be deformed to factor through a collapse of a collar, eventually contracting $M$ onto a subset of lower dimension. Since $\dim M = n$ and the target is $S^n$, any such map factors through an $(n-1)$-dimensional spine up to homotopy, and is therefore null-homotopic. Alternatively, one can apply Theorem 5.1.8: embed $M$ as the boundary of some $(n+1)$-manifold and note that the extension condition is vacuously satisfied for a suitable construction.

QED

**Remarks.** This theorem is a form of the Hopf Degree Theorem. It reduces the classification of homotopy classes $[M, S^n]$ to the computation of the degree, an integer (or mod 2 integer). The proof combines three fundamental results: homotopy invariance (Theorem 5.1.6), the extension criterion (Theorems 5.1.8 and 5.1.9), and the fact that every integer can be realized as the degree of some map $M \to S^n$ when $M$ is closed and oriented.
