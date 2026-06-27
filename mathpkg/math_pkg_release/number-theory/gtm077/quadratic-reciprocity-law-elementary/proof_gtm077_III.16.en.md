---
role: proof
locale: en
of_concept: quadratic-reciprocity-law-elementary
source_book: gtm077
source_chapter: "III"
source_section: "16"
---
# Proof of the Law of Quadratic Reciprocity (Elementary Form)

**Statement (Elementary Quadratic Reciprocity Law).** For odd positive primes $p, q$:

1. **Reciprocity:** $\displaystyle\left( \frac{p}{q} \right) \left( \frac{q}{p} \right) = (-1)^{((p-1)/2)((q-1)/2)}$

2. **First Completion Theorem:** $\displaystyle\left( \frac{-1}{p} \right) = (-1)^{(p-1)/2}$

3. **Second Completion Theorem:** $\displaystyle\left( \frac{2}{p} \right) = (-1)^{(p^2-1)/8}$

Here $\left( \frac{a}{p} \right)$ denotes the Legendre symbol.

**Proof Outline.** The book states these theorems in §16 (pp. 118-120) but defers the elementary proof. Instead, it develops the algebraic number-theoretic proof throughout the text, culminating in Theorems 135-136.

**First Completion Theorem.** By Euler's criterion (Theorem 46a),

$$\left( \frac{-1}{p} \right) \equiv (-1)^{(p-1)/2} \pmod{p}.$$

Since both sides are $\pm 1$ and $p > 2$, the congruence implies equality:

$$\left( \frac{-1}{p} \right) = (-1)^{(p-1)/2}.$$

Alternatively, using quadratic fields: $\left(\frac{-1}{p}\right) = +1$ if and only if $p$ splits in $k(\sqrt{-1}) = \mathbb{Q}(i)$, which happens exactly when $p \equiv 1 \pmod{4}$, since the class number $h_0 = 1$ and $p$ is then a norm $p = a^2 + b^2$. Each square is $\equiv 0$ or $1 \pmod{4}$, so $a^2 + b^2 \equiv 0, 1, 2 \pmod{4}$, and $p \equiv 1 \pmod{4}$ is the only possibility for odd $p$.

**Second Completion Theorem.** By Euler's criterion,

$$\left( \frac{2}{p} \right) \equiv 2^{(p-1)/2} \pmod{p}.$$

A more detailed computation using Gauss's Lemma or evaluating $2^{(p-1)/2}$ modulo $p$ yields the formula $\left( \frac{2}{p} \right) = (-1)^{(p^2-1)/8}$.

**Reciprocity Law.** The field-theoretic proof (Theorem 135 in §46) distinguishes three cases:

*Case 1:* $p \equiv 1 \pmod{4}$ and $q \equiv 1 \pmod{4}$. If $\left(\frac{q}{p}\right) = +1$, then $p$ splits in $k(\sqrt{q})$, and $p^{h_0}$ is a quadratic residue mod $q$. Since $h_0$ is odd (Theorem 133), $p$ itself is a residue mod $q$, so $\left(\frac{p}{q}\right) = +1$. The hypothesis is symmetric, so $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$. The sign factor $(-1)^{((p-1)/2)((q-1)/2)} = +1$ matches.

*Case 2:* One prime $\equiv 1 \pmod{4}$, the other $\equiv 3 \pmod{4}$. Without loss, $q \equiv 1 \pmod{4}$, $p \equiv 3 \pmod{4}$. From $\left(\frac{q}{p}\right) = +1$ we deduce $\left(\frac{p}{q}\right) = +1$ and $\left(\frac{-p}{q}\right) = \left(\frac{-1}{q}\right)\left(\frac{p}{q}\right) = +1$. Conversely, $\left(\frac{-p}{q}\right) = +1$ implies $\left(\frac{q}{p}\right) = +1$ using the field $k(\sqrt{-p})$. Thus $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$, matching the sign factor $(-1)^{((p-1)/2)((q-1)/2)} = +1$.

*Case 3:* $p \equiv q \equiv 3 \pmod{4}$. Then one can show $\left(\frac{-p}{q}\right) = +1$ implies $\left(\frac{-q}{p}\right) = -1$. For the general proof, consider the field $k(\sqrt{pq})$ where (by Theorem 134) $p$ or $q$ is the norm of an integer. From $4p = x^2 - pqy^2$, with $x$ divisible by $p$, we obtain $4 = pu^2 - qy^2$, which implies $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)(-1)$. The sign factor $(-1)^{((p-1)/2)((q-1)/2)} = (-1)^{1 \cdot 1} = -1$, consistent with the formula.

The Jacobi symbol extension for composite denominators preserves the reciprocity relation via the congruences:

$$\frac{ab - 1}{2} \equiv \frac{a - 1}{2} + \frac{b - 1}{2} \pmod{2}, \qquad \frac{a^2 b^2 - 1}{8} \equiv \frac{a^2 - 1}{8} + \frac{b^2 - 1}{8} \pmod{2}.$$

These modular identities allow factorization of the sign factors, extending the reciprocity law to all odd integers.

**Historical Note.** Gauss discovered the first proof in 1796 at age nineteen and published it in *Disquisitiones Arithmeticae* (1801). He later gave six more proofs. The law was conjectured by Euler and partially proved by Legendre, whose proof contained an essential gap. Since then, over 200 distinct proofs have been published, with the algebraic number-theoretic approach (using Gauss sums and theta-series) being the most general and conceptually satisfying.
