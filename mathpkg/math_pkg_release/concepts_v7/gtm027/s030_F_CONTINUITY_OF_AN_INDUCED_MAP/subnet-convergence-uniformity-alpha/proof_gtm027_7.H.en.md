---
role: proof
locale: en
of_concept: subnet-convergence-uniformity-alpha
source_book: gtm027
source_chapter: "7"
source_section: "H"
---

# Proof of Subnet Construction for Uniform Convergence on a Directed Cover

Let $X$ be a set, let $\alpha$ be a cover of $X$ which is directed by $\supset$ (for $A, B \in \alpha$ there exists $C \in \alpha$ with $C \supset A \cup B$). Let $(Y, \mathcal{U})$ be a uniform space and $F$ the family of functions $X \to Y$ with the uniformity $\mathfrak{u} \mid \alpha$ of uniform convergence on members of $\alpha$.

Suppose $S = \{S_n : n \in D\}$ is a net in $F$, and for each $A \in \alpha$ there is given a subnet $\{S \circ T_A(m) : m \in E_A\}$ of $S$ converging to $s \in F$ uniformly on $A$. We construct a subnet of $S$ converging to $s$ relative to the topology of $\mathfrak{u} \mid \alpha$.

**Construction.** Define the directed set

$$E = \{(A, m, U) : A \in \alpha, m \in E_A, U \in \mathcal{U}\}$$

with the product direction: $(A, m, U) \geq (A', m', U')$ iff $A \supset A'$, $m \geq m'$ in $E_A$ (after appropriate identification), and $U \subseteq U'$.

For each $(A, m, U) \in E$, define

$$T(A, m, U) = T_A(m)$$

so that $S \circ T(A, m, U) = S(T_A(m))$ is the subnet value.

**Verification.** Given any basic entourage for $\mathfrak{u} \mid \alpha$, which is of the form

$$W(A_0, U_0) = \{(f, g) : (f(x), g(x)) \in U_0 \text{ for all } x \in A_0\}$$

with $A_0 \in \alpha$ and $U_0 \in \mathcal{U}$, we must find an index beyond which $S \circ T$ lies in this entourage from $s$.

Since the subnet for $A_0$ converges to $s$ uniformly on $A_0$, there exists $m_0 \in E_{A_0}$ such that for all $m \geq m_0$ in $E_{A_0}$, $(S(T_{A_0}(m))(x), s(x)) \in U_0$ for all $x \in A_0$.

Take any $(A, m, U) \geq (A_0, m_0, U_0)$. Then $A \supset A_0$ and the subnet for $A$ restricts to $A_0$; the uniform convergence on $A$ is inherited. Hence $S \circ T(A, m, U)$ is $U_0$-close to $s$ on $A_0$. This establishes convergence.

Explicitly, the subnet is given by the composition $S \circ T$ where $T : E \to D$ is defined by $T(A, m, U) = T_A(m)$, and $E$ is directed as above.
