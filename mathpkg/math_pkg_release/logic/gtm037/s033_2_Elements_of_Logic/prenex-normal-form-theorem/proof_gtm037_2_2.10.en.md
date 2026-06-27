---
role: proof
locale: en
of_concept: prenex-normal-form-theorem
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

By induction on $\varphi$. The only difficult step is the passage from $\varphi_1$ and $\varphi_2$ to $\varphi_1 \lor \varphi_2$ (or to $\varphi_1 \land \varphi_2$). Since these cases are symmetric, we deal only with the first. Thus assume, with obvious notation,

$$\vdash \varphi_1 \leftrightarrow Q_0\alpha_0 \cdots Q_{m-1}\alpha_{m-1}\psi_1$$
$$\vdash \varphi_2 \leftrightarrow Q_0'\beta_0 \cdots Q_{n-1}\beta_{n-1}\psi_2.$$

By change of bound variable we may assume that none of $\alpha_0, \ldots, \alpha_{m-1}$ occur in $Q_0'\beta_0 \cdots Q_{n-1}\beta_{n-1}\psi_2$, and that none of $\beta_0, \ldots, \beta_{n-1}$ occur in $Q_0\alpha_0 \cdots Q_{m-1}\alpha_{m-1}\psi_1$. Thus by 10.76 we may pull the quantifiers of the first prenex form past $\psi_2$, and the quantifiers of the second past the first, yielding a prenex normal form for $\varphi_1 \lor \varphi_2$.

[Proof truncated in source — the remaining induction steps for atomic formulas, negation, and the full application of 10.76 are not present in the extracted section text.]
