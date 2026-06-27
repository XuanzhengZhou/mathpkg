---
role: proof
locale: en
of_concept: runge-approximation-theorem
source_book: gtm035
source_chapter: "2"
source_section: "2.9"
---

# Proof of Runge Approximation Theorem

**Theorem 2.9 (Runge).** Let $K$ be a compact subset of $\mathbb{C}$ and let $\Omega$ be an open set containing $K$. Let $F$ be holomorphic on $\Omega$. If $\mathbb{C} \setminus K$ is connected, then $F$ can be uniformly approximated on $K$ by polynomials. More generally, if we choose one point $p_j$ in each bounded component of $\mathbb{C} \setminus K$, then $F$ can be uniformly approximated on $K$ by rational functions whose only poles lie among the $p_j$.

## Proof

Let $W$ be the linear space of rational functions whose poles lie among the chosen points $\{p_j\}$ (if $\mathbb{C} \setminus K$ is connected, there are no such points and $W$ consists of polynomials). Let $\mu$ be a measure on $K$ with $\mu \perp W$.

For $z$ not in $K$ and not equal to any $p_j$, the function $\zeta \mapsto 1/(\zeta - z)$ belongs to $W$. Hence

$$\hat{\mu}(z) = \int_K \frac{d\mu(\zeta)}{\zeta - z} = 0$$

for all such $z$.

The Cauchy transform $\hat{\mu}$ is analytic on $\mathbb{C} \setminus K$. In each bounded component $\Omega_j$ of $\mathbb{C} \setminus K$ that contains a designated point $p_j$, we have

$$\frac{d^k \hat{\mu}}{dz^k}(p_j) = k! \int_K \frac{d\mu(\zeta)}{(\zeta - p_j)^{k+1}} = 0, \quad k = 0, 1, 2, \ldots,$$

since $(\zeta - p_j)^{-(k+1)} \in W$ and $\mu \perp W$. Thus all derivatives of $\hat{\mu}$ vanish at $p_j$, so $\hat{\mu} = 0$ identically on $\Omega_j$.

Consequently, $\hat{\mu} = 0$ on $\mathbb{C} \setminus K$, and in particular $\hat{\mu} = 0$ almost everywhere with respect to planar Lebesgue measure. By Lemma 2.7, $\mu = 0$.

Therefore $\mu \perp W \implies \mu = 0$, and by the Riesz-Banach theorem, $W^\perp = \{0\}$ implies $W$ is dense in $C(K)$. Since $F$ is holomorphic on a neighborhood of $K$, $F$ belongs to the uniform closure of $W$ on $K$, which gives the desired approximation. $\square$
