---
role: proof
locale: en
of_concept: rich-extension-lemma
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

Let $\langle \varphi_\alpha : \alpha < m \rangle$ be a list of all sentences of $\mathcal{L}'$ of the form $\exists\beta\psi$, where $m = |\operatorname{Fmla}_{\mathcal{L}}|$ is an infinite cardinal. We construct a sequence $\langle \mathbf{d}_\alpha : \alpha < m \rangle$ of new individual constants by transfinite recursion.

Suppose we have defined $\mathbf{d}_\beta$ for all $\beta < \alpha$, where $\alpha < m$. The set of constants used so far, $\{\mathbf{d}_\beta : \beta < \alpha\}$, has cardinality $|\alpha| < m$. Since we adjoined $m$ new constants in $\mathcal{L}'$, there remain unused constants. Choose $\mathbf{d}_\alpha$ to be a new constant not occurring in $\varphi_\alpha$ (which involves at most finitely many constants) and not among $\{\mathbf{d}_\beta : \beta < \alpha\}$.

Now define $\Delta_0 = \Gamma$, and for each $\alpha < m$, let $\Delta_{\alpha+1} = \Delta_\alpha \cup \{\exists\beta\psi \rightarrow \operatorname{Subf}_{\mathbf{d}_\alpha}^\beta\psi\}$ where $\varphi_\alpha = \exists\beta\psi$. At limit ordinals, take unions.

**Consistency preservation.** We claim each $\Delta_\alpha$ is consistent. The proof is by induction on $\alpha$. The base $\alpha = 0$ holds by hypothesis. For the successor step, suppose $\Delta_\alpha$ is consistent but $\Delta_{\alpha+1}$ is inconsistent. Then

$$\Delta_\alpha \vdash \neg(\exists\beta\psi \rightarrow \operatorname{Subf}_{\mathbf{d}_\alpha}^\beta\psi),$$

which implies $\Delta_\alpha \vdash \exists\beta\psi$ and $\Delta_\alpha \vdash \neg\operatorname{Subf}_{\mathbf{d}_\alpha}^\beta\psi$. Since $\mathbf{d}_\alpha$ does not occur in $\Delta_\alpha$ or $\exists\beta\psi$, we may replace $\mathbf{d}_\alpha$ by a fresh variable and universally generalize, obtaining $\Delta_\alpha \vdash \forall\beta\neg\psi$, i.e., $\Delta_\alpha \vdash \neg\exists\beta\psi$, contradicting consistency of $\Delta_\alpha$. Limit stages preserve consistency since inconsistency requires only finitely many formulas.

Let $\Delta = \bigcup_{\alpha < m} \Delta_\alpha$. Then $\Delta$ is consistent (any finite subset is contained in some $\Delta_\alpha$) and rich (by construction, for every $\exists\beta\psi$ there is a constant $\mathbf{d}_\alpha$ witnessing it).
