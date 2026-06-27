---
role: proof
locale: en
of_concept: convergence-class-topology-correspondence
source_book: gtm027
source_chapter: "2"
source_section: "Sequences and Subsequences"
---

# Proof of Convergence Class Defines a Topology

**Theorem 9.** Let $\mathcal{C}$ be a convergence class for a set $X$. For each subset $A$ of $X$, let $A^c$ be the set of all points $s$ such that, for some net in $A$, the net $\mathcal{C}$-converges to $s$. Then the operator $A \mapsto A^c$ is a Kuratowski closure operator on $X$, and a net in $X$ converges to a point $s$ relative to the topology associated with this closure operator if and only if it $\mathcal{C}$-converges to $s$.

*Proof.* The proof proceeds in two stages: first, we show that $c$ is a Kuratowski closure operator; second, we show that the $\mathcal{C}$-convergence coincides with convergence in the topology $\mathfrak{J}$ determined by $c$.

**Stage 1: $c$ is a closure operator.**

We verify the four Kuratowski closure axioms.

(i) $\emptyset^c = \emptyset$. There is no net whose range lies in the empty set, so vacuously $\emptyset^c = \emptyset$.

(ii) $A \subset A^c$ for every $A \subset X$. For each $a \in A$, the constant net $S_n = a$ for all $n$ has range contained in $A$, and by condition (a) of a convergence class, this constant net $\mathcal{C}$-converges to $a$. Hence $a \in A^c$.

(iii) $(A \cup B)^c = A^c \cup B^c$ for all $A, B \subset X$. The inclusion $A^c \subset (A \cup B)^c$ is immediate since $A \subset A \cup B$ and any net in $A$ is also a net in $A \cup B$. Similarly $B^c \subset (A \cup B)^c$, so $A^c \cup B^c \subset (A \cup B)^c$.

For the opposite inclusion, suppose $\{S_n, n \in D\}$ is a net in $A \cup B$ which $\mathcal{C}$-converges to $s$. Define
$$D_A = \{n \in D : S_n \in A\}, \qquad D_B = \{n \in D : S_n \in B\}.$$
Then $D_A \cup D_B = D$. Since $D$ is directed, at least one of $D_A$ or $D_B$ must be cofinal in $D$ (if neither were cofinal, there would exist $n_A, n_B \in D$ such that no element of $D_A$ exceeds $n_A$ and no element of $D_B$ exceeds $n_B$; choosing $m \geq n_A, n_B$ gives $m \notin D_A \cup D_B = D$, contradiction). If $D_A$ is cofinal, then $\{S_n, n \in D_A\}$ is a subnet of $\{S_n, n \in D\}$ (the inclusion map $D_A \hookrightarrow D$ is monotone cofinal), which by condition (b) also $\mathcal{C}$-converges to $s$. Since this subnet lies entirely in $A$, we have $s \in A^c$. Similarly, if $D_B$ is cofinal then $s \in B^c$. Hence $s \in A^c \cup B^c$, establishing $(A \cup B)^c \subset A^c \cup B^c$.

(iv) $A^{cc} = A^c$ for every $A \subset X$. The inclusion $A^c \subset A^{cc}$ follows from (ii) applied to $A^c$. For the reverse inclusion, suppose $t \in A^{cc}$. Then there exists a net $\{T_m, m \in D\}$ in $A^c$ which $\mathcal{C}$-converges to $t$. For each $m \in D$, since $T_m \in A^c$, there exists a directed set $E_m$ and a net $\{S(m,n), n \in E_m\}$ in $A$ which $\mathcal{C}$-converges to $T_m$. Let $F = D \times \prod\{E_m : m \in D\}$ be the product directed set, and for $(m,f) \in F$ define $R(m,f) = (m, f(m))$. Then $S \circ R$ is a net whose terms lie in $A$ (since each $S(m, f(m)) \in A$). By condition (d) of a convergence class (the iterated limits condition), the net $S \circ R$ $\mathcal{C}$-converges to $t$. Hence $t \in A^c$, and $A^{cc} \subset A^c$.

Thus $c$ satisfies all four Kuratowski axioms and determines a topology $\mathfrak{J}$ on $X$ in which a set $U$ is open iff $X \setminus U$ is $c$-closed (i.e., $(X \setminus U)^c = X \setminus U$).

**Stage 2: $\mathcal{C}$-convergence coincides with $\mathfrak{J}$-convergence.**

First, suppose $\{S_n, n \in D\}$ $\mathcal{C}$-converges to $s$ but does not converge to $s$ in the topology $\mathfrak{J}$. Then there exists a $\mathfrak{J}$-open neighborhood $U$ of $s$ such that $\{S_n\}$ is not eventually in $U$. Hence $\{S_n\}$ is frequently in $X \setminus U$. The set of indices $E = \{n \in D : S_n \in X \setminus U\}$ is cofinal in $D$, so $\{S_n, n \in E\}$ is a subnet of the original net. By condition (b), this subnet also $\mathcal{C}$-converges to $s$. But the subnet lies entirely in $X \setminus U$, so $s \in (X \setminus U)^c = X \setminus U$ (since $X \setminus U$ is $c$-closed). This contradicts $s \in U$. Therefore every $\mathcal{C}$-convergent net is $\mathfrak{J}$-convergent to the same limit.

Conversely, suppose $\{S_n, n \in D\}$ $\mathfrak{J}$-converges to $s$ but does not $\mathcal{C}$-converge to $s$. By condition (c), there exists a subnet $\{S_n, n \in E\}$ (with $E$ cofinal in $D$) such that no subnet of this subnet $\mathcal{C}$-converges to $s$. In particular, $s$ is not $\mathcal{C}$-a limit of any net in the range of this subnet; equivalently, $s \notin B^c$ where $B = \{S_n : n \in E\}$. Hence $s$ lies in the $\mathfrak{J}$-open set $X \setminus B^c$. But the subnet $\{S_n, n \in E\}$ must be eventually in every $\mathfrak{J}$-neighborhood of $s$ (since it is a subnet of a $\mathfrak{J}$-convergent net), which contradicts that all its terms lie in $B \subset B^c$. Therefore every $\mathfrak{J}$-convergent net is $\mathcal{C}$-convergent to the same limit.

We have shown that the $\mathcal{C}$-convergence and the $\mathfrak{J}$-convergence are identical. $\square$

**Corollary.** There is a one-to-one correspondence between the topologies on a set $X$ and the convergence classes on $X$. This correspondence is order-inverting: if $\mathcal{C}_1$ and $\mathcal{C}_2$ are convergence classes with associated topologies $\mathfrak{J}_1$ and $\mathfrak{J}_2$, then $\mathcal{C}_1 \subset \mathcal{C}_2$ if and only if $\mathfrak{J}_2 \subset \mathfrak{J}_1$. Moreover, the intersection $\mathcal{C}_1 \cap \mathcal{C}_2$ is a convergence class, and its associated topology is the smallest topology larger than both $\mathfrak{J}_1$ and $\mathfrak{J}_2$. Dually, the convergence class of $\mathfrak{J}_1 \cap \mathfrak{J}_2$ is the smallest convergence class larger than both $\mathcal{C}_1$ and $\mathcal{C}_2$.
