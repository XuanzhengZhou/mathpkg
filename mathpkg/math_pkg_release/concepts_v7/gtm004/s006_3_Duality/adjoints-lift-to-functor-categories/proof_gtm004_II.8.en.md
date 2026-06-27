---
role: proof
locale: en
of_concept: adjoints-lift-to-functor-categories
source_book: gtm004
source_chapter: "II"
source_section: "8"
---

# Proof of Adjoints Lift to Functor Categories

Let $F \dashv G$ with $F: \mathfrak{C} \to \mathfrak{D}$, $G: \mathfrak{D} \to \mathfrak{C}$, and let $\mathfrak{P}$ be a small category. Define the induced functors

$$F^{\mathfrak{P}}: \mathfrak{C}^{\mathfrak{P}} \to \mathfrak{D}^{\mathfrak{P}}, \qquad G^{\mathfrak{P}}: \mathfrak{D}^{\mathfrak{P}} \to \mathfrak{C}^{\mathfrak{P}}$$

by post-composition: for a functor $H: \mathfrak{P} \to \mathfrak{C}$, set $F^{\mathfrak{P}}(H) = F \circ H$, and similarly for $G^{\mathfrak{P}}$. For natural transformations, the action is component-wise.

Let $\eta: \mathfrak{D}(FX, Y) \cong \mathfrak{C}(X, GY)$ be the adjugant equivalence for $F \dashv G$. For functors $A: \mathfrak{P} \to \mathfrak{C}$ and $B: \mathfrak{P} \to \mathfrak{D}$, we construct a natural equivalence

$$\tilde{\eta}_{A,B}: \mathfrak{D}^{\mathfrak{P}}(F^{\mathfrak{P}}(A), B) \cong \mathfrak{C}^{\mathfrak{P}}(A, G^{\mathfrak{P}}(B)).$$

Given a natural transformation $\varphi: F \circ A \Rightarrow B$ (i.e., a morphism in $\mathfrak{D}^{\mathfrak{P}}$), define $\tilde{\eta}(\varphi): A \Rightarrow G \circ B$ component-wise by

$$\tilde{\eta}(\varphi)_P = \eta_{A(P), B(P)}(\varphi_P): A(P) \to G(B(P)), \quad P \in \mathfrak{P}.$$

The naturality of $\eta$ (equation 7.1) ensures that $\tilde{\eta}(\varphi)$ is indeed a natural transformation. The inverse is defined similarly using $\xi = \eta^{-1}$, giving $\tilde{\xi}(\psi)_P = \xi_{A(P), B(P)}(\psi_P)$. Thus $\tilde{\eta}$ is a natural equivalence, establishing $F^{\mathfrak{P}} \dashv G^{\mathfrak{P}}$.
