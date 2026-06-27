---
role: proof
locale: en
of_concept: quadratic-reciprocity-law
source_book: gtm077
source_chapter: "III"
source_section: "16"
---
# Proof of the Quadratic Reciprocity Law

**Statement (Quadratic Reciprocity Law).** For positive odd integers $a, n$,

$$\left( \frac{a}{n} \right) = \left( \frac{n}{a} \right) (-1)^{((a-1)/2)((n-1)/2)},$$

together with the completion theorems:

$$\left( \frac{-1}{n} \right) = (-1)^{(n-1)/2}, \qquad \left( \frac{2}{n} \right) = (-1)^{(n^2-1)/8},$$

for odd $n > 0$.

**Proof Strategy.** The book does not present an elementary proof in this section. As Hecke states (§16):

> "For this reason we will dispense entirely with a presentation of an elementary proof. Rather we set ourselves the problem of carrying over the concepts of rational number theory, in particular the concept of integer, to other domains of numbers, where new relations between rational integers will also be obtained, e.g., the reciprocity law itself will be presented as a side result."

The proof is developed organically through the book via algebraic number theory. The main steps are:

**1. Quadratic Fields (§29–§30).** The decomposition law for rational primes in quadratic fields $k(\sqrt{d})$ is studied. A rational prime $p \nmid 2d$ splits in $k(\sqrt{d})$ if and only if $\left(\frac{d}{p}\right) = +1$.

**2. Group-Theoretic Foundation (§§5–13).** The structure of the residue class group $\Re(n)$ and its characters are analyzed. The relation $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod{p}$ (Euler's criterion, Theorem 46a) connects the Legendre symbol to group theory.

**3. Jacobi Symbol Extension (§16, §31).** The symbol is extended to composite denominators preserving multiplicativity:

$$\left( \frac{ab}{n} \right) = \left( \frac{a}{n} \right) \cdot \left( \frac{b}{n} \right).$$

The completion theorems follow from the congruences:

$$\frac{ab - 1}{2} \equiv \frac{a - 1}{2} + \frac{b - 1}{2} \pmod{2}, \qquad \frac{a^2 b^2 - 1}{8} \equiv \frac{a^2 - 1}{8} + \frac{b^2 - 1}{8} \pmod{2}.$$

**4. Field-Theoretic Proof (Theorem 135, §46).** The reciprocity law is proved by considering quadratic fields:
- If $\left(\frac{q}{p}\right) = +1$, then $p$ splits in $k(\sqrt{q})$.
- Using the ideal class group structure and the genus theory of quadratic fields, one shows that $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$ when at least one of $p, q$ is $\equiv 1 \pmod{4}$.
- When $p \equiv q \equiv 3 \pmod{4}$, the field $k(\sqrt{pq})$ is used, and the sign factor $(-1)^{((p-1)/2)((q-1)/2)}$ emerges naturally.

**5. Analytic Proof via Gauss Sums (§§52–57).** The most general proof evaluates Gauss sums

$$G(\chi) = \sum_{a \bmod n} \chi(a) e^{2\pi i a / n}$$

using theta-series and their transformation formulas. The reciprocal relation

$$\theta\left(\frac{1}{\tau}\right) = \sqrt{\tau} \, \theta(\tau)$$

connects Gauss sums to theta-series, and the limit behavior of theta-series determines the value of Gauss sums, from which the reciprocity law follows as a consequence.

**Conclusion.** The quadratic reciprocity law, first discovered by Euler and Legendre and first proved by Gauss in 1796, is the central theorem of elementary number theory. Its deepest understanding, however, comes only through the methods of algebraic number theory, where it appears as a special case of far-reaching reciprocity laws for higher power residues.
