---
role: proof
locale: en
of_concept: polynomial-evaluation-homomorphism
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

Uniqueness: Since $1$ and $t$ generate $\Gamma[t]$ as an algebra, any algebra homomorphism is determined by its values on these generators. The conditions $\Phi(1)=e$ and $\Phi(t)=a$ thus determine $\Phi$ uniquely.

Existence: Define $\Phi(\sum_k \alpha_k t^k) = \sum_k \alpha_k a^k$. This is well-defined since the representation is unique. For addition: $\Phi(f+g) = \sum (\alpha_k+\beta_k)a^k = \sum \alpha_k a^k + \sum \beta_k a^k = \Phi(f)+\Phi(g)$. For multiplication: using the convolution formula, $\Phi(fg) = \sum_k (\sum_{i+j=k}\alpha_i\beta_j)a^k = \sum_{i,j} \alpha_i\beta_j a^{i+j} = (\sum_i \alpha_i a^i)(\sum_j \beta_j a^j) = \Phi(f)\Phi(g)$. And $\Phi(1) = e$. Thus $\Phi$ is an algebra homomorphism.
