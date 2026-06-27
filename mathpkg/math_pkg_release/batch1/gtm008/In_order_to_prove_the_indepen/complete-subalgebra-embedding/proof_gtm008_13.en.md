---
role: proof
locale: en
of_concept: complete-subalgebra-embedding
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by induction on the rank of elements in $V^{(B)}$.

**Part 1.** Since any function into $B$ is also a function into $B'$ (as $B \subseteq B'$), we have by induction on $\alpha$ that $V_{\alpha}^{(B)} \subseteq V_{\alpha}^{(B')}$ for all $\alpha$. The base case $V_0^{(B)} = \emptyset = V_0^{(B')}$ is trivial. For the successor step, if $u \in V_{\alpha+1}^{(B)}$, then $u: \mathcal{D}(u) \to B \subseteq B'$ and $\mathcal{D}(u) \subseteq V_{\alpha}^{(B)} \subseteq V_{\alpha}^{(B')}$ by induction hypothesis, so $u \in V_{\alpha+1}^{(B')}$. Hence $V^{(B)} = \bigcup_{\alpha} V_{\alpha}^{(B)} \subseteq \bigcup_{\alpha} V_{\alpha}^{(B')} = V^{(B')}$.

**Part 2.** By simultaneous induction on the recursive definition of the Boolean values. For $u, v \in V^{(B)}$, the definitions of $[\![u \in v]\!]$ and $[\![u = v]\!]$ involve only Boolean operations ($\sum$, $\prod$, $\cdot$, $\Rightarrow$) applied to values in $B$. Since $B$ is a complete subalgebra of $B'$, the suprema and infima of subsets of $B$ are the same whether computed in $B$ or $B'$. Thus the Boolean values are identical in both structures.
