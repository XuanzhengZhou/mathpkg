---
role: proof
locale: en
of_concept: linear-independence-in-minimal-product-representation
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "5"
---

Suppose $A = \sum_{i=1}^r u_i' \times v_i$ is a minimal representation. We first show that $\{v_i\}$ is linearly independent. If not, some $v_k$ can be expressed as $v_k = \sum_{i \neq k} \alpha_i v_i$. Then using the bilinearity properties

$$u' \times (v_1 + v_2) = u' \times v_1 + u' \times v_2, \quad u' \times \alpha v = u'\alpha \times v,$$

we could rewrite the sum with fewer terms, contradicting the minimality of $r$.

Similarly, suppose $\{u_i'\}$ is linearly dependent. Then some $u_k'$ can be expressed as $u_k' = \sum_{j} e_j' \beta_{jk}$ where the number of $e_j'$ is less than $r$. Using

$$(u_1' + u_2') \times v = u_1' \times v + u_2' \times v,$$

we obtain $\sum u_i' \times v_i = \sum e_j' \times (\sum_i \beta_{ji} v_i)$, yielding an expression with fewer than $r$ terms, again contradicting minimality.

Hence both $\{u_i'\}$ and $\{v_i\}$ are linearly independent sets. Moreover, $r$ equals both $\dim \operatorname{span}\{u_i'\}$ and $\dim \operatorname{span}\{v_i\}$, and these dimensions equal the rank of $A$.
