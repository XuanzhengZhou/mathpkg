---
role: proof
locale: en
of_concept: decidability-transfer-to-products
source_book: gtm037
source_chapter: "23"
source_section: ""
---
The decision procedure for $\{\chi : \mathbf{PK} \models \chi\}$ is as follows. Given $\chi$, let $(\varphi, \psi_0, \ldots, \psi_m)$ be determined as in 23.3. Then let $T = \{k \leq m : \mathbf{K} \models \neg \psi_k\}$, which can be effectively determined, by assumption. Let $\theta$ be the following sentence of the theory of Boolean algebras:

$$\forall v_0 \cdots \forall v_m [v_0 + \cdots + v_m = 1 \wedge \bigwedge_{i < j < m} (v_i \cdot v_j = 0) \wedge \bigwedge_{k \in T} v_k = 0 \rightarrow \varphi]$$

We claim

(1) $\mathbf{PK} \models \chi$ iff $\theta$ holds in all atomic BA's.

By 21.34 and 15.6, this completes the decision procedure.

To prove (1), first suppose that $\mathbf{PK} \models \chi$. By 21.34 it suffices to show that $\theta$ holds in any BA of the form $\mathbf{S}I$. Assume that $J_0, \ldots, J_m \subseteq I$, they form a partition of $I$, and $J_k = 0$ whenever $k \in T$; we must show that $\mathbf{S}I \models \varphi[J_0, \ldots, J_m]$.

Now for $k \in (m + 1) \sim T$ there is a structure $\mathfrak{A}_k \in \mathbf{K}$ such that $\mathfrak{A}_k \models \psi_k$. Define $\mathfrak{B}: I \rightarrow \mathbf{K}$ as follows. Given $i \in I$, there is a unique $k \in (m+1)$ such that $i \in J_k$. Set $\mathfrak{B}_i = \mathfrak{A}_k$. Then $\mathbf{PK} \models \chi$ implies $\prod_{i \in I} \mathfrak{B}_i \models \chi$. By the choice of $(\varphi, \psi_0, \ldots, \psi_m)$ via 23.3, we obtain $\mathbf{S}I \models \varphi[J_0, \ldots, J_m]$, as desired.

Conversely, suppose $\theta$ holds in all atomic BA's. Let $\mathfrak{B}_i \in \mathbf{K}$ for each $i \in I$, and we need to show $\prod_{i \in I} \mathfrak{B}_i \models \chi$. By 21.34, it suffices to show $\mathbf{S}I \models \varphi[K_0, \ldots, K_m]$ where $K_k = \{i \in I : \mathfrak{B}_i \models \psi_k\}$. Note that $K_k = 0$ for $k \in T$ by definition of $T$. Since the $K_k$ form a partition of $I$ and $\theta$ holds in $\mathbf{S}I$, the definition of $\theta$ yields $\mathbf{S}I \models \varphi[K_0, \ldots, K_m]$, completing the proof.
