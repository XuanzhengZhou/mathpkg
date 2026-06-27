---
role: proof
locale: en
of_concept: normal-form-for-elliptic-hyperbolic-umbilics
source_book: gtm014
source_chapter: "II"
source_section: "5"
---

The proof proceeds by successive coordinate changes to diagonalize the quadratic part and eliminate higher-order terms. Full details are given for the hyperbolic case; the elliptic case is similar with Lemma 5.22 replacing Lemma 5.13.

**Step 1: Reduction using the Malgrange Preparation Theorem.** By finite determinacy and the Malgrange Preparation Theorem, one reduces to studying the local algebra of the map germ. The transversality hypothesis $j^1 f \pitchfork S_2$ ensures that certain differentials are linearly independent, which legitimizes the coordinate changes that follow.

**Step 2: Diagonalization of the quadratic form.** Applying Lemma 5.13, after a smooth rotation of the $(x_1, x_2)$ coordinates (depending on the parameters $y_3, \ldots, y_n$), one may assume the quadratic terms in the first two coordinates are diagonal. Expressing $x_1^2$ and $x_2^2$ in terms of the pullbacks of the target coordinate functions $y_1, y_2$ and lower-order terms, one obtains:

\[
x_1^2 = f^*\alpha_1 + f^*\beta_1 x_1 + f^*\gamma_1 x_2,
\]
\[
x_2^2 = f^*\alpha_2 + f^*\beta_2 x_1 + f^*\gamma_2 x_2,
\]

where the $\alpha$'s, $\beta$'s and $\gamma$'s are functions of $y_3, \ldots, y_n$.

**Step 3: Eliminating linear terms.** Replacing $x_1$ by $x_1 + f^*\beta_1/2$ and $x_2$ by $x_2 + f^*\gamma_2/2$, one can assume $\beta_1$ and $\gamma_2$ are zero. Setting $\gamma = -\gamma_1$ and $\beta = -\beta_2$, this yields (5.18):

\[
f^*\alpha_1 = x_1^2 + f^*\gamma \, x_2,
\]
\[
f^*\alpha_2 = x_2^2 + f^*\beta \, x_1,
\]

with $f^* y_i = x_i$ for $i > 2$.

**Step 4: Applying the implicit function theorem.** Setting $x_3 = y_3 = \cdots = x_n = y_n = 0$ in (5.18) and comparing quadratic terms, one finds:

\[
\alpha_1(y_1, y_2, 0, \ldots, 0) = y_1 + \text{(higher order)},
\]
\[
\alpha_2(y_1, y_2, 0, \ldots, 0) = y_2 + \text{(higher order)}.
\]

The transversality hypothesis reduces to the linear independence of the differentials $dx_1, dx_2, d(f^*\beta), d(f^*\alpha)$ at $0$, which justifies making $\beta$ and $\gamma$ into new coordinate functions. This yields the canonical form (5.11).

For the **elliptic case**, Lemma 5.13 is replaced by its elliptic analogue (Lemma 5.22): one finds a smooth scaling $\lambda$ such that in the coordinates $\bar{x}_1 = \lambda x_1$, $\bar{x}_2 = (1/\lambda) x_2$, the quadratic form becomes $\bar{a}(\bar{x}_1^2 - \bar{x}_2^2)$. The remaining steps are analogous, leading to the canonical form (5.12).
