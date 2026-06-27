---
role: proof
locale: en
of_concept: lemma-9-9-finite-d-associative-iff-theta-1
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

If $\theta = 1$, then the multiplication formula reduces to a commutative associative multiplication, and $D$ is associative (in fact, $D$ is isomorphic to a quadratic extension of $F$ or a direct product).

Conversely, assume $D$ is associative. Then every associator $[r, s, t] = (rs)t - r(st)$ vanishes. Consider elements of the form $r = 0 + \lambda y$, $s = z + \lambda 0$, $t = k + \lambda 0$ (with $k = 1$ to simplify).

From the definition of multiplication, we compute the associator and set it to zero. The detailed computation (involving case analysis on the multiplication formula) yields, after specialization with $t = k = 1$ and $y = 0$:

$$x^{\theta^2} = x \quad \text{and} \quad b(x^{\theta^2} - x^2) = 0$$

for all $x \in F$. Since $\theta \neq 1$ would make the construction trivial or impossible, the first equation gives $\theta^2 = 1$. Then the second equation forces $b = 0$.

With $b = 0$, the associator condition further reduces to:

$$t^2 k(a^{\theta} - a) = 0$$

for all $t, k, y$. This holds if and only if $a^{\theta} = a$, i.e., $a$ lies in the subfield $K$ of elements fixed by $\theta$.

Since $\theta^2 = 1$, $K$ must be $GF(q)$ where $F = GF(q^2)$ and $\theta$ is the Frobenius automorphism $x^{\theta} = x^q$. But as $x$ varies over $F$, $x^{1+\theta} = x^{1+q}$ varies over all of $K$. Thus there exists $x \in F$ such that $x^{1+\theta} = a$, which would mean $a = x^{1+\theta} + x \cdot 0$ has a solution, violating condition (2) of the construction. The only way to avoid this contradiction is $\theta = 1$.

Therefore, $D$ is associative precisely when $\theta = 1$.
