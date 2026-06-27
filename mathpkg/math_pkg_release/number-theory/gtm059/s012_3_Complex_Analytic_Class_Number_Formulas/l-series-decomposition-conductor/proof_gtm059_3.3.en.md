---
role: proof
locale: en
of_concept: l-series-decomposition-conductor
source_book: gtm059
source_chapter: "3"
source_section: "3. Complex Analytic Class Number Formulas"
---

By definition of the conductor $f$, the character $\chi$ modulo $m$ is induced from a primitive character $\psi$ modulo $f$. This means that for every integer $n$ coprime to $m$, $\chi(n) = \psi(n)$ if $(n, m/f) = 1$, and $\chi(n) = 0$ if $(n, m/f) > 1$ (i.e., if $n$ shares a prime factor with $m$ that does not divide $f$).

From the Euler product representation for $\Re(s) > 1$:

$$L(s, \chi) = \prod_{p} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1}.$$

For primes $p$ dividing $m$, we have $\chi(p) = 0$ by definition (unless $p \mid f$, in which case $\chi(p) = \psi(p)$ since $\psi$ is primitive modulo $f$). For primes $p \nmid m$, $\chi(p) = \psi(p)$ because both characters are periodic and agree on residue classes coprime to $m$.

Therefore:

$$L(s, \chi) = \prod_{p \nmid m} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1} \cdot \prod_{p \mid f} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1}.$$

The Euler product for $L(s, \psi)$ includes all primes:

$$L(s, \psi) = \prod_{p} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1} = \prod_{p \nmid m} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1} \cdot \prod_{p \mid f} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1} \cdot \prod_{p \mid m, p \nmid f} \left(1 - \frac{\psi(p)}{p^s}\right)^{-1}.$$

Comparing the two expressions, we see that $L(s, \chi)$ omits the Euler factors for primes $p \mid m$ with $p \nmid f$ (where $\chi(p) = 0$), so:

$$L(s, \chi) = L(s, \psi) \prod_{\substack{p \mid m \\ p \nmid f}} \left(1 - \frac{\psi(p)}{p^s}\right).$$

The product is finite (since there are only finitely many primes dividing $m$), and the equality extends analytically to $\Re(s) > 0$ by meromorphic continuation.
