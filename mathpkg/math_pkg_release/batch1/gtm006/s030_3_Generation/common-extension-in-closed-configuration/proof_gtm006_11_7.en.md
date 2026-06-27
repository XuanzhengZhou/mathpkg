---
role: proof
locale: en
of_concept: common-extension-in-closed-configuration
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

Let $\mathcal{A}_0 = \mathcal{A}$ and let $\mathcal{B}_0$ be an extension of $\mathcal{B}$ that contains $\mathcal{A}$. Such a $\mathcal{B}_0$ exists since $\mathcal{A}$ is contained in some extension of $\mathcal{B}$ (by hypothesis, each is contained in an extension of the other). Now construct $\mathcal{A}_1$ as an extension of $\mathcal{A}_0$ that contains $\mathcal{B}_0$. Such an $\mathcal{A}_1$ exists since $\mathcal{B}_0$ contains $\mathcal{A}$ and $\mathcal{B}$, and by the mutual extendability hypothesis.

Continuing this alternation yields sequences:
\[
\mathcal{A} = \mathcal{A}_0 \subseteq \mathcal{B}_0 \subseteq \mathcal{A}_1 \subseteq \mathcal{B}_1 \subseteq \cdots
\]
all contained in $\mathcal{P}$. Let $\mathcal{C} = igcup_{i=0}^{\infty} \mathcal{A}_i = igcup_{i=0}^{\infty} \mathcal{B}_i$. Then $\mathcal{C}$ is an extension of both $\mathcal{A}$ and $\mathcal{B}$, as each $\mathcal{A}_i$ (resp. $\mathcal{B}_i$) is an extension of $\mathcal{A}$ (resp. $\mathcal{B}$).

Now consider the special case $\mathcal{P} = \mathcal{F}(\mathcal{A}) = \mathcal{F}(\mathcal{B})$. Choose $\mathcal{B}_1$ to be the union of the $\mathcal{B}$-socles of all elements of $\mathcal{A}$. Then the free extension $\mathcal{A}_1$ of $\mathcal{A}$ has been shown to be a free extension of $\mathcal{B}_1$, and by Lemma 11.6, $\mathcal{B}_1$ is itself a free extension of $\mathcal{B}$. Any free extension of $\mathcal{B}$ that includes $\mathcal{A}$ must contain $\mathcal{B}_1$, and we can choose $\mathcal{A}_1 = \mathcal{B}_1$, so $\mathcal{B}_1$ is the desired common free extension $\mathcal{C}$.
