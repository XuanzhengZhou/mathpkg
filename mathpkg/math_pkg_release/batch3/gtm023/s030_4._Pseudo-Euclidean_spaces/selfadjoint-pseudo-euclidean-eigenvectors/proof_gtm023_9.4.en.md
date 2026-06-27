---
role: proof
locale: en
of_concept: selfadjoint-pseudo-euclidean-eigenvectors
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Consider the symmetric bilinear functions
$$\Phi(x, y) = (\varphi x, y) \quad \text{and} \quad \Psi(x, y) = (x, y).$$
The hypothesis $(x, \varphi x) \neq 0$ for all light-vectors $x$ implies that $\Phi$ and $\Psi$ never vanish simultaneously on a non-zero vector: if $\Phi(x, x) = 0$ and $\Psi(x, x) = 0$, then $(x, x) = 0$ (so $x$ is a light-vector) and $(x, \varphi x) = 0$, contradicting the assumption. Hence
$$\Phi(x)^2 + \Psi(x)^2 > 0 \quad \text{for all vectors } x \neq 0.$$

The theorem of section 9.11 (on pairs of symmetric bilinear functions) applies to $\Phi$ and $\Psi$, showing that there exists an orthonormal basis $e_v\ (v = 1 \ldots n)$ such that
$$(\varphi e_v, e_\mu) = \lambda_v \varepsilon_v \delta_{v\mu} \quad (v, \mu = 1 \ldots n).$$
These relations imply that
$$\varphi e_v = \lambda_v \varepsilon_v e_v \quad (v = 1 \ldots n),$$
so the $e_v$ are eigenvectors of $\varphi$.
