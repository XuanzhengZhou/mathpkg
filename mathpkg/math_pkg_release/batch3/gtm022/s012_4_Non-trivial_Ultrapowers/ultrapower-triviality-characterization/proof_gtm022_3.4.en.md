---
role: proof
locale: en
of_concept: ultrapower-triviality-characterization
source_book: gtm022
source_chapter: "3"
source_section: "4"
---

**Proof.** Suppose $\mathcal{F}$ is $\alpha$-complete. An element of $M^I / \mathcal{F}$ is $f\mathcal{F}$ for some $f: I \rightarrow M$. For each $m \in M$, put $J_m = \{i \in I \mid f(i) = m\}$. Then $\{J_m \mid m \in M\}$ is a partition of $I$ into $\alpha$ disjoint subsets (since $|M| = \alpha$, some of the $J_m$ may be empty). By Lemma 4.5, $J_m \in \mathcal{F}$ for some $m \in M$. This implies $f\mathcal{F} = m$, and therefore every element of $M^I / \mathcal{F}$ equals some element of $M$ under the natural embedding. Hence $M = M^I / \mathcal{F}$.

Suppose now that $\mathcal{F}$ is $\alpha$-incomplete. Then $\alpha$ must be infinite, and so there exists a family $\{X_\beta \mid \beta < \alpha\}$ of elements of $\mathcal{F}$ whose intersection $\bigcap_{\beta < \alpha} X_\beta$ is not in $\mathcal{F}$. Define $Y_0 = I - X_0$, and for $\beta > 0$ define

$$Y_\beta = X_0 \cap X_1 \cap \cdots \cap X_{\beta-1} - X_\beta.$$

Then $\{Y_\beta \mid \beta < \alpha\}$ is a partition of $I$ into $\alpha$ disjoint subsets. Since $\bigcap_{\beta < \alpha} X_\beta \notin \mathcal{F}$, the set $Y_\alpha = \bigcap_{\beta < \alpha} X_\beta$ (if defined) is not in $\mathcal{F}$. Moreover, no $Y_\beta$ for $\beta < \alpha$ belongs to $\mathcal{F}$: if $Y_\beta \in \mathcal{F}$ for some $\beta < \alpha$, then $X_\beta - X_{\beta+1} \in \mathcal{F}$ (or more precisely the set difference of the corresponding intersections is in $\mathcal{F}$), which would contradict the construction. Thus none of the $Y_\beta$ is in $\mathcal{F}$.

Since $|M| = \alpha$, we can index the elements of $M$ by the ordinals less than $\alpha$: $M = \{m_\beta \mid \beta < \alpha\}$. Define $f: I \rightarrow M$ by $f(i) = m_\beta$ if $i \in Y_\beta$. Then for each $m \in M$, the set $\{i \in I \mid f(i) = m\}$ is some $Y_\beta$, which is not in $\mathcal{F}$. Hence $f\mathcal{F}$ is not equal to any element of $M$ under the natural embedding, and therefore $M^I / \mathcal{F} \neq M$. $\square$
