---
role: proof
locale: en
of_concept: noetherian-local-property
source_book: gtm052
source_chapter: "II"
source_section: "3"
---
The "if" part follows from the definition, so we have to show if $X$ is locally noetherian, and if $U = \operatorname{Spec} A$ is an open affine subset, then $A$ is a noetherian ring. First note that if $B$ is a noetherian ring, so is any localization $B_f$. The open subsets $D(f) \cong \operatorname{Spec} B_f$ form a base for the topology of $\operatorname{Spec} B$. Hence on a locally noetherian scheme $X$ there is a base for the topology consisting of the spectra of noetherian rings.

Now let $U = \operatorname{Spec} A$ be an open affine. Then $U$ can be covered by open subsets $D(f_i)$, where $f_i \in A$, such that each $\operatorname{Spec} A_{f_i}$ is the spectrum of a noetherian ring. Let $\mathfrak{a} \subseteq A$ be an ideal. For each $i$, consider the extended ideal $\varphi_i(\mathfrak{a}) \cdot A_{f_i}$ in $A_{f_i}$.

**Lemma.** If $A$ is a ring, $f_1,\ldots,f_r \in A$ generate the unit ideal, and $\varphi_i: A \to A_{f_i}$ are the canonical maps, then for any two ideals $\mathfrak{a},\mathfrak{b} \subseteq A$, $\varphi_i(\mathfrak{a}) \cdot A_{f_i} \subseteq \varphi_i(\mathfrak{b}) \cdot A_{f_i}$ for all $i$ implies $\mathfrak{a} \subseteq \mathfrak{b}$.

*Proof of Lemma.* If $\mathfrak{a} \not\subseteq \mathfrak{b}$, then there is $b \in \mathfrak{a}$ with $b \notin \mathfrak{b}$. For each $i$, the hypothesis gives $\varphi_i(b) \in \varphi_i(\mathfrak{b}) \cdot A_{f_i}$, so we can write $\varphi_i(b) = a_i/f_i^{n_i}$ in $A_{f_i}$ for each $i$, where $a_i \in \mathfrak{a}$ and $n_i > 0$. Increasing the $n_i$ if necessary, we can make them all equal to a fixed $n$. This means that in $A$ we have
$$f_i^{m_i}(f_i^n b - a_i) = 0$$
for some $m_i$. And as before, we can make all the $m_i = m$. Thus $f_i^{m+n} b \in \mathfrak{a}$ for each $i$. Since $f_1,\ldots,f_r$ generate the unit ideal, the same is true of their $N$th powers for any $N$. Take $N = n + m$. Then we have $1 = \sum c_i f_i^N$ for suitable $c_i \in A$. Hence
$$b = \sum c_i f_i^N b \in \mathfrak{a}$$
as required. This proves the lemma.

Now we can easily show that $A$ is noetherian. Let $\mathfrak{a}_1 \subseteq \mathfrak{a}_2 \subseteq \ldots$ be an ascending chain of ideals in $A$. Then for each $i$,
$$\varphi_i(\mathfrak{a}_1) \cdot A_{f_i} \subseteq \varphi_i(\mathfrak{a}_2) \cdot A_{f_i} \subseteq \ldots$$
is an ascending chain of ideals in $A_{f_i}$, which must become stationary because $A_{f_i}$ is noetherian. There are only finitely many $A_{f_i}$, so from the lemma we conclude that the original chain is eventually stationary, and hence $A$ is noetherian.
