---
role: proof
locale: en
of_concept: theorem-172
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Theorem 172

**Theorem 172.** There are exactly $e_0$ independent singular primary numbers, say $\omega_1, \ldots, \omega_{e_0}$. Here $e_0$ is the basis number belonging to 2 of the group of strict ideal classes of the field. The $e_0$ characters $Q(\omega_i, \mathfrak{a})$ form the complete system of characters of the group of the strict class complexes for odd $\mathfrak{a}$.

**Proof.** The proof proceeds by establishing two inequalities that together imply the result.

**Step 1: Upper bound $q \leq e_0$ (Lemma (a)).** Let $q$ denote the number of independent complexes of singular primary numbers. Let $\omega_1, \ldots, \omega_{q}$ be representatives. For each $\omega_i$, define the character

$$\chi_i(\mathfrak{a}) = \left(\frac{\omega_i}{\mathfrak{a}}\right)$$

on odd ideals $\mathfrak{a}$. By the reciprocity law,

$$\left(\frac{\omega_i}{\gamma}\right) = \left(\frac{\gamma}{\omega_i}\right)$$

for integers $\gamma$ relatively prime to $2\omega_i$, since $\omega_i$ is primary and totally positive. The last symbol is $+1$ because $\omega_i$ is singular. Hence

$$\chi_i(\mathfrak{a}) = \chi_i(\mathfrak{b}) \quad \text{if } \mathfrak{a} \sim \mathfrak{bc}^2.$$

Furthermore, $\chi_i(\mathfrak{a}_1\mathfrak{a}_2) = \chi_i(\mathfrak{a}_1) \cdot \chi_i(\mathfrak{a}_2)$, so the $\chi_i$ are group characters of the group of ideal class complexes. By Theorem 169 they are independent characters. On the other hand, by Theorem 33 the group of ideal class complexes has exactly $e$ independent characters (since it has order $2^e$). Hence $q \leq e$.

A similar argument using strict equivalence yields $q \leq e_0$.

**Step 2: Lower bound $e_0 \leq q$ (Lemma (c)).** Let $\varepsilon_1, \ldots, \varepsilon_p$ be the $p = e_0 + m - r_1$ independent totally positive singular numbers. By Lemma (c), the $p$ functions $Q(\varepsilon_i, \mathfrak{a})$ form independent group characters of $\mathfrak{B}$. Since $\mathfrak{B}$ has order $2^{m-r_1+q}$, we obtain

$$m - r_1 + q \geq p = m - r_1 + e_0, \quad \text{so } e_0 \leq q.$$

**Step 3: Conclusion.** From $q \leq e_0$ (Step 1) and $e_0 \leq q$ (Step 2), we have $e_0 = q$. Thus there are exactly $e_0$ independent singular primary numbers $\omega_1, \ldots, \omega_{e_0}$.

Moreover, $\mathfrak{B}$ has order $2^{m-r_1+q} = 2^{m-r_1+e_0} = 2^p$. The $e_0$ characters $Q(\omega_i, \mathfrak{a})$ therefore form the complete system of characters of the group of strict class complexes for odd $\mathfrak{a}$. ∎
