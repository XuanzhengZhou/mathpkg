---
role: proof
locale: en
of_concept: continuous-linear-mapping-equivalent-conditions
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Equivalent conditions for continuity of linear mappings between normed spaces

**Theorem (40.1).** Let $E$ and $F$ be normed spaces over $\mathbb{K}$ and let $T: E \to F$ be a linear mapping. The following conditions are equivalent:

(a) $T$ is continuous;
(b) there exists a constant $K \geq 0$ such that $\|Tx\| \leq K\|x\|$ for all $x \in E$;
(c) $\{\|Tx\| : \|x\| = 1\}$ is bounded;
(d) $\{\|Tx\| : \|x\| < 1\}$ is bounded;
(e) $\{\|Tx\| : \|x\| \leq 1\}$ is bounded.

Moreover, if $M_1, M_2, M_3$ are the suprema of the sets in (c), (d), (e), then $M_1 = M_2 = M_3$. Denoting their common value by $M$, one has $\|Tx\| \leq M\|x\|$ for all $x \in E$, and $M$ is minimal among all such constants.

**Proof.**

(a) $\Rightarrow$ (b): Since $T$ is continuous at $\theta$, there exists $\delta > 0$ such that $\|x\| < \delta$ implies $\|Tx\| < 1$. For any $x \neq \theta$, set $y = \frac{\delta}{2\|x\|}x$; then $\|y\| = \delta/2 < \delta$, so $\|Ty\| < 1$, i.e., $\|Tx\| < \frac{2}{\delta}\|x\|$. Taking $K = 2/\delta$ yields (b). (The case $x = \theta$ is trivial.)

(b) $\Rightarrow$ (c): If $\|x\| = 1$, then $\|Tx\| \leq K\|x\| = K$, so the set in (c) is bounded by $K$, and $M_1 \leq K$.

(c) $\Rightarrow$ (d): If $0 < \|x\| < 1$, then $\|Tx\| = \|x\| \cdot \|T(x/\|x\|)\| \leq M_1\|x\| < M_1$. Hence the set in (d) is bounded by $M_1$, and $M_2 \leq M_1$.

(d) $\Rightarrow$ (e): If $\|x\| \leq 1$, then $\|Tx\| \leq M_2$ (for $x = \theta$ this is trivial; for $\|x\| < 1$ it holds by definition of $M_2$; for $\|x\| = 1$, approximate $x$ by vectors of norm $< 1$ and use continuity of the norm). Thus the set in (e) is bounded, and $M_3 = M_2$.

(e) $\Rightarrow$ (a): By hypothesis, $M_3 < \infty$. Note that $\|Tx\| \leq M_3\|x\|$ for all $x \in E$: this is trivial if $x = \theta$; if $x \neq \theta$, then $y = \|x\|^{-1}x$ has norm $1$, therefore $\|Ty\| \leq M_3$, i.e., $\|Tx\| \leq M_3\|x\|$. If $x_n \in E$, $x_n \to \theta$, then $\|Tx_n\| \leq M_3\|x_n\|$ shows that $Tx_n \to \theta = T\theta$, thus $T$ is continuous at $\theta$; therefore $T$ is continuous on $E$.

Thus the conditions (a)--(e) are equivalent. In the course of the proof, it was shown that $M_2 \leq M_1$ and $M_3 = M_2$; since $M_1 \leq M_3$ trivially (the unit sphere is contained in the closed unit ball), it follows that $M_2 = M_1 = M_3$. Writing $M$ for the common value, it was shown in the proof of "(e) $\Rightarrow$ (a)" that $\|Tx\| \leq M\|x\|$ for all $x$. On the other hand, if $K \geq 0$ satisfies $\|Tx\| \leq K\|x\|$ for all $x \in E$, then $M \leq K$ as shown in the proof of "(b) $\Rightarrow$ (c)." Thus $M$ is the minimal such constant.
