---
role: proof
locale: en
of_concept: constructive-two-squares-decomposition
source_book: gtm050
source_chapter: "2"
source_section: "2.6"
---

The proof is constructive and proceeds by infinite descent on the multiplier $k$.

**Step 1: Find an initial representation.** Since $p \equiv 1 \pmod{4}$, $-1$ is a quadratic residue modulo $p$, so there exists an integer $x$ with $x^{2} \equiv -1 \pmod{p}$. Then $x^{2} + 1^{2} = kp$ for some $k < p$. Set $c = x$, $d = 1$.

**Step 2: Reduction step.** If $k = 1$, we are done. Otherwise $k > 1$. Choose integers $r, s$ such that $r \equiv c \pmod{k}$, $s \equiv d \pmod{k}$, and $|r|, |s| \leq k/2$. (This is always possible by taking least absolute residues.) Then
\[
r^{2} + s^{2} \equiv c^{2} + d^{2} = kp \equiv 0 \pmod{k},
\]
so $r^{2} + s^{2} = k\ell$ for some integer $\ell \geq 0$. Since $|r|, |s| \leq k/2$, we have
\[
\ell = \frac{r^{2} + s^{2}}{k} \leq \frac{(k/2)^{2} + (k/2)^{2}}{k} = \frac{k}{2} < k.
\]
If $\ell = 0$, then $r = s = 0$, so $c \equiv d \equiv 0 \pmod{k}$, which gives $k^{2} \mid c^{2}+d^{2} = kp$, hence $k \mid p$. But $k < p$ and $p$ is prime, so $k = 1$, contradicting $k > 1$. Thus $0 < \ell < k$.

Now compute
\[
(c^{2} + d^{2})(r^{2} + s^{2}) = (kp)(k\ell) = k^{2}p\ell.
\]
Using the Brahmagupta--Fibonacci identity,
\[
(c^{2} + d^{2})(r^{2} + s^{2}) = (cr + ds)^{2} + (cs - dr)^{2} = (cr - ds)^{2} + (cs + dr)^{2}.
\]
Modulo $k$, we have $cr + ds \equiv c^{2} + d^{2} = kp \equiv 0 \pmod{k}$ and $cs - dr \equiv cd - dc = 0 \pmod{k}$. Hence both $cr + ds$ and $cs - dr$ are divisible by $k$ (choose the appropriate sign combination). Set
\[
a = \frac{cr + ds}{k}, \quad b = \frac{cs - dr}{k}.
\]
Then
\[
a^{2} + b^{2} = \frac{(cr+ds)^{2} + (cs-dr)^{2}}{k^{2}} = \frac{k^{2}p\ell}{k^{2}} = p\ell.
\]
But we also have the alternative sign choice $(cr - ds, cs + dr)$, and one of the two choices yields integers divisible by $k$ with the property that after division, we obtain a representation of $p$ itself (i.e., $\ell = 1$) or we obtain a new multiplier $\ell < k$ and repeat.

**Step 3: Termination.** The sequence of positive integer multipliers strictly decreases. By the well-ordering principle, the process must terminate at $k = 1$, yielding $p = a^{2} + b^{2}$.

In the example $p = 229$, one finds $122^{2} + 1^{2} = 65 \cdot 229$. Taking $k = 65$, choose $r \equiv 122 \pmod{65}$ with $|r| \leq 32$: $r = 122 - 2 \cdot 65 = -8$, and $s = 1$. Then $(-8)^{2} + 1^{2} = 65$, giving $\ell = 1$. Then $(122^{2} + 1^{2})(8^{2} + 1^{2}) = (122 \cdot 8 + 1 \cdot 1)^{2} + (122 \cdot 1 - 8 \cdot 1)^{2}$ or equivalently choosing opposite signs, and dividing by $65^{2}$ yields $229 = 15^{2} + 2^{2}$.
