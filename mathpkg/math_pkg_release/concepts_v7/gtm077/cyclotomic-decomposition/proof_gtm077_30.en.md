---
role: proof
locale: en
of_concept: cyclotomic-decomposition
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of Theorem 91-92: Decomposition Law for Cyclotomic Fields

We first prove the key lemma: If the prime $p$ does not divide $D \cdot m$, then for each integer $\omega$ of the field $K(\zeta)$,

$$\omega^{p^f} \equiv \omega \pmod{p},$$

where $f$ is the smallest positive exponent such that $p^f \equiv 1 \pmod{m}$.

**Proof of the Lemma.** Write $\omega = a_0 + a_1\zeta + \cdots + a_{h-1}\zeta^{h-1}$ with rational integers $a_i$. For the integral polynomial $Q(x) = a_0 + a_1x + \cdots + a_{h-1}x^{h-1}$ over $k(1)$, we have the functional congruence

$$Q(x)^p \equiv Q(x^p) \pmod{p}, \quad \text{more generally} \quad (Q(x))^{p^f} \equiv Q(x^{p^f}) \pmod{p}.$$

Replacing $x$ by $\zeta$ yields a valid numerical congruence, proving the lemma.

**Proof of Theorem 91.** If $\mathfrak{p}^2 \mid p$, choose $\omega$ divisible by $\mathfrak{p}$ but not by $\mathfrak{p}^2$. From the lemma, $\omega^{p^f} \equiv \omega \pmod{\mathfrak{p}^2}$. Since $p^f \geq 2$, we have $\omega^{p^f} \equiv 0 \pmod{\mathfrak{p}^2}$, hence $\omega \equiv 0 \pmod{\mathfrak{p}^2}$, contradiction.

**Proof of Theorem 92.** By definition of $f$, $f_1 = f$ follows from $p^{f_1} \equiv 1 \pmod{m}$ and $f_1 \leq f$. Since by Theorem 91 the conjugate prime ideals divide $p$ only to the first power, by the remark in §29, $p$ splits into exactly $h/f$ factors.
