---
role: proof
locale: en
of_concept: v-equals-l-implies-gch
source_book: gtm001
source_chapter: "17"
source_section: "17.1"
---

We shall show that $\mathcal{P}(\aleph_\alpha) \subseteq L_{\aleph_\alpha + 1}$.

Suppose that $a \subseteq \aleph_\alpha$ and let $t$ be a term such that $D(t) = a$. Let $\eta = \max(\aleph_\alpha + 1, \bar{t}^+)$ and let $X = M^\eta(\aleph_\alpha \cup \{t\})$, where $\bar{t}$ is the cardinality of $t$ and $\bar{t}^+$ is the next cardinal after $\bar{t}$. Obviously $\bar{X} = \aleph_\alpha$. Since $M$ has the collapsing property, it follows that if $\pi: \eta' \rightarrow X$ is the collapsing map of $X$, then $\pi: \eta' \rightarrow \eta$ is a strong $M$-map. Let $t'$ be a term such that $t' < \eta'$ and $\pi(t') = t$. Noting that $\pi(\beta) = \beta$ for all $\beta < \aleph_\alpha$, we have for any $\beta < \aleph_\alpha$:

$$\beta \in a \leftrightarrow L \models \check{\beta} \in \pi(t')$$
$$\leftrightarrow L \models \check{\beta} \in t'$$
$$\leftrightarrow \beta \in D(t').$$

Hence $a = D(\hat{x}^{\gamma + 1}(x \in \aleph_\alpha \wedge x \in t'))$, where $\gamma = \max(\aleph_\alpha, \ldots)$. This shows $a \in L_{\aleph_\alpha + 1}$, establishing $\mathcal{P}(\aleph_\alpha) \subseteq L_{\aleph_\alpha + 1}$, from which GCH follows.
