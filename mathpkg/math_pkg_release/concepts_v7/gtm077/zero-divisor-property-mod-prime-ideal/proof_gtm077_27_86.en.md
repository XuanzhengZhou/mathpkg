---
role: proof
locale: en
of_concept: zero-divisor-property-mod-prime-ideal
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 86

**Theorem.** If $\mathfrak{p}$ is a prime ideal, and if for two polynomials
$P(x_1, \ldots, x_m)$ and $Q(x_1, \ldots, x_m)$ with integer coefficients in
$K$,

$$P(x_1, \ldots, x_m) \cdot Q(x_1, \ldots, x_m) \equiv 0 \pmod{\mathfrak{p}},$$

then at least one of $P, Q$ is $\equiv 0 \pmod{\mathfrak{p}}$.

**Proof.** We proceed by induction on the number of variables $m$.

*Base case $m = 0$.* Polynomials of zero variables are constants (integers in
$K$). The statement reduces to: if $\alpha\beta \equiv 0 \pmod{\mathfrak{p}}$,
then $\alpha \equiv 0 \pmod{\mathfrak{p}}$ or
$\beta \equiv 0 \pmod{\mathfrak{p}}$. This is precisely the defining property
of a prime ideal, so the theorem holds for $m = 0$.

*Inductive step.* Assume the theorem holds for all polynomials in $m$ or fewer
variables. Consider polynomials in $m+1$ variables $x_0, x_1, \ldots, x_m$.
Any such polynomial can be written as

$$P(x_0, \ldots, x_m) = \sum_{k} x_0^k P_k(x_1, \ldots, x_m)$$

where the $P_k$ are polynomials in $m$ variables. Note that
$P \equiv 0 \pmod{\mathfrak{p}}$ if and only if all $P_k \equiv 0 \pmod{\mathfrak{p}}$.

Suppose $P \cdot Q \equiv 0 \pmod{\mathfrak{p}}$ but
$P \not\equiv 0 \pmod{\mathfrak{p}}$. Let $r$ be the highest index such that
$P_r \not\equiv 0 \pmod{\mathfrak{p}}$, and let $s$ be the highest index such
that the corresponding coefficient polynomial $Q_s$ of $Q$ is
$\not\equiv 0 \pmod{\mathfrak{p}}$.

Write $P = x_0^r P_r + \text{(lower terms in } x_0\text{)}$ and
$Q = x_0^s Q_s + \text{(lower terms in } x_0\text{)}$.

The coefficient of $x_0^{r+s}$ in the product $P \cdot Q$ is
$P_r(x_1, \ldots, x_m) \cdot Q_s(x_1, \ldots, x_m)$. Since the product is
$\equiv 0 \pmod{\mathfrak{p}}$, this coefficient must be
$\equiv 0 \pmod{\mathfrak{p}}$. By the induction hypothesis (applied to
polynomials in $m$ variables), either $P_r \equiv 0 \pmod{\mathfrak{p}}$ or
$Q_s \equiv 0 \pmod{\mathfrak{p}}$, a contradiction.

Therefore $P \equiv 0 \pmod{\mathfrak{p}}$ or $Q \equiv 0 \pmod{\mathfrak{p}}$.
