---
role: proof
locale: en
of_concept: elation-groups-in-translation-plane
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

**Proof.** Parts (i) and (ii) are obvious since they are true for all groups of elations with a common axis. Part (iii) is Exercise 4.25, but we give a proof for completeness.

Let $\pi$ be any element of $\Pi_{[x_1, x_2]}$; then $\pi \in \Pi_{[C, x_2]}$ for some point $C \in [\infty]$. If $C = A$ or $B$ then, clearly, $\pi \in \Pi_{[A, x_2]} \cap \Pi_{[B, x_2]}$, so assume $C \neq A, C \neq B$.

By Theorem 4.7, $\pi$ is uniquely determined by the image of a single point $T$ not on $[\infty]$. Since $C \neq A$ or $B$, $AT \neq AT^\pi$ and $BT \neq BT^\pi$, so if $S = AT \cap BT^\pi$ then $S \neq T$. Since $\mathcal{P}$ is a translation plane, there exist elations $\alpha \in \Pi_{[A, x_2]}$, $\beta \in \Pi_{[B, x_2]}$ such that $T^\alpha = S$ and $S^\beta = T^\pi$. Hence $\alpha\beta \in \Pi_{[A, x_2]}\Pi_{[B, x_2]}$ with $T^{\alpha\beta} = T^\pi$, so by uniqueness $\pi = \alpha\beta$ and $\pi \in \langle \Pi_{[A, x_2]}, \Pi_{[B, x_2]} \rangle$. Moreover, one can show $\alpha\beta$ is in fact an $(x_1, x_2)$-elation, yielding the equality.