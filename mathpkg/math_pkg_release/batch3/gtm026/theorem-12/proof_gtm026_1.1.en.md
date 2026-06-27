---
role: proof
locale: en
of_concept: theorem-12
source_book: gtm026
source_chapter: "1"
source_section: "1.27"
---

As just mentioned above, the proof of 1.26 shows that $U$ creates limits and that $U$ creates quotients of congruences. By 1.22 (1) it suffices to prove that for an arbitrary set $S$, $U$ satisfies the solution set condition at $S$. Given an $(\Omega, E)$-algebra $(X, \delta)$ and a function $f:S \longrightarrow X$ let $A$ be the intersection of all $\Omega$-subalgebras of $(X, \delta)$ containing $f(S)$. It is obvious that $A$ is itself an $\Omega$-subalgebra. Moreover, if $\{p, q\} \in E$ is an $n$-ary equation then the naturality squares

(where $\bar{\delta}$ is the subalgebra structure on $A$ and $i:A \longrightarrow X$ is the inclusion map) prove that $(A, \bar{\delta})$ is an $(\Omega, E)$-algebra, since $i$ is a monomorphism. We clearly have a factorization

By the condition that $(\Omega, E)$ is bounded, $\bar{\delta}$ ranges over a small set once $A$ is fixed. To complete the proof, then, it is enough to show that there exists a cardinal number $\alpha$, depending only on $\Omega$ and $S$, such that the cardinality of $A$ is

The remainder of the proof assumes some familiarity with ordinal and cardinal arithmetic (see the primer on set theory at the end of this section), but we have tried to spell things out so that the inexperienced reader can still grasp the flavor of the proof. Let us mention that, for cardinals $\beta$ and $\gamma$, $\beta + \gamma$ is the cardinality of the disjoint union of the sets $\gamma$ and $\beta$ and, similarly, $\beta \times \gamma$ and $\beta^\gamma$ denote (again somewhat ambiguously) the cardinalities of the cartesian product $\beta \times \gamma$ and the set of all functions from $\gamma$ to $\beta$, respectively. By the axiom of choice, if $\beta$ is an infinite cardinal then $\beta = \beta \times \beta$. Recall that, if $\beta$ is an ordinal (in particular, if $\beta$ is a cardinal) then “$\gamma < \beta$” and “$\gamma \in \beta$” are the same statement and such $\gamma$ is itself an ordinal. If $(\gamma_i : i \in I)$ is a family in $\beta$ then $\text{Sup}(\gamma_i)$ is the least element of the set of upper bounds in $\beta$ of $(\gamma_i)$, this being the least element 0 of $\beta$ if $I$ is empty and being the ordinal $\beta$ in case no such upper bounds exist.

Let us turn to the proof. $\alpha$ is constructed as follows. Let $\alpha_1$ be any infinite cardinal $> \text{card}(S)$ and $> \text{card}(\Omega_n)$ for all $n$. This is possible because $(\Omega, E)$ is bounded. Let $\alpha_2$ be any infinite cardinal $> \text{every } n$ for which $\Omega_n$ is non-empty. This is possible, again because $(\Omega, E)$ is bounded. Define $\alpha = \alpha_1^{\alpha_2}$. We will show that $\text{card}(A) \leqslant \alpha$. An outline of our approach is as follows:

Step 1. We construct a transfinite tower $A_\beta$ of subsets of $X$, starting with $A_0

$\gamma_i$. Therefore $\beta(i) \leqslant \tilde{\beta}$ for all $i$ and $\bar{\alpha} = \text{Sup}(\beta(i)) \leqslant \tilde{\beta} < \alpha$. Therefore $\delta_\omega(a_i) \in A_{\bar{\alpha}} \subset A_\alpha$ as desired.

Step 3. card($A_\alpha$) $\leqslant \alpha$ as follows. We have card($A_0$) $\leqslant \text{card}(S) < \alpha_1 \leqslant \alpha$. Now let $0 < \beta < \alpha$ and assume that card($A_\gamma$) $\leqslant \alpha$ for all $\gamma < \beta$. Then card($\bigcup(A_\gamma : \gamma < \beta)$) $\leqslant \beta \times \alpha \leqslant \alpha \times \alpha = \alpha$. Therefore, for $\omega \in \Omega_n$,

$$\text{card}(\delta_\omega((\bigcup(A_\gamma : \gamma < \beta))^n)) \leqslant \text{card}((\bigcup(A_\gamma : \gamma < \beta))^n) \leqslant (\beta \times \alpha)^n$$
$$\leqslant (\alpha \times \alpha)^n = \alpha^n \leqslant \alpha$$

(the last statement was observed in step 2). Therefore,

$$\text{card}(A_\beta) \leqslant \alpha + \text{card}(\bigcup(\Omega_n \times \alpha : \Omega_n \neq \emptyset))$$
$$\leqslant \alpha + \text{card}(\bigcup(\alpha_1 \times \alpha : \Omega_n \neq \emptyset))$$
$$\leqslant \alpha + (\alpha_2 \times \alpha_1 \times \alpha) \leqslant \alpha + \alpha = \alpha.$$

By transfinite induction, card($A_\beta$) $\leqslant \alpha$ for all $\beta < \alpha$. Then card($A_\alpha$) = card($\bigcup(A_\beta : \beta < \alpha)$) $\leqslant \beta \times \

By the hypothesis on $W$ there exists a unique lift $\bar{h} : A_2 \longrightarrow A$ with $\bar{h}W = hV$; and, moreover, $\bar{h} = \text{coeq}(f, g)$ in $\mathcal{A}$. Given an $\mathcal{A}$-morphism $h' : A_2 \longrightarrow A'$, $h'U = h$ if and only if $h'UV = hV$ (as $V$ creates coequalizers of $V$-absolute pairs) if and only if $h'W = hV$. Since $h'W = hV$ has unique solution $h' = \bar{h}$, $h'U = h$ has unique solution $\bar{h}$ as desired.

2. Let $(\Delta, D)$ be a diagram in $\mathcal{A}$ and let $\psi_i : B \longrightarrow D_iU$ be a limit of $(\Delta, DU)$ in $\mathcal{B}$. We must show that there exists a unique lift $\bar{\psi}_i : A \longrightarrow D_i$ in $\mathcal{A}$ with $\bar{\psi}_iU = \psi_i$ and that moreover $(A, \bar{\psi})$ is a limit of $(\Delta, D)$ in $\mathcal{A}$. Applying $V$, and using the hypothesis that $V$ preserves limits we have that $\psi_iV : BV \longrightarrow D_iW$ is a limit of $(\Delta, DW)$ in $\mathcal{K}$. The remaining details are based on the same principles as the corresponding parts of the proof of (1).

The following result is a major theorem in universal algebra:

1.29 Sandwich Theorem. Assume given a commutative diagram of functors and assume that $V$ is algebraic and that $\mathcal{A}$ has coequalizers. Then the following statements are true:

1. $U$ has a left adjoint if and only if $W$ does.
2. If $W$ is algebraic, so is $U$.

Since $V$ has a left adjoint, if $U$ has a left adjoint then $W$ has a left adjoint by 2.2.30. In view

Here, $AU = (AW, \gamma: AWT \rightarrow AW)$. The regions (1) all commute because $\eta'$ is a natural transformation; (2) commutes, being one of the triangular identities (2.2.16); (3) commutes because $pU$ is a morphism in $\mathcal{B}$; $K\eta'.pW: (K, \xi) \rightarrow AU$ is a T-homomorphism if and only if the perimeter of the diagram commutes; and (4) commutes if and only if $(a.p)W = (b.p)W$. Therefore $a.p = b.p$ implies that $K\eta'.pW$ is a T-homomorphism. Conversely, if $K\eta'.pW$ is a T-homomorphism then at least $KT\eta'.(a.p)W = KT\eta'.(b.p)W$; but since $(KTF', KT\eta')$ is free over $KT$ with respect to $W$, $a.p = b.p$.

The rest is easy. Let $p: KF' \rightarrow A = \text{coeq}(a, b)$ in $\mathcal{A}$. Since $a.p = b.p$, $f = K\eta'.pW: (K, \xi) \rightarrow AU$ is a T-homomorphism. Let $A'$ in $\mathcal{A}$ be arbitrary and let $f': (K, \xi) \rightarrow A'U$ be any T-homomorphism. As $(KF', K\eta')$ is free over $K$ with respect to $W$, there exists unique $p': KF'$

$A'$ in $\mathcal{A}$ such that $K\eta'.p'W = f'$. Since $f' : (K, \xi) \longrightarrow A'U$ was assumed a T-homomorphism it follows that $a.p' = b.p'$ so that, since $p = \text{coeq}(a, b)$, there exists a unique $\psi : A \longrightarrow A'$ in $\mathcal{A}$ such that $p.\psi = p'$. The remaining details are clear.

In the context of 1.29, if $W$ and $V$ are algebraic then $U$ is just a homomorphism (as in 2.3.3) from $(\mathcal{A}, W)$ to $(\mathcal{B}, V)$; 1.29 then asserts that homomorphisms between algebraic categories are themselves algebraic (assuming the existence of coequalizers; theorems that assert $\mathcal{K}^T$ has colimits will appear later in section 7). It is pleasant to report that $\text{Set}^T$ is always small co-complete (7.10). For the immediate present let us offer a simple proof of
