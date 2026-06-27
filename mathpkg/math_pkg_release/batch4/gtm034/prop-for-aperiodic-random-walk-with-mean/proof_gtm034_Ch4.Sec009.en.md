---
role: proof
locale: en
of_concept: prop-for-aperiodic-random-walk-with-mean
source_book: gtm034
source_chapter: "4"
source_section: "009"
---

Proof: As $u(x)$ and $v(x)$ both tend to a limit when $x \to +\infty$ (by P18.8) one has $g(x,y) \leq A [\min(x,y) + 1]$ for some $A > 0$. The random walk has finite second moment, so that one can apply the dominated convergence theorem to conclude

$$\lim_{x \to +\infty} H_B(x,y) = \lim_{x \to +\infty} \sum_{t=0}^{\infty} g(x,t)P(t,y) = \sum_{t=0}^{\infty} \lim_{x \to +\infty} g(x,t)P(t,y),$$

and P4 then follows from P18.8 applied to P3.

Curiously P4 does not give the simplest possible representation for the limit of the hitting probabilities. We shall encounter this problem again in Chapter VI, where a far more direct approach (also based on the renewal theorem) will yield the formula

$$\lim_{x \to -\infty} H_A(x,y) = \frac{1}{E[Z]} P[Z \geq y

There was also an adjoint equation, too evident to comment upon,

$$\sum_{y \in R-B} a(-y)P(y,x) = a(-x), \quad x \in R-B.$$

Here $B$ was the origin. In the case of the half-line (say $B = [x \mid x \leq -1]$), these equations are
