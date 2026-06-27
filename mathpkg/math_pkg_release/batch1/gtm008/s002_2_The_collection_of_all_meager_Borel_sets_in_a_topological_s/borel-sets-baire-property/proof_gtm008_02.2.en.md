---
role: proof
locale: en
of_concept: borel-sets-baire-property
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

If $B$ is open then $B = (B + 0) - 0$.

If $B$ is closed then
$$B = [B^0 + (B - B^0)] - 0.$$

Thus in the notation of Theorem 3.6, the result holds for each element of $A_0$.
If it holds for each element of $A_\alpha$ and if $B \in A_{\alpha+1}$ then there is an $\omega$-sequence $B_0, B_1, \ldots$, of elements in $A_\alpha$, such that $B = \sum_{i < \omega} B_i$ or $B = \prod_{i < \omega} B_i$.

Since $-G$ is closed, $(-G) - (-G)^0$ is meager and hence

$$B = [(-G)^0 + (-G - (-G)^0) + N_2] - (N_1 - N_2)$$

where $(-G - (-G)^0) + N_2$ and $N_1 - N_2$ are meager.
