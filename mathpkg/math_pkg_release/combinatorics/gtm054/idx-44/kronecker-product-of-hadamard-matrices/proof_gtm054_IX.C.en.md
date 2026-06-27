---
role: proof
locale: en
of_concept: kronecker-product-of-hadamard-matrices
source_book: gtm054
source_chapter: "IX"
source_section: "C"
---

Let $H_i$ be an $m_i \times m_i$ Hadamard matrix ($i = 1, 2$). Then

$$\begin{align*}
(H_1 \times H_2)(H_1 \times H_2)^* &= (H_1 \times H_2)(H_1^* \times H_2^*) \tag{by C34}\\
&= H_1 H_1^* \times H_2 H_2^* \tag{by C35}\\
&= m_1 I_{m_1 \times m_1} \times m_2 I_{m_2 \times m_2} \tag{by C26}\\
&= m_1 m_2 I_{m_1 m_2 \times m_1 m_2}.
\end{align*}$$

Additionally, the entries of $H_1 \times H_2$ are $\pm 1$ by definition of the Kronecker product applied to $(\pm 1)$-matrices. Thus $H_1 \times H_2$ satisfies the defining condition of a Hadamard matrix, so it is an $m_1 m_2 \times m_1 m_2$ Hadamard matrix.
