---
role: proof
locale: en
of_concept: multiplicative-property-characteristic-functions
source_book: gtm095
source_chapter: "2"
source_section: "12"
---

# Proof of Multiplicative Property of Characteristic Functions

Let $\xi_1, \xi_2, \ldots, \xi_n$ be independent random variables and $S_n = \xi_1 + \cdots + \xi_n$. Then

$$\begin{aligned}
\varphi_{S_n}(t) &= \mathsf{E}\, e^{it(\xi_1 + \cdots + \xi_n)} \\
&= \mathsf{E}\, \left( e^{it\xi_1} \cdots e^{it\xi_n} \right) \\
&= \mathsf{E}\, e^{it\xi_1} \cdots \mathsf{E}\, e^{it\xi_n} \\
&= \prod_{j=1}^{n} \varphi_{\xi_j}(t),
\end{aligned}$$

where the crucial step $\mathsf{E}(e^{it\xi_1} \cdots e^{it\xi_n}) = \mathsf{E}\, e^{it\xi_1} \cdots \mathsf{E}\, e^{it\xi_n}$ follows from the property that the expectation of a product of independent bounded random variables (either real or complex; see Theorem 6 of Sect. 6, and Problem 1) is equal to the product of their expectations. Each factor $e^{it\xi_j}$ is bounded (by 1 in absolute value) and the random variables $\xi_1, \ldots, \xi_n$ are independent, hence the complex-valued random variables $e^{it\xi_1}, \ldots, e^{it\xi_n}$ are also independent.

Note: This multiplicative property is the key to the proofs of limit theorems for sums of independent random variables by the method of characteristic functions (see Sect. 3, Chap. 3). In contrast, the distribution function $F_{S_n}$ is expressed in terms of the distribution functions of the individual terms by convolution: $F_{S_n} = F_{\xi_1} \ast \cdots \ast F_{\xi_n}$ (see Subsection 4 of Sect. 8), which is considerably more complicated.
