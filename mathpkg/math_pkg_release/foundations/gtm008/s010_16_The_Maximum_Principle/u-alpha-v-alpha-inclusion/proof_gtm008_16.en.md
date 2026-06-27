---
role: proof
locale: en
of_concept: u-alpha-v-alpha-inclusion
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Parts 1 and 2 are proved by induction on $\alpha$. Part 1 is obvious.

For part 2: Let $v \in V_{\alpha+1}^{(\mathbf{B})}$. Then $\mathcal{D}(v) \subseteq V_{\alpha}^{(\mathbf{B})}$. By the induction hypothesis, there exists a function $f: \mathcal{D}(v) \rightarrow U_{\alpha}^{(\mathbf{B})}$ such that

$$(\forall x \in \mathcal{D}(v)) [\llbracket x = f(x) \rrbracket = 1].$$

Define $u \in U_{\alpha+1}^{(\mathbf{B})}$ by $u(y) = \sum_{x \in \mathcal{D}(v)} v(x) \cdot \llbracket y = f(x) \rrbracket$ for $y \in U_{\alpha}^{(\mathbf{B})}$. Then one verifies that $\llbracket u = v \rrbracket = 1$.

For part 3: This follows from Corollary 16.3 with $d = U_{\alpha}^{(\mathbf{B})}$, since elements of $U_{\alpha+1}^{(\mathbf{B})}$ have domain exactly $U_{\alpha}^{(\mathbf{B})}$ by definition.
