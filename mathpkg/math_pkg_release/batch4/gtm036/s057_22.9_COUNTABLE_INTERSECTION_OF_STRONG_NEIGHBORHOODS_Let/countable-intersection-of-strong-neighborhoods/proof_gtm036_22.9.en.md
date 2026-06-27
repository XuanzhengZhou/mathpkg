---
role: proof
locale: en
of_concept: countable-intersection-of-strong-neighborhoods
source_book: gtm036
source_chapter: "5"
source_section: "22.9"
---

Let $U = \bigcap \{U_n : n = 1, 2, \cdots\}$. If $U$ is a strong neighborhood of $0$, then clearly $U$ absorbs strongly bounded sets. Conversely, assume that $U$ absorbs strongly bounded sets; then to show that $U$ is a strong neighborhood of $0$, it is sufficient to exhibit a weak* closed convex circled subset $V$ which is radial at $0$, since such a subset is the polar of a bounded subset of $E$. Let $\{B_n\}$ be a co-base for the strongly bounded subsets of $E^*$ such that each $B_n$ is weak* compact convex circled (there is such a co-base by 22.3). For each $n$, there is a positive number $t_n$ such that $t_n B_n \subset \frac{1}{2} U$, and there is a weak* closed convex circled strong neighborhood $W_n$ of $0$ which is contained in $\frac{1}{2} U_n$. Let $V_n = \langle t_1 B_1 \cup \cdots \cup t_n B_n \rangle + W_1 \cap \cdots \cap W_n$; then $V_n$ is a weak* closed convex circled strong neighborhood of $0$, $V_{n+1} \subset V_n$, and $\bigcap \{V_n : n = 1, 2, \cdots\} \subset U$. Let $V = \bigcap \{V_n : n = 1, 2, \cdots\}$. Since each $V_n$ is a strong neighborhood of $0$, $V$ absorbs strongly bounded sets; moreover, $V$ is convex, circled, and weak* closed. To show that $V$ is radial at $0$, it is sufficient to prove that $V \cap B_0$ is radial at $0$ for each strongly bounded set $B_0$. Since $V$ absorbs $B_0$, there is a positive number $t$ such that $t B_0 \subset V$. Because $V$ is closed under scalar multiplication by numbers of modulus at most $1$, it follows that $V \cap B_0$ is radial at $0$. Consequently, $V$ is a strong neighborhood of $0$ and $B_0$ absorbs strongly bounded sets, $B_0$ is a strong neighborhood of $0$.
