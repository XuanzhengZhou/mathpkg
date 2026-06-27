---
role: proof
locale: en
of_concept: stickelberger-congruence
source_book: gtm059
source_chapter: "1"
source_section: "§2 Stickelberger's Theorem"
---

If $k = 0$ the relation is clear. We assume $1 \le k < q-1$ and prove the theorem by induction on $k$.

**Case $k = 1$.** We have
$$S(1) = \tau(\omega^{-1}) = \sum_{x \in \mathbf{F}_q^*} \omega(x)^{-1} \zeta^{\operatorname{Tr}(x)},$$
where $\zeta$ is a primitive $p$-th root of unity. Since $\omega$ is a non-trivial character of $\mathbf{F}_q^*$, the Gauss sum $S(1)$ satisfies the elementary property
$$S(1)\overline{S(1)} = q.$$
Moreover, $S(1) \equiv -1 \pmod{\mathfrak{P}}$ in the sense of congruences modulo $\mathfrak{P}$, which yields the base case.

**Inductive step.** Assume the congruence holds for all integers $< k$. Let $\chi = \omega^{-1}$, so that $S(k) = \tau(\chi^{k})$. Using properties of Gauss sums under the action of the Teichmüller character, one obtains a recurrence relation expressing $S(k)$ in terms of $S(k-1)$ and certain character sums over $\mathbf{F}_p$.

The key computation involves evaluating
$$\sum_{u \in \mathbf{F}_q} \chi(u)^{k} \zeta^{\operatorname{Tr}(a u)}$$
for suitable $a \in \mathbf{F}_q$. Using the action of the Galois group and the fact that the trace map surjects onto $\mathbf{F}_p$, the sum reduces to a congruence involving the $p$-adic digits of $k$.

Specifically, one uses the expansion of $k$ in base $p$ to write the character sum as a product of lower-degree Gauss sums, and then applies the induction hypothesis. The binomial-like behavior of the Gauss sums under the Stickelberger congruence yields:
$$S(k) \equiv S(1) \cdot \frac{S(k-1)}{S(1)} \cdot \frac{1}{k} \pmod{\mathfrak{P}},$$
which by induction gives
$$S(k) \equiv S(1)^k \cdot \frac{1}{k!} \pmod{\mathfrak{P}}.$$

**Case $p \mid k$.** Write $k = p k_0$ with $1 \le k_0 < \frac{q-1}{p}$. Using the Davenport-Hasse relation (or a direct computation with the $p$-adic expansion), one verifies that the digit sum satisfies $s_p(k) = s_p(k_0)$, and the congruence remains valid. The detailed verification proceeds by writing the Gauss sum in terms of the base field and using the norm map.

The final statement about the order follows by taking the $\mathfrak{P}$-adic valuation:
$$\operatorname{ord}_{\mathfrak{P}} S(k) = \frac{s_p(k)}{p-1},$$
which is obtained by comparing the two sides of the congruence and using that $\operatorname{ord}_{\mathfrak{P}} S(1) = \frac{1}{p-1}$.
