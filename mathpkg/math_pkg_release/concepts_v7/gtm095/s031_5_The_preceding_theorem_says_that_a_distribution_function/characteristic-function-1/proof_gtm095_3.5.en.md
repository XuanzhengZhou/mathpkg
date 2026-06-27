---
role: proof
locale: en
of_concept: characteristic-function-1
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Theorem 4 (Characterization of independence via characteristic functions)

**Theorem 4.** A necessary and sufficient condition for the components of the random vector $\xi = (\xi_1, \ldots, \xi_n)^*$ to be independent is that its characteristic function is the product of the characteristic functions of the components:

$$E e^{i(t_1 \xi_1 + \cdots + t_n \xi_n)} = \prod_{k=1}^{n} E e^{it_k \xi_k}, \quad (t_1, \ldots, t_n)^* \in \mathbb{R}^n.$$

## Proof

**Necessity.** If $\xi_1, \ldots, \xi_n$ are independent, then by the property of expectation for independent random variables (Problem 1),

$$E e^{i(t_1 \xi_1 + \cdots + t_n \xi_n)} = E\left[ \prod_{k=1}^{n} e^{it_k \xi_k} \right] = \prod_{k=1}^{n} E e^{it_k \xi_k}.$$

**Sufficiency.** Let $F(x_1, \ldots, x_n)$ be the distribution function of the vector $\xi = (\xi_1, \ldots, \xi_n)^*$ and $F_k(x)$ the distribution functions of $\xi_k$, $1 \leq k \leq n$. Define

$$G(x_1, \ldots, x_n) = F_1(x_1) \cdots F_n(x_n).$$

Then, by Fubini's theorem, for all $(t_1, \ldots, t_n)^* \in \mathbb{R}^n$,

$$\int_{\mathbb{R}^n} e^{i(t_1 x_1 + \cdots + t_n x_n)} dG(x_1, \ldots, x_n) = \prod_{k=1}^{n} \int_{\mathbb{R}} e^{it_k x_k} dF_k(x_k)$$
$$= \prod_{k=1}^{n} E e^{it_k \xi_k} = E e^{i(t_1 \xi_1 + \cdots + t_n \xi_n)}$$
$$= \int_{\mathbb{R}^n} e^{i(t_1 x_1 + \cdots + t_n x_n)} dF(x_1, \ldots, x_n).$$

Thus the characteristic functions of $F$ and $G$ coincide. By the uniqueness theorem (Theorem 2), the distribution functions $F$ and $G$ are identical:

$$F(x_1, \ldots, x_n) = F_1(x_1) \cdots F_n(x_n),$$

which is precisely the definition of independence of the random variables $\xi_1, \ldots, \xi_n$. This completes the proof.
