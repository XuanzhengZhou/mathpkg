---
role: proof
locale: en
of_concept: nowhere-dense-set-properties
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
\textbf{(1)} The first statement is obvious: any subset of a nowhere dense set inherits the property, since if $B \subset A$ and $A$ is nowhere dense, then for any interval $I$ there exists a subinterval $J \subset I \setminus A \subset I \setminus B$.

\textbf{(2)} To prove the second, note that if $A_1$ and $A_2$ are nowhere dense, then for each interval $I$ there is an interval $I_1 \subset I \setminus A_1$ and an interval $I_2 \subset I_1 \setminus A_2$. Hence $I_2 \subset I \setminus (A_1 \cup A_2)$. This shows that $A_1 \cup A_2$ is nowhere dense. The statement for any finite number follows by induction.

\textbf{(3)} Finally, any open interval contained in the complement $A'$ is also contained in the complement of the closure $(\overline{A})'$, since $A' \subset (\overline{A})'$. Therefore if $A'$ contains a dense open set (equivalently, $A$ is nowhere dense), then $(\overline{A})'$ also contains that dense open set, so $\overline{A}$ is nowhere dense.
