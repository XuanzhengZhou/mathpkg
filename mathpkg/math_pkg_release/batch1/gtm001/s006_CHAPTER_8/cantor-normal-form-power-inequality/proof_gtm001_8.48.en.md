---
role: proof
locale: en
of_concept: cantor-normal-form-power-inequality
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** Note that $\alpha^{\beta_n} \cdot m_n + \cdots + \alpha^{\beta_0} \cdot m_0 \le \alpha^{\beta_n} \cdot (m_n + 1)$, since all lower-degree terms are absorbed by $\alpha^{\beta_n}$ when $\alpha$ is a limit ordinal. Therefore, by monotonicity of exponentiation,

$$(\alpha^{\beta_n} \cdot m_n + \cdots + \alpha^{\beta_0} \cdot m_0)^\gamma \le [\alpha^{\beta_n} \cdot (m_n + 1)]^\gamma.$$

By Proposition 8.47, $[\alpha^{\beta_n} \cdot (m_n + 1)]^\gamma \le \alpha^{\beta_n \cdot \gamma} \cdot (m_n + 1)$ (for $\gamma \in K_{\mathrm{I}}$ the equality holds; for $\gamma \in K_{\mathrm{II}}$ the inequality bound applies). In either case, the stated inequality follows.
