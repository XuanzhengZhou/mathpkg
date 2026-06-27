---
role: proof
locale: en
of_concept: fermat-two-squares-theorem
source_book: gtm050
source_chapter: "2"
source_section: "2.6"
---

The proof proceeds by infinite descent, following Euler's argument. Let $p = 4n+1$ be prime and suppose, for contradiction, that $p$ is not a sum of two squares.

First, since $p \equiv 1 \pmod{4}$, $-1$ is a quadratic residue modulo $p$. Hence there exist integers $x, y$ such that $x^{2} + y^{2} \equiv 0 \pmod{p}$ with $0 < x, y < p$ and $\gcd(x,y) = 1$. It follows that $x^{2} + y^{2} = kp$ for some positive integer $k < p$.

If $k = 1$ then $p = x^{2} + y^{2}$ and we are done. If $k > 1$, Euler's step (5) provides a method to replace $k$ by a smaller positive integer $k' < k$ while preserving the form $A^{2} + B^{2} = k'p$. Repeating this process yields an infinitely descending sequence of positive integers, which is impossible. By contradiction, the process must terminate at $k = 1$, giving $p = a^{2} + b^{2}$.

The constructive version of the proof replaces the indirect infinite descent with a direct algorithm: starting from $a^{2} + b^{2} = kp$ with $k > 1$, one finds integers $c, d$ such that $c^{2} + d^{2} = k\ell$ with $\ell < k$, and then uses the identity
\[
(a^{2} + b^{2})(c^{2} + d^{2}) = (ac \pm bd)^{2} + (ad \mp bc)^{2}
\]
to obtain a new representation with a smaller multiplier. Iterating this reduction eventually yields $p = a^{2} + b^{2}$.
