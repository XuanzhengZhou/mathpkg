---
role: proof
locale: en
of_concept: exactness-of-completion-functor
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

Since $A$ is a Zariski ring, it is noetherian and Hausdorff, so Theorem 6 applies, giving exactness of the completed sequence.

More directly: the hypothesis $f(E) = g^{-1}(0)$ implies $\bar{g}(\bar{f}(\xi)) = 0$ for all $\xi \in \hat{E}$ by continuity. Thus the kernel $\bar{g}^{-1}(0)$ of $\bar{g}$ contains $\bar{f}(\hat{E})$. We prove equality.

The submodule $G' = g(F)$ of $G$ has the $\mathfrak{m}$-topology as induced topology ($\S$2, Theorem 4). Its completion $\hat{G}'$ is identical with its closure in $\hat{G}$. By continuity $\bar{g}$ maps $\hat{F}$ into $\hat{G}'$, and since $\bar{g}(\hat{F})$ is closed (as $\hat{A}$ is a Zariski ring) and contains $g(F) = G'$, we have $\bar{g}(\hat{F}) = \hat{G}'$.

Now let $\eta \in \hat{F}$ with $\bar{g}(\eta) = 0$. Approximate $\eta$ by $y_n \in F$ with $\eta - y_n \in \hat{A}\mathfrak{m}^n\hat{F} = \mathfrak{m}^n\hat{F}$. Then $g(y_n) \in \mathfrak{m}^n\bar{g}(\hat{F}) \cap g(F) = \mathfrak{m}^n\hat{G}' \cap G' = \mathfrak{m}^n G' = g(\mathfrak{m}^n F)$. Lift to get $x_n \in F$ with $g(x_n) = g(y_n)$ and $x_n \in \mathfrak{m}^n F$. Then $\{y_n - x_n\}$ is Cauchy in $\ker(g) = f(E)$. Its limit provides a preimage under $\bar{f}$, proving exactness.