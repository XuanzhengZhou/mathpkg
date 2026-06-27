---
role: proof
locale: en
of_concept: "existence-of-relatively-free-algebra"
source_book: gtm022
source_chapter: "I"
source_section: "4"
---
Proof. Let $(F, \rho)$ be the free $T$-algebra on $X$. Define a relation $\sim$ on $F$ by: $u \sim v$ if $\varphi(u) = \varphi(v)$ for every homomorphism $\varphi$ of $F$ into any algebra in $\mathcal{V}$.

Clearly $\sim$ is an equivalence relation on $F$. If $t \in T_k$ and $u_i \sim v_i$ ($i = 1, \ldots, k$), then for every homomorphism $\varphi: F \rightarrow A \in \mathcal{V}$,
$$\varphi(t(u_1, \ldots, u_k)) = t_A(\varphi(u_1), \ldots, \varphi(u_k)) = t_A(\varphi(v_1), \ldots, \varphi(v_k)) = \varphi(t(v_1, \ldots, v_k)),$$
so $t(u_1, \ldots, u_k) \sim t(v_1, \ldots, v_k)$. Thus $\sim$ is a congruence relation.

Define $R$ to be the set of $\sim$-congruence classes of $F$. For $t \in T_k$, define $t_R(\bar{u}_1, \ldots, \bar{u}_k) = \overline{t_F(u_1, \ldots, u_k)}$, which is independent of representatives. Then $R$ is a $T$-algebra and the canonical map $\eta: F \rightarrow R$, $\eta(u) = \bar{u}$, is a homomorphism. Define $\sigma: X \rightarrow R$ by $\sigma(x) = \overline{\rho(x)}$.

We show $(R, \sigma)$ is relatively free on $X$. Let $A \in \mathcal{V}$ and $\tau: X \rightarrow A$ be given. Since $(F, \rho)$ is free, there exists a homomorphism $\psi: F \rightarrow A$ with $\psi \rho = \tau$. If $u \sim v$, then by definition $\psi(u) = \psi(v)$, so $\psi$ factors through $\eta$: there is a homomorphism $\varphi: R \rightarrow A$ with $\varphi \bar{u} = \psi(u)$. Then $\varphi \sigma(x) = \varphi(\overline{\rho(x)}) = \psi(\rho(x)) = \tau(x)$. Uniqueness of $\varphi$ is clear.

Uniqueness up to isomorphism follows by the standard universal property argument (cf. Theorem 2.2). $\square$
