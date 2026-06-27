---
role: proof
locale: en
of_concept: lambda-mathcal-mathcal-a11
source_book: gtm054
source_chapter: "10"
source_section: "XA"
---

If $(V, \bigcup_{A \in \mathcal{A}} \mathcal{P}(A))$ is an exchange system, then so is $\Lambda$, by Exercise A4.

Conversely, suppose that $\Lambda$ is an exchange system. It suffices to prove that $(V, \bigcup_{A \in \mathcal{A}} \mathcal{P}_{k-1}(A))$ is an exchange system; the rest follows by repeated application of this result and Exercise A4. Let $A_1, A_2 \in \bigcup_{A \in \mathcal{A}} \mathcal{P}_{k-1}(A)$, and let $x_1 \in A_1 + (A_1 \cap A_2)$.

Case 1: there exists $y \in V$ such that $A_1 + \{y\}, A_2 + \{y\} \in \mathcal{A}$. Then $x_1 \in (A_1 + \{y\}) + [(A_1 + \{y\}) \cap (A_2 + \{y\})]$. Since $\Lambda$ is an exchange system, there exists $x_2 \in (A_2 + \{y\}) + [(A_1 + \{y\}) \cap (A_2 + \{y\})]$ such that $A_1 + \{y, x_1, x_2\} \in \mathcal{A}$. Since $x_2 \notin A_1 + \{y\}$, we have

$$A_1 + \{x_1, x_2\} \in \mathcal{P}_{k-1

conditions are imposed on $\Lambda$, there is no reason to believe that $A_0$ is a heaviest block. We can only be sure that $A_0$ is a "local maximum" in the sense of the following exercise.
