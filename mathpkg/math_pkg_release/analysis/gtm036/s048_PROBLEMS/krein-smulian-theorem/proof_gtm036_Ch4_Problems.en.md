---
role: proof
locale: en
of_concept: krein-smulian-theorem
source_book: gtm036
source_chapter: "4"
source_section: "PROBLEMS"
---

For if $r > 1$ there is some $\alpha \in \Gamma$ with $A_\alpha \subset A_\gamma + (r - 1)U$ for all $\gamma$. Hence $A_\alpha \subset r(A_\gamma \cup U)^\circ$; it follows that $(U^\circ \cap B)^{-} \subset rA_\alpha^\circ$, and hence that $U^\circ \cap B^{-} = \bigcap \{r(U^\circ \cap B): r > 1\} = (U^\circ \cap B)^{-}$, which is weak* closed.

By hypothesis $B^{-}$ is weak* closed. Thus $B^{-} = B_0^\circ$. Now there is some $\gamma$ with $A_\gamma \subset A_\beta + U$ for all $\beta$. It is enough to show $(B_0 + U)^\circ \subset A_\gamma^\circ$, for then $A_\gamma \subset (B_0 + U)^\circ \subset B_0 + 2U$, and $\{A_\gamma : \gamma \in \Gamma\}$ converges to $B_0 = \bigcap \{A_\gamma : \gamma \in \Gamma\}$. If $f \in (B_0 + U)^\circ$, let $m = \sup \{|f(x)| : x \in B_0\}$ and $n = \sup \{|f(x)| : x \in U\}$. Then $m + n \leq 1$; if $m > 0$, $f \in mB_0^\circ = mB^{-}$ and so for $r > 1$, $f \in mrA_\beta^\circ$ for some $\beta$. Thus on $A_\gamma$, $|f(x)| \leq mr + n$. If $m = 0$, then for $r > 1$, $f \in (r - 1)B^{-}$ and so $f \in r(r - 1)A_\beta^\circ$ for some $\beta$, so that on $A_\gamma$, $|f(x)| \leq r(r - 1) + 1$.
