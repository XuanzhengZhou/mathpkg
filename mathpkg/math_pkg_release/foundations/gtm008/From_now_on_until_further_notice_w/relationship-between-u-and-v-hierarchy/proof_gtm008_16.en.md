---
role: proof
locale: en
of_concept: relationship-between-u-and-v-hierarchy
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Statements 1 and 2 are proved by induction on $\alpha$.

**Statement 1** is obvious for the base case. For the inductive step, note that $U_\alpha^{(\mathbf{B})} \subseteq V_\alpha^{(\mathbf{B})}$ implies each $u \in U_\alpha^{(\mathbf{B})}$ has $u \in V_\alpha^{(\mathbf{B})}$, so $\llbracket u = u \rrbracket = 1$ already witnesses the claim with $v = u$.

**Statement 2.** Let $v \in V_{\alpha+1}^{(\mathbf{B})}$. Then $\mathcal{D}(v) \subseteq V_\alpha^{(\mathbf{B})}$. By the induction hypothesis, there exists a function $f: \mathcal{D}(v) \to U_\alpha^{(\mathbf{B})}$ such that

$$(\forall x \in \mathcal{D}(v))\; \llbracket x = f(x) \rrbracket = 1.$$

Define $u \in U_{\alpha+1}^{(\mathbf{B})}$ using $f$ to transport the values; one then verifies $\llbracket u = v \rrbracket = 1$.

**Statement 3.** This follows from Corollary 16.3 applied with $d = U_\alpha^{(\mathbf{B})}$.
