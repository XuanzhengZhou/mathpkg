---
role: proof
locale: en
of_concept: case-iii-minimum-polynomial
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

The classification of Lorentz transformations into Cases I, II, III is based on the structure of the minimum polynomial $\mu$ of $\varphi$. Case III is defined by the condition that the only eigenvalue is $1$, so $\mu = (t-1)^k$ for some $k$.

The upper bound $k \leq 4$ follows from the Cayley-Hamilton theorem: the dimension of the Minkowski space $E$ is $4$, so the characteristic polynomial has degree $4$, and the minimum polynomial divides the characteristic polynomial, hence $\deg \mu \leq 4$. The lower bound $k \geq 1$ is trivial since $\mu$ is monic and non-constant for any linear transformation.

If $k = 1$, then $\mu = t - 1$, which means $\varphi - \iota = 0$, i.e., $\varphi = \iota$, the identity transformation.

To show $k = 2$ is impossible: assume $k = 2$, so $(\varphi - \iota)^2 = 0$. Applying $\varphi^{-1}$ (which exists since $\varphi$ is a Lorentz transformation and hence invertible) to this equation yields $(\iota - \varphi^{-1})^2 = 0$, which implies $(\varphi^{-1} - \iota)^2 = 0$. This would force the space to decompose into $2$-dimensional invariant subspaces, contradicting the structure of the Minkowski inner product (specifically, the impossibility of a nontrivial Jordan block of size $2$ while preserving the indefinite inner product of index $1$). Hence $k \neq 2$.
