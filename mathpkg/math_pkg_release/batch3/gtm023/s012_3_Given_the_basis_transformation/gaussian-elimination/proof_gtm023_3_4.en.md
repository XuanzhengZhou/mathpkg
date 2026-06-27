---
role: proof
locale: en
of_concept: gaussian-elimination
source_book: gtm023
source_chapter: "3"
source_section: "4. Elementary transformations"
---

Consider the system of $m$ equations in $n$ unknowns:

$$\sum_{\nu=1}^{n} \alpha_\nu^\mu \xi^\nu = \eta^\mu \quad (\mu = 1, \dots, m).$$

**Step 1 (Zero-row check).** If all coefficients in the $i$-th row are zero, examine $\eta^i$. If $\eta^i \neq 0$, the $i$-th equation is a contradiction ($0 = \eta^i \neq 0$) and the system has no solution. If $\eta^i = 0$, the $i$-th equation is the identity $0 = 0$ and may be omitted.

Hence we may assume every remaining equation contains at least one nonzero coefficient.

**Step 2 (Pivot selection).** Rearrange the unknowns (which corresponds to column permutations in the matrix) so that $\alpha_1^1 \neq 0$.

**Step 3 (Elimination of $\xi^1$).** For each $\mu = 2, \dots, m$, multiply the first equation by $-(\alpha_1^1)^{-1} \alpha_1^\mu$ and add to the $\mu$-th equation. This yields the equivalent system:

$$\alpha_1^1 \xi^1 + \alpha_2^1 \xi^2 + \cdots + \alpha_n^1 \xi^n = \zeta^1$$
$$\beta_2^2 \xi^2 + \cdots + \beta_n^2 \xi^n = \zeta^2$$
$$\vdots$$
$$\beta_2^m \xi^2 + \cdots + \beta_n^m \xi^n = \zeta^m$$

where the unknown $\xi^1$ has been eliminated from equations $2$ through $m$.

**Step 4 (Recursion).** Apply the same reduction (Steps 1-3) to the subsystem consisting of the last $(m-1)$ equations. If a contradiction is encountered, the system has no solution. Otherwise, the recursion continues until all equations are processed.

After $r$ recursive steps (where $r$ is the rank of the coefficient matrix), the system takes the triangular form

$$\kappa_1^1 \xi^1 + \kappa_2^1 \xi^2 + \cdots + \kappa_r^1 \xi^r + \cdots + \kappa_n^1 \xi^n = \omega^1$$
$$\kappa_2^2 \xi^2 + \cdots + \kappa_r^2 \xi^r + \cdots + \kappa_n^2 \xi^n = \omega^2$$
$$\ddots \quad \vdots$$
$$\kappa_r^r \xi^r + \cdots + \kappa_n^r \xi^n = \omega^r$$

with $\kappa_\nu^\nu \neq 0$ for $\nu = 1, \dots, r$.

**Step 5 (Back-substitution).** Solve beginning with the last equation:

$$\xi^r = -(\kappa_r^r)^{-1}\left(\omega^r - \sum_{\nu=r+1}^{n} \kappa_\nu^r \xi^\nu\right).$$

Insert this expression into the first $(r-1)$ equations, reducing the system to a triangular one of $r-1$ equations. Continuing by induction yields the general solution

$$\xi^\nu = \sum_{\mu=r+1}^{n} \lambda_\mu^\nu \xi^\mu + \varrho^\nu \quad (\nu = 1, \dots, r)$$

where $\xi^\nu\ (\nu = r+1, \dots, n)$ are arbitrary parameters.
