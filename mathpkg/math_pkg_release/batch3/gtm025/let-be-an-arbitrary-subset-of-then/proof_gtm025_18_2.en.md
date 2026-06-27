---
role: proof
locale: en
of_concept: "let-be-an-arbitrary-subset-of-then"
source_book: gtm025
source_chapter: "Differentiation"
source_section: "18.2"
---

With no harm done, we can [and do] suppose that $A$ is bounded. There are bounded open sets $U_n$, $n = 1, 2, \ldots$, such that

$$U_1 \supset U_2 \supset \cdots \supset U_n \supset \cdots \supset A$$

and $\lambda(U_n) - 2^{-n} < \lambda(A)$. Let $a = \inf U_1$, and consider the functions

$$\varphi_n(x) = \lambda(U_n \cap ]a, x[)$$

and

$$\varphi(x) = \lambda(A \cap ]a, x[).$$

For $x \in U_n$ and sufficiently small positive $h$, it is clear that

$$\frac{\varphi_n(x + h) - \varphi_n(x)}{h} = \frac{\varphi_n(x) - \varphi_n(x - h)}{h} = 1;$$

hence $\varphi_n'(x)$ exists for all $x \in U_n$ and

$$\varphi_n'(x) = 1.$$

We want to apply Fubini's theorem (17.18) to the sum

$$(\varphi_1

and so for $a \leq x \leq b$ we have

$$\sum_{n=1}^{\infty} (\varphi_n(x) - \varphi(x)) \leq \sum_{n=1}^{\infty} (\varphi_n(b) - \varphi(b)) \leq \sum_{n=1}^{\infty} 2^{-n} < \infty.$$

Let

$$s(x) = \sum_{n=1}^{\infty} (\varphi_n(x) - \varphi(x)).$$

By (17.18) and (17.12), the relations

$$s'(x) = \sum_{n=1}^{\infty} (\varphi_n'(x) - \varphi'(x)) < \infty$$

hold for almost all $x$ in $]a, b[$, and so also we have

$$\lim_{n \to \infty} \varphi_n'(x) = \varphi'(x)$$

a.e. in $]a, b[$. Thus $\varphi'(x) = 1$ on $\bigcap_{n=1}^{\infty} U_n$ except on a set of $\lambda$-measure zero, and this implies the first assertion of the theorem.$^1$

If $A$ is $\lambda$-measurable, then

$$1 = \frac{\lambda(A \cap x - h, x + k)}{h + k} + \frac{\lambda(A' \cap x - h, x + k)}{h + k}$$

for all $h, k$. As $h$ and $k$ go to 0, $\psi_{A'}(x)$ goes to 1 for almost all $x \in A'$ [apply the first part of the theorem to the set $A'$]. Hence $\psi_{A}(x)$ goes to zero a.e. on $A'$.
