---
role: proof
locale: en
of_concept: interior-convex-set-properties
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Properties of interior and closure of convex sets with interior

Let $E$ be a TVS over $\mathbb{K}$ and suppose that $A$ is a convex subset of $E$ with nonempty interior.

(i) If $a, b \in \operatorname{int} A$, then every internal point of the segment from $a$ to $b$ is also in $\operatorname{int} A$ by Lemma (25.19) applied with $b$ also interior (so $b \in \operatorname{int} A \subset \overline{A}$). Thus $\operatorname{int} A$ is convex.

(ii) Obviously $\overline{A} \supset \overline{\operatorname{int} A}$. Conversely, if $b \in \overline{A}$ and $V$ is any neighborhood of $b$, it is to be shown that $V$ intersects $\operatorname{int} A$. Choose any $a \in \operatorname{int} A$ and define $c_{\alpha} = \alpha a + (1 - \alpha)b$ for $0 < \alpha < 1$. By Lemma (25.19), $c_{\alpha} \in \operatorname{int} A$ for all $\alpha$. As $\alpha \rightarrow 0$, $c_{\alpha} \rightarrow 0a + 1b = b$, therefore $c_{\alpha} \in V$ for $\alpha$ sufficiently small. Hence $V \cap \operatorname{int} A \ne \varnothing$, so $b \in \overline{\operatorname{int} A}$.

(iii) Obviously $\operatorname{int} \overline{A} \supset \operatorname{int} A$. Conversely, assuming $x \in \operatorname{int} \overline{A}$, we show $x \in \operatorname{int} A$. Translating by $-x$, we can suppose $x = \theta$. Choose $a \in \operatorname{int} A$. By continuity of scalar multiplication, for $\lambda > 0$ sufficiently small, $\lambda a \in \operatorname{int} \overline{A}$, and by (i) applied to $\overline{A}$, $\lambda a$ is an interior point of $\overline{A}$. Then $-\lambda a$ is also in $\operatorname{int} \overline{A}$ for $\lambda$ sufficiently small. By Lemma (25.19), $\theta$ (as internal point of segment between $a$ and some negative point) is interior to $A$.
