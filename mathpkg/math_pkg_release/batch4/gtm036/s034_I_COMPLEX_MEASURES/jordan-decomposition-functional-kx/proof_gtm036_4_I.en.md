---
role: proof
locale: en
of_concept: jordan-decomposition-functional-kx
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
For real scalars, let $\phi \in (K(X))^*$. For each $f \geq 0$, define
$$\phi^+(f) = \sup \{ \phi(g): 0 \leq g \leq f \}.$$
By continuity of $\phi$, $\phi^+(f) < \infty$ for each $f \in K(X)$. The functional $\phi^+$ extends uniquely to a positive linear functional on $K(X)$ by writing general $f \in K(X)$ as $f = f^+ - f^-$ with $f^+, f^- \geq 0$ and setting $\phi^+(f) = \phi^+(f^+) - \phi^+(f^-)$. Similarly, $\phi^- = \phi^+ - \phi$ is a positive linear functional, and $\phi = \phi^+ - \phi^-$. By the Riesz representation theorem for positive linear functionals on $K(X)$ (see e.g., Halmos [4] pp. 247-248), there exist regular Borel measures $\mu^+$, $\mu^-$ such that $\phi^+(f) = \int f d\mu^+$ and $\phi^-(f) = \int f d\mu^-$ for all $f \in K(X)$, giving $\phi(f) = \int f d\mu^+ - \int f d\mu^-$.

For complex scalars, write $\phi = \phi_{\Re} + i \phi_{\Im}$ where $\phi_{\Re}, \phi_{\Im}$ are real-valued linear functionals on the real subspace of $K(X)$. Decompose each into positive and negative parts, yielding four positive functionals and thus four regular Borel measures.
