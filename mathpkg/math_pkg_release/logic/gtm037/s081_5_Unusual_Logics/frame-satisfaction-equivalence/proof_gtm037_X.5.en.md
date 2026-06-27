---
role: proof
locale: en
of_concept: frame-satisfaction-equivalence
source_book: gtm037
source_chapter: "X"
source_section: "5"
---

**Proof of Lemma 30.7.** The proof proceeds by induction on the formula $\varphi$.

*Base case: atomic formulas.* Consider an atomic formula $R\rho_0 \cdots \rho_m$ where $R$ is a relation variable or constant of type $\sigma = (\tau_0, \ldots, \tau_m) \neq 0$ and $\rho_0, \ldots, \rho_m$ are terms of types $\tau_0, \ldots, \tau_m$ respectively. By the definition of satisfaction in frame semantics:

$$(\mathfrak{A}, G) \models R\rho_0 \cdots \rho_m[x] \quad \text{iff} \quad (\rho_0^{\mathfrak{A}}[x], \ldots, \rho_m^{\mathfrak{A}}[x]) \in S,$$

where $S = xR$ if $R$ is a variable, and $S = R^{\mathfrak{A}}$ if $R$ is a constant. By the construction of $\mathfrak{A}_G^*$, the relation $S^{\mathfrak{A}_G^*}$ encodes exactly this membership: for the $m$-tuple $(\rho_0^{\mathfrak{A}}[x], \ldots, \rho_m^{\mathfrak{A}}[x])$ and $V = S$, we have $(\rho_0^{\mathfrak{A}}[x], \ldots, \rho_m^{\mathfrak{A}}[x]) \in V$ iff $(U_0, \ldots, U_m) \in V$ with each $U_i$ the value of $\rho_i^{\mathfrak{A}}[x]$. By definition of $\varphi^*$, the translation of the atomic formula into $\mathcal{L}''$ is satisfied in $\mathfrak{A}_G^*$ precisely under the same condition. Hence the equivalence holds for atomic formulas.

For equality $\sigma = \tau$ where $\sigma, \tau$ are terms of the same type, the equivalence is immediate since term evaluation is unaffected by the frame: the values of terms depend only on $\mathfrak{A}$ and the assignment $x$, and the universe $A_G^*$ contains all elements of the relevant type domains.

*Inductive step: propositional connectives.* For $\neg\varphi$, we have:
$$(\mathfrak{A}, G) \models \neg\varphi[x] \;\text{iff}\; \text{not}\big[(\mathfrak{A}, G) \models \varphi[x]\big] \;\text{iff}\; \text{not}\big[\mathfrak{A}_G^* \models \varphi^*[x]\big] \;\text{iff}\; \mathfrak{A}_G^* \models \neg\varphi^*[x].$$

For $\varphi \lor \psi$ and $\varphi \land \psi$, the equivalence follows directly from the induction hypothesis and the definitions of satisfaction in both settings.

*Inductive step: universal quantifier over relation variables.* For $\forall P_i^\tau \varphi$, we have by the frame satisfaction definition:
$$(\mathfrak{A}, G) \models \forall P_i^\tau \varphi[x] \;\text{iff}\; \text{for every } R \in G^\tau,\; (\mathfrak{A}, G) \models \varphi[x(P_i^\tau/R)].$$

By the induction hypothesis, the right-hand side is equivalent to: for every $R \in G^\tau$, $\mathfrak{A}_G^* \models \varphi^*[x(P_i^\tau/R)]$. Since $G^\tau$ is precisely the interpretation of the type predicate $T_i$ in $\mathfrak{A}_G^*$ (i.e., $T_i^{\mathfrak{A}_G^*} = G^\tau$), the condition "for every $R \in G^\tau$" translates to the first-order universal quantifier restricted to $T_i$ in $\mathcal{L}''$. By the definition of the translation $()^*$, this matches the semantics of the translated formula in $\mathfrak{A}_G^*$.

*Inductive step: universal quantifier over operation variables.* The case $\forall v_i^\tau \varphi$ is analogous, using the fact that $F^\tau \subseteq \{f : G^{\tau_0} \times \cdots \times G^{\tau_{m-1}} \to G^{\tau_m}\}$ for $\tau = (\tau_0, \ldots, \tau_m)$, and the translation $()^*$ handles operation quantification by quantifying over the appropriate function domain in the extended structure.

By induction on the structure of $\varphi$, the equivalence holds for all formulas. $\square$
