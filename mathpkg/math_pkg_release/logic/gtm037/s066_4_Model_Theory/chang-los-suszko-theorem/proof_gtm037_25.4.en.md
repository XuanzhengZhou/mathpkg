---
role: proof
locale: en
of_concept: chang-los-suszko-theorem
source_book: gtm037
source_chapter: "25"
source_section: "4"
---

**$(i) \Rightarrow (ii)$.** Suppose $\mathrm{Mod}\,\Gamma = \mathrm{Mod}\,\Delta$, where $\Delta$ is a set of universal-existential sentences. Suppose $\mathcal{A}$ is a subset of $\mathrm{Mod}\,\Gamma$ directed by $\subseteq$. Let $\varphi$ be any member of $\Delta$; say $\varphi$ is the sentence

$$\forall v_{i0} \cdots \forall v_{i(m-1)} \exists v_{im} \cdots \exists v_{i(n-1)} \psi.$$

To show that $\varphi$ holds in $\bigcup \mathcal{A}$, take any $x \in {^{\omega}}(\bigcup \mathcal{A})$. Then by directedness there is an $A \in \mathcal{A}$ such that $x_{ij} \in A$ for each $j < m$. Since $A \models \varphi$, choose $y \in {^{\omega}}A$ with $y \upharpoonright \omega \sim \{i_j : m \leq j < n\} = x \upharpoonright \omega \sim \{i_j : m \leq j < n\}$ and $A \models \psi[y]$. Then clearly $\bigcup \mathcal{A} \models \psi[y]$, so $\bigcup \mathcal{A} \models \varphi$.

**$(ii) \Rightarrow (iii)$.** Trivial, since a chain of type $\omega$ is in particular a directed subset.

**$(iii) \Rightarrow (i)$.** Assume (iii). Let $\Delta$ be the set of all universal-existential sentences $\chi$ such that $\Gamma \models \chi$. We show $\mathrm{Mod}\,\Gamma = \mathrm{Mod}\,\Delta$. The inclusion $\mathrm{Mod}\,\Gamma \subseteq \mathrm{Mod}\,\Delta$ is obvious.

For the converse, take $\mathfrak{A} \in \mathrm{Mod}\,\Delta$. Let $\mathcal{L}'$ be the language $\mathcal{L}$ expanded by new constants $c_a$ for each $a \in A$. Let $\Delta'$ be the set of all universal sentences of $\mathcal{L}'$ that hold in $(\mathfrak{A}, a)_{a \in A}$. One shows that $\Delta' \cup \Gamma$ has a model; otherwise by compactness there is a conjunction $\varphi$ of members of $\Delta'$ such that $\Gamma \models \neg\varphi$. Now $\models \neg\varphi \leftrightarrow \psi$ for some existential sentence $\psi$ of $\mathcal{L}'$. Replacing the constants $c_a$ by variables yields a universal-existential sentence $\chi$ of $\mathcal{L}$ with $\Gamma \models \chi$, so $\chi \in \Delta$ and $\mathfrak{A} \models \chi$, contradicting the fact that $\neg\psi$ holds in $(\mathfrak{A}, a)_{a \in A}$.

Let $(\mathfrak{B}, l_a)_{a \in A}$ be a model of $\Delta' \cup \Gamma$. Since the $\mathcal{L}'$-diagram of $\mathfrak{A}$ is a subset of $\Delta'$, we have $l: \mathfrak{A} \to \mathfrak{B}$ is an embedding. Now one constructs an alternating elementary chain

$$\mathfrak{A} = \mathfrak{B}_0 \subseteq \mathfrak{B}_1 \subseteq \mathfrak{B}_2 \subseteq \cdots$$

such that $\mathfrak{B}_1$ is a model of $\Gamma$, $\mathfrak{B}_1 \equiv_{\mathrm{ee}} \mathfrak{B}_3 \equiv_{\mathrm{ee}} \mathfrak{B}_5 \equiv_{\mathrm{ee}} \cdots$, and $\mathfrak{B}_0 \preceq \mathfrak{B}_2 \preceq \mathfrak{B}_4 \preceq \cdots$. This is achieved by iteratively applying the above embedding argument and taking elementary extensions. Hence $\mathfrak{B}_{2n+1}$ is a model of $\Gamma$ for each $n \in \omega$, so by (iii), $\bigcup_{n \in \omega} \mathfrak{B}_{2n+1}$ is a model of $\Gamma$.

And by 19.36, $\mathfrak{A} \preceq \bigcup_{n \in \omega} \mathfrak{B}_{2n}$. But $\bigcup_{n \in \omega} \mathfrak{B}_{2n} = \bigcup_{n \in \omega} \mathfrak{B}_{2n+1}$, so $\mathfrak{A}$ is an elementary substructure of a model of $\Gamma$, hence $\mathfrak{A} \in \mathrm{Mod}\,\Gamma$. Thus $\mathrm{Mod}\,\Gamma = \mathrm{Mod}\,\Delta$, completing the proof.
