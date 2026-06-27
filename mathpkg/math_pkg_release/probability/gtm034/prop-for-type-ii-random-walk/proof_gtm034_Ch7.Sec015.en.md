---
role: proof
locale: en
of_concept: prop-for-type-ii-random-walk
source_book: gtm034
source_chapter: "7"
source_section: "015"
---

Proof: P28.7 applied to P1 gives

$$\frac{1}{2} H_C(-\infty,0) + \frac{1}{2} H_C(+\infty,0) = H_C(x,0) + [a(x) - a(x - c)]\Pi_C(0,c).$$

Letting first $x \to +\infty$, and then $x \to -\infty$, one obtains the two equations

$$\frac{1}{2} H_C(+\infty,0) - \frac{1}{2} H_C(-\infty,0) = \Pi_C(0,c) \lim_{x \to +\infty} [a(x - c) - a(x)],$$

$$\frac{1}{2} H_C(-\infty,0) - \frac{1}{2} H_C(+\infty,0) = \Pi_C(0,c) \lim_{x \to -\infty} [a(x - c) - a(x)].$$

They show that the limits in P2 exist, and that one is the negative of the other. (The point $c$ being arbitrary, we set $c = y \neq 0$.) To evaluate these limits we call

$$\lim_{x \to +\infty} [a(x + 1) - a(x)] = \alpha.$$

Then P2 is proved as soon as we show that $\alpha = (\sigma^2)^{-1}$. However, taking the Césaro mean, i.e., writing for $x > 0$

$$a(x) = \sum_{k=1}^{x} [a(k) - a(k - 1)],$$

and proceeding in a similar way for $x < 0$, we find

$$

tools. The properties of the potential kernel, described in the next three lemmas, will be crucial for the proof, in P8, that $a(x)$ increases more slowly than a linear function of $|x|$.
