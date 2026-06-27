---
role: proof
locale: en
of_concept: cliffords-theorem
source_book: gtm052
source_chapter: "IV"
source_section: "§5"
---
If $D$ is effective and special, then $K - D$ is also effective, so we can apply Lemma 5.5, and obtain

$$\dim|D| + \dim|K - D| \leqslant \dim|K| = g - 1.$$

On the other hand, by Riemann-Roch we have

$$\dim|D| - \dim|K - D| = \deg D + 1 - g.$$

Adding these two expressions, we have

$$2 \dim|D| \leqslant \deg D,$$

or in other words $\dim|D| \leqslant \frac{1}{2} \deg D$.

This gives the first statement of the theorem. Also, it is clear that we have equality in case $D = 0$ or $D = K$. Conversely, suppose equality holds. If $D \neq 0, K$, we prove by induction on $g$ that $X$ must be hyperelliptic, and $|D|$ a multiple of the $g_2^1$. Let $D'$ be the divisor formed by taking the common part of $D$ and $K-D$. By construction of $D'$, we have an exact sequence

$$0 \to \mathcal{L}(D') \to \mathcal{L}(D) \oplus \mathcal{L}(E) \to \mathcal{L}(D + E - D') \to 0,$$

where $E \sim K - D$ and we consider these as subspaces of the constant sheaf $\mathcal{K}$ on $X$, with the first map being addition and the second subtraction. Taking global sections, we have

$$\dim|D| + \dim|E| \leqslant \dim|D'| + \dim|D + E - D'|.$$

But $E \sim K - D$ and $D + E - D' \sim K - D'$, and using the equality condition, we conclude that $\dim|D'| = \frac{1}{2} \deg D'$. By the induction hypothesis, this implies $X$ is hyperelliptic.

Now if $D \neq 0, K$ and $\dim|D| = \frac{1}{2} \deg D$, letting $r = \dim|D|$ and considering the linear system $|D| + (g - 1 - r)g_2^1$, it has degree $2g - 2$ and dimension $\geqslant g - 1$ by Lemma 5.5, so it must equal the canonical system $|K| = (g-1)g_2^1$. Hence $|D| = r \cdot g_2^1$.
