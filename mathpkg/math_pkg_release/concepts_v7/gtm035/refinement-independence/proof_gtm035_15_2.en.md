---
role: proof
locale: en
of_concept: refinement-independence
source_book: gtm035
source_chapter: "15"
source_section: "15.2"
---
# Proof of Independence of Refinement Choice

**Lemma 15.2.** The homomorphism $K^{\mathcal{U}, \mathcal{V}} : H^p(\mathcal{U}, \mathbb{Z}) \to H^p(\mathcal{V}, \mathbb{Z})$ depends only on the coverings $\mathcal{U}$ and $\mathcal{V}$, and not on the particular choice of the refining map $\phi$.

## Proof (referenced to Hurewicz–Wallman)

The detailed proof is given in W. Hurewicz and H. Wallman, *Dimension Theory* (Princeton University Press, 1948), Chapter 8, Section 4. The essential argument is:

1. Let $\phi$ and $\psi$ be two maps of the label sets of $\mathcal{V}$ to those of $\mathcal{U}$, both satisfying $V_\beta \subseteq U_{\phi(\beta)}$ and $V_\beta \subseteq U_{\psi(\beta)}$ for each $\beta$. Let $\rho_\phi$ and $\rho_\psi$ be the corresponding cochain maps.

2. One constructs a cochain homotopy between $\rho_\phi$ and $\rho_\psi$. Specifically, define a map $D: C^p(\mathcal{U}) \to C^{p-1}(\mathcal{V})$ by

   $$(D c^p)(V_{\beta_0}, \ldots, V_{\beta_{p-1}}) = \sum_{i=0}^{p-1} (-1)^i c^p(U_{\phi(\beta_0)}, \ldots, U_{\phi(\beta_i)}, U_{\psi(\beta_i)}, \ldots, U_{\psi(\beta_{p-1})})$$

   whenever the relevant intersections are nonempty, and zero otherwise.

3. One verifies the homotopy identity:

   $$\rho_\phi - \rho_\psi = \delta \circ D + D \circ \delta.$$

   This shows that $\rho_\phi$ and $\rho_\psi$ differ by a cochain null-homotopy, hence they induce the same map on cohomology groups.

4. Therefore, for any cocycle $c \in Z^p(\mathcal{U})$, the two images $\rho_\phi c$ and $\rho_\psi c$ represent the same cohomology class in $H^p(\mathcal{V}, \mathbb{Z})$. Thus $K^{\mathcal{U},\mathcal{V}}$ is well-defined independent of the choice of $\phi$.
