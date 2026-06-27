---
role: proof
locale: en
of_concept: u-alpha-v-alpha-equivalence
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

1 and 2 are proved by induction on $\alpha$. 1 is obvious.

2. Let $v \in V_{\alpha+1}^{(B)}$. Then $\mathcal{D}(v) \subseteq V_{\alpha}^{(B)}$. By the induction hypothesis, there exists a function $f: \mathcal{D}(v) \rightarrow U_{\alpha}^{(B)}$ such that $(\forall x \in \mathcal{D}(v)) [\llbracket x = f(x) \rrbracket = 1]$. Define $u \in U_{\alpha+1}^{(B)}$ by $u(z) = \sum_{x \in \mathcal{D}(v)} [\llbracket z = f(x) \rrbracket \cdot v(x)]$ for $z \in U_{\alpha}^{(B)}$. Then one verifies $\llbracket u = v \rrbracket = 1$.

3. Follows from Corollary 16.3 with $d = U_{\alpha}^{(\mathbf{B})}$.
