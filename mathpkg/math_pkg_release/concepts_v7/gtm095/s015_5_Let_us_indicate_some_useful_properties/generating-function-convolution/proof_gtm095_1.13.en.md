---
role: proof
locale: en
of_concept: generating-function-convolution
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of the Convolution Property (Proposition)

Let $A(x) = \sum_{n \geq 0} a_n x^n$ and $B(x) = \sum_{n \geq 0} b_n x^n$ be two generating functions. Their product is computed by the Cauchy product of the two power series:

$$
A(x)B(x) = \left(\sum_{i=0}^{\infty} a_i x^i\right)\!\left(\sum_{j=0}^{\infty} b_j x^j\right)
= \sum_{n=0}^{\infty} \left(\sum_{i+j=n} a_i b_j\right) x^n
= \sum_{n=0}^{\infty} \left(\sum_{i=0}^{n} a_i b_{n-i}\right) x^n.
$$

The inner sum $c_n = \sum_{i=0}^{n} a_i b_{n-i}$ is the discrete convolution (or Cauchy product) of the sequences $(a_n)$ and $(b_n)$. The sequence $(c_n)_{n \geq 0}$ is therefore in bijective correspondence with the generating function $C(x) = A(x)B(x)$:

$$
\boxed{(a_n) \leftrightarrow A(x),\; (b_n) \leftrightarrow B(x) \;\Longrightarrow\; \left(\sum_{i=0}^{n} a_i b_{n-i}\right)_{n \geq 0} \leftrightarrow A(x)B(x)}.
$$

This property is the foundation of the generating function method: it translates the combinatorial operation of convolution (which counts all ways to split $n$ into two parts) into the purely algebraic operation of multiplication of generating functions. $\square$
