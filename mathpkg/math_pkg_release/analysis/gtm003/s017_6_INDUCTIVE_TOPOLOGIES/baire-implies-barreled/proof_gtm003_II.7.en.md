---
role: proof
locale: en
of_concept: baire-implies-barreled
source_book: gtm003
source_chapter: "II"
source_section: "7.1"
---

Let $D$ be a barrel in $E$. Since $D$ is radial and circled, we have $E = \bigcup_{n \in \mathbb{N}} nD$. Since $E$ is a Baire space, there exists $n_0 \in \mathbb{N}$ such that $n_0 D$ (which is closed) has an interior point. Scaling by $1/n_0$, it follows that $D$ has an interior point $y$. Since $D$ is circled, $-y \in D$. The convexity of $D$ then implies that
$$
0 = \frac{1}{2}y + \frac{1}{2}(-y)
$$
is an interior point of $D$, by (1.1). Hence $D$ is a neighborhood of $0$, and since $D$ was an arbitrary barrel, $E$ is barreled.
