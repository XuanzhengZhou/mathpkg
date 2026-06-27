---
role: proof
locale: en
of_concept: interaction-potential-energy
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

**Proof.** By definition, $U_{ij}$ is chosen such that its negative gradient gives the force. For a central force $\mathbf{F}_{ij} = f_{ij} \mathbf{e}_{ij}$, we set
$$U_{ij}(\mathbf{r}) = \int_{r_0}^{r} f_{ij}(\rho) \, d\rho.$$

Then differentiating with respect to $\mathbf{r}_i$:
$$-\frac{\partial U_{ij}(\mathbf{r}_i - \mathbf{r}_j)}{\partial \mathbf{r}_i} = -f_{ij} \frac{\partial |\mathbf{r}_i - \mathbf{r}_j|}{\partial \mathbf{r}_i} = f_{ij} \mathbf{e}_{ij} = \mathbf{F}_{ij}.$$

This verifies that $U_{ij}$ is indeed a valid potential energy for the interaction.
