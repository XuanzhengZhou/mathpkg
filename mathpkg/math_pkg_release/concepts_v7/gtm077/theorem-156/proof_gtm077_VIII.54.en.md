---
role: proof
locale: en
of_concept: theorem-156
source_book: gtm077
source_chapter: "VIII"
source_section: "54"
---
# Proof of Theorem 156 — Multiplicativity of Gauss Sums

**Statement (Theorem 156).** If the Gauss sum $C(\omega)$ belongs to the denominator $\mathfrak{a}$, and if $\mathfrak{a}$ is the square of an integral ideal, then for any $\varkappa$ relatively prime to $\mathfrak{a}$,

$$C(\varkappa \omega) = \left( \frac{\varkappa}{\mathfrak{a}} \right) C(\omega).$$

**Proof.** The proof proceeds in several stages, building up from the simplest case to the general one.

**Step 1: The case $\mathfrak{a} = \mathfrak{p}$ (a prime ideal).** When the denominator is a prime ideal $\mathfrak{p}$, the Gauss sum can be expressed using the quadratic residue symbol. For an odd prime ideal $\mathfrak{p}$, we have the identity

$$C(\omega) = \sum_{\mu \bmod \mathfrak{p}} \left( \frac{\mu}{\mathfrak{p}} \right) e^{2\pi i S(\mu \omega)}. \tag{171}$$

To verify this formula, we group the terms in the definition

$$C(\omega) = \sum_{\mu \bmod \mathfrak{p}} e^{2\pi i S(\mu^2 \omega)}$$

by the value of $\mu^2$ modulo $\mathfrak{p}$. Excluding the residue class $\mu = 0$, each quadratic residue occurs exactly twice (for $\mu$ and $-\mu$), while non-residues correspond to terms where $\mu^2$ is not a square. The value of the sum is therefore

$$1 + 2 \sum_{\substack{\mu^2 \\ \text{quad. res.}}} e^{2\pi i S(\mu^2 \omega)} = \sum_{\mu \bmod \mathfrak{p}} \left( \frac{\mu}{\mathfrak{p}} \right) e^{2\pi i S(\mu \omega)},$$

since each square except 0 occurs exactly twice, and $\left(\frac{\mu}{\mathfrak{p}}\right) = +1$ for residues, $-1$ for non-residues, and $0$ when $\mu \equiv 0 \pmod{\mathfrak{p}}$.

Now replacing $\mu$ by $\mu \varkappa$ (which merely permutes the residue classes since $\varkappa$ is relatively prime to $\mathfrak{p}$) gives

$$C(\varkappa \omega) = \sum_{\mu \bmod \mathfrak{p}} \left( \frac{\mu \varkappa}{\mathfrak{p}} \right) e^{2\pi i S(\mu \omega)} = \left( \frac{\varkappa}{\mathfrak{p}} \right) \sum_{\mu \bmod \mathfrak{p}} \left( \frac{\mu}{\mathfrak{p}} \right) e^{2\pi i S(\mu \omega)} = \left( \frac{\varkappa}{\mathfrak{p}} \right) C(\omega).$$

Thus the theorem holds for a prime ideal denominator.

**Step 2: Denominator a prime power $\mathfrak{p}^a$.** Using Lemma (b) which gives a reduction formula for Gauss sums, we apply (170) repeatedly:

$$C\left(\frac{\beta}{\alpha^a}\right) = N(\mathfrak{p}) \, C\left(\frac{\beta}{\alpha^{a-2}}\right) \quad (\text{for } a \geq 2).$$

For even $a$, repeated application reduces the Gauss sum to one with denominator $1$, giving $C(\omega) = 1$, and since $\left(\frac{\varkappa}{\mathfrak{p}^a}\right) = \left(\frac{\varkappa}{\mathfrak{p}}\right)^a = 1$ for even $a$, both sides are equal. For odd $a$, the reduction yields the same multiplicative factor $\left(\frac{\varkappa}{\mathfrak{p}}\right) = \left(\frac{\varkappa}{\mathfrak{p}^a}\right)$, which matches the formula.

**Step 3: General composite denominator.** Let $\mathfrak{a} = \mathfrak{p}_1^{a_1} \cdots \mathfrak{p}_r^{a_r}$ be the prime ideal factorization. By the factorization formula (169), the Gauss sum $C(\omega)$ with denominator $\mathfrak{a}$ decomposes as a product of Gauss sums with denominators $\mathfrak{p}_i^{a_i}$. Applying the result from Step 2 to each factor and using the multiplicativity of the symbol $\left(\frac{\varkappa}{\mathfrak{a}}\right) = \prod_i \left(\frac{\varkappa}{\mathfrak{p}_i}\right)^{a_i}$ yields the theorem for arbitrary odd denominators.

**Remark.** This theorem is essential for connecting Gauss sums with theta-series. The limit behavior of theta-series as their parameter approaches a rational point recovers the Gauss sum, and the transformation formula for theta-functions then relates Gauss sums with different denominators, ultimately yielding the quadratic reciprocity law.
