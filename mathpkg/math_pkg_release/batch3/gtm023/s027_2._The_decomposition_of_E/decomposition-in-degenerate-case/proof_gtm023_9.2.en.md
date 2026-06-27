---
role: proof
locale: en
of_concept: decomposition-in-degenerate-case
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Choose a subspace $E_1$ complementary to the nullspace $E_0$, so that $E = E_0 \oplus E_1$. We show $\Phi$ is non-degenerate in $E_1$.

Assume there exists $x_1 \in E_1$ such that $\Phi(x_1, y_1) = 0$ for all $y_1 \in E_1$. Take an arbitrary $y \in E$ and write it as $y = y_0 + y_1$ with $y_0 \in E_0$, $y_1 \in E_1$. Then

$$\Phi(x_1, y) = \Phi(x_1, y_0) + \Phi(x_1, y_1).$$

Since $y_0 \in E_0$, we have $\Phi(x_1, y_0) = 0$ (the nullspace condition is symmetric). And $\Phi(x_1, y_1) = 0$ by assumption. Hence $\Phi(x_1, y) = 0$ for all $y \in E$, which means $x_1 \in E_0$. But $x_1 \in E_1$, so $x_1 \in E_0 \cap E_1 = \{0\}$. Thus $x_1 = 0$, proving $\Phi$ is non-degenerate on $E_1$.

Applying the decomposition theorem to the non-degenerate bilinear function $\Phi|_{E_1}$ on $E_1$, we obtain $E_1 = E_1^+ \oplus E_1^-$. Hence

$$E = E_1^+ \oplus E_1^- \oplus E_0.$$

Choose an orthonormal basis of $E_1^+$ with respect to $\Phi$, an orthonormal basis of $E_1^-$ with respect to $-\Phi$, and an arbitrary basis of $E_0$. These bases together form a basis of $E$ in which the matrix of $\Phi$ is diagonal with entries $+1$, $-1$, $0$ as stated.
