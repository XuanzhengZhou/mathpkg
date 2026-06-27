---
role: proof
locale: en
of_concept: eigenvalues-are-roots-of-minimum-polynomial
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

A scalar $\lambda \in \Gamma$ is an eigenvalue of $\varphi$ if and only if there exists a non-zero vector $x \in E$ with $\varphi x = \lambda x$, i.e., $(\varphi - \lambda \iota)x = 0$. This is equivalent to $K(t - \lambda) \neq 0$.

By Corollary I to Proposition III, $K(t - \lambda) = 0$ if and only if $t - \lambda$ and $\mu$ are relatively prime. Since $\deg(t - \lambda) = 1$, being non-relatively-prime to $\mu$ is equivalent to $(t - \lambda) \mid \mu$. Thus $K(t - \lambda) \neq 0$ iff $(t - \lambda) \mid \mu$, which means $\mu(\lambda) = 0$.

Hence the eigenvalues of $\varphi$ are precisely the distinct roots of $\mu$.
