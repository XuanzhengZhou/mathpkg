---
role: proof
locale: en
of_concept: erdos-rado
source_book: gtm008
source_chapter: "5"
source_section: "21. A Proof of Marczewski's Theorem"
---

For each $\delta < \alpha^+$ we construct a set $A_\delta \subseteq A$ such that

(a) $(\forall \delta < \alpha^+)[\bar{A}_\delta \leq \gamma^\alpha]$, and

(b) $A = \bigcup_{\delta < \alpha^+} A_\delta$.

This proves the theorem since $\bar{A} \leq \alpha^+ \cdot \gamma^\alpha = \gamma^\alpha$ (as $\gamma \geq \aleph_0$ implies $\alpha^+ \leq \gamma^\alpha$ for $\alpha \geq \aleph_0$, and otherwise the bound is immediate).

We define $A_\delta$ by recursion. For convenience we start with $A_{-1} = \emptyset$. Suppose $A_\delta$ for $\delta < \beta$ (where $\beta < \alpha^+$) has already been defined. Let

$$E_\beta = \bigcup_{\delta < \beta} \left( \bigcup A_\delta \right).$$

For each $K \subseteq E_\beta$ let

$$\bar{K} = \{x \in A \mid x \cap E_\beta = K\}$$

and let $K^*$ be a maximal quasi-disjoint subset of $\bar{K}$. Moreover, we require that

$$(\exists S, T \in \bar{K})[S \cap T = K] \;\Longrightarrow\; \bigcap K^* = K.$$

Set $A_\beta = \bigcup \{K^* \mid K \subseteq E_\beta\}$. Since $E_\beta$ is the union of at most $\alpha^+ \cdot \gamma^\alpha$ sets (by induction hypothesis), each of cardinality $\leq \alpha$, we have $\bar{E}_\beta \leq \alpha \cdot \alpha^+ \cdot \gamma^\alpha = \gamma^\alpha$. The number of subsets $K$ of $E_\beta$ of cardinality $\leq \alpha$ is at most $(\gamma^\alpha)^\alpha = \gamma^\alpha$. Each $K^*$, being a quasi-disjoint subset of $A$, has cardinality $\leq \gamma$ by hypothesis. Therefore

$$\bar{A}_\beta \leq \gamma^\alpha \cdot \gamma = \gamma^\alpha,$$

proving (a).

To prove (b), suppose that

$$A - \bigcup_{\delta < \alpha^+} A_\delta \neq \emptyset.$$

Let $S \in A - \bigcup_{\delta < \alpha^+} A_\delta$, and for $\delta < \alpha^+$, let $K_\delta = S \cap E_\delta$. Since $S \in \bar{K}_\delta$, we have $K_\delta^* \neq \emptyset$.

**Claim:** $(\forall \delta < \alpha^+)(\exists T \in K_\delta^*)[S \cap (T - E_\delta) \neq \emptyset]$.

Suppose the claim fails, i.e., for some $\delta < \alpha^+$ we have $(\forall T \in K_\delta^*)[S \cap (T - E_\delta) = \emptyset]$. Then

$$(\forall T \in K_\delta^*)[S \cap T \subseteq S \cap E_\delta = K_\delta = T \cap E_\delta],$$

since $T \in \bar{K}_\delta$ implies $T \cap E_\delta = K_\delta$. Therefore

$$(\forall T \in K_\delta^*)[S \cap T = K_\delta].$$

Since $K_\delta^* \neq \emptyset$, by our requirement on $K_\delta^*$ (taking $S$ and any $T \in K_\delta^*$ as the two elements of $\bar{K}_\delta$ intersecting in $K_\delta$), we obtain

$$\bigcap K_\delta^* = K_\delta.$$

Now $K_\delta^* \cup \{S\}$ is quasi-disjoint: for distinct $T, T' \in K_\delta^*$, we have $T \cap T' = \bigcap K_\delta^* = K_\delta$; and $S \cap T = K_\delta$ for all $T \in K_\delta^*$. Since $K_\delta^*$ is maximal, $S \in K_\delta^* \subseteq A_\delta$, contradicting $S \in A - \bigcup A_\delta$. This proves the claim.

By the claim, for each $\delta < \alpha^+$ choose $T_\delta \in K_\delta^*$ and $x_\delta \in S \cap (T_\delta - E_\delta)$. Since $\bar{S} \leq \alpha$, the sequence $\langle x_\delta \mid \delta < \alpha^+\rangle$ of length $\alpha^+$ must have repetitions. Choose $\delta_1 < \delta_2 < \alpha^+$ with $x_{\delta_1} = x_{\delta_2} = x_0$. Then $x_0 \in T_{\delta_1} \cap T_{\delta_2}$. By construction $T_{\delta_1}, T_{\delta_2} \in K_{\delta_2}^*$ (since $K_{\delta_1}^* \subseteq \bar{K}_{\delta_2}$ for $\delta_1 < \delta_2$). Because $K_{\delta_2}^*$ is quasi-disjoint,

$$T_{\delta_1} \cap T_{\delta_2} = \bigcap K_{\delta_2}^* = K_{\delta_2} = S \cap E_{\delta_2}.$$

But $x_0 \in T_{\delta_1} - E_{\delta_1}$ and $E_{\delta_1} \subseteq E_{\delta_2}$, so $x_0 \notin E_{\delta_2}$, contradicting $x_0 \in S \cap E_{\delta_2}$ (since $x_0 \in S$). This contradiction establishes (b). $\square$
