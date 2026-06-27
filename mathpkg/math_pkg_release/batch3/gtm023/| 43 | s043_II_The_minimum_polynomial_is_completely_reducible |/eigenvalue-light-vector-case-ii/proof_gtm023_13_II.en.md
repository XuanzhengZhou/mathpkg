---
role: proof
locale: en
of_concept: eigenvalue-light-vector-case-ii
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

Since the minimum polynomial $\mu$ of $\varphi$ is completely reducible (splits into linear factors over the base field), the existence of eigenvalues $\lambda$ and $1/\lambda$ follows from the fact that not all roots of $\mu$ are equal to $1$. Because $\varphi$ is a Lorentz transformation, it preserves the Minkowski inner product, and the eigenvalues occur in reciprocal pairs: if $\lambda$ is an eigenvalue with eigenvector $e$, then $\varphi^{-1}$ has eigenvalue $1/\lambda$ with the same eigenvector $e$, but more directly, the condition that $\mu$ is not purely a power of $(t-1)$ forces the existence of at least one eigenvalue $\lambda \neq 1$, and the reciprocal $1/\lambda$ also appears as an eigenvalue.

Let $e$ and $e'$ be eigenvectors corresponding to $\lambda$ and $1/\lambda$ respectively:

$$\varphi e = \lambda e, \quad \varphi e' = \frac{1}{\lambda} e'.$$

Since $\lambda \neq 1$, we have $(e, e) = (1/\lambda^2)(e, e)$ from the invariance of the inner product under $\varphi$, which forces $(e, e) = 0$. The same argument shows $(e', e') = 0$. Thus $e$ and $e'$ are light-vectors (vectors lying on the light-cone).

The linear independence of $e$ and $e'$ follows because they belong to distinct eigenvalues ($\lambda \neq 1/\lambda$ since $\lambda \neq \pm 1$). For two linearly independent light-vectors in a Minkowski space, section 9.21 of the book shows that their inner product cannot vanish, hence $(e, e') \neq 0$.
