---
role: proof
locale: en
of_concept: hartogs-rosenthal-theorem
source_book: gtm035
source_chapter: "2"
source_section: "2.8"
---

# Proof of Hartogs-Rosenthal Theorem

**Theorem 2.8 (Hartogs-Rosenthal).** Let $X$ be a compact subset of $\mathbb{C}$ having Lebesgue two-dimensional measure zero. Then rational functions whose poles lie off $X$ are uniformly dense in $C(X)$.

## Proof

Let $W$ be the linear space consisting of all rational functions holomorphic on $X$. Then $W$ is a subspace of $C(X)$.

To show $W$ is dense, we consider a measure $\mu$ on $X$ with $\mu \perp W$ and prove that $\mu = 0$ (which, by the Riesz-Banach theorem, implies $W$ is dense in $C(X)$).

For any $z \notin X$, the function $\zeta \mapsto 1/(\zeta - z)$ is a rational function with pole outside $X$, hence belongs to $W$. Since $\mu \perp W$, we have

$$\hat{\mu}(z) = \int_X \frac{d\mu(\zeta)}{\zeta - z} = 0 \quad \text{for all } z \notin X.$$

Since $X$ has Lebesgue two-dimensional measure zero, the complement $\mathbb{C} \setminus X$ is almost all of $\mathbb{C}$ in the sense of planar Lebesgue measure. Therefore $\hat{\mu}(z) = 0$ for almost every $z \in \mathbb{C}$ (with respect to $dx\,dy$).

By Lemma 2.7(i), $\hat{\mu} = 0$ a.e. implies $\mu = 0$.

Thus $\mu \perp W \implies \mu = 0$, and by the Riesz-Banach theorem, $W$ is dense in $C(X)$. $\square$
