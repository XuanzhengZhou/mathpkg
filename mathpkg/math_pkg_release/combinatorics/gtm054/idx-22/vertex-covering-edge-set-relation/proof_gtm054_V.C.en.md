---
role: proof
locale: en
of_concept: vertex-covering-edge-set-relation
source_book: gtm054
source_chapter: "V"
source_section: "C"
---

\textbf{(a)} Let $\mathcal{F}$ be a vertex-covering $\beta_{10}$-set of edges. By the minimality of $\mathcal{F}$, the subgraph $\Gamma_{\mathcal{F}}$ must be a forest. Since its cycle space is trivial, formula IIIA15b yields

$$\nu_0(\Gamma) = \nu_0(\Gamma_{\mathcal{F}}) = \nu_1(\Gamma_{\mathcal{F}}) + \nu_{-1}(\Gamma_{\mathcal{F}}) \leq \beta_{10}(\Gamma) + \alpha_1(\Gamma) + k,$$

since the selection of one edge from each component of $\Gamma_{\mathcal{F}}$ yields an independent set. Combining this with the identity $\nu_0(\Gamma) = \alpha_1(\Gamma) + \beta_{10}(\Gamma) + \delta(\Gamma) - k$ (obtained from the definition of deficiency and accounting for isolated vertices) yields $\beta_{10} + k = \alpha_1 + \delta$.

\textbf{(b)} For the first inequality $\delta \leq \alpha_0$, observe that an independent vertex set of size $\alpha_0$ avoids at least $\alpha_0$ vertices, so the deficiency $\delta$ cannot exceed $\alpha_0$. For the second inequality $\alpha_0 \leq \beta_{10} + k$, note that any vertex-covering $\beta_{10}$-set of edges together with the $k$ isolated vertices covers all vertices, and from any covering of edges one can extract a vertex cover that bounds the size of any independent vertex set. Specifically, selecting one endpoint from each edge in a $\beta_{10}$-set together with the isolated vertices yields a set of size at most $\beta_{10} + k$ that meets every edge, hence every independent set has size at most $\beta_{10} + k$.
