---
role: proof
locale: en
of_concept: lemma-2848b663
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Lemma (b)

Let $\varepsilon_1, \ldots, \varepsilon_{m+e}$ be $m+e$ independent singular numbers. Then the $m+e$ functions of the odd ideal $\mathfrak{a}$

$$Q(\varepsilon_i, \mathfrak{a}) \quad (i = 1, 2, \ldots, m+e)$$

form a system of independent group characters of the group $\mathfrak{B}_0$ (the group of strict ideal classes mod 4).

**Proof.** By Theorem 165, the functions $Q(\varepsilon_i, \mathfrak{a})$ are group characters of $\mathfrak{B}_0$. This follows because $Q(\varepsilon_i, \mathfrak{ab}) = Q(\varepsilon_i, \mathfrak{a}) \cdot Q(\varepsilon_i, \mathfrak{b})$ for odd ideals $\mathfrak{a}, \mathfrak{b}$, which is a consequence of the multiplicativity of the quadratic residue symbol. Moreover, if $\mathfrak{a} \sim \mathfrak{bc}^2$ in the strict sense, then $Q(\varepsilon_i, \mathfrak{a}) = Q(\varepsilon_i, \mathfrak{b})$, so these functions are well-defined on the group $\mathfrak{B}_0$ of strict ideal class complexes.

To show independence, suppose that for some product

$$\prod_{i=1}^{m+e} Q(\varepsilon_i, \mathfrak{a})^{c_i} = 1$$

for all odd ideals $\mathfrak{a}$, where $c_i \in \{0, 1\}$. By Theorem 169, the characters $Q(\varepsilon_i, \mathfrak{a})$ are independent — meaning that if a nontrivial product equals the principal character, then the corresponding product of the $\varepsilon_i$ must be a square. Since the $\varepsilon_i$ are independent singular numbers (no nontrivial product is a square), the characters are independent.

Thus the $m+e$ functions $Q(\varepsilon_i, \mathfrak{a})$ form a system of independent group characters of $\mathfrak{B}_0$. ∎
