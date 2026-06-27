---
role: exercise
locale: en
chapter: "9"
section: "48"
exercise_number: 21
---

Let $\Lambda = (V, \mathcal{M})$ be a matroid with rank function $r$. Let $\Lambda = \Lambda_1 \oplus \Lambda_2$, where $\Lambda_i = (V_i, \mathcal{M}_i)$ and $r_i$ is the rank function for $\Lambda_i$ ($i = 1, 2$). Show that

(a) $\mathcal{I}(\Lambda) = \{J_1 \cup J_2: J_i \in \mathcal{I}(\Lambda_i), i = 1, 2\}$;
(b) $\mathcal{B}(\Lambda) = \{B_1 \cup B_2: B_i \in \mathcal{B}(\Lambda_i), i = 1, 2\}$;
(c) $\mathcal{S}(\Lambda) = \{S_1 \cup S_2: S_i \in \mathcal{S}(\Lambda_i), i = 1, 2\}$;
(d) $r(U) = r_1(U \cap V_1) + r_2(U \cap V_2)$, for all $U \in \mathcal{P}(V)$.

It was pointed out above in §B that if $\mathcal{A}$ is a subspace of $\mathcal{P}(V)$, then $(\text{Fnd}(\mathcal{A}), \mathcal{M}(\mathcal{A}))$ is an example of a matroid. A necessary and sufficient condition for $(\text{Fnd}(\mathcal{A}), \

We have shown that $\pi_U[\mathcal{M}] \subseteq \mathcal{M}$ and in fact that $\Lambda_U = \Lambda_{[U]}$. Hence $\Lambda_U$ is a direct summand of $\Lambda$. Since $U \neq \varnothing$ and $\Lambda$ is connected, $\Lambda_U = \Lambda$. Hence $U = V$ as required.
