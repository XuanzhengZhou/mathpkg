---
role: proof
locale: en
of_concept: if-m-is-transitive-almost-universal-and-closed-under-the-eight-fundamental-opera
source_book: gtm001
source_chapter: "14"
source_section: ""
---

(By induction on $k$ the number of logical symbols in $\varphi(a_1, \ldots, a_m)$). If $k = 0$ then $\varphi(a_1, \ldots, a_m)$ either (1) contains none of the variables $a_1, \ldots, a_m$ or it is of the form (2) $a_i \in a_j$ or (3) $a_i \in b_j$ or (4) $b_i \in a_j$.

**Case 1.** If $\varphi(a_1, \ldots, a_m)$ contains none of the variables $a_1, \ldots, a_m$ then $a = c_1 \times c_2 \times \cdots \times c_m$ or $a = 0$ according as $\varphi^M(a_1, \ldots, a_m)$ holds or does not hold. In either case $a \in M$.

**Case 2.** If $\varphi(a_1, \ldots, a_m)$ is $a_i \in a_j$ then $i < j$ or $i = j$ or $j < i$. If $i < j$ then since $(c_i \times c_j) \cap E \in M$, and $c_1 \times \cdots \times c_{i-

If $k > 0$ then $\varphi(a_1, \ldots, a_m)$ is of the form (1) $\neg \psi(a_1, \ldots, a_m)$ or (2) $\psi(a_1, \ldots, a_m) \wedge \eta(a_1, \ldots, a_m)$ or (3) $(\exists x) \psi(a_1, \ldots, a_m, x)$.

Case 1. If $\varphi(a_1, \ldots, a_m)$ is $\neg \psi(a_1, \ldots, a_m)$ then as our induction hypothesis we have

$$\{ \langle x_1, \ldots, x_m \rangle | x_1 \in c_1 \wedge \cdots \wedge x_m \in c_m \wedge \psi^M(x_1, \ldots, x_m) \} \in M.$$

Then

$$\{ \langle x_1, \ldots, x_m \rangle | x_1 \in c_1 \wedge \cdots \wedge x_m \in c_m \wedge \neg \psi^M(x_1, \ldots, x_m) \}$$
$$= c_1 \times \cdots \times c_m - \{ \langle x_1, \ldots, x_m \rangle | x_1 \in c_1 \wedge \cdots \wedge x_m \in c_m \wedge \psi^M(x_1, \ldots, x_m) \}$$
$$\wedge \psi^M(x_1, \ldots, x_m) \} \in M.$$

Case 2. If $\varphi(a_1, \ldots, a_m)$ is $\psi(a_1, \ldots, a_m) \wedge \eta(a_1, \ldots, a_m)$ then from the induction hypothesis

$$\{ \langle x_1, \ldots, x_m \rangle | x_1 \in c_1 \wedge \cdots \wedge x_m \in c_m \wedge \psi^M(x_1, \ldots, x_m) \wedge \eta^M(x_1

of Regularity (Axiom 6). By Proposition 14.5 ($\forall x, y \in M)[\{x, y\} \in M]$.
Therefore $M$ is a model of the Axiom of Pairing (Axiom 2).
Since $M$ is transitive $a \in M$ implies that $\cup(a) \subseteq M$. Hence
$(\exists y \in M)[\cup(a) \subseteq y]$.

Since by Proposition 14.5, $b \times a \in M$ and since $M$ is closed under the eight fundamental operations
$(b \times a) \cap E = \mathcal{F}_2(b \times a, a) \in M$.

Then from Proposition 14.7
$\cup(a) = \mathcal{D}((b \times a) \cap E) \in M$.

Thus $M$ is a model of the Axiom of Unions (Axiom 3).
Since $a \in M$ implies $\mathcal{P}(a) \cap M \subseteq M$, $(\exists y \in M)[\mathcal{P}(a) \cap M \subseteq y]$. Then by Proposition 14.10
$\mathcal{P}(a) \cap M = \{x | x \in y \land [x \subseteq a]^M\} \in M$.

Therefore $M$ is a model of the Axiom of Powers (Axiom 4).
If ($\forall x, y, z \in M)[\varphi^M(x, y) \land \varphi^M(x, z) \rightarrow y = z]$ and if $a \in M$, then
$F \triangleq \{\langle x, y \rangle \in M^2 | x \in a \land \varphi^M(x, y)\}$

is a function. Since $\mathcal{D}(F) \subseteq a$ both $\mathcal{D}(F) \land \mathcal{W}(F)$ are sets. Therefore since $F“a \subseteq M$, $(\exists z \in M)[F“a \subseteq z)$. Then
$\{y \in M |

Therefore

$$\cup \{x \in a | \text{Ord}(x)\} \in M.$$

But the union of a collection of ordinals is an ordinal, i.e.,

$$(\exists \beta \in M)(\forall \gamma \in a)[\gamma \leq \beta].$$

Then $(\forall \gamma \in a)[\gamma \in \beta + 1]$. Since $\alpha \subseteq a$ it follows that $\alpha \leq \beta + 1$. Since $\beta \in M$ it follows that $\beta + 1 = \beta \cup \{\beta\} \in M$. Hence $\alpha \in M$. $\square$

Remark. With the proof of Proposition 14.11 we have achieved our major objective for this section. There is however an interesting theory of classes in which certain results of this section are generalized. We state the main results of this theory leaving the proofs as exercises.
