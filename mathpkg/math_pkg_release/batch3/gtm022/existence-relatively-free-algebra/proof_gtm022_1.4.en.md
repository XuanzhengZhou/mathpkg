---
role: proof
locale: en
of_concept: existence-relatively-free-algebra
source_book: gtm022
source_chapter: "I"
source_section: "4"
---

Let $(F, \rho)$ be the free $T$-algebra on $X$. Define a congruence relation on $F$ by $u \sim v$ if $\varphi(u) = \varphi(v)$ for every homomorphism $\varphi: F \to A$ with $A \in V$. Then $\sim$ is an equivalence relation, and if $t \in T_k$ and $u_i \sim v_i$, then
$$\varphi(t(u_1, \ldots, u_k)) = t(\varphi(u_1), \ldots, \varphi(u_k)) = t(\varphi(v_1), \ldots, \varphi(v_k)) = \varphi(t(v_1, \ldots, v_k)),$$
so $\sim$ is a congruence. Define $R = F/{\sim}$ with $t(\bar{u}_1, \ldots, \bar{u}_k) = \overline{t(u_1, \ldots, u_k)}$ and $\sigma(x) = \overline{\rho(x)}$. Given $\tau: X \to A$ with $A \in V$, the universal property of $F$ gives a unique homomorphism $\psi: F \to A$ with $\psi\rho = \tau$, which factors through $R$ to give the required homomorphism.
