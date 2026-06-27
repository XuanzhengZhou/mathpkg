---
role: proof
locale: en
of_concept: orthogonal-decomposition-stability-under-normal
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

($\Rightarrow$) Assume $\varphi$ is normal. Let $x_i \in E_i$ be arbitrary. For any $x_j \in E_j$ with $j \neq i$, the orthogonality of the decomposition gives $(x_i, x_j) = 0$. Since $E_j$ is stable under $\varphi$, we have $\varphi x_j \in E_j$. Then

$$(\tilde{\varphi} x_i, x_j) = (x_i, \varphi x_j) = 0,$$

because $x_i \perp E_j$ and $\varphi x_j \in E_j$. This shows $\tilde{\varphi} x_i \in E_j^\perp$ for all $j \neq i$, which implies $\tilde{\varphi} x_i \in E_i$ (since $E_i = \bigcap_{j \neq i} E_j^\perp$ in an orthogonal decomposition). Thus each $E_i$ is stable under $\tilde{\varphi}$.

For normality of $\varphi_i$, note that for $x \in E_i$, $\tilde{\varphi_i} = \tilde{\varphi}|_{E_i}$ (since $E_i$ is stable under $\tilde{\varphi}$). Then

$$|\varphi_i x|^2 = |\varphi x|^2 = |\tilde{\varphi} x|^2 = |\tilde{\varphi_i} x|^2,$$

which implies $\varphi_i$ is normal.

($\Leftarrow$) Conversely, assume each $E_i$ is stable under $\tilde{\varphi}$ and each $\varphi_i$ is normal. For any vector $x = \sum_i x_i$ with $x_i \in E_i$, orthogonality of the decomposition gives

$$|\varphi x|^2 = \sum_i |\varphi_i x_i|^2 = \sum_i |\tilde{\varphi_i} x_i|^2 = \sum_i |\tilde{\varphi} x_i|^2 = |\tilde{\varphi} x|^2.$$

Hence $|\varphi x| = |\tilde{\varphi} x|$ for all $x$, which is equivalent to $\varphi$ being normal.
