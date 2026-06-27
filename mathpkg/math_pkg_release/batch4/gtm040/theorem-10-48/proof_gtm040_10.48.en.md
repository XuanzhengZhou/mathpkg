---
role: proof
locale: en
of_concept: theorem-10-48
source_book: gtm040
source_chapter: "10"
source_section: "48"
---

**Proof of Theorem 10-48:** Let $\alpha > 0$ be a superregular measure such that $\alpha f = 1$. Duality in the remainder of this section means $\alpha$-duality. Let $\hat{P} = \text{dual } P$ and $\hat{\pi} = \text{dual } f$. Since

$$0 < \text{dual } g = \text{dual }(Nf) = \hat{\pi}\hat{N}$$

and

$$1 = \alpha f = (\text{dual } f)(\text{dual } \alpha) = \hat{\pi}1,$$

the exit boundary of $\hat{P}$ relative to $\hat{\pi}$ is defined. Under the canonical identification of $*S$ and $\hat{S}^*$ (Lemma 10-49),

$$J(x, \cdot) = \text{dual } \hat{K}(\cdot, x)$$

by the continuity of the functions $J(\cdot, i)$ and $\hat{K}(i, \cdot)$. Under duality a $\hat{P}$-superregular function $h$ corresponds to a $P$-superregular row vector $\sigma = \text{dual } h$. Since $\hat{P} = \text{dual } P$ and $\hat{\pi} = \text{dual } f$, regularity and normalization are both preserved. Minimality is also preserved since duality preserves inequalities. Therefore $B^e = \hat{B}_e$.

Now let $h = \text{dual } \sigma$, and apply Theorem 10-41 (the Poisson-Martin representation for superregular functions). Then

$$h_i = \int_{S \cup \hat{B}_e} \hat{K}(i, x)\,d\nu(x)$$

with $\hat{\pi}h = \nu(S \cup \hat{B}_e)$. Therefore

$$\frac{\sigma_i}{\alpha_i} = \int_{S \cup \hat{B}_e} \frac{1}{\alpha_i} J(x, i)\,d\nu(x)$$

and $\sigma f = \nu(S \cup \hat{B}_e)$. Identifying $B^e$ and $\hat{B}_e$ and calling $\nu$ by the same name on $B^e$ as on $\hat{B}_e$, we obtain

$$\sigma_i = \int_{S \cup B^e} J(x, i)\,d\nu(x)$$

as required.

Conversely, if $\sigma$ is given by

$$\sigma_i = \int_{S \cup B^e} J(x, i)\,d\nu(x),$$

then

$$(\text{dual } \sigma)_i = \int_{S \cup \hat{B}_e} \hat{K}(i, x)\,d\nu(x).$$

Therefore $\text{dual } \sigma$ is $\hat{P}$-superregular by Theorem 10-41, and $\sigma$ must be superregular. The decomposition $\sigma = \gamma N + \rho$ with $\rho$ regular follows by separating the integral over $S$ (yielding $\gamma N$) from the integral over $B^e$ (yielding $\rho$). The Borel measurability of $S$ and $B^e$ in $*S$ follows from the continuity properties of the Martin kernel.
