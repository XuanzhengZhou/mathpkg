---
role: proof
locale: en
of_concept: syntactic-semantic-arity-equality
source_book: gtm026
source_chapter: "5"
source_section: "5"
---

**Proof of Theorem 5.11.**

**Step 1:** $\mathrm{ar}(\tilde{\omega}) \leqslant \mathrm{ar}(\omega)$. There exist $f: \mathrm{ar}(\omega) \longrightarrow X$ and $h \in (\mathrm{ar}(\omega))T$ with $\langle h, fT \rangle = \omega$. Let $S = \{uf : u \in \mathrm{ar}(\omega)\}$ be the image of $f$ with inclusion map $i: S \longrightarrow X$, and define $p: \mathrm{ar}(\omega) \twoheadrightarrow S$ by $up = uf$. Then $\mathrm{card}(S) \leqslant \mathrm{ar}(\omega)$ and one can verify that $S$ is a support of $\tilde{\omega}$.

**Step 2:** $\mathrm{ar}(\omega) \leqslant \mathrm{ar}(\tilde{\omega})$. Let $S$ be a support of $\tilde{\omega}$ with $\mathrm{card}(S) = \mathrm{ar}(\tilde{\omega})$ and inclusion $i: S \hookrightarrow X$. Let $(ST, S\mu)$ be the free $T$-algebra on $S$. Define:

$$\psi = (ST, S\mu)\tilde{\omega}: (ST)^S \longrightarrow ST$$

Since $S$ is a support, there exists a factorization through the restriction to $S$. Let $g: S \longrightarrow ST$ be the inclusion of generators (i.e., $g = S\eta$). Define $\rho = \langle S\eta, \psi \rangle \in ST$. Then:

$$\langle \rho, iT \rangle = \langle S\eta, \psi \cdot iT \rangle = \langle i \cdot g, \psi \cdot iT \rangle = \langle g, iT^X \cdot (XT, X\mu)\tilde{\omega} \rangle = \cdots = \omega$$

This exhibits $\omega$ as the image under $iT$ of an element of $ST$, showing $\mathrm{ar}(\omega) \leqslant \mathrm{card}(S) = \mathrm{ar}(\tilde{\omega})$.

**Step 3: The arity-0 case.** If $\mathrm{ar}(\tilde{\omega}) = 0$, the above argument requires $ST \neq \emptyset$ when $S = \emptyset$. If $\emptyset T = \emptyset$, then $\emptyset$ would be a $T$-algebra, which contradicts nontriviality. Otherwise $ST \neq \emptyset$ and the factorization exists, completing the proof. $\square$
