---
role: proof
locale: en
of_concept: pullback-as-universal-construction
source_book: gtm004
source_chapter: "II"
source_section: "8"
---

# Proof of Pull-back as a Universal Construction

Let $\mathfrak{L}$ be the category with three objects and two non-identity morphisms $\bullet \to \bullet \leftarrow \bullet$. A functor $\mathfrak{L} \to \mathfrak{C}$ is a diagram $(\varphi: A \to X, \psi: B \to X)$ in $\mathfrak{C}$. Let $\mathfrak{C}^{\mathfrak{L}}$ be the functor category and let $F: \mathfrak{C} \to \mathfrak{C}^{\mathfrak{L}}$ be the constant functor sending $Z$ to the constant diagram $(1_Z, 1_Z)$.

Suppose $F \dashv G$ with counit $\pi: FG \to 1_{\mathfrak{C}^{\mathfrak{L}}}$. For a diagram $(\varphi, \psi) \in \mathfrak{C}^{\mathfrak{L}}$, let $G(\varphi, \psi) = Y \in \mathfrak{C}$ and let

$$\pi_{(\varphi, \psi)}: F(Y) \to (\varphi, \psi)$$

be the component of the counit. In $\mathfrak{C}$, this counit consists of two morphisms $\alpha: Y \to A$, $\beta: Y \to B$ such that $\varphi \circ \alpha = \psi \circ \beta$ (since $\pi$ is a morphism in the functor category, i.e., a commutative diagram in $\mathfrak{C}$).

Now, a morphism $(\gamma, \delta): F(Z) \to (\varphi, \psi)$ in $\mathfrak{C}^{\mathfrak{L}}$ is precisely a pair $\gamma: Z \to A$, $\delta: Z \to B$ with $\varphi \circ \gamma = \psi \circ \delta$. By the adjunction property (7.3),

$$\pi_{(\varphi, \psi)} \circ F(\eta(\gamma, \delta)) = (\gamma, \delta),$$

where $\eta$ is the adjugant. This yields $\alpha \circ \eta(\gamma, \delta) = \gamma$ and $\beta \circ \eta(\gamma, \delta) = \delta$. The uniqueness of $\zeta = \eta(\gamma, \delta)$ follows from the fact that $\eta$ is a bijection.

Thus $(Y; \alpha, \beta)$ satisfies the universal property of the pull-back of $\varphi$ and $\psi$.
