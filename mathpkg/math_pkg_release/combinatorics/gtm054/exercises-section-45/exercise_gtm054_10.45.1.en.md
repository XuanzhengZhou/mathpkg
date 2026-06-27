---
role: exercise
locale: en
chapter: "10"
section: "45"
exercise_number: 1
---

$\Lambda$ is an exchange system of type

X Matroid Theory

Proof. Suppose that $\Lambda$ is an exchange system of type 1. Let $A_1, A_2 \in \mathcal{A}$ such that $|A_1| = |A_2| = k$ and let $x_1 \in A_1 + (A_1 \cap A_2)$. Let

$$\mathcal{F} = \{A \in \mathcal{A} \cap \mathcal{P}_k(V): x_1 \in A; A \cap A_2 \supseteq A_1 \cap A_2\}.$$

Then $\mathcal{F} \neq \emptyset$ since $A_1 \in \mathcal{F}$. Select $A_0 \in \mathcal{F}$ so that $|A_0 \cap A_2|$ is as large as possible. Since $x_1 \in A_0$ but $x_1 \notin A_2$, while $|A_0| = |A_2|$, there exists $y \in A_0 + (A_0 \cap A_2)$. Suppose $y \neq x_1$ and consider the triple $(A_0, A_2, y)$. Since $\Lambda$ is an exchange system of type 1, there exists $z \in A_2 + (A_0 \cap A_2)$ such that $A_3 = A_0 + \{y, z\} \in \mathcal{A}$. Now $|A_3| = k$ and $x_1 \in A_3$. Moreover, $A_3 \cap A_2 = (A_0 \cap A_2) + \{z\} \supset A_0 \cap A_2$. Hence $A_3 \in \mathcal{F}$, but the maximality of $|A_0 \cap A_2|$ has been contradicted. Therefore $y$ must be $x_1$; that is, $A_0 + (A_0 \cap A_2) = \{x_1\}$. Since $|A_0| = |A_2|$, there exists $x_2 \in V$ such that $\{x_2\} =

then $J_1 + \{x_1\}$ is a basis for a $(k - 1)$-dimensional subspace of $\mathcal{V}$ which cannot contain $J_2$, since $J_2$ spans some $k$-dimensional subspace. Hence $J_1 + \{x_1, x_2\}$ is independent for some $x_2 \in J_2 + (J_1 \cap J_2)$. Thus $(V, \mathcal{I})$ is an exchange system, and by Exercise A4, so is $(V, \mathcal{B})$. If $S_1$ and $S_2$ are spanning $k$-subsets of $\mathcal{V}$ and $x_1 \in S_1 + (S_1 \cap S_2)$, then $\dim \langle S_1 + \{x_1\} \rangle = \dim(\mathcal{V})$ or $\dim(\mathcal{V}) - 1$. In the first case, choose any $x_2 \in S_2 + (S_1 \cap S_2)$. In the second case, there exists some $x_2 \in S_2 + (S_1 \cap S_2)$ such that $x_2 \notin \langle S_1 + \{x_1\} \rangle$. Hence $S_1 + \{x_1, x_2\}$ spans $\mathcal{V}$.
