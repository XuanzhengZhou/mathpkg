---
role: proof
locale: en
of_concept: feferman-vaught-theorem
source_book: gtm037
source_chapter: "23"
source_section: "3"
---

We proceed by induction on $\chi$. By a preliminary normalization (23.2), we do not have to produce a full partitioning sequence for all connectives; it suffices to handle atomic formulas, negation, and existential quantification.

**Atomic case**: Suppose $\chi$ is $\mathbf{R}_n v_{k0} \cdots v_{k(\rho n-1)}$. Let $\zeta_n = (\varphi, \psi_0, \ldots, \psi_m)$ be the sequence defining $\mathbf{R}_n$ in $\mathcal{L}_{\text{prod}}$. For each $j \leq m$ let $\chi_j = \psi_j(v_{k0}, \ldots, v_{k(\rho n-1)})$. Consider the $\mathcal{L}_{\text{fac}}$, $\mathcal{L}_{\text{ind}}$-sequence $(\varphi, \chi_0, \ldots, \chi_m)$. With $\mathfrak{C} = \prod_{i \in I} \mathfrak{A}_i$, we have:

$$\prod_{i \in I} \mathfrak{A}_i \models \chi[f] \quad \text{iff} \quad (f_{k0}, \ldots, f_{k(\rho n-1)}) \in \mathbf{R}_n^{\mathfrak{C}}$$
$$\text{iff there is a } g \text{ extending } f \text{ such that } \mathfrak{B} \models \varphi[K_{\psi_0}^1 g, \ldots, K_{\psi_m}^1 g]$$
$$\text{iff } \mathfrak{B} \models \varphi[K_{\chi_0}^2 f, \ldots, K_{\chi_m}^2 f].$$

**Negation**: If $\chi = \neg \chi_0$ and $\zeta = (\varphi, \psi_0, \ldots, \psi_m)$ is correlated with $\chi_0$, then $\chi$ is correlated with $(\neg \varphi, \psi_0, \ldots, \psi_m)$.

**Existential quantification**: Suppose $\chi = \exists v_j \chi_0$ and $\zeta = (\varphi, \psi_0, \ldots, \psi_m)$ is correlated with $\chi_0$ (in particular, $\zeta$ is a partitioning sequence). For each $k \leq m$ let $\mu_k$ be the formula $\exists v_j \psi_k$, and let $\theta$ be the formula:

$$\forall v_{m+1} \cdots \forall v_{2m+1}[v_{m+1} + \cdots + v_{2m+1} = 1 \wedge$$
$$\bigwedge_{k < l \leq m} (v_{m+k+1} \cdot v_{m+l+1} = 0) \wedge$$
$$\bigwedge_{k \leq m} (v_{m+k+1} \cdot v_k = v_{m+k+1}) \rightarrow \varphi(v_{m+1}, \ldots, v_{2m+1})].$$

Then $(\theta, \mu_0, \ldots, \mu_m)$ is an $\mathcal{L}_{\text{fac}}$, $\mathcal{L}_{\text{ind}}$-sequence that correlates with $\chi$.

To verify: suppose $\prod_{i \in I} \mathfrak{A}_i \models \forall v_j \chi[f]$. Given $J_0, \ldots, J_m \in B$ forming a partition of $I$ with $J_k \subseteq K_{\mu_k}^2 f$ for each $k \leq m$, we define $g \in \prod_{i \in I} A_i$ by choosing, for each $i \in I$ in the unique $J_k$, an element $g_i \in A_i$ witnessing $\exists v_j \psi_k$ with respect to $\text{pr}_i \circ f$. Then $g$ witnesses $\chi_0$, and since $\zeta$ is a partitioning sequence, we have $K_{\psi_k}^2 f \subseteq K_{\psi_k}^2 g$ for each $k$, and $\mathfrak{B} \models \varphi[K_{\psi_0}^2 g, \ldots, K_{\psi_m}^2 g]$. By the properties of Boolean algebras, this yields $\mathfrak{B} \models \theta[K_{\mu_0}^2 f, \ldots, K_{\mu_m}^2 f]$.

The converse direction is similar. This completes the induction.
