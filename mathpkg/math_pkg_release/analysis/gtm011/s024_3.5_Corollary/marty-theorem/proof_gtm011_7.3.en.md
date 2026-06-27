---
role: proof
locale: en
of_concept: marty-theorem
source_book: gtm011
source_chapter: "7"
source_section: "3"
---

**Proof (forward direction).** The reason for introducing $\mu(f)$ is as follows: If $f: G \to \mathbb{C}_\infty$ is meromorphic then for $z$ close to $z'$ we have that $d(f(z), f(z'))$ is approximated by $\mu(f)(z) |z - z'|$. So if a bound can be obtained for $\mu(f)$ then $f$ is a Lipschitz function. If $f$ belongs to a family of functions and $\mu(f)$ is uniformly bounded for $f$ in this family, then the family is a uniformly Lipschitz set of functions.

Suppose $\mu(\mathcal{F})$ is locally bounded. Fix a compact set $K \subset G$ and let $M = \sup\{\mu(f)(z) : f \in \mathcal{F}, z \in K\} < \infty$. Then for any $f \in \mathcal{F}$ and $z, z' \in K$, the chordal distance satisfies
$$d(f(z), f(z')) \leq M |z - z'|.$$

To establish this inequality rigorously, select a polygonal path $P$ in $K$ and points $w_0, \ldots, w_n$ on $P$ such that:
1. $\sum_{k=1}^{n} |w_k - w_{k-1}| \leq 2|z - z'|$;
2. $\left| \frac{(1 + |f(w_{k-1})|^2)}{[(1 + |f(w_k)|^2)(1 + |f(w_{k-1})|^2)]^{\frac{1}{2}}} - 1 \right| < \alpha, \quad 1 \leq k \leq n$;
3. $\left| \frac{f(w_k) - f(w_{k-1})}{w_k - w_{k-1}} - f'(w_{k-1}) \right| < \alpha, \quad 1 \leq k \leq n$.

Then if $\beta_k = [(1 + |f(w_{k-1})|^2)(1 + |f(w_k)|^2)]^{\frac{1}{2}}$,

$$d(f(z), f(z')) \leq \sum_{k=1}^{n} d(f(w_{k-1}), f(w_k)) = \sum_{k=1}^{n} \frac{2}{\beta_k} |f(w_k) - f(w_{k-1})|$$
$$\leq \sum_{k=1}^{n} \frac{2}{\beta_k} \left| \frac{f(w_k) - f(w_{k-1})}{w_k - w_{k-1}} - f'(w_{k-1}) \right| |w_k - w_{k-1}| + \sum_{k=1}^{n} \frac{2}{\beta_k} \cdots$$

Since it is possible to let $w$ approach $z'$ without $w$ ever being a pole of $f$ (poles are isolated), this gives that $f(w) \to f(z') = \infty$ and $|z-w| \to |z-z'|$. The inequality holds if at most one of $z$ and $z'$ is a pole. A similar procedure gives that the inequality holds for all $z$ and $z'$ in $K$.

So if $K = B(a; r)$ and $\varepsilon > 0$ are given, then for $\delta < \min \{r, \varepsilon/2M\}$ we have that $|z-a| < \delta$ implies $d(f(z), f(a)) < \varepsilon$, and $\delta$ is independent of $f$ in $\mathcal{F}$. This gives that $\mathcal{F}$ is equicontinuous at each point $a$ in $G$.

The local boundedness of $\mu(\mathcal{F})$ thus implies equicontinuity of $\mathcal{F}$, and by Arzelà–Ascoli (applied in $C(G, \mathbb{C}_\infty)$), $\mathcal{F}$ is normal.

**Note on the converse.** The proof of the converse (that normality implies local boundedness of $\mu(\mathcal{F})$) is left to the reader.

**Example.** If $f_n(z) = nz$ for $n \geq 1$, then $\mu(f_n)(z) = \frac{2n}{1 + n^2 |z|^2}$. The family $\{f_n\}$ is not normal since $\mu(\{f_n\})$ is not locally bounded at $z = 0$.
