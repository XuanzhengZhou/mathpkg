---
role: proof
locale: en
of_concept: containment-of-linear-varieties
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Containment Criterion for Linear Varieties

Let $E$ be a vector space over $\mathbb{K}$. A linear variety in $E$ is a set of the form $V = x + N$ where $x \in E$ and $N$ is a linear subspace of $E$ (equivalently, a coset of $N$ in $E$). The subspace $N$ is uniquely determined by $V$, namely $N = \{y - z : y, z \in V\}$.

**Lemma 21.5.** Let $V = x + N$ and $W = y + M$ be linear varieties in $E$. Then $V \subset W$ if and only if $N \subset M$ and $x - y \in M$.

*Proof.*

($\Rightarrow$) Assume $V \subset W$. Since $x \in V$, we have $x \in W = y + M$, so $x - y \in M$. Now take any $n \in N$. Then $x + n \in V \subset W = y + M$, so $x + n - y \in M$. Since $x - y \in M$ and $M$ is a linear subspace,

$$n = (x + n - y) - (x - y) \in M.$$

Thus $N \subset M$.

($\Leftarrow$) Assume $N \subset M$ and $x - y \in M$. For any $v \in V$, write $v = x + n$ with $n \in N$. Then $n \in M$ (since $N \subset M$), so

$$v = y + (x - y) + n \in y + M = W,$$

since $(x - y) + n \in M$. Hence $V \subset W$.

**Remark.** As an immediate consequence, two linear varieties $x + N$ and $y + M$ are equal if and only if $N = M$ and $x - y \in N$.
