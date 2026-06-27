---
role: proof
locale: en
of_concept: finite-filtration-implies-homologically-finite
source_book: gtm004
source_chapter: "VIII"
source_section: "3"
---

# Proof of Finite Filtration Implies Homologically Finite

Recall the definitions. A filtration of a chain complex $C$ is **finite** if, for each $q$, there exist $p_0, p_1$ with

* (3.8)(i) $C_q^{(p)} = 0$ for $p \le p_0$,
* (3.8)(ii) $C_q^{(p)} = C_q$ for $p \ge p_1$.

A filtration is **homologically finite** if, for each $q$, there exist $p_0', p_1'$ with

* (3.9)(i) $H_q(C^{(p)}) = 0$ for $p \le p_0'$,
* (3.9)(ii) $H_q(C^{(p)}) = H_q(C)$ for $p \ge p_1'$.

---

**Proof.** The implication (3.8)(i) $\Rightarrow$ (3.9)(i) is plain: if $C_q^{(p)} = 0$ for all $p \le p_0$, then the subcomplex $C^{(p)}$ is zero in degree $q$ for such $p$, so its homology $H_q(C^{(p)})$ vanishes as well.

Now assume (3.8)(ii). Then for each $q$ and sufficiently large $p$, we have

$$C_q^{(p)} = C_q, \qquad C_q^{(p+1)} = C_q.$$

Thus for large $p$ the inclusion $C^{(p)} \hookrightarrow C$ is the identity map in degree $q$, inducing the identity on homology. Consequently,

$$H_q(C^{(p)}) = H_q(C) \quad \text{for all sufficiently large } p,$$

which is exactly condition (3.9)(ii).

Hence finiteness of the filtration (3.8) directly implies homological finiteness (3.9). $\square$
