---
role: proof
locale: en
of_concept: extension-of-bilinear-function
source_book: gtm023
source_chapter: "II"
source_section: "2.22"
---

Let $\varrho: E \rightarrow E_1$ and $\sigma: F \rightarrow F_1$ be surjective linear mappings that reduce to the identity on $E_1$ and $F_1$ respectively. Define $\Phi: E \times F \rightarrow \Gamma$ by
$$\Phi(x, y) = \Phi_1(\varrho x, \sigma y).$$
Since $\varrho$ and $\sigma$ are linear, $\Phi$ is linear in each argument:
$$\Phi(\lambda_1 x_1 + \lambda_2 x_2, y) = \Phi_1(\varrho(\lambda_1 x_1 + \lambda_2 x_2), \sigma y) = \Phi_1(\lambda_1 \varrho x_1 + \lambda_2 \varrho x_2, \sigma y)$$
$$= \lambda_1 \Phi_1(\varrho x_1, \sigma y) + \lambda_2 \Phi_1(\varrho x_2, \sigma y) = \lambda_1 \Phi(x_1, y) + \lambda_2 \Phi(x_2, y).$$
The analogous computation for the second argument shows $\Phi$ is bilinear. For $x_1 \in E_1$, $y_1 \in F_1$, since $\varrho$ and $\sigma$ reduce to the identity, $\varrho x_1 = x_1$ and $\sigma y_1 = y_1$, hence
$$\Phi(x_1, y_1) = \Phi_1(x_1, y_1).$$
Thus $\Phi$ restricts to $\Phi_1$ on $E_1 \times F_1$, providing the required extension.
