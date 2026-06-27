---
role: proof
locale: en
of_concept: self-duality-of-z-nz
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Proof.**

Fix a primitive $n$-th root of unity $\zeta$. Define the map $\varphi: \mathbb{Z}/n\mathbb{Z} \to \widehat{\mathbb{Z}/n\mathbb{Z}}$ by sending $x \in \mathbb{Z}/n\mathbb{Z}$ to the character $\varphi_x$ given by

$$\varphi_x(y) = \zeta^{xy} \quad \text{for all } y \in \mathbb{Z}/n\mathbb{Z}.$$

Each $\varphi_x$ is indeed a homomorphism from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{C}^\times$, since

$$\varphi_x(y_1 + y_2) = \zeta^{x(y_1 + y_2)} = \zeta^{xy_1} \zeta^{xy_2} = \varphi_x(y_1) \varphi_x(y_2).$$

The map $\varphi$ is a group homomorphism: $\varphi_{x_1 + x_2}(y) = \zeta^{(x_1+x_2)y} = \zeta^{x_1y}\zeta^{x_2y} = \varphi_{x_1}(y)\varphi_{x_2}(y)$.

If $\varphi_x$ is the trivial character, then $\zeta^{xy} = 1$ for all $y \in \mathbb{Z}/n\mathbb{Z}$. Taking $y = 1$ gives $\zeta^x = 1$, which implies $x \equiv 0 \pmod{n}$. Hence $\varphi$ is injective.

Since $|\widehat{\mathbb{Z}/n\mathbb{Z}}| = n = |\mathbb{Z}/n\mathbb{Z}|$, injectivity implies surjectivity. Therefore $\varphi$ is an isomorphism, establishing the self-duality of $\mathbb{Z}/n\mathbb{Z}$ under the pairing $(x, y) \mapsto \zeta^{xy}$.
