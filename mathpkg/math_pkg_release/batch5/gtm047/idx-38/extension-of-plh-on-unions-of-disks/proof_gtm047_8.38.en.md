---
role: proof
locale: en
of_concept: extension-of-plh-on-unions-of-disks
source_book: gtm047
source_chapter: "8"
source_section: "38"
---

Since $A_1$ and $A_1'$ are disks with the same number of holes (or, equivalently, $k$-annuli for the same $k$) there is a PLH $f_1: A_1 \leftrightarrow A_1'$, and $f_1$ can be chosen so that

$$A_1 \cap A_i \neq \emptyset \implies f_1(A_1 \cap A_i) = A_1' \cap A_i'.$$

Such an $f_1$ can be defined by repeated applications of Theorem 5.4, which asserts that every PLH between the boundaries of two polyhedral disks can be extended so as to give a PLH between the disks. The theorem is applied in the way suggested by Figure 33.2. Here we want $f_1(J_k) = J_k'$, to get an $f_1$ satisfying the condition above. First we define $f_1|_{J_1}: J_1 \leftrightarrow J_1'$. Then we extend $f_1$ to the dotted disk which joins $J_1$ to $J_2$, mapping it onto the corresponding strip joining $J_1'$ to $J_2'$. Then we extend again, so that $J_2 \leftrightarrow J_2'$. Similarly for the other polygons $J_i, J_i'$. Finally, extend $f_1$ to the rest of $A_1$ (which is the interior of a polyhedral disk).

Inductively, suppose that we have given

$$f_{j-1} : \bigcup_{i=1}^{j-1} A_i \leftrightarrow \bigcup_{i=1}^{j-1} A_i',$$

such that for $i \leq j-1$, and for every $k$, $f_{j-1}(A_i \cap A_k) = A_i' \cap A_k'$. We define $f_j$ as follows. Let $PS$ be an arc of $A_j \cap A_i$ for some $i < j$. Let $QR$ be another arc of $A_j \cap A_i$ for some $i < j$. Let the cyclic order of the images of these intersection arcs on $\operatorname{Bd} A_j'$ be considered. Take a disk in $A_j$, joining the intersection polygons, and take a disk in $A_j'$, joining the image arcs $P'S' = f_{j-1}(PS), Q'R' = f_{j-1}(QR)$. Then the image points $P', Q', R',$ and $S'$ appear in the stated cyclic order on the boundary of the second disk, because otherwise $\operatorname{Bd} X$ would contain a Möbius band. Therefore $f_{j-1}$ can be extended so as to map the first dotted disk onto the second.

We do this for every polygon in $A_j \cap \bigcup_{i=1}^{j-1} A_i$. For the other boundary components of $A_j$, we proceed merely as in the definition of $f_1$. Then we extend the mapping to the rest of $A_j$, as in the definition of $f_1$.

By induction, the lemma follows.
