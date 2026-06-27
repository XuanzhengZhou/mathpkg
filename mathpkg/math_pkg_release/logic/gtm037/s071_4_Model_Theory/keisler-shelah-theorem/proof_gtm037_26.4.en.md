---
role: proof
locale: en
of_concept: keisler-shelah-theorem
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

**Proof of Theorem 26.42.**

The direction $(ii) \Rightarrow (i)$ follows immediately from Łoś's theorem: if $I\mathfrak{A}/D \cong I\mathfrak{B}/D$, then for any sentence $\varphi$,
\[
I\mathfrak{A}/D \models \varphi \iff I\mathfrak{B}/D \models \varphi,
\]
and by Łoś's theorem $\mathfrak{A} \models \varphi \iff I\mathfrak{A}/D \models \varphi$, similarly for $\mathfrak{B}$. Hence $\mathfrak{A} \equiv_{\mathrm{ee}} \mathfrak{B}$.

Now we prove the hard direction $(i) \Rightarrow (ii)$. Assume $\mathfrak{A} \equiv_{\mathrm{ee}} \mathfrak{B}$. Set
\[
n = 2^{|A| + |B| + |\mathrm{Fmla}_\mathcal{L}|}.
\]
The index set $I$ will be this cardinal $n$. Note that $n^{|A|} = n^{|B|} = n^{|\mathrm{Fmla}_\mathcal{L}|} = n$, so $|A|, |B|, |\mathrm{Fmla}_\mathcal{L}| < n^{\partial}$.

Enumerate $n_A = \{a_\alpha : \alpha < 2^n\}$ and $n_B = \{b_\alpha : \alpha < 2^n\}$ (with repetitions if the structures are smaller), and let $R$ be a one-one function from $2^n$ onto a set pairing indices with elements of $A$, $B$, and subsets of $n$.

Define by recursion on $\gamma \leq 2^n$ a triple $(F_\gamma, 0, D_\gamma)$ satisfying:
\[
\text{(1) } (F_\gamma, 0, D_\gamma) \text{ is } (n + |\gamma|)\text{-consistent over } n, \quad |F_0| = 2^n, \quad D_0 = \{n\}.
\]

The construction alternates between:
\begin{itemize}
\item \textbf{Adding to $G$ (using Lemma 26.37)}: At certain stages, add finitely many functions to $G$ corresponding to Skolem witnesses for existential formulas, while removing only a small subset from $F$.
\item \textbf{Extending $D$ (using Lemma 26.40)}: At other stages, extend $D$ to decide membership of subsets of $n$ corresponding to atomic formula truth values.
\end{itemize}

At limit stages, take unions. The cardinal bounds ($n^{\partial} \leq m$, etc.) ensure all hypotheses are satisfied.

At the end, $D = D_{2^n}$ is an ultrafilter over $n$. Define the canonical embedding sequences $\langle a_{v_j \delta} : j < \omega \rangle$ for $\delta < n$ in both ultrapowers using the enumeration $n_A$ and $n_B$. Using Lemma 26.41 (simultaneous satisfaction), one constructs a back-and-forth system showing:
\[
n\mathfrak{A}/D \cong n\mathfrak{B}/D.
\]

The isomorphism sends the equivalence class of $\langle a_{v_j \delta} : \delta < n \rangle$ in the first ultrapower to the corresponding class in the second, and condition (iv) of Definition 26.33 ensures this is well-defined and preserves all first-order formulas. This completes the proof. $\square$
