---
role: proof
locale: en
of_concept: global-continuation-of-holomorphic-functions-on-stein
source_book: gtm038
source_chapter: "VI"
source_section: "5"
---

We assign to every point $x \in A$ a neighborhood $U_x \subset X$ and a holomorphic function $\tilde{f}_x$ such that $\tilde{f}_x|A \cap U_x = f|A \cap U_x$. To every point $x \in X - A$ let there be assigned a neighborhood $U_x \subset X$ with $U_x \cap A = \emptyset$ and the function $\tilde{f}_x := 0|U_x$. Let

$$\mathfrak{U} := (U_x)_{x \in X}, \quad \eta(x) := \tilde{f}_x \in \Gamma(U_x, \mathcal{O}).$$

Then $\eta \in C^0(\mathfrak{U}, \mathcal{O})$ and $\xi := \delta \eta \in Z^1(\mathfrak{U}, \mathcal{O})$. Moreover, for all $x_0, x_1 \in X$,

$$\xi(x_0, x_1)|A \cap U_{x_0x_1} = \tilde{f}_{x_0}|A \cap U_{x_0x_1} - \tilde{f}_{x_1}|A \cap U_{x_0x_1} = 0.$$

Therefore $\xi \in Z^1(\mathfrak{U}, \mathcal{I}(A))$, where we denote the ideal sheaf of $A$ by $\mathcal{I}(A)$. By Theorem B, $H^1(X, \mathcal{I}(A)) = 0$ and hence also $H^1(\mathfrak{U}, \mathcal{I}(A)) = 0$. Therefore there is a $\rho \in C^0(\mathfrak{U}, \mathcal{I}(A))$ with $\delta \rho = \xi$. Then $\eta - \rho$ is a 0-cocycle and thus a global holomorphic function $\hat{f}$ on $X$ that restricts to $f$ on $A$.
