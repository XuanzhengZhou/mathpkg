---
role: proof
locale: en
of_concept: group-extension-coprime
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "3. The multiplicative group of Q_p"
---

*Proof.* Since $a$ and $b$ are coprime, there exist integers $r, s \in \mathbb{Z}$ such that $ar + bs = 1$.

If $x \in A \cap B'$, then $ax = 0$ (since $x \in A$ and $|A| = a$) and $bx = 0$ (since $x \in B'$). Hence $(ar + bs)x = 1 \cdot x = x = 0$, proving $A \cap B' = \{0\}$.

Moreover, every $x \in E$ can be written as $x = (ar)x + (bs)x$. Since $bB' = 0$ by definition, we have $bE \subset A$ (the image of $b$ annihilates the quotient $B$), so $bsx \in A$. On the other hand, $abE = 0$ (since $b$ annihilates $B$ and $a$ annihilates $A$), which implies $a(arx) = a^2 r x \in aE \subset A$, and more directly $b(arx) = abrx = 0$, so $arx \in B'$. Hence $E = A + B'$, and together with $A \cap B' = 0$, we have $E = A \oplus B'$.

The projection $E \to B$ restricted to $B'$ is injective (since $A \cap B' = 0$ and the kernel of the projection is $A$) and surjective (since $E \to B$ is surjective and $A$ maps to $0$). Hence $B' \cong B$.

Conversely, if $B''$ is any subgroup of $E$ isomorphic to $B$, then $bB'' = 0$ (since $|B| = b$), so $B'' \subset B'$. Since $B''$ and $B'$ have the same order $b$, they are equal. Thus $B'$ is the unique subgroup of $E$ isomorphic to $B$. $\square$
