---
role: proof
locale: en
of_concept: conservation-of-total-mechanical-energy
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

**Proof.** By the work-energy theorem,
$$T(t_1) - T(t_0) = \int_{\mathbf{r}(t_0)}^{\mathbf{r}(t_1)} (\mathbf{F}, d\mathbf{r}).$$

For a conservative system with potential energy $U$, we have $\mathbf{F} = -\partial U / \partial \mathbf{r}$, so
$$\int_{\mathbf{r}(t_0)}^{\mathbf{r}(t_1)} (\mathbf{F}, d\mathbf{r}) = -\int_{\mathbf{r}(t_0)}^{\mathbf{r}(t_1)} \frac{\partial U}{\partial \mathbf{r}} \cdot d\mathbf{r} = U(\mathbf{r}(t_0)) - U(\mathbf{r}(t_1)).$$

Therefore $T(t_1) - T(t_0) = U(t_0) - U(t_1)$, which implies $T(t_1) + U(t_1) = T(t_0) + U(t_0)$, i.e., $E(t_1) = E(t_0)$.
