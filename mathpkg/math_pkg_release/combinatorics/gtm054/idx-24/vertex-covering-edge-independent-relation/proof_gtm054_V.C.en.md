---
role: proof
locale: en
of_concept: vertex-covering-edge-independent-relation
source_book: gtm054
source_chapter: "V"
source_section: "C"
---

\textbf{(a)} Let $\mathcal{F}$ be a vertex-covering $\beta_{10}$-set of edges. By the minimality of $\mathcal{F}$, $\Gamma_{\mathcal{F}}$ must be a forest. Since its cycle space is trivial, IIIA15b yields
$$\nu_0(\Gamma) = \nu_0(\Gamma_{\mathcal{F}}) = \nu_1(\Gamma_{\mathcal{F}}) + \nu_{-1}(\Gamma_{\mathcal{F}}) \leq \beta_{10}(\Gamma) + \alpha_1(\Gamma) + k,$$
since the selection of one edge from each component of $\Gamma_{\mathcal{F}}$ yields an independent set. Combining this with Theorem B14 yields the equality $\beta_{10} + k = \alpha_1 + \delta$.

\textbf{(b)} From part (a) and the definitions, the inequality $\delta \leq \alpha_0 \leq \beta_{10} + k$ follows directly. The left inequality comes from the relationship between the deficiency and the independent vertex number, while the right inequality is derived from the bound on $\alpha_0$ in terms of vertex-covering edge sets.
