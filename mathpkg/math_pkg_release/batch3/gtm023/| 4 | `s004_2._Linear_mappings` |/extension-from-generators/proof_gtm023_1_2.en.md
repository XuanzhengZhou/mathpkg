---
role: proof
locale: en
of_concept: extension-from-generators
source_book: gtm023
source_chapter: "1"
source_section: "2"
---

*Uniqueness.* Suppose $\varphi$ is a linear extension of $\varphi_0$. Since $S$ generates $E$, any $x \in E$ can be written as $x = \sum_i \lambda^i x_i$ with $x_i \in S$. By linearity,
$$
\varphi x = \varphi\left(\sum_i \lambda^i x_i\right) = \sum_i \lambda^i \varphi x_i = \sum_i \lambda^i \varphi_0 x_i.
$$
Thus $\varphi$ is uniquely determined by $\varphi_0$ on all of $E$, proving at most one extension exists.

*Necessity of condition.* If an extension $\varphi$ exists, then whenever $\sum_i \lambda^i x_i = 0$ with $x_i \in S$, we have
$$
\sum_i \lambda^i \varphi_0 x_i = \sum_i \lambda^i \varphi x_i = \varphi\left(\sum_i \lambda^i x_i\right) = \varphi 0 = 0.
$$

*Sufficiency of condition.* Assume that $\sum_i \lambda^i \varphi_0 x_i = 0$ whenever $\sum_i \lambda^i x_i = 0$. Define $\varphi$ by
$$
\varphi\left(\sum_i \lambda^i x_i\right) = \sum_i \lambda^i \varphi_0 x_i, \quad x_i \in S.
$$
To verify $\varphi$ is well-defined, suppose
$$
\sum_i \lambda^i x_i = \sum_j \mu^j y_j, \quad x_i, y_j \in S.
$$
Then $\sum_i \lambda^i x_i - \sum_j \mu^j y_j = 0$, so by hypothesis
$$
\sum_i \lambda^i \varphi_0 x_i - \sum_j \mu^j \varphi_0 y_j = 0,
$$
hence $\sum_i \lambda^i \varphi_0 x_i = \sum_j \mu^j \varphi_0 y_j$. Thus $\varphi$ is well-defined. Linearity follows immediately from the definition, and by construction $\varphi$ extends $\varphi_0$.
