---
role: proof
locale: en
of_concept: cross-ratio-determines-mapping
source_book: gtm006
source_chapter: "2"
source_section: "5"
---

Choose a frame $P_1, P_2, P_3$ in $\mathcal{P}(V)$. There exists a semi-linear transformation $\alpha$ of $V$ onto $W$ which sends the frame $P_1, P_2, P_3$ onto the frame $P_1^\beta, P_2^\beta, P_3^\beta$, and whose associated automorphism is $\phi$.

(Clearly such an $\alpha$ exists: there are many linear transformations from $V$ onto $W$ and the group of linear transformations of $W$ is three-transitive on its one-dimensional subspaces. Hence $P_1, P_2, P_3$ can be mapped onto $P_1^\beta, P_2^\beta, P_3^\beta$ by a linear transformation. But the mapping $(x, y) \rightarrow (x^\phi, y^\phi)$ is a semi-linear transformation with at least three fixed vectors and thus any three one-dimensional subspaces of $W$ are fixed by a semi-linear transformation with companion automorphism $\phi$.)

If $X$ is an arbitrary point of $\mathcal{P}(V)$ with parametric coordinate $r$ in the $P_i$ frame, then by the definition of cross ratio, $X^\beta$ must have parametric coordinate $r^\phi$ in the $P_i^\beta$ frame. But by the previous theorem, $X^\alpha$ also has parametric coordinate $r^\phi$ in the $P_i^\beta$ frame, and hence $X^\beta = X^\alpha$. i.e. $\beta$ is induced by $\alpha$.