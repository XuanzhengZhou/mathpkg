---
role: proof
locale: en
of_concept: basis-cardinality-uniqueness
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

This theorem has been proved in I, §21 under the assumption that there exists at least one finite basis of $V$. We shall therefore assume now that every basis of $V$ is infinite.

Let $B$ be a basis of $V$ and let $x$ be any element of $V$. By $(S_2)$, there exist finite subsets $E$ of $B$ such that $x \in s(E)$. We assert that there exists a smallest finite subset $E_x$ of $B$ such that $x \in s(E_x)$ (and such that any other subset $E$ of $B$ with the property $x \in s(E)$ contains $E_x$). To see this, it is sufficient to prove the following: if $E'$ and $E''$ are two subsets of $B$ such that $x \in s(E') \cap s(E'')$ and if we have $x \notin s(E'_1)$ for every proper subset $E'_1$ of $E'$, then $E' \subset E''$.

Assume the contrary, let $z \in E'$, $z \notin E''$. Then $z \in s(E' \setminus \{z\} \cup \{x\})$ by applying $(S_5)$ to the fact that $x \in s(E')$. Since $x \in s(E'')$, we obtain $z \in s(E' \setminus \{z\} \cup E'')$, contradicting that $B$ is a basis (since $z$ would then depend on other basis elements). Hence the minimal finite subset $E_x$ exists.

Now for each $x \in V$, let $E_x$ be the minimal finite subset of $B$ with $x \in s(E_x)$. For another basis $B'$, we have $B' \subset \bigcup_{x \in B'} E_x \subset$ the set of all finite subsets of $B$. Since each $E_x$ is finite and $B$ is infinite, standard cardinal arithmetic gives $|B'| \leq |B|$. By symmetry $|B| \leq |B'|$, so $|B| = |B'|$.
