---
role: proof
locale: en
of_concept: yext-ext-natural-equivalence
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "9. Ext^n and n-Extensions"
---

# Proof of Natural Equivalence of $\operatorname{Yext}_A^n$ and $\operatorname{Ext}_A^n$

**Theorem 9.1.** There is a natural equivalence of set-valued bifunctors

$$\theta_n : \operatorname{Yext}_A^n(-, -) \stackrel{\sim}{\longrightarrow} \operatorname{Ext}_A^n(-, -), \qquad n = 1, 2, \ldots$$

Note that since $\operatorname{Ext}_A^n(A, B)$ carries a natural abelian group structure, the equivalence $\theta_n$, once established, introduces a natural abelian group structure into $\operatorname{Yext}_A^n(A, B)$.

*Proof.* We proceed by a method analogous to the one used in the proof of Theorem III.2.4 (the $n = 1$ case). We first choose a projective resolution

$$P : \cdots \longrightarrow P_n \xrightarrow{\partial_n} P_{n-1} \longrightarrow \cdots \longrightarrow P_0$$

of $A$. Proposition 5.8 applied to the functor $\operatorname{Hom}_A(-, B)$ yields the exact sequence

$$\operatorname{Hom}_A(P_{n-1}, B) \xrightarrow{i^*} \operatorname{Hom}_A(R_n, B) \xrightarrow{j^*} \operatorname{Ext}_A^n(A, B) \longrightarrow 0 \tag{9.4}$$

where $i : R_n \rightarrowtail P_{n-1}$ is the embedding of $R_n = \operatorname{im} \partial_n$ in $P_{n-1}$, and $j^*$ is the canonical projection.

**Definition of $\theta$.** Let an $n$-extension

$$E : 0 \longrightarrow B \longrightarrow E_n \longrightarrow E_{n-1} \longrightarrow \cdots \longrightarrow E_1 \longrightarrow A \longrightarrow 0$$

represent an element $[E] \in \operatorname{Yext}_A^n(A, B)$. By the Comparison Theorem, the projective resolution $P$ and the $n$-extension $E$ can be compared: the identity map $A \rightarrow A$ lifts to a chain map from $P$ (truncated) into the bottom part of $E$, yielding in particular a map $\varphi : R_n \rightarrow B$ via the factorization through kernels. Explicitly, we obtain a commutative diagram

\[
\begin{CD}
P_n @>\partial_n>> P_{n-1} @>>> \cdots @>>> P_0 @>>> A @>>> 0 \\
@VVV @VVV @. @VVV @| \\
E_n @>>> E_{n-1} @>>> \cdots @>>> E_1 @>>> A @>>> 0 \\
@AAA @. @. @. \\
0 @>>> B
\end{CD}
\]

The map $P_n \rightarrow E_n$ composed with $E_n \rightarrow B$ restricts to $R_n \rightarrow B$, giving $\varphi$. If another chain map is chosen, the resulting $\varphi$ differs by a map factoring through $P_{n-1}$, i.e., by a map in $\operatorname{im} i^*$, so $[\varphi] \in \operatorname{Ext}_A^n(A, B)$ is well-defined. Moreover, equivalent $n$-extensions yield the same $[\varphi]$, as one checks by composing the chain of comparisons. We set

$$\theta([E]) = [\varphi].$$

**Definition of $\tilde{\theta}$.** Let $\varphi : R_n \rightarrow B$ represent an element $[\varphi] \in \operatorname{Ext}_A^n(A, B)$. We associate with $\varphi$ the equivalence class of the $n$-extension $C_\varphi$ obtained via the push-out construction. Specifically, form the push-out of the pair $(i, \varphi)$:

\[
\begin{CD}
R_n @>i>> P_{n-1} \\
@V{\varphi}VV @VVV \\
B @>>> E_n
\end{CD}
\]

Then define the $n$-extension

$$C_\varphi : 0 \longrightarrow B \longrightarrow E_n \longrightarrow P_{n-2} \longrightarrow \cdots \longrightarrow P_0 \longrightarrow A \longrightarrow 0$$

where the map $E_n \rightarrow P_{n-2}$ is induced by $\partial_{n-1}$ (using the universal property of the push-out, since $\partial_{n-1} \circ i = 0$). If $\varphi$ is replaced by $\varphi' = \varphi + \psi \circ i$ for some $\psi : P_{n-1} \rightarrow B$, then a straightforward diagram chase shows that the resulting $n$-extension is equivalent to $C_\varphi$. Thus

$$\tilde{\theta}([\varphi]) = [C_\varphi]$$

is a well-defined map $\tilde{\theta} : \operatorname{Ext}_A^n(A, B) \rightarrow \operatorname{Yext}_A^n(A, B)$.

**The two maps are inverse.** Plainly $\theta \tilde{\theta} = 1$: starting with $\varphi$, constructing $C_\varphi$, and then using the comparison theorem to recover $\varphi$ yields the same $\varphi$ (up to equivalence). Conversely, the diagram

\[
\begin{CD}
P_n @>>> P_{n-1} @>>> P_{n-2} @>>> \cdots @>>> P_0 @>>> A \\
@VVV @VVV @| @| @| \\
E_n @>>> E_{n-1} @>>> E_{n-2} @>>> \cdots @>>> E_1 @>>> A
\end{CD}
\]

where the leftmost vertical map is defined by the push-out property of $E$ (for the $n$-extension obtained by comparing $P$ with $E$) shows that $\tilde{\theta} \theta = 1$ as well.

**Naturality.** It remains to prove that $\theta$ is a natural transformation. First let $\beta : B \rightarrow B'$ be given. The induced map $\beta_* : \operatorname{Yext}_A^n(A, B) \rightarrow \operatorname{Yext}_A^n(A, B')$ sends $[E]$ to $[E_\beta]$, where $E_\beta$ is obtained by composing the first map $B \rightarrow E_n$ with $\beta$. Then

$$\theta(\beta_*[E]) = \theta([E_\beta]) = [\beta \circ \varphi] = \beta_*[\varphi] = \beta_*(\theta[E]).$$

Now let $\alpha : A' \rightarrow A$ be given. We construct the pull-back $E^\alpha$ as follows: form the pull-back of $(\eta, \alpha)$ where $\eta : E_1 \rightarrow A$ is the last map in the $n$-extension $E$. Since the maps $P_0' \rightarrow P_0 \rightarrow E_1 \rightarrow A$ and $P_0' \rightarrow A' \rightarrow A$ coincide, we obtain a (unique) map $P_0' \rightarrow E_1^\alpha$ making the diagram commutative. There is, as usual, the extra argument establishing that $P_1' \rightarrow P_0' \rightarrow E_1^\alpha$ coincides with $P_1' \rightarrow E_2 \rightarrow E_1^\alpha$. Thus we obtain

$$\theta(\alpha^*[E]) = \theta([E^\alpha]) = [\varphi \circ \chi] = \alpha^*[\varphi] = \alpha^*(\theta[E]),$$

where $\chi : R_n' \rightarrow R_n$ is the map induced by the chain map $P' \rightarrow P$ between the chosen projective resolutions.

This completes the proof that $\theta$ is a natural equivalence. $\square$

---

**Remark.** The connecting homomorphisms of the long exact $\operatorname{Ext}$-sequences admit a description in terms of $n$-extensions:

- For the connecting homomorphism $\omega : \operatorname{Ext}_A^n(A, B'') \rightarrow \operatorname{Ext}_A^{n+1}(A, B')$ in the second variable: if $E$ represents $[\varphi] \in \operatorname{Ext}_A^n(A, B'')$, then the $(n+1)$-extension

  $$E' : 0 \rightarrow B' \rightarrow B \rightarrow E_n \rightarrow E_{n-1} \rightarrow \cdots \rightarrow E_1 \rightarrow A \rightarrow 0$$

  (obtained by splicing the short exact sequence $B' \rightarrowtail B \twoheadrightarrow B''$ with $E$) represents $\omega[\varphi] \in \operatorname{Ext}_A^{n+1}(A, B')$.

- For the connecting homomorphism in the first variable: if $E'$ represents $[\varphi] \in \operatorname{Ext}_A^n(A', B)$, then the $(n+1)$-extension obtained by composing $E'$ with $A' \rightarrowtail A \twoheadrightarrow A''$ at the right end — namely

  $$E'' : 0 \rightarrow B \rightarrow E_n \rightarrow \cdots \rightarrow E_1 \rightarrow A \rightarrow A'' \rightarrow 0$$

  — represents $(-1)^{n+1} \omega[\varphi] \in \operatorname{Ext}_A^{n+1}(A'', B)$, up to the sign $(-1)^{n+1}$.
