---
role: proof
locale: en
of_concept: quadratic-reciprocity-law
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

Let $p$ and $q$ be distinct odd primes. Consider the $p$-th cyclotomic field $\mathbb{Q}(z)$ and its unique quadratic subfield $K$.

We have $m = (-1)^{\frac{1}{2}(p-1)} p$ in the notation of Theorem 32, since $K = \mathbb{Q}(\sqrt{p})$ if $p \equiv 1 \pmod{4}$ and $K = \mathbb{Q}(\sqrt{-p})$ if $p \equiv 3 \pmod{4}$.

Consider the decomposition of $q$ in $K$. There are two cases:

\textbf{Case 1:} $q$ is decomposed in $K$. Then by Theorem 32, $\left(\frac{m}{q}\right) = \left(\frac{(-1)^{(p-1)/2}p}{q}\right) = 1$. On the other hand, in $\mathbb{Q}(z)$ the number $g$ of prime factors of $q$ is even (since the decomposition field contains $K$). Hence $q^{\frac{1}{2}(p-1)} = (q^f)^{\frac{1}{2}g} \equiv 1^{\frac{1}{2}g} \equiv 1 \pmod{p}$. By Euler's criterion, $\left(\frac{q}{p}\right) = 1$.

\textbf{Case 2:} $q$ is inertial in $K$. Then $\left(\frac{(-1)^{(p-1)/2}p}{q}\right) = -1$. In this case $g$ is odd, so $f$ must be even (since $fg = p-1$ is even). Then $q^{\frac{1}{2}(p-1)} = (q^f)^{\frac{1}{2}g}$. Since $f$ is the order of $q$ modulo $p$, we have $q^f \equiv 1 \pmod{p}$, but for $f/2$ we have $q^{f/2} \equiv -1 \pmod{p}$ (otherwise $f$ would not be minimal). Thus $q^{\frac{1}{2}(p-1)} = (q^{f/2})^g \equiv (-1)^g \equiv -1 \pmod{p}$ since $g$ is odd. Therefore $\left(\frac{q}{p}\right) = -1$.

In both cases we have $\left(\frac{q}{p}\right) = \left(\frac{(-1)^{(p-1)/2}p}{q}\right)$.

Now expand the right side using multiplicativity of the Legendre symbol:
$$\left(\frac{q}{p}\right) = \left(\frac{-1}{q}\right)^{\frac{p-1}{2}} \left(\frac{p}{q}\right).$$

By Euler's criterion, $\left(\frac{-1}{q}\right) = (-1)^{\frac{q-1}{2}}$. Therefore:
$$\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}} \left(\frac{p}{q}\right).$$

Multiplying both sides by $\left(\frac{p}{q}\right)$ and noting that $\left(\frac{p}{q}\right)^2 = 1$ (since $p \neq q$), we obtain:
$$\left(\frac{p}{q}\right) \cdot \left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}.$$
