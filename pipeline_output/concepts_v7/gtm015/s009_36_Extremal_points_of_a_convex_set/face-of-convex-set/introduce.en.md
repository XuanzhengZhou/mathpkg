---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a vector space over $\mathbb{K}$ and let $A$ be a convex subset of $E$. A convex subset $F$ of $A$ is called a **face** of $A$ if it satisfies the following condition: whenever an open segment $\langle u, v \rangle$ is contained in $A$ and meets $F$, the entire segment lies in $F$. Formally:

$$\langle u, v \rangle \subset A \text{ and } \langle u, v \rangle \cap F \neq \varnothing \implies \langle u, v \rangle \subset F.$$

The idea is that a face is a convex subset of $A$ that is "extremal in the segment sense": if a line segment inside $A$ touches $F$ at any interior point, then the whole segment must belong to $F$.

The concept of face refines that of extremal point. In fact, a singleton $\{a\} \subset A$ is a face of $A$ if and only if $a$ is an extremal point of $A$. (If $a$ is extremal and $\langle u, v \rangle \subset A$ with $\langle u, v \rangle \cap \{a\} \neq \varnothing$, then $u = v = a$, so $\langle u, v \rangle = \{a\} \subset \{a\}$. Conversely, if $\{a\}$ is a face and $a \in \langle u, v \rangle \subset A$, then $\langle u, v \rangle \cap \{a\} \neq \varnothing$, forcing $\langle u, v \rangle \subset \{a\}$, hence $u = v = a$.)

Faces provide the natural setting for Zorn's lemma arguments that establish the existence of extremal points, as in the Krein-Mil'man theorem. The family of closed faces of a compact convex set, ordered by reverse inclusion, satisfies the chain condition needed for Zorn's lemma because the intersection of a chain of nonempty closed faces is nonempty (by compactness) and is again a face.
