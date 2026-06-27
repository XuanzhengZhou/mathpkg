---
role: proof
locale: en
of_concept: primary-ideal-disjoint-from-m-under-extension
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

\textbf{Proof of (a).} If $x$ is any element of $\mathfrak{p}$, then some power of $x$ belongs to $\mathfrak{q}$, while if $x$ is an element of $M$, then any power of $x$ belongs to $M$. Since $\mathfrak{q} \cap M = \emptyset$ by hypothesis, no power of an element of $M$ can belong to $\mathfrak{q}$. Therefore no element of $\mathfrak{p}$ can belong to $M$, showing $\mathfrak{p} \cap M = \emptyset$.

Since $\mathfrak{p} \cap M = \emptyset$, Theorem 15(b) implies $\mathfrak{p}^e \neq R_M$, and similarly $\mathfrak{q}^e \neq R_M$. For a primary ideal disjoint from $M$, one checks that $\mathfrak{q}^{ec} = \mathfrak{q}$ and $\mathfrak{p}^{ec} = \mathfrak{p}$, so both are contracted ideals. Moreover, since $M \cap \mathfrak{q} = \emptyset$, for any $x \in \mathfrak{n}$ there exists $m \in M$ with $mx = 0 \in \mathfrak{q}$. As $\mathfrak{q}$ is primary and $m \notin \mathfrak{p}$ (since $\mathfrak{p} \cap M = \emptyset$), we must have $x \in \mathfrak{q}$. Thus $\mathfrak{n} \subset \mathfrak{q}$, and similarly $\mathfrak{n} \subset \mathfrak{p}$.

\textbf{Proof of (b).} To show $\mathfrak{q}^e$ is primary, take $x'/s, y'/t \in R_M$ with $(x'/s)(y'/t) \in \mathfrak{q}^e$ and $x'/s \notin \mathfrak{p}^e$. This means there exist $a \in \mathfrak{q}, m \in M$ such that $x'y'/st = a/m$ in $R_M$, so $m'x'y' \in \mathfrak{q}$ for some $m' \in M$. Since $\mathfrak{q}$ is primary and no element of $M$ is in $\mathfrak{p}$, the element $m'x'$ cannot be in $\mathfrak{p}$ (as $x'/s \notin \mathfrak{p}^e$). Thus $y' \in \mathfrak{q}$, implying $y'/t \in \mathfrak{q}^e$. Hence $\mathfrak{q}^e$ is primary. That its radical is $\mathfrak{p}^e$ follows from the fact that extension commutes with taking radicals.
