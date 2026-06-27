---
role: proof
locale: en
of_concept: product-forcing-generic-decomposition
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

Let $G$ be $P = P_1 	imes P_2$-generic over $M$. Define
$$G_1 	riangleq \{p_1 \in P_1 \mid \langle p_1, 1 angle \in G\},$$
$$G_2 	riangleq \{p_2 \in P_2 \mid \langle 1, p_2 angle \in G\}.$$

**Step 1: $G_1$ is $P_1$-generic over $M$.** Let $D \in M$ be a dense subset of $P_1$. Define
$$D^* 	riangleq \{\langle p_1, p_2 angle \in P \mid p_1 \in D\}.$$
Then $D^*$ is dense in $P$ (if $\langle q_1, q_2 angle \in P$, choose $p_1 \leq q_1$ with $p_1 \in D$, then $\langle p_1, q_2 angle \in D^*$ and $\langle p_1, q_2 angle \leq \langle q_1, q_2 angle$). Since $D^* \in M$ and $G$ is generic, $G \cap D^* 
eq \emptyset$. Hence $G_1 \cap D 
eq \emptyset$.

**Step 2: $G_2$ is $P_2$-generic over $M[G_1]$.** Let $S \in M[G_1]$ be a dense subset of $P_2$. There exists a $P_1$-name $\dot{S} \in M$ and $p \in G_1$ such that $p \Vdash_{P_1} 	ext{"}\dot{S} 	ext{ is dense in } P_2	ext{"}$. Define
$$E 	riangleq \{\langle q_1, q_2 angle \in P \mid q_1 \Vdash_{P_1} q_2 \in \dot{S}\}.$$
One shows $E$ is dense below $\langle p, 1 angle$ in $P$: given $r = \langle r_1, r_2 angle$, find $q_1 \leq r_1, p$ deciding $r_2 \in \dot{S}$, then find $q_2 \leq r_2$ such that $q_1 \Vdash q_2 \in \dot{S}$. Then $\langle q_1, q_2 angle \in E$ and $\langle q_1, q_2 angle \leq r$.

Since $E \in M$ and $p \in G$, by Theorem 10.11, $G \cap E 
eq \emptyset$. Let $\langle q_1, q_2 angle \in G \cap E$. Then $q_2 \in G_2$ and $M[G_1] \models q_2 \in \dot{S}_G = S$. Therefore $G_2 \cap S 
eq \emptyset$.

**Step 3: $G = G_1 	imes G_2$.** Since $\langle p_1, p_2 angle \leq \langle p_1, 1 angle, \langle 1, p_2 angle$, we have $\langle p_1, p_2 angle \in G$ iff $\langle p_1, 1 angle \in G$ and $\langle 1, p_2 angle \in G$, hence $G = G_1 	imes G_2$.
