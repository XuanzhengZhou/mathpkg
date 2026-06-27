---
role: proof
locale: en
of_concept: prop-for-aperiodic-transient-random-walk-in
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Suppose P5 is false, and call $G(x,0) = u(x)$. Then, in view of P1, we must have

$$\lim_{|x| \to \infty} [u(x) + u(-x)] = L > 0.$$

Now we choose an $\epsilon$, $0 < \epsilon < L/3,$ and decompose $R$ into three sets $A, B, C$ as follows. $A$ is to be a sphere, i.e., $A = [x | |x| \leq r]$ with the radius $r$ chosen so that

$$|

Since $L > 3\epsilon$ the above inequalities give

$$|u(x) - u(y)| > L - 2\epsilon > \epsilon.$$

Now $y = x + t$ with $|t| = 1$, and according to the definition of the set $A$, $x$ must be in $A$, which it is not. This contradiction proves P5. Observe that aperiodicity is not strictly necessary for P5. All we need is that $\bar{R}$ be a group with more than one generator, i.e., that the random walk does not take place on a one-dimensional subspace of $R$.

Now we are free to concentrate on one-dimensional random walk, which unfortunately presents much greater difficulties. First we deal with the comparatively straightforward case when the absolute first moment is finite. The results constitute a rather intuitive extension of the renewal theorem, which was obtained by Blackwell [4] and several other authors around 1952, but which had been conjectured and proved in special cases before 1940.$^2$
