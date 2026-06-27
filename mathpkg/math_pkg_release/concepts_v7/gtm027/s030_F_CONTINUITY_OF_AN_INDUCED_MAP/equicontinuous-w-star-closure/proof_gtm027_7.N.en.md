---
role: proof
locale: en
of_concept: equicontinuous-w-star-closure
source_book: gtm027
source_chapter: "7"
source_section: "N"
---

# Proof of Equicontinuity of the Weak-Star Closure

Let $X$ be a topological vector space and $F \subseteq X^*$. If $F$ is equicontinuous, then its $w^*$-closure $\overline{F}^{w^*}$ is also equicontinuous.

**Proof.** Recall that $F$ is equicontinuous iff it is norm bounded (for normed spaces; for general locally convex spaces, equicontinuity means there exists a neighborhood $U$ of $0$ in $X$ such that $|f(x)| \leq 1$ for all $f \in F$, $x \in U$).

Take any $g \in \overline{F}^{w^*}$. For any net $\{f_\alpha\} \subseteq F$ with $f_\alpha \to g$ pointwise, and any $x \in X$,

$$|g(x)| = \lim_\alpha |f_\alpha(x)| \leq \sup_{f \in F} |f(x)|.$$

The equicontinuity condition involves a uniform bound on a neighborhood of $0$, and this bound is preserved under pointwise limits. Specifically, if $|f(x)| \leq 1$ for all $f \in F$ and $x \in U$, then for $g \in \overline{F}^{w^*}$ and $x \in U$, $|g(x)| = \lim |f_\alpha(x)| \leq 1$.

For normed spaces: $\|g\| = \sup_{\|x\| \leq 1} |g(x)| = \sup_{\|x\| \leq 1} \lim_\alpha |f_\alpha(x)| \leq \sup_{f \in F} \|f\| < \infty$, so $\overline{F}^{w^*}$ is norm bounded, hence equicontinuous.
