---
role: proof
locale: en
of_concept: tensor-restriction-maximum-modulus
source_book: gtm035
source_chapter: "11"
source_section: "11.6"
---
# Proof that $A^{(n)}$ is a Maximum Modulus Algebra

**Theorem 11.6.** $(A^{(n)}, X^{(n)}, \Omega, \pi)$ is a maximum modulus algebra.

*Proof.* Clearly, $A^{(n)}$ is an algebra of continuous functions on $X^{(n)}$. Let $\Delta$ be a closed disk in $\Omega$ with center $\lambda_0$. Fix $x^0 \in \pi^{-1}(\lambda_0) \subseteq X^{(n)}$. We must show that

$$|F(x^0)| \leq \max_{\pi^{-1}(\partial \Delta)} |F|$$

for every $F \in A^{(n)}$.

By definition, $A^{(n)}$ is the restriction of $\otimes^n A$ to $X^{(n)}$, and $X^{(n)} = \{(x_1, \ldots, x_n) \in X^n : p(x_1) = \cdots = p(x_n)\}$ with $\pi(x_1, \ldots, x_n) = p(x_1)$.

Given the closed disk $\Delta \subset \Omega$ centered at $\lambda_0$, we consider the closed polydisk $\Delta^n \subset \mathbb{C}^n$ and its distinguished boundary $T^n = (\partial \Delta)^n$. The diagonal $\gamma = \{(\lambda, \ldots, \lambda) : |\lambda - \lambda_0| = r\}$ is a subset of $T^n$.

Applying Theorem 11.4 to $F$ (viewed as an element of $\otimes^n A$ via any extension) and the point $x^0 \in \Pi^{-1}(0, \ldots, 0)$ after translating coordinates so that $\lambda_0$ corresponds to $0$, we obtain

$$|F(x^0)| \leq \max_{\Pi^{-1}(\gamma)} |F|.$$

But $\Pi^{-1}(\gamma) = \{(x_1, \ldots, x_n) \in X^n : p(x_1) = \cdots = p(x_n), \; |p(x_1) - \lambda_0| = r\} = \pi^{-1}(\partial \Delta)$. Hence

$$|F(x^0)| \leq \max_{\pi^{-1}(\partial \Delta)} |F|,$$

which is precisely the defining inequality of a maximum modulus algebra. Since $x^0 \in \pi^{-1}(\lambda_0)$ and the closed disk $\Delta$ were arbitrary, $(A^{(n)}, X^{(n)}, \Omega, \pi)$ is a maximum modulus algebra. $\square$
