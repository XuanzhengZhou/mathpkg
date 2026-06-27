---
role: proof
locale: en
of_concept: operator-norm-algebra
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

It is easily seen that if $\mathcal{E}$ and $\mathcal{F}$ are arbitrary normed spaces, then $\mathcal{L}(\mathcal{E},\mathcal{F})$ is a linear submanifold of the full space of linear transformations of $\mathcal{E}$ into $\mathcal{F}$, and is therefore a linear space in its own right. In order to verify this, it need only be checked that if $S$ and $T$ are bounded, and if $\lambda$ is a scalar, then $S + T$ and $\lambda S$ are bounded too. But for an arbitrary vector $x$ in $\mathcal{E}$ we have

$$\| (S + T) x \| \leq \| S x \| + \| T x \| \leq \| S \| \| x \| + \| T \| \| x \|$$

and

$$\| (\lambda S) x \| = \| \lambda (S x) \| \leq |\lambda| \| S \| \| x \|,$$

and from these inequalities it follows not only that $S + T$ and $\lambda S$ are bounded, but also that

$$\| S + T \| \leq \| S \| + \| T \|$$

and

$$\| \lambda S \| = |\lambda| \| S \|.$$

Since $\| S \| = 0$ implies $S = 0$, we see that $\| \|$ is, in fact, a norm on $\mathcal{L}(\mathcal{E},\mathcal{F})$. The submultiplicativity $\|ST\| \leq \|S\|\|T\|$ follows directly from Theorem 12.3. And it is obvious that $\|1_{\mathcal{E}}\| = 1$.
