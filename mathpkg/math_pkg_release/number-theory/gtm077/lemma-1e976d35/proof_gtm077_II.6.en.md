---
role: proof
locale: en
of_concept: lemma-1e976d35
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Lemma (c)

Let $\varepsilon_1, \ldots, \varepsilon_p$ be the $p = e_0 + m - r_1$ independent totally positive singular numbers. Then the $p$ functions $Q(\varepsilon_i, \mathfrak{a})$ ($i = 1, \ldots, p$) form a system of independent group characters of the group $\mathfrak{B}$ for odd $\mathfrak{a}$.

**Proof.** The argument parallels that of Lemma (b), applied to the group $\mathfrak{B}$ instead of $\mathfrak{B}_0$. By Theorem 165, each $Q(\varepsilon_i, \mathfrak{a})$ is a group character of $\mathfrak{B}$ — the defining property $Q(\varepsilon_i, \mathfrak{a}) = Q(\varepsilon_i, \mathfrak{b})$ for $\mathfrak{a} \sim \mathfrak{bc}^2$ holds because the $\varepsilon_i$ are singular (and totally positive). The multiplicativity $Q(\varepsilon_i, \mathfrak{a}_1\mathfrak{a}_2) = Q(\varepsilon_i, \mathfrak{a}_1) \cdot Q(\varepsilon_i, \mathfrak{a}_2)$ follows from the general properties of the quadratic residue symbol.

Independence is again guaranteed by Theorem 169: if a product $\prod Q(\varepsilon_i, \mathfrak{a})^{c_i}$ is identically $+1$, then $\prod \varepsilon_i^{c_i}$ must be a square. Since the $\varepsilon_i$ are independent singular numbers, this forces all $c_i = 0$.

Since $\mathfrak{B}$ has order $2^{m-r_1+q}$, it follows from the existence of $p$ independent characters that

$$m - r_1 + q \geq p = m - r_1 + e_0,$$

hence $e_0 \leq q$. Combined with Lemma (a), we obtain $e_0 = q$, and thus $\mathfrak{B}$ has order $2^p$. ∎
