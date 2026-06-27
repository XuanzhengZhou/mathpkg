---
role: proof
locale: en
of_concept: retraction-plus-deformation-implies-deformation-retract
source_book: gtm057
source_chapter: "V"
source_section: "1"
---
Let $\{h_s\}$ be a deformation of $X$ into $Y$. Define a new deformation $\{k_s\}$ by
$$k_s(p) = \begin{cases} h_{2s}(p), & 0 \leq s \leq \frac{1}{2}, \\ \rho(h_{2-2s}(p)), & \frac{1}{2} \leq s \leq 1. \end{cases}$$
Then $k_0(p) = h_0(p) = p$, and $k_1(p) = \rho(h_0(p)) = \rho(p)$. Continuity holds because $k_{1/2} = h_1 = \rho \circ h_1$. Thus $\rho$ is realized by $\{k_s\}$.
