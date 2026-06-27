---
role: proof
locale: en
of_concept: theorem-23-8
source_book: gtm008
source_chapter: "22"
source_section: "22 The Completion of a Boolean Algebra

For the following let"
---
We have to show that for a given $u \in V^{(B)}$ or $u \in V^{(B')}$

$$\llbracket (\exists v) (\forall x) [x \in v \leftrightarrow (\exists y \in u) [x \in y]] \rrbracket = 1.$$

Define $v$ by

$$\mathcal{D}(v) = \bigcup_{y \in \mathcal{D}(u)} \mathcal{D}(y)$$

and

$$(\forall x \in \mathcal{D}(v)) [v(x) = \llbracket (\exists y \in u) [x \in y] \rrbracket].$$

Obviously, $v \in V^{(B)}$ or $v \in V^{(B')}$ (use Theorem 23.7) according as $u \in V^{(B)}$ or $u \in V^{(B')}$. Since $\llbracket (\forall x \in v) (\exists y \in u) [x \in y] \rrbracket = 1$ by Theorem 23.7, it remains to show that

$$\llbracket (\forall y \in u) (\forall x \in y) [x \in v] \rrbracket = 1,$$

$$\

Remark. Note that the foregoing proof requires a Boolean algebra of type $\tilde{B}$ and cannot be carried out for an algebra of type $B$. The difficulty is in defining $v$: If $a \in V^{(\tilde{B})}$ then for each $x \in \mathcal{D}(v)$ we have $a(x) \in B$, but we do not know that $[\varphi(x)] \in B$. While $V^{(\tilde{B})}$ must satisfy the Axiom of Subsets it need not satisfy the Axiom of Replacement, and even if this axiom is satisfied, the Axiom of Powers need not hold in $V^{(\tilde{B})}$. Therefore we have to look for suitable restrictions on $\tilde{B}$. An important though rather weak condition is given by the following.
