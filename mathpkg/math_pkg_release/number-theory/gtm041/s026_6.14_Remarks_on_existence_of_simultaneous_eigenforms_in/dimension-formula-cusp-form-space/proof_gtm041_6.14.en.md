---
role: proof
locale: en
of_concept: dimension-formula-cusp-form-space
source_book: gtm041
source_chapter: "6"
source_section: "6.14"
---

Let $\kappa = \dim M_{2k,0}$ where $2k \geq 12$. The dimension formula for the space of entire modular forms $M_{2k}$ is well known:
$$\dim M_{2k} = \begin{cases} [2k/12] + 1 & \text{if } 2k \not\equiv 2 \pmod{12}, \\ [2k/12] & \text{if } 2k \equiv 2 \pmod{12}. \end{cases}$$

The subspace of cusp forms $M_{2k,0}$ has codimension 1 in $M_{2k}$ when $2k \geq 4$ (the non-cuspidal part being spanned by the Eisenstein series $G_{2k}$, except when $2k = 2$ where $G_2$ is not a modular form). Therefore
$$\kappa = \dim M_{2k,0} = \dim M_{2k} - 1,$$
which yields
$$\kappa = \begin{cases} \left[ \frac{2k}{12} \right] - 1 & \text{if } 2k \equiv 2 \pmod{12}, \\ \left[ \frac{2k}{12} \right] & \text{if } 2k \not\equiv 2 \pmod{12}. \end{cases}$$

The special case $2k \equiv 2 \pmod{12}$ occurs because $\dim M_{2k}$ has an extra drop in dimension for these weights, related to the fact that $G_{2k}$ vanishes at $i\infty$ for these values.
