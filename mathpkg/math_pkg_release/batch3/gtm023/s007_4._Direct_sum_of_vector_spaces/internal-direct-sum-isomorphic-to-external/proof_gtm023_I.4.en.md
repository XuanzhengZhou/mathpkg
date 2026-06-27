---
role: proof
locale: en
of_concept: internal-direct-sum-isomorphic-to-external
source_book: gtm023
source_chapter: "I"
source_section: "4. Direct sum of vector spaces"
---

**Proof.** Let $\tilde{E} = \bigoplus_{\alpha} E_\alpha$ be the external direct sum. Define a linear mapping $\sigma: E \to \tilde{E}$ by
$$\sigma x = \sum_{\alpha} i_\alpha x_\alpha, \quad \text{where} \quad x = \sum_{\alpha} x_\alpha, \; x_\alpha \in E_\alpha,$$
and $i_\alpha$ are the canonical injections of the external direct sum. The decomposition $x = \sum_\alpha x_\alpha$ is unique because $E$ is the internal direct sum of the $E_\alpha$.

Conversely, define a linear mapping $\tau: \tilde{E} \to E$ by
$$\tau \tilde{x} = \sum_{\alpha} \pi_\alpha \tilde{x},$$
where $\pi_\alpha$ are the canonical projections of the external direct sum. Since only finitely many components of $\tilde{x}$ are non-zero, the sum is finite.

Using the relations satisfied by the canonical injections and projections (notably $\pi_\alpha \circ i_\alpha = \iota_{E_\alpha}$ and $\pi_\alpha \circ i_\beta = 0$ for $\alpha \neq \beta$), one verifies
$$\tau \circ \sigma = \iota_E \quad \text{and} \quad \sigma \circ \tau = \iota_{\tilde{E}}.$$
Hence $\sigma$ is an isomorphism of $E$ onto $\tilde{E}$ and $\tau$ is the inverse isomorphism. $\square$
