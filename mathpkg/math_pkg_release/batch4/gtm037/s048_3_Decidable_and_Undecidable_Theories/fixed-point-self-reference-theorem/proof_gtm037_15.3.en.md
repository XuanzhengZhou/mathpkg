---
role: proof
locale: en
of_concept: fixed-point-self-reference-theorem
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

For any $x \in \omega$, let

$$f(x) = g^+ \psi(x) \quad \text{if } x = g^+ \psi \text{ for some formula } \psi,$$
$$f(x) = 0 \quad \text{otherwise.}$$

Thus $f$ is recursive. By hypothesis, let $\chi$ be a formula of $\mathcal{L}_{\text{nos}}$ with $\operatorname{Fv}(\chi) \subseteq \{v_0, v_1\}$ such that $\chi$ syntactically defines $f$. Let $\theta$ be the formula $\exists v_1[\varphi(v_1) \land \chi(v_0, v_1)]$, and let $\psi$ be the sentence $\theta(\Delta g^+ \theta)$.
