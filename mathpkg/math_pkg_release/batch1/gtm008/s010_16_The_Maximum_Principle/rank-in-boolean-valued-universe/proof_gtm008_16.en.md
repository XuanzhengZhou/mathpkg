---
role: proof
locale: en
of_concept: rank-in-boolean-valued-universe
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

1. The equality $\llbracket u \in R(\check{\alpha}) \rrbracket = \sum_{v \in V_{\alpha}^{(\mathbf{B})}} \llbracket u = v \rrbracket$ follows from the definition of the Boolean-valued rank function $R$ and the fact that $V_{\alpha}^{(\mathbf{B})}$ is a set of representatives for all elements of $R(\check{\alpha})$.

2. Assume $\mathcal{D}(u) \subseteq V_{\alpha}^{(\mathbf{B})}$. Then, since by part 1 we have $\llbracket x \in R(\check{\alpha}) \rrbracket = 1$ for all $x \in V_{\alpha}^{(\mathbf{B})}$, it follows that

   $$\llbracket u \subseteq R(\check{\alpha}) \rrbracket = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow \llbracket x \in R(\check{\alpha}) \rrbracket) = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow 1) = 1.$$

3. This follows from part 1 and Theorem 16.25. Let $A_{\alpha} = \{t \in V^{(\mathbf{B})} \mid \mathcal{D}(t) = \mathcal{D}(u) \land \llbracket t \subseteq R(\check{\alpha}) \rrbracket = 1\}$. By Theorem 16.25,

   $$\llbracket u \subseteq R(\check{\alpha}) \rrbracket = \sum_{t \in A_{\alpha}} \llbracket u = t \rrbracket.$$
