---
role: proof
locale: en
of_concept: closure-as-union-of-full-extensions
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

We construct the sequence of full extensions and show their union is closed and equals the generated configuration.

Let $\mathcal{C} = \mathcal{C}_0$, and define a sequence $\mathcal{C}_i$ of configurations as follows: given $\mathcal{C}_i$, form $\mathcal{C}_{i+1}$ by taking all elements of $\mathcal{C}_i$ together with their incidences, and for each pair $X$, $Y$ of like elements of $\mathcal{C}_i$ that are not incident with a common element in $\mathcal{C}_i$, add a new element $XY$ (unlike $X$ and $Y$) incident with $X$ and $Y$ only. Then each $\mathcal{C}_{i+1}$ is a full one-step extension of $\mathcal{C}_i$.

Let $\mathcal{B} = igcup_{i=0}^{\infty} \mathcal{C}_i$. We claim $\mathcal{B}$ is closed. Take any two like elements $U, V \in \mathcal{B}$ not incident with a common element in $\mathcal{B}$. Since each belongs to some $\mathcal{C}_i$, let $n = \max(i, j)$. Then $U, V \in \mathcal{C}_n$. By construction, $\mathcal{C}_{n+1}$ contains an element $UV$ incident with $U$ and $V$, so $UV \in \mathcal{B}$, making $U$ and $V$ incident in $\mathcal{B}$. Thus $\mathcal{B}$ is closed.

Since $\mathcal{B}$ is a closed configuration containing $\mathcal{C}$ and contained in $\mathcal{P}$, we have $\langle \mathcal{C} angle_{\mathcal{P}} \subseteq \mathcal{B}$. Conversely, any closed sub-configuration of $\mathcal{P}$ containing $\mathcal{C}$ must contain every full extension of $\mathcal{C}$, hence contains each $\mathcal{C}_i$ and therefore contains $\mathcal{B}$. Thus $\mathcal{B} \subseteq \langle \mathcal{C} angle_{\mathcal{P}}$. Therefore $\langle \mathcal{C} angle_{\mathcal{P}} = \mathcal{B}$, which is closed and is the union of all full $n$-step extensions of $\mathcal{C}$.
