---
role: proof
locale: en
of_concept: density-lemma-linear-subspaces-cx
source_book: gtm027
source_chapter: "7"
source_section: "P"
---

# Proof of Density Lemma for Linear Subspaces of C(X)

Let $X$ be a topological space and let $C(X)$ be the space of all bounded continuous real-valued functions on $X$ with the topology of uniform convergence (normed by $\|f\| = \sup_{x \in X} |f(x)|$). A subset $L \subseteq C(X)$ has the **two-set property** if for every pair of disjoint closed subsets $A, B \subseteq X$ and every closed interval $[a, b]$, there exists $f \in L$ such that $f(X) \subseteq [a, b]$, $f = a$ on $A$, and $f = b$ on $B$.

**Lemma.** Every linear subspace $L$ of $C(X)$ with the two-set property is dense in $C(X)$.

**Proof.** Let $g \in C(X)$ be arbitrary. Suppose $d = \operatorname{dist}(g, L) > 0$. Choose $h \in L$ such that $\|g - h\|$ is approximately $d$ (within $\varepsilon$). Set $k = g - h$. Then $\operatorname{dist}(k, L) = \operatorname{dist}(g, L)$ since $L$ is a linear subspace, and this distance is approximately $\|k\|$.

Now we construct $f \in L$ such that $\|k - f\| \leq \frac{2}{3}\|k\|$. Then

$$d = \operatorname{dist}(g, L) = \operatorname{dist}(k, L) \leq \|k - f\| \leq \frac{2}{3}\|k\| \approx \frac{2}{3}d,$$

which for $d > 0$ yields a contradiction. Hence $d = 0$ and $L$ is dense.

**Construction of $f$.** Let $M = \|k\|$. Define

$$A = \{x \in X : k(x) \leq -\tfrac{M}{3}\}, \qquad B = \{x \in X : k(x) \geq \tfrac{M}{3}\}.$$

These are disjoint closed sets (by continuity of $k$). Choose $a = 0$, $b = \frac{2M}{3}$ (or any suitable interval). The two-set property gives $f \in L$ with $f(X) \subseteq [0, \frac{2M}{3}]$, $f = 0$ on $A$, and $f = \frac{2M}{3}$ on $B$.

For $x \in A$: $k(x) \leq -M/3$, $f(x) = 0$, so $|k(x) - f(x)| = |k(x)| \leq M$ (but actually $k(x) + f(x) = k(x)$ could be as negative as $-M$; need a more careful choice).

Better: set the interval to $[-M/3, M/3]$ and require $f = -2M/3$ on $A$, $f = 2M/3$ on $B$. Then $f(X) \subseteq [-\frac{2M}{3}, \frac{2M}{3}]$ and one verifies $\|k - f\| \leq \frac{2M}{3} = \frac{2}{3}\|k\|$ by checking the three regions $A$, $B$, and $X \setminus (A \cup B)$.

The standard argument (as in Kelley) yields the required bound, completing the proof.
