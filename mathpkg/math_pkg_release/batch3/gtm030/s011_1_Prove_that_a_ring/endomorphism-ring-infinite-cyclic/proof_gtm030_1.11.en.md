---
role: proof
locale: en
of_concept: endomorphism-ring-infinite-cyclic
source_book: gtm030
source_chapter: "1"
source_section: "1.11"
---
Let $\mathfrak{G} = I_{+}$ be the additive group of integers, which is infinite cyclic with generator $1$. Let $\mathfrak{E}$ be its endomorphism ring.

Define $\varphi: \mathfrak{E} \to I$ by $\varphi(\eta) = 1\eta$, the image of the generator under $\eta$.

**Well-defined and injective:** Since $\eta$ is an endomorphism, we have $n\eta = n(1\eta)$ for all integers $n$, because by additivity $\eta(n) = n \cdot \eta(1) = n \cdot 1\eta$. Thus an endomorphism is completely determined by its effect on the generator $1$. If $\varphi(\eta) = \varphi(\rho)$, then $1\eta = 1\rho$, so $n\eta = n\rho$ for all $n$, hence $\eta = \rho$. Therefore $\varphi$ is injective.

**Surjective:** For any integer $u \in I$, define $\eta_u: I_{+} \to I_{+}$ by $n\eta_u = nu$. Then
$$(n+m)\eta_u = (n+m)u = nu + mu = n\eta_u + m\eta_u,$$
so $\eta_u$ is an endomorphism, and $\varphi(\eta_u) = 1\eta_u = u$. Thus $\varphi$ is surjective.

**Additive homomorphism:** If $\varphi(\eta) = u$ and $\varphi(\rho) = v$, then
$$\varphi(\eta + \rho) = 1(\eta + \rho) = 1\eta + 1\rho = u + v = \varphi(\eta) + \varphi(\rho).$$

**Multiplicative homomorphism:** For composition,
$$\varphi(\eta\rho) = 1(\eta\rho) = (1\eta)\rho = u\rho = uv = \varphi(\eta)\varphi(\rho),$$
using the fact that $\rho$ applied to $u$ (as a group element) gives $u \cdot 1\rho = uv$, since $u\rho = u \cdot v$ by the endomorphism property on the generator $1$.

Therefore $\varphi$ is a ring isomorphism $\mathfrak{E} \cong I$.
