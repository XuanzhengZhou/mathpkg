---
role: exercise
locale: en
chapter: "3"
section: "Exercises"
exercise_number: 6
source_book: gtm026
---

In this exercise we relate the distributive laws of 3.6 to the distributive laws studied by Beck ([Beck '69]). Let $\mathbf{S} = (S, \eta, \mu)$ and $\mathbf{T} = (T, e, m)$ be algebraic theories in $\mathcal{H}$. A distributive law of $\mathbf{S}$ over $\mathbf{T}$ is a distributive law $\lambda: TS \longrightarrow ST$ of $S$ over $T$ satisfying the additional requirement that $\lambda$ is a theory map from $\mathbf{S}$ to $\mathbf{S}$ relative to $T$ in the sense of exercise 3.2.10, that is we require the diagrams:

(a) Let $X$ be an input process in $\mathcal{H}$ and let $\lambda: TX \longrightarrow XT$ be a distributive law of $X$ over $\mathbf{T}$. Recalling that $AX^@ T$ has $X$-dynamical structure $AX^@ \lambda A\mu_0 T: AX^@ TX \longrightarrow AX^@ T$, define $\bar{\lambda}: TX^@ \longrightarrow X^@ T$ as the unique dynamorphic extension

Prove that $\lambda \mapsto \bar{\lambda}$ establishes a bijective correspondence between distributive laws of $X$ over $\mathbf{T}$ and distributive laws of $X^@$ over $\mathbf{T}$.

If $\lambda: TS \longrightarrow ST$ is a distributive law of $\mathbf{S}$ over $\mathbf{T}$, a $\lambda$-algebra is $(Q, \gamma, \xi)$ where $(Q, \gamma)$ is an $\mathbf{S}$-algebra and $(Q, \xi)$ is a $\mathbf{T}$-algebra subject to the $\lambda$-law

(b) In the context of (a), prove that the category of $\lambda$-algebras is isomorphic to the category of $\bar{\lambda}$-algebras.

(c) If $\lambda$ is a distributive law of $\mathbf{S}$ over $\mathbf{T}$ then, mimicking the proof of 3.15, prove that $\mathcal{H}^\lambda \longrightarrow \mathcal{H}^S$ is algebraic and that $\mathcal{H}^\lambda \longrightarrow \mathcal{H}$ is algebraic with algebraic theory

$$\mathbf{ST} = (ST, \text{id} \xrightarrow{\eta e} ST, STST \xrightarrow{S\lambda T} SSTT \xrightarrow{\mu m} ST)$$

(d) If $\lambda$ is a distributive law of $\mathbf{S}$ over $\mathbf{T}$, prove that $\mathcal{H}^\lambda \longrightarrow \mathcal{H}^T$ is algebraic.

(e) This is the proper formulation of 3.8. Let $\mathcal{K} = \text{Set}$, let $S$ be the theory for monoids, and let $T$ be the theory for abelian groups. Prove that $\lambda: TS \longrightarrow ST$ defined by

$$QTS \xrightarrow{Q\lambda} QST$$

$$\prod_{i=1}^{m} \sum_{Q} n_{q,i} q \mapsto \sum_{Q^m} n_{q_1} \cdots n_{q_m}(q_1 \cdots q_m)$$

is a distributive law of $S$ over $T$. Verify that $\lambda$-algebras are rings.
