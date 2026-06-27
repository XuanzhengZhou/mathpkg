---
role: proof
locale: en
of_concept: interior-of-n-prime-contains-no-ltd
source_book: gtm047
source_chapter: "8"
source_section: "33"
---

Suppose that $\Delta$ is an LTD lying in $\operatorname{Int} N'$. We may suppose that $\Delta$ is in general position relative to the pseudo-cells $E$, in the sense that each component of each set $E \cap \Delta$ is either a polygon $J$ lying in $\operatorname{Int} E \cap \operatorname{Int} \Delta$ or a broken line $B$ intersecting $\operatorname{Bd} \Delta$ and $\operatorname{Bd} X$ precisely in its end-points; in either case, $\Delta$ and $E$ cross one another at $J$ or $B$.

**Step 1: Eliminate polygon intersections.** Suppose that some set $E \cap \Delta$ contains a polygon $J \subset \operatorname{Int} \Delta$. Then $J$ bounds a disk $\Delta_J \subset \operatorname{Int} \Delta$; we may suppose that $\Delta_J$ is inmost in $\Delta$, in the sense that $\Delta_J$ contains no other such polygon. It follows that $\Delta_J$ lies in a single set $C_v''$. Let $E_J$ be the disk in $E$ bounded by $J$. Since $\Delta_J \cap K' = \emptyset$, it follows by Lemma 8 that $E_J$ does not contain the center of $E$. Therefore $J$ (together with any components of $E \cap \Delta$ that may lie in $\operatorname{Int} E_J$) can be eliminated from $\Delta$ by a familiar splitting process. Thus we may assume that no set $E \cap \Delta$ contains a polygon.

**Step 2: Eliminate broken line intersections.** Suppose that some component of $E \cap \Delta$ is a broken line $B$, with its end-points in $\operatorname{Bd} \Delta$. Then $\operatorname{Bd} B$ lies in the polygon $J = E \cap \operatorname{Bd} X$, and $J$ is the union of two broken lines. Further splitting operations eliminate such intersections. After finitely many steps, all intersections are removed, contradicting the existence of the LTD.
