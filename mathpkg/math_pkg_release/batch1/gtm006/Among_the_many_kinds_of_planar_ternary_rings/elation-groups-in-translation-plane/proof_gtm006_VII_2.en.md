---
role: proof
locale: en
of_concept: elation-groups-in-translation-plane
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

Parts (i) and (ii) are obvious since they are true for all groups of elations with a common axis.

For part (iii), let $\pi$ be any element of $\Pi_{[x_1, x_2]}$. Then $\pi \in \Pi_{[C, x_2]}$ for some point $C \in [\infty]$. If $C = A$ or $B$, then clearly $\pi \in \Pi_{[A, x_2]} \cap \Pi_{[B, x_2]}$. So assume $C \neq A$ and $C \neq B$.

By Theorem 4.7, $\pi$ is uniquely determined by the image of a single point $T$ not on $[\infty]$. Since $C \neq A$ and $C \neq B$, we have $AT \neq AT^\pi$ and $BT \neq BT^\pi$. Let $S = AT \cap BT^\pi$; then $S \neq T$.

Since $\mathcal{P}$ is a translation plane, there exist elations $\alpha \in \Pi_{[A, x_2]}$ and $\beta \in \Pi_{[B, x_2]}$ such that $T^\alpha = S$ and $S^\beta = T^\pi$. Hence $\alpha\beta \in \Pi_{[A, x_2]} \cap \Pi_{[B, x_2]}$ with $T^{\alpha\beta} = T^\pi$. By the uniqueness in Theorem 4.7, $\pi = \alpha\beta$, so $\pi \in \Pi_{[A, x_2]} \cap \Pi_{[B, x_2]}$.

Conversely, if $\pi \in \Pi_{[A, x_2]} \cap \Pi_{[B, x_2]}$ with $A \neq B$, then both $A$ and $B$ are centers of $\pi$. Since an elation with distinct centers must have axis joining those centers, and $A, B \in [\infty]$, the axis is $[\infty] = x_2$ and the center is $[\infty] \cap [\infty] = x_1$ (the intersection of the two center lines), so $\pi \in \Pi_{[x_1, x_2]}$.
