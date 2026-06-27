---
role: proof
locale: en
of_concept: gcd-linear-combination
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of GCD as Linear Combination (Theorem 1)

Let $a$ and $b$ be integers, not both zero. Consider the set

$$S = \{ax + by \mid x, y \in \mathbb{Z}\}.$$

$S$ is a **module** (closed under addition and under multiplication by arbitrary integers). Let $d$ be the smallest positive integer belonging to $S$. We claim that $S$ consists precisely of all multiples of $d$.

Indeed, let $n$ be any element of $S$. By the division algorithm, write $n = qd + r$ with $0 \leq r < d$. Since $d \in S$, we have $qd \in S$ (because a module is closed under integer multiples), and therefore $r = n - qd \in S$. But $0 \leq r < d$ and $d$ is the smallest positive element of $S$, so we must have $r = 0$. Hence $n = qd$, i.e., every element of $S$ is a multiple of $d$. Conversely, every multiple of $d$ belongs to $S$ because $d \in S$.

Now, since $a = a \cdot 1 + b \cdot 0 \in S$ and $b = a \cdot 0 + b \cdot 1 \in S$, both $a$ and $b$ are multiples of $d$, so $d \mid a$ and $d \mid b$; thus $d$ is a common divisor of $a$ and $b$. Moreover, any common divisor $c$ of $a$ and $b$ must divide every linear combination $ax + by$, and in particular $c \mid d$. Hence $d$ is the greatest common divisor $(a, b)$.

Therefore there exist integers $x_0, y_0$ such that

$$ax_0 + by_0 = (a, b).$$

In particular, if $(a, b) = 1$, the equation $ax + by = 1$ is solvable in integers, and conversely.
