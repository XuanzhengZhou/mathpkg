---
role: proof
locale: en
of_concept: inclusion-creates-limits
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

**Proof.** Let $|P|$ denote the discrete subcategory of $P$ consisting of all objects and only identity arrows. The inclusion $i : |P| \rightarrow P$ induces a functor $i^* = X^i : X^P \rightarrow X^{|P|}$ by precomposition. Now $X^{|P|}$ is isomorphic to the product category $\prod_{p \in |P|} X$, so limits in $X^{|P|}$ are computed componentwise. The functor $i^*$ essentially forgets the action of $P$ on arrows while retaining the object-wise data.

To show $i^*$ creates limits: given a diagram $S : J \rightarrow X^P$ and a limiting cone $\tau : L \rightarrow i^* S$ in $X^{|P|}$, we must lift this to a limiting cone in $X^P$. The cone $\tau$ assigns to each $p \in |P|$ a limit $L_p$ of $E_p S$ in $X$. By the pointwise limits theorem, these $L_p$ assemble into a functor $L : P \rightarrow X$ and the components $\tau_p$ form a natural transformation $\tau : L \rightarrow S$ in $X^P$, which is a limiting cone. This is exactly the content of the pointwise limits theorem, rephrased as creation of limits by $i^*$. $\square$
