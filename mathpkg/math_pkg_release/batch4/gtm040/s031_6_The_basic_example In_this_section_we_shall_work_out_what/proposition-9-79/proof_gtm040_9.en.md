---
role: proof
locale: en
of_concept: proposition-9-79
source_book: gtm040
source_chapter: "9"
source_section: ""
---

The proof relies on Propositions 9-76 and 9-77, which give the relationships between $M$, $Z$, and the diagonal matrix $D$ with entries $D_{jj} = 1/\alpha_j$.

From Proposition 9-77, we have $\alpha M = (\alpha E Z_{\text{dg}} - \alpha Z)D$, where $Z_{\text{dg}}$ is the diagonal matrix with entries $Z_{jj}$, and $E$ is the matrix of all ones. Expanding:
$$\alpha M = (E Z_{\text{dg}} - \alpha Z)D,$$
where we use the fact that $\alpha E = 1E$ (since $\alpha$ is a probability vector, $\alpha E = E$? Actually, let us be precise).

From Proposition 9-76,
$$Z_{\text{dg}} D = E Z_{\text{dg}} D - 1^T,$$
and rearranging gives (1):
$$(\alpha M)_j = M_{\alpha j} = \frac{Z_{jj}}{\alpha_j} - 1.$$

For (2), we use the symmetry of the reverse chain. The mean passage time $\bar{M}_{\alpha j}$ for the reverse chain satisfies:
$$\bar{M}_{\alpha j} = M_{\alpha j} + \alpha_j \bar{M}_{jj} = M_{\alpha j} + 1.$$
Substituting from (1):
$$\bar{M}_{\alpha j} = \frac{Z_{jj}}{\alpha_j} - 1 + 1 = \frac{Z_{jj}}{\alpha_j},$$
so $Z_{jj} = \bar{M}_{\alpha j} \alpha_j$.

For (3), using (1) and Proposition 9-77 (which gives $M_{ij} = (Z_{jj} - Z_{ij})/\alpha_j$):
$$M_{\alpha j} - M_{ij} = \left(\frac{Z_{jj}}{\alpha_j} - 1\right) - \frac{Z_{jj} - Z_{ij}}{\alpha_j} = \frac{Z_{ij}}{\alpha_j} - 1.$$
By duality (Proposition 9-77 for the reverse chain), $Z_{ij} = \hat{Z}_{ji} \alpha_i / \alpha_j$, and thus
$$\frac{Z_{ij}}{\alpha_j} - 1 = \frac{\hat{Z}_{ji}}{\alpha_i} - 1 = \hat{M}_{\alpha i} - \hat{M}_{ji},$$
where the last equality follows from applying (1) to the reverse chain $\hat{P}$.
