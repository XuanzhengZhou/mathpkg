---
role: proof
locale: en
of_concept: proposition-2
source_book: gtm026
source_chapter: "1"
source_section: "3.12"
---

$\alpha \circ g^\Delta = \alpha.id_{BT} \circ g^\Delta = \alpha.gT$.

Let us return briefly to $A\Omega$. While 1.11 provided us with a unique derivation tree for each formula, there is more than one way in which one could choose to assemble the tree from its pieces. The associative law of clone composition may be regarded as the statement that different assembling procedures build the same tree. To be specific, let us consider the example of 2.15 where the formula $eie + dz + idz + i++$ in $D\Omega$ was broken up in two different ways:

$$\alpha \circ (\beta \circ \gamma) \quad (e)ie + (dz + idz + i++) +$$
$$(\alpha \circ \beta) \circ \gamma \quad (e)ie + (dz + i)(dz + i)++$$

It is not necessary to introduce parentheses as formal symbols to make these distinctions. Let us agree to interpret the parentheses enclosing $p$ in $(p)$ as the desire to consider the formula $p \in A\Omega$ as a mere variable in $(A\Omega)\Omega$. Thus $(e)ie + (dz + idz + i++) +$ and $(e)ie + (dz + i)(dz + i)++$ become elements of $(D\Omega)\Omega$ of word lengths 6 and 8, respectively. Since $A\Omega$ is an $\Omega$-algebra, it has a total description map (1.18) $A\mu:(A\Omega)\Omega \longrightarrow A\Omega$ which

The reader may check that in 3.7, $A\mu:A \times G \times G \rightarrow A \times G$ is the continuous map which sends $(a, g, h)$ to $(a, g*h)$. In 3.5, $A\mu$ is the union map sending the collection $A$ of subsets of $A$ to its union $\{a \in A : \text{there exists } S \in A \text{ with } a \in S\}$.

3.14 Kleisli Composition Law. For each $\beta:B \rightarrow C$ define $\beta^{\#}:BT \rightarrow CT = (\beta T:BT \rightarrow CTT).(C\mu:CTT \rightarrow CT)$. Then for all $\alpha:A \rightarrow B$ and $\beta:B \rightarrow C$, $\alpha \circ \beta = \alpha.\beta^{\#}$.

$\alpha \circ \beta = \alpha \circ (\beta.\text{id}_{CT}) = \alpha \circ \beta^{\#}.\text{id}_{CT} = \alpha.\beta T.\text{id}_{CT} = \alpha.(\beta T.\text{id}_{CTT}) \circ \text{id}_{CT} = \alpha.(\beta T^{\#}.\text{id}_{CTT}) \circ \text{id}_{CT}) = \alpha.(\beta T^{\#}.C\mu) = \alpha.\beta T.C\mu$.

We will see in the next section that the correct interpretation of 3.14 is the obvious one: algebraic theories really are like the motivating example $\text{Set}(\Omega, E)$. The next two statements establish the four axioms on $\mu$ we mentioned earlier.
