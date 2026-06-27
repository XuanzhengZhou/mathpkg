---
role: proof
locale: en
of_concept: "let-be-any-extended-real-valued-function-defined-on"
source_book: gtm025
source_chapter: "Measurable Functions"
source_section: "11.7"
---

We have

$$(\varphi \circ f)^{-1}([a, \infty]) = f^{-1}(\varphi^{-1}([a, \infty]))$$
$$= f^{-1}\left((\varphi^{-1}([a, \infty]) \cap R) \cup A_+ \cup A_-\right)$$
$$= f^{-1}(\varphi^{-1}([a, \infty]) \cap R) \cup f^{-1}(A_+) \cup f^{-1}(A_-),$$

where $A_+ = \{\infty\} \cap \varphi^{-1}

$\{x \in X : f(x) = -\infty\}$, and $\{x \in X : f(x) = 0\}$, respectively. Then $h$ is $\mathcal{A}$-measurable.

Proof. In each case, we define a suitable function $\varphi$ such that the function in question is equal to $\varphi \circ f$ and apply (11.7). For (i), let

$$\varphi(t) = \begin{cases} t + \alpha & \text{if } t \in R, \\ \pm \infty & \text{if } t = \pm \infty. \end{cases}$$

To prove (ii), let

$$\varphi(t) = \begin{cases} -\infty & \text{if } t = -\infty, \\ \alpha t & \text{if } t \in R, \\ \infty & \text{if } t = \infty, \end{cases}$$

if $\alpha > 0$, and

$$\varphi(t) = \begin{cases} \infty & \text{if } t = -\infty, \\ \alpha t & \text{if } t \in R, \\ -\infty & \text{if } t = \infty, \end{cases}$$

if $\alpha < 0$; if $\alpha = 0$, the assertion is trivial.

For (iii), let $\varphi(\pm \infty) = \beta_{\pm}$ and $\varphi(t) = |t|^p$ for real $t$. Since $\varphi$ is continuous on $R$, it is clear that $\varphi^{-1}([a, \infty]) \cap R$ is a Borel set for all real $a$.

The proof of (iv) is similar, with $\varphi(t) = t^m$ for real $t$ and $\varphi(\pm \infty) = \beta_{\pm}$.

To prove (v), let $\varphi(t) = \frac{1}{t}$ for $t \neq 0, \infty, -\infty$, and let $\varphi(0) = \beta_0$, $\varphi(\pm \infty) = \beta_{\pm}$.
