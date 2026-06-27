---
role: proof
locale: en
of_concept: kernel-of-multiplicative-homomorphism
source_book: gtm028
source_chapter: "I"
source_section: "9. Quotient rings"
---

Let $f: R \to S$ be a ring homomorphism such that $f(m)$ is a unit in $S$ for every $m \in M$. Suppose $x \in R$ and there exists $m \in M$ with $mx = 0$. Then

$$
0 = f(0) = f(xm) = f(x) f(m).
$$

Since $f(m)$ is a unit in $S$, it is invertible. Multiplying both sides of $f(x) f(m) = 0$ by $f(m)^{-1}$ yields $f(x) = 0$. Therefore every such $x$ lies in $\ker f$, so

$$
\mathfrak{n} = \{ x \in R \mid \exists m \in M,\; xm = 0 \} \subseteq \ker f.
$$
