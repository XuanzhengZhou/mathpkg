---
role: proof
locale: en
of_concept: many-sorted-translation
source_book: gtm037
source_chapter: "29"
source_section: "5. Unusual Logics"
---

The proof proceeds by induction on the structure of terms $\sigma$ and formulas $\varphi$ in the many-sorted language $\mathcal{L}$.

For terms: if $\sigma$ is a variable $v_i^s$, then $\sigma^{\mathfrak{A}}[x] = x_i \in A_s = \sigma^{\mathfrak{A}^*}[x]$ since the assignment $x$ is drawn from the disjoint union of the $A_s$. If $\sigma$ is $\mathbf{O}\rho_0 \cdots \rho_{m-1}$ with $\mathbf{O}$ of rank $(s_0, \ldots, s_m)$, then by induction $\rho_i^{\mathfrak{A}}[x] = \rho_i^{\mathfrak{A}^*}[x]$, and the interpretation of $\mathbf{O}$ in $\mathfrak{A}^*$ is defined to agree with $f_{\mathbf{O}}$ on the appropriate product of the $A_{s_i}$, so $\sigma^{\mathfrak{A}}[x] = \sigma^{\mathfrak{A}^*}[x]$.

For formulas: the atomic case follows from the term equality established above. The cases for $\neg$, $\lor$, $\land$ are immediate by induction. For $\forall v_i^s \varphi$, the translation $(\forall v_i^s \varphi)^*$ is $\forall v_i (\mathbf{P}_s(v_i) \to \varphi^*)$. Now $\mathfrak{A} \models \forall v_i^s \varphi[x]$ iff for all $a \in A_s$, $\mathfrak{A} \models \varphi[x_a^i]$. By induction, this holds iff for all $a \in A_s$, $\mathfrak{A}^* \models \varphi^*[x_a^i]$. Since $\mathbf{P}_s^{\mathfrak{A}^*} = A_s$ by construction, this is equivalent to $\mathfrak{A}^* \models \forall v_i (\mathbf{P}_s(v_i) \to \varphi^*)[x]$, as required.

The verification that $\mathfrak{A}^*$ satisfies the sort axioms $\Gamma$ follows directly from the construction: $A_s$ is nonempty for each $s$, so $\exists v_0 \mathbf{P}_s(v_0)$ holds, and the operation and relation symbols of $\mathcal{L}^*$ respect the sort closures encoded in $\Gamma$.
