---
role: proof
locale: en
of_concept: upper-triangular-matrices-form-subring
source_book: gtm013
source_chapter: "1"
source_section: "1.14"
---

Let $A = \llbracket a_{\alpha\beta} \rrbracket$ and $B = \llbracket b_{\alpha\beta} \rrbracket$ be upper triangular matrices in $\mathbb{CFM}_{\Gamma}(R)$. For $\alpha > \beta$: $(A + B)_{\alpha\beta} = a_{\alpha\beta} + b_{\alpha\beta} = 0 + 0 = 0$, so $A + B$ is upper triangular. Also $-A$ is upper triangular and $0$ is upper triangular.

For multiplication: if $\alpha > \gamma$, then for each $\beta \in \Gamma$, either $\alpha > \beta$ (so $a_{\alpha\beta} = 0$) or $\beta \geq \alpha > \gamma$ implies $\beta > \gamma$ (so $b_{\beta\gamma} = 0$). Hence every term in $\sum_{\beta} a_{\alpha\beta} b_{\beta\gamma}$ is zero, giving $(\alpha, \gamma)$-entry zero. Thus $AB$ is upper triangular. Since $A$ and $B$ are column finite, the product $AB$ is defined and column finite. The same reasoning applies to $\mathbb{RFM}_{\Gamma}(R)$ and to lower triangular matrices.
