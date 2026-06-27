---
role: proof
locale: en
of_concept: faiths-injective-direct-sum-theorem
source_book: gtm013
source_chapter: "7"
source_section: "25. Injective Modules and Noetherian Rings—The Faith–Walker Theorems"
---

(a) $\Rightarrow$ (c). This implication is immediate. (Also note that Exercise (25.4) yields its converse directly.)

(c) $\Rightarrow$ (b). Assume that (c) holds but that (b) does not. Then there is a strictly increasing sequence

$$I_1 \subset I_2 \subset \ldots$$

in $\mathcal{L}_R(E)$. The right annihilators of this sequence

$$r_E(I_1) \supset r_E(I_2) \supset \ldots$$

are strictly decreasing. Choose $x_n \in r_E(I_n) \setminus r_E(I_{n+1})$ and let

$$I = \bigcup_{n=1}^{\infty} I_n.$$

Then for each $a \in I$ there exists an $n > 0$ such that $ax_{n+k} = 0$ for all $k = 1, 2, \ldots$. Thus, the map

$$f: a \mapsto (ax_1, ax_2, \ldots) \quad (a \in I)$$

is an $R$-homomorphism $f: I \to E^{(\mathbb{N})}$. But now by the Injective Test Lemma there exists a

$$y = (y_1, \ldots, y_n, 0, \ldots) \in E^{(\mathbb{N})}$$

such that, for all $a \in I$

$$(ax_1, ax_2, \ldots) = f(a) = ay = (ay_1, \ldots, ay_n, 0, \ldots).$$

But this is contrary to our choice of $x_{n+1} \notin r_E(I_{n+2})$.

(b) $\Rightarrow$ (a). [The text of this portion of the proof is partially truncated in the source. The argument proceeds via the Injective Test Lemma: given a left ideal $I \leq R$ and an $R$-homomorphism $f: I \to E^{(A)}$, one uses the ACC on $E$-annihilator left ideals to find a maximal element $\ell_R(x_{A \setminus F_0})$, then shows that the image of $f$ is contained in a finite sub-sum, reducing to the injectivity of $E$.]
