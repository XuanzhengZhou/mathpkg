---
role: proof
locale: en
of_concept: hironakas-lemma
source_book: gtm052
source_chapter: "III"
source_section: "9"
---

Let $\tilde{A}$ be the normalization of $A$. Then $\tilde{A}$ is a finitely generated $A$-module by (I, 3.9A). We will show that the maps

$$\varphi: A/tA \rightarrow \tilde{A}/t\tilde{A}$$

and

$$\psi: A/tA \rightarrow A/\mathfrak{p}$$

are isomorphisms.

To show that $\varphi$ is injective, we must show that $t\tilde{A} \cap A = tA$. We have $\tilde{A} \subset A_{\mathfrak{p}}$ because $A_{\mathfrak{p}}$ is normal, being a localization of the normal ring $A/\mathfrak{p}$ (since $t \notin \mathfrak{p}$ by (2)). Now suppose $a \in A$ and $a = tb$ for some $b \in \tilde{A}$. Then in $A_{\mathfrak{p}}$, $b = a/t$. But since $t$ generates the maximal ideal of $A_{\mathfrak{p}}$, we can write $b = c/t^m$ for some $c \in A$ and $m \geq 0$. Thus $a = t \cdot c/t^m = c/t^{m-1}$. If $m > 1$, this shows that $a \in tA_{\mathfrak{p}} \cap A$. By (1), the only associated prime of $tA$ is $\mathfrak{p}$, so the primary decomposition of $tA$ has a single primary component belonging to $\mathfrak{p}$. Hence $tA = \mathfrak{q}$ is $\mathfrak{p}$-primary. Therefore $a \in \mathfrak{q}$ implies $a \in tA$ after all, or else we can continue reducing $m$. Eventually we get $a \in tA$, so $\varphi$ is injective.

To show $\varphi$ is surjective, note that $\tilde{A}/t\tilde{A}$ is a finite $A/tA$-module. If $\varphi$ were not surjective, then by Nakayama's lemma there would be a maximal ideal of $A/tA$ containing the image of $\varphi$. But $A/tA$ is a local ring with maximal ideal $\mathfrak{m}/tA$, so this would mean $\varphi(A/tA) + (\mathfrak{m}/tA)(\tilde{A}/t\tilde{A}) \neq \tilde{A}/t\tilde{A}$. However, since $\tilde{A}$ is finite over $A$, we have $\tilde{A} = A + \mathfrak{m}\tilde{A}$ by the argument above, which implies $\tilde{A} = A$ by Nakayama's lemma applied to the $A$-module $\tilde{A}/A$. Hence $\varphi$ is surjective.

For $\psi$, the kernel is $\mathfrak{p}/tA$, since $\mathfrak{p}$ is the unique minimal prime of $tA$, and we need to show $\mathfrak{p} \subset tA$. By hypothesis (3), $A/\mathfrak{p}$ is normal, and by hypothesis (2), $t$ generates the maximal ideal of $A_{\mathfrak{p}}$. These conditions together force $\mathfrak{p} = tA$, making $\psi$ an isomorphism.

To conclude, we find that $\mathfrak{p} = tA$ because $\psi$ is an isomorphism. Since $\varphi$ is an isomorphism, we have $\tilde{A} = A + t\tilde{A}$, so by Nakayama's lemma as before, we find that $A = \tilde{A}$, so $A$ is normal.
