---
role: proof
locale: en
of_concept: refinement-homomorphism
source_book: gtm035
source_chapter: "15"
source_section: "15.1"
---
# Proof of Refinement Homomorphism for Čech Cohomology

**Lemma 15.1.** Let $\mathcal{U} = \{U_\alpha\}$ and $\mathcal{V} = \{V_\beta\}$ be open coverings of a compact Hausdorff space $X$ with $\mathcal{V} > \mathcal{U}$ (i.e., $\mathcal{V}$ refines $\mathcal{U}$). Let $\phi$ be a map of the label sets such that $V_\beta \subseteq U_{\phi(\beta)}$ for each $\beta$. Define $\rho: C^p(\mathcal{U}) \to C^p(\mathcal{V})$ by

$$\rho c^p(V_{\beta_0}, V_{\beta_1}, \ldots, V_{\beta_p}) = c^p(U_{\phi(\beta_0)}, \ldots, U_{\phi(\beta_p)}).$$

Then $\rho$ induces a well-defined homomorphism

$$K^{\mathcal{U}, \mathcal{V}} : H^p(\mathcal{U}, \mathbb{Z}) \to H^p(\mathcal{V}, \mathbb{Z})$$

on cohomology.

## Proof (referenced to Hurewicz–Wallman)

The detailed proof is given in W. Hurewicz and H. Wallman, *Dimension Theory* (Princeton University Press, 1948), Chapter 8, Section 4. The essential steps are:

1. **$\rho$ is a cochain map.** One verifies that $\rho$ commutes with the coboundary operator $\delta$: $\rho \circ \delta_{\mathcal{U}} = \delta_{\mathcal{V}} \circ \rho$. Indeed, for a $p$-cochain $c^p$,

   $$(\rho \delta c^p)(V_{\beta_0}, \ldots, V_{\beta_{p+1}}) = \sum_{i=0}^{p+1} (-1)^i c^p(U_{\phi(\beta_0)}, \ldots, \widehat{U_{\phi(\beta_i)}}, \ldots, U_{\phi(\beta_{p+1})}) = (\delta \rho c^p)(V_{\beta_0}, \ldots, V_{\beta_{p+1}}).$$

2. **$\rho$ preserves cocycles and coboundaries.** Since $\rho \circ \delta = \delta \circ \rho$, the image of a cocycle (resp. coboundary) under $\rho$ is a cocycle (resp. coboundary).

3. **$\rho$ induces $K^{\mathcal{U},\mathcal{V}}$ on cohomology.** Define $K^{\mathcal{U},\mathcal{V}}([c]) = [\rho c]$ for a cohomology class $[c] \in H^p(\mathcal{U}, \mathbb{Z})$. The map is well-defined: if $c$ and $c'$ represent the same class (i.e., $c - c' = \delta d$), then $\rho c - \rho c' = \rho \delta d = \delta \rho d$ is a coboundary, so $[\rho c] = [\rho c']$.

4. **$K^{\mathcal{U},\mathcal{V}}$ is a group homomorphism.** $\rho$ is $\mathbb{Z}$-linear, hence the induced map on cohomology respects addition.
