---
role: proof
locale: en
of_concept: union-of-open-sets
source_book: gtm012
source_chapter: "1"
source_section: "5. Metric spaces"
---

# Proof of Theorem: Arbitrary Union of Open Sets is Open

Suppose $(A_{\beta})_{\beta \in B}$ is any collection of open subsets of a metric space $(S, d)$. Let $A = \bigcup_{\beta \in B} A_{\beta}$. We must show $A$ is open.

Suppose $x \in A = \bigcup_{\beta \in B} A_{\beta}$. Then for some particular $\beta$, $x \in A_{\beta}$. Since $A_{\beta}$ is open, there is an $r > 0$ so that $B_r(x) \subset A_{\beta}$. But $A_{\beta} \subset A$, so $B_r(x) \subset A$. Thus $A$ is open. $\square$
