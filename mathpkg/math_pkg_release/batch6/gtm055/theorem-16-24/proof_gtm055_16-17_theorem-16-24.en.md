---
role: proof
locale: en
of_concept: theorem-16-24
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

Proof. As was noted in the proof of Proposition 16.2 in a somewhat more general context, it is obvious that the natural embedding $j$ of $\mathcal{E}$ in $\mathcal{E}^*$ is a homeomorphism between $\mathcal{E}$ in its weak topology and $j(\mathcal{E})$ in the (relative) weak* topology (see also Problem B). If $\mathcal{E}$ is reflexive, so that $j$ maps $\mathcal{E}$ onto $\mathcal{E}^*$, then, since $j$ is an isometry, it must also map $\mathcal{E}_1$ onto $(\mathcal{E}^*)^1$, and the latter set is weak* compact by Alaoglu’s theorem (Th. 15.11). Hence $\mathcal{E}_1$ is compact in the weak topology on $\mathcal{E}$. Suppose, on the other hand, that $\mathcal{E}_1$ is weakly compact, and consider the space $\mathcal{E}_w$ consisting of $\mathcal{E}$ equipped with its weak topology. The set $\mathcal{E}_1$ is compact and absolutely convex and has polar $(\mathcal{E}^*)_1$. Hence by Lemma 16.21, a linear functional on $\mathcal{E}^*$ is bounded on $(\mathcal{E}^*)_1$ if and only if it is of the form $j(x)$ for some vector $x$ in $\mathcal{E}$. In other words, $j$ maps $\mathcal{E}$ onto $\mathcal{E}^*$.

Problems

A. (i) Let $\mathcal{E}_1, \ldots, \mathcal{E}_n$ be Banach spaces, and let $\mathcal{E} = \mathcal{E}_1 \oplus p \cdots \oplus p \mathcal{E}_n$ for some number $p, 1 < p < +\infty$ (Prob. 11T). Show that $\mathcal{E}$ is reflexive if and only if each $\mathcal{E

E. Let $\mathcal{E}$ be a reflexive Banach space and let $T$ be a bounded linear transformation of $\mathcal{E}$ into a normed space $\mathcal{F}$. Show that $T$ carries an arbitrary closed, bounded, convex subset of $\mathcal{E}$ onto a closed, bounded, convex subset of $\mathcal{F}$. (Hint: Recall Example 15D and the fact (Prob. 15L) that a closed convex set is also weakly closed. Use the Šmul’yan criterion.)

F. Let $\mathcal{E}$ and $\mathcal{F}$ be normed spaces, let $T$ be an element of $\mathcal{L}(\mathcal{E}, \mathcal{F})$, and let $j_{\mathcal{E}}$ and $j_{\mathcal{F}}$ denote the natural embeddings of $\mathcal{E}$ and $\mathcal{F}$, respectively, in their second duals. Show that commutativity holds in the diagram

$$\mathcal{E}^{**} \xrightarrow{T^{**}} \mathcal{F}^{**}$$

(Thus if $\mathcal{E}$ and $\mathcal{F}$ are reflexive, and if their natural embeddings are used to identify them with their respective second duals, then $T^{**}$ is identified with $T$.)

G. Let $\mathcal{M}$ be a subspace of a Banach space $\mathcal{E}$.

(i) Verify that the mapping $\delta$ described in Proposition 16.12 is given by the composition $\alpha^* \circ \beta$ as shown in the diagram

$$\mathcal{E}^{**} \xrightarrow{\beta} (\mathcal{M}^a)^* \xrightarrow{\alpha^*} (\mathcal{E}/\mathcal{M})^{**}$$

$$\mathcal{M}^a \xleftarrow{\alpha} (\mathcal{E}/\mathcal{M})^*$$

and complete the proof of the proposition.

(ii) Let $i$ and $\pi$ denote, respectively, the inclusion mapping of $\mathcal{M}$ into $\mathcal{E}$ and the natural projection of $\mathcal{E}$ onto $\mathcal{E}/\mathcal{M}$. Show that the mapping $\delta$ of Proposition 16.12 also coincides

In the language of homological algebra Problem G says that

$$\begin{align*}
(0) &\longrightarrow M^* \longrightarrow \mathcal{E}^* \longrightarrow \pi^* (\mathcal{E} / M)^* \longrightarrow (0)
\end{align*}$$

is an exact sequence. Likewise, Problem F says commutativity holds in the diagram

$$\begin{align*}
(0) &\longrightarrow M^* \longrightarrow \mathcal{E}^* \longrightarrow \pi^* (\mathcal{E} / M)^* \longrightarrow (0)
\end{align*}$$

where the $j$'s denote the appropriate natural embeddings. Thus the calculations involved in Problem H all reduce to routine diagram chases. Indeed, we are looking at just one more version of the protean “five lemma” [47; p. 14]; see [67].

I. Let $\mathcal{E}$ and $\mathcal{F}$ be normed spaces and let $T$ be an element of $\mathcal{L}(\mathcal{E}, \mathcal{F})$ having kernel $\mathcal{K} = \mathcal{K}(T)$ and range $\mathcal{R} = \mathcal{R}(T)$. Show that the kernel of $T^*$ is $\mathcal{R}^a$ and that $\mathcal{K} = a(\mathcal{R}(T^*))$. Show also that $T^*$ is continuous when $\mathcal{F}^*$ and $\mathcal{E}^*$ are both equipped with their weak* topologies.

J. Let $\mathcal{E}$ and $\mathcal{F}$ be Banach spaces, and let $T$ be a bounded linear transformation of $\mathcal{E}$ into $\mathcal{F}$ such that $\mathcal{R} = \mathcal{R}(T)$ is closed in $\mathcal{F}$. Prove that the range of $T^*$ coincides with $\mathcal{K}^a$ where $\mathcal{K} = \mathcal{K}(T)$. Thus if $T$ has closed range, then the range of $T^*$ is weak* closed (and therefore norm closed as well). (Hint: If $\hat{T}$ denotes the mapping of $\mathcal{E} / \mathcal{K}$ onto $\mathcal

M. Let $\mathcal{E}$ be a normed space and let $j_{\mathcal{E}}$ and $j_{\mathcal{E}^*}$ denote, respectively, the natural embeddings of $\mathcal{E}$ in $\mathcal{E}^*$ and $\mathcal{E}^*$ in $\mathcal{E}^{***}$. Verify that $(j_{\mathcal{E}})^*$ is a left inverse of $j_{\mathcal{E}^*}$, and use this fact to show that $(j_{\mathcal{E}}(\mathcal{E}))^a$ and $j_{\mathcal{E}^*}(\mathcal{E}^*)$ are complementary subspaces in $\mathcal{E}^{***}$. (Hint: See Problem 13E.)

N. Show that a Banach space $\mathcal{E}$ is reflexive if and only if $\mathcal{E}^*$ is reflexive. (Hint: This fact is an immediate consequence of the preceding problem, but it may also be derived from the Šmul’yan criterion.)

O. Let $(\varphi)$ denote the vector space consisting of all those complex sequences that are eventually zero, and let $(\delta)$ denote the vector space of all complex sequences. Show that $\langle (\varphi), (\delta) \rangle$ is a dual pair with respect to the bilinear functional defined on $(\varphi) \div (\delta)$ by

$$\langle x, y \rangle = \sum_{n=0}^{\infty} \xi_n \eta_n,$$

where $x = \{\xi_n\}_{n=0}^{\infty}$ and $y = \{\eta_n\}_{n=0}^{\infty}$. Show also that if $\{x_m\}_{m=1}^{\infty}$ is a sequence in $(\varphi)$ and if $x_m = \{\xi_n\}_{n=0}^{\infty}$ for each index $m$, then the sequence $\{x_m\}$ is weakly convergent in $(\varphi)$ if and only if the sequence $\{\xi_n^{(m)}\}_{m=1}^{\infty}$ is convergent in $\mathbb{C}$ for every nonnegative integer $n$ and there exists a fixed nonnegative integer $N$ such that $\xi_n^{(m)} = 0$ for all $n \geq N$ and all sufficiently large $m

(iii) Show, dually, that if $M$ is an arbitrary linear manifold in $\mathcal{F}$, and if $aM(=0M)$ is the preannihilator of $M$ in $\mathcal{E}$, then $\langle \mathcal{E}/aM, M \rangle$ is a dual pair with respect to the bilinear functional $\langle x + aM, y \rangle = \langle x, y \rangle$, $x \in \mathcal{E}$, $y \in M$. Verify also that the topology induced on $\mathcal{E}/aM$ by $M$ coincides with the quotient topology on $\mathcal{E}/aM$ obtained from the weak topology on $\mathcal{E}$ when and only when $M$ is closed in the topology induced on $\mathcal{F}$ by $\mathcal{E}$. (Hint: According to (ii) the quotient topology on $\mathcal{E}/aM$ is induced by $(aM)^a$.)

Q. Let $\langle \mathcal{E}, \mathcal{F} \rangle$ and $\langle \mathcal{E}', \mathcal{F}' \rangle$ be dual pairs, and let $T$ be a linear transformation of $\mathcal{E}$ into $\mathcal{E}'$. Show that there exists a mapping $T^*: \mathcal{F}' \rightarrow \mathcal{F}$ satisfying the condition

$$\langle Tx, y' \rangle = \langle x, T^*y' \rangle, \quad x \in \mathcal{E}, \quad y' \in \mathcal{F}'$$

if and only if $T$ is weakly continuous, i.e., continuous when $\mathcal{E}$ and $\mathcal{E}'$ are given the topologies induced by $\mathcal{F}$ and $\mathcal{F}'$, respectively. Show also that if $T$ is weakly continuous then $T^*$ is a uniquely determined linear transformation. (The mapping $T^*$ is called the adjoint of $T$.) In the remainder of this problem we suppose $T$ to be weakly continuous.

(i) Verify that the adjoint $T^*$ is in turn weakly continuous with respect to the reversed dual pairs $\langle \mathcal{

uniform convergence on the collection of all those absolutely convex subsets of $\mathcal{F}$ that are compact in the topology induced by $\mathcal{E}$. This topology is called the Mackey topology on $\mathcal{E}$ with respect to the dual pair $\langle \mathcal{E}, \mathcal{F} \rangle$. Verify that if $\mathcal{E}$ is a separated locally convex space, then the Mackey topology on $\mathcal{E}$ with respect to the dual pair $\langle \mathcal{E}, \mathcal{E}^* \rangle$ agrees with the Mackey topology as defined in Example 15K.

T. (i) A subset $B$ of a separated locally convex space $\mathcal{E}$ is called a barrel in $\mathcal{E}$ if $B$ is closed, absolutely convex, and absorbing. Verify that a subset $B$ of $\mathcal{E}$ is a barrel if and only if there exists a weak* bounded subset $A$ of $\mathcal{E}^*$ such that $B = 0A$ in the dual pair $\langle \mathcal{E}, \mathcal{E}^* \rangle$. (Hint: If $B$ is a barrel, then $B = 0(B^0)$; use Proposition 16.17.)

(ii) A separated locally convex space $\mathcal{E}$ is said to be barreled if every barrel in $\mathcal{E}$ is a neighborhood of 0 in $\mathcal{E}$. Show that $\mathcal{E}$ is barreled if and only if every subset of $\mathcal{E}^*$ that is weak* bounded is also equicontinuous on $\mathcal{E}$. Conclude that the given locally convex topology on a barreled space $\mathcal{E}$ coincides with both the Mackey topology and the strong topology (in the dual pair $\langle \mathcal{E}, \mathcal{E}^* \rangle$). (Hint: Recall Example N.)

U. Verify that every Frechét space is barreled. (Hint: If $B$ is a barrel in a Frechét space $\mathcal{E}$, then $\{nB\}_{n=1}^{\infty}$ is a countable closed covering of the complete metric space $\

to 0 in the given topology on $\mathcal{E}$ but is unbounded with respect to the Mackey topology, a contradiction.)

X. Let $\mathcal{E}$ be a separated locally convex space.

(i) Verify that the collection of all compact subsets of $\mathcal{E}$ is admissible, and hence that the topology $\mathcal{T}$ of uniform convergence on compact subsets of $\mathcal{E}$ is an admissible polar topology on $\mathcal{E}^*$. Verify also that if $\{f_\lambda\}_{\lambda \in \Lambda}$ is a net in $\mathcal{E}^*$ and if there exists a neighborhood $V$ of 0 in $\mathcal{E}$ such that $f_\lambda \in V^0$, $\lambda \in \Lambda$, then $\{f_\lambda\}$ converges to a (continuous linear) functional $f$ in the topology $\mathcal{T}$ if and only if $\{f_\lambda\}$ converges to $f$ in the weak* topology, that is, pointwise. Conclude that $\mathcal{T}$ induces the same topology on equicontinuous subsets of $\mathcal{E}^*$ as does the weak* topology. (Hint: If $\{f_\lambda\}$ converges pointwise to $f$, then $f \in V^0$. Hence, for a given positive $\varepsilon$, $f$ and $f_\lambda$ differ by no more than $|f_\lambda(x) - f(x)| + 2\varepsilon$ on the set $x + \varepsilon V$, and sets of this form cover $\mathcal{E}$. Recall Example N.)

(ii) Let $U$ and $V$ be neighborhoods of 0 in $\mathcal{E}$ such that $U \subset V$, let $W'$ be a subset of $U^0$ that is open in the relative weak* topology on $U^0$, and suppose given a subset $M$ of $\mathcal{E}$ such that $(M \cup V)^0 \subset W'$. Show that there exists a finite subset $D$ of $V$ such that $(D \cup M)^0 \cap (U^0 \setminus W') = \emptyset$, and hence such that $(D \cup M

17 Banach spaces and integration theory

In this chapter we introduce some topics that combine in different, but not unrelated, ways the theory of normed spaces discussed thus far in Part II and the theories of integration discussed in Chapters 6–10 of Part I. Our first observation is that there are natural and important generalizations of the $(\ell_p)$ spaces obtained by employing Lebesgue integration in place of summation.
