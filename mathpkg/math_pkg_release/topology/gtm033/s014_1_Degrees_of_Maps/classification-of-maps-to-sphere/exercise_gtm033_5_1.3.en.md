---
role: exercise
locale: en
chapter: "5"
section: "1. Degrees of Maps"
exercise_number: 3
---

# Exercise 3

Let $\mathfrak{M}_n$ be the category whose objects are compact connected $n$-manifolds and whose morphisms are homotopy classes $[f]$ of maps $f: M \to N$. For an object $M$, let $\pi^n(M)$ be the set of homotopy classes of maps $M \to S^n$. Given $[f]: M \to N$, define $[f]^*: \pi^n(N) \to \pi^n(M)$ by $[f]^*[g] = [g \circ f]$. This makes $\pi^n$ a contravariant functor from $\mathfrak{M}_n$ to the category of sets.

(a) Show that there is a unique way of lifting this functor to the category of groups so that $\pi^n(S^n) = \mathbb{Z}$, with the identity map corresponding to $1 \in \mathbb{Z}$.

(b) Given the group structure of (a), show that for each $M$ there is an isomorphism

$$\pi^n(M) \cong \begin{cases} \mathbb{Z} & \text{if } M \text{ is orientable and } \partial M = \varnothing \\ \mathbb{Z}_2 & \text{if } M \text{ is nonorientable and } \partial M = \varnothing \\ 0 & \text{if } \partial M \neq \varnothing. \end{cases}$$

Prove that there is no natural family of such isomorphisms.
