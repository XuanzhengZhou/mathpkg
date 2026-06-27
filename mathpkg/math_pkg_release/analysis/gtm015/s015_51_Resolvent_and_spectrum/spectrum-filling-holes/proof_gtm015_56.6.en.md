---
role: proof
locale: en
of_concept: spectrum-filling-holes
source_book: gtm015
source_chapter: "56"
source_section: "56.6"
---

# Proof of Spectrum changes by filling holes

**Proof.** Since $\sigma_B(x) \supset \sigma_A(x)$, write $\sigma_B(x) = \sigma_A(x) \cup W$ where $W = \sigma_B(x) \setminus \sigma_A(x)$. 

Each $\lambda \in W$ lies in $\sigma_B(x)$ but not in $\sigma_A(x)$. Since $\lambda \notin \partial \sigma_B(x)$ (otherwise $\lambda \in \partial \sigma_A(x)$ by 56.5, contradicting $\lambda \notin \sigma_A(x)$), $\lambda$ is an interior point of $\sigma_B(x)$, hence belongs to a bounded component of $\rho_A(x)$, i.e., a hole of $\sigma_A(x)$.

Moreover, the unbounded component of $\rho_A(x)$ contains $\{\lambda : |\lambda| > r(x)\}$, which is contained in $\rho_B(x)$ as well, so the unbounded components coincide.
