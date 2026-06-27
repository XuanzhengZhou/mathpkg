---
role: proof
locale: en
of_concept: cliffords-theorem
source_book: gtm052
source_chapter: "IV"
source_section: "5"
---

If $D$ is effective and special, then $K - D$ is also effective, so we can apply Lemma 5.5, and obtain

$$\dim|D| + \dim|K - D| \leqslant \dim|K| = g - 1.$$

On the other hand, by Riemann–Roch we have

$$\dim|D| - \dim|K - D| = \deg D + 1 - g.$$

Adding these two expressions, we have

$$2 \dim|D| \leqslant \deg D,$$

or in other words

$$\dim|D| \leqslant \frac{1}{2} \deg D.$$

This gives the first statement of the theorem. Also, it is clear that we have equality in case $D = 0$ or $D = K$.

For the converse direction when equality holds, suppose $D \neq 0, K$ and $\dim|D| = \frac{1}{2} \deg D$. Let $D'$ be the fixed part of $|D|$ and $E = D - D'$ its moving part. One shows by induction on $\deg D$ that $X$ must be hyperelliptic. The argument uses the fact that equality forces various inequalities in the proof to become equalities, leading to the conclusion that $|D|$ is a multiple of a $g_2^1$. In particular, by the induction hypothesis applied to $D'$, one concludes that $X$ is hyperelliptic, and then that $|D|$ must be a multiple of the unique $g_2^1$ on $X$.
