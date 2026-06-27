---
role: proof
locale: en
of_concept: free-extension-existence-and-uniqueness
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

We construct $\mathcal{P}$ to be $\mathcal{F}(\mathcal{C})$.

Let $\mathcal{C} = \mathcal{C}_0$, and define a sequence $\mathcal{C}_i$ of configurations as follows: if $\mathcal{C}_i$ is given, then $\mathcal{C}_{i+1}$ consists of all the elements of $\mathcal{C}_i$ (with their incidences), and in addition, for each pair $X$ and $Y$ of two like elements of $\mathcal{C}_i$ which are not incident with a common element in $\mathcal{C}_i$, we define an element $XY$, which is unlike $X$ and $Y$ and is incident with $X$ and $Y$ only, and is to be in $\mathcal{C}_{i+1}$.

It is easy to see that each $\mathcal{C}_i$ is an $i$-step full free extension of $\mathcal{C}$. Let $\mathcal{P} = igcup_{i=0}^{\infty} \mathcal{C}_i$.

We verify that $\mathcal{P}$ is closed. Take any two like elements $U, V \in \mathcal{P}$. There exist indices $i, j$ such that $U \in \mathcal{C}_i$ and $V \in \mathcal{C}_j$. Let $n = \max(i, j)$. Then $U, V \in \mathcal{C}_n$. If $U$ and $V$ are already incident with a common element in $\mathcal{C}_n$, they are incident in $\mathcal{P}$. Otherwise, by construction, $\mathcal{C}_{n+1}$ contains the element $UV$ incident with $U$ and $V$ only, so $U$ and $V$ are incident in $\mathcal{P}$. Thus $\mathcal{P}$ is closed.

Furthermore, each new element $XY$ introduced at any stage is incident with exactly two elements ($X$ and $Y$), so each $\mathcal{C}_{i+1}$ is a free one-step extension of $\mathcal{C}_i$, and $\mathcal{P}$ is a free extension of $\mathcal{C}$. Therefore $\mathcal{P}$ is a closed free extension of $\mathcal{C}$, so $\langle \mathcal{C} angle_{\mathcal{P}} = \mathcal{P}$. We set $\mathcal{F}(\mathcal{C}) = \mathcal{P}$.

For uniqueness up to isomorphism: if $\mathcal{Q}$ is another closed configuration that is a free extension of $\mathcal{C}$ with $\langle \mathcal{C} angle_{\mathcal{Q}} = \mathcal{Q}$, then the same iterative construction produces isomorphic configurations at each stage, yielding $\mathcal{Q} \cong \mathcal{F}(\mathcal{C})$.
