---
role: proof
locale: en
of_concept: dist-zbar-rk-bound
source_book: gtm035
source_chapter: "Chapter 21"
source_section: "21.3"
---
# Proof of Lemma 21.3 (Bound for $\operatorname{dist}(\bar{z}, R(K))$ in Terms of Area)

**Lemma 21.3.** $\operatorname{dist}(\bar{z}, R(K)) \leq \left( \frac{1}{\pi} \operatorname{area}(K) \right)^{1/2}$.

Note that Lemma 21.3 is a quantitative version of the Hartogs–Rosenthal theorem that $R(K) = C(K)$ if $K$ has zero area; for then $\bar{z} \in R(K)$ and so $R(K) = C(K)$ by the Stone–Weierstrass theorem.

**Proof.** Let $\psi$ be a $C^\infty$ function with compact support in the plane such that $\psi(z) \equiv \bar{z}$ on a neighborhood of $K$. By the generalized Cauchy integral formula,

$$\psi(z) = -\frac{1}{\pi} \iint \frac{\partial\psi}{\partial\bar{\zeta}} \frac{du\,dv}{\zeta - z}, \quad \zeta = u + iv,$$

for all $z \in \mathbb{C}$. Restricting $\psi$ to $K$, and using $\frac{\partial\psi}{\partial\bar{\zeta}} \equiv 1$ on $K$, we get

$$\bar{z} = -\frac{1}{\pi} \iint_K \frac{du\,dv}{\zeta - z} - \frac{1}{\pi} \iint_{K'} \frac{\partial\psi}{\partial\bar{\zeta}} \frac{du\,dv}{\zeta - z}$$

for $z \in K$, where $K' = \mathbb{C} \setminus K$. Since the integrand in the second integral is, for fixed $\zeta$, a function in $R(K)$ (it is holomorphic in $z$ on a neighborhood of $K$ and hence approximable by rational functions with poles off $K$), it follows — by approximating the integral by Riemann sums — that the second integral represents a function in $R(K)$. We get

$$\operatorname{dist}(\bar{z}, R(K)) \leq \sup_{z \in K} \left| \frac{1}{\pi} \iint_K \frac{du\,dv}{\zeta - z} \right|.$$

Lemma 21.3 follows by applying Lemma 21.2 to this last integral. ∎
