---
role: proof
locale: en
of_concept: theorem-30-6-second-order-prenex-normal-form
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

The usual first-order transformations yield a prenex normal form for $\varphi$. To obtain the specific form where all second-order quantifiers precede all first-order quantifiers, and within the first-order block all universal quantifiers precede all existential quantifiers, we need equivalences that allow interchanging quantifier types.

\textbf{Equivalence (1)} (obvious):
$$\models \exists v_i \exists R_k^j \psi \leftrightarrow \exists R_k^j \exists v_i \psi.$$

\textbf{Equivalence (2)} (introducing an extra argument):
$$\models \forall v_i \exists R_k^j \psi \leftrightarrow \exists R_k^{j+1} \forall v_i \psi',$$
where $R_k^{j+1}$ is a new relation variable and $\psi'$ is obtained from $\psi$ by replacing each atomic subformula $R_k^j \sigma_0 \cdots \sigma_{j-1}$ by $R_k^{j+1} \sigma_0 \cdots \sigma_{j-1} v_i$. This works because the new relation $R_k^{j+1}$ can encode the dependence of the existentially chosen $j$-ary relation on $v_i$.

\textbf{Equivalence (3)} and \textbf{(4)} are dual cases for $\forall R_k^j$ and $\exists v_i$ interchanges.

\textbf{Equivalence (5)} (shifting quantifiers in prenex form): If $\psi = Q_0 \alpha_0 \cdots Q_{m-1} \alpha_{m-1} \chi$ with $\chi$ quantifier-free, then shifting individual quantifiers past relation quantifiers preserves equivalence under certain conditions.

\textbf{Equivalence (6)} (shifting $\exists v_i \forall v_j$ to the right):
$$\models \exists v_i \forall v_j Q_0 \alpha_0 \cdots Q_{m-1} \alpha_{m-1} \chi$$
$$\leftrightarrow \exists R_k^1 \forall v_i \forall v_j \exists v_l Q_0 \alpha_0 \cdots Q_{m-1} \alpha_{m-1} (R_k^1 v_l \wedge (R_k^1 v_l \rightarrow \chi)),$$
where $R_k^1$ and $v_l$ are new.

Using (1), (3), and (6), we shift all existential individual quantifiers $\exists v_i$ to the far right of the quantifier prefix. Then using (2) and (4), we shift all second-order quantifiers to the far left. The resulting formula has the form
$$\psi = Q_0 \alpha_0 \cdots Q_{m-1} \alpha_{m-1} \forall \beta_0 \cdots \forall \beta_{n-1} \exists \gamma_0 \cdots \exists \gamma_{p-1} \chi,$$
where all $\alpha$'s are relation variables, $\beta$'s and $\gamma$'s are individual variables, and $\chi$ is quantifier-free, as required.
