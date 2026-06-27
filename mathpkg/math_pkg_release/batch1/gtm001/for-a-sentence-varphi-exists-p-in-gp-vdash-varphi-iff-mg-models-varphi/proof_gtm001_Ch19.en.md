---
role: proof
locale: en
of_concept: for-a-sentence-varphi-exists-p-in-gp-vdash-varphi-iff-mg-models-varphi
source_book: gtm001
source_chapter: "19"
source_section: ""
---

First we prove this for a limited sentence $\varphi$ by transfinite induction on Ord($\varphi$) then we prove it for an unlimited sentence $\varphi$ by induction on the number of logical symbols in $\varphi$. Though there are many cases, almost all of the cases can be proved by a straightforward check of the definition and the induction hypothesis. Therefore we treat only the case where $\varphi$ is $\neg \psi$ or $t \in G$.

$(\exists p \in G)(p \Vdash \varphi) \leftrightarrow (\exists p \in G)(\forall q \leq p)[\neg(q \Vdash \psi)]$
$\leftrightarrow \neg(\forall p \in G)(\exists q \leq p)[q \Vdash \psi].$
$\leftrightarrow \neg(\exists q \in G)[q \Vdash \psi]$.

(Corollary of Lemma 19.6)
$\leftrightarrow \neg M[G] \models \psi.$
$\leftrightarrow M[G] \models \neg \psi.$

$(\exists p \in G)[p \Vdash t \in G] \leftrightarrow (\exists p \in G)(\exists q \geq p)[p \Vdash \forall^\alpha x_i(x_i \in t \leftrightarrow x_i \in \mathbf{q})]$
$\rightarrow (\exists q \in G)[M[G] \models t = \mathbf{q}$
$\rightarrow M[G] \models t \in \mathbf{G}$

$M[G] \models t \in \mathbf{G} \rightarrow (\exists q \in G)[M[G] \models t = \mathbf{q}]$
$\rightarrow (\exists q \in G)[M[G] \models \forall^\alpha x_i(x_i \in t \leftrightarrow x_i \in \mathbf{q})]$
$\rightarrow (\exists q \in G)(\exists p \

of $M[G]$. Let $k = \{ \langle p, s \rangle | s \in T_\alpha \wedge p \models s \in t \wedge \varphi(s, t_1, \ldots, t_n) \}$. Then $k \in M$.

Let

$$t' = \hat{x}_1^\alpha (\exists \beta p \in G) [\langle p, x_i \rangle \in \mathbf{k}].$$

Then

$$D^G(t') = \{ D^G(s) | (\exists p \in G) [s \in T_\alpha \wedge p \models s \in t \wedge \varphi(s, t_1, \ldots, t_n) ]$$

$$= \{ D^G(s) | s \in T_\alpha \wedge D^G(s) \in D^G(t) \wedge$$

$$M[G] \models \varphi(D^G(s), D^G(t_1), \ldots, D^G(t_n))$$

$$= \{ D^G(s) \in D^G(t) | M[G] \models \varphi(D^G(s), D^G(t_1), \ldots, D^G(t_n)) \}.$$

(4) Axiom of Infinity. This is obvious since $\omega$ is in $T$.

(5) Axiom of Foundation. This is obvious since $M[G]$ is a transitive model.

(6) Axiom of Extensionality. This is obvious since $M[G]$ is a transitive model.

(7) Axiom Schema of Replacement. Let $a \in M[G]$. We would like to show from the assumption $M[G] \models (\forall x)(\exists y)\varphi(x, y)$, that

$$(\exists b \in M[G]) (M[G] \models (\forall x \in a)(\exists y \in b)\psi(x, y)).$$

Let $a = D^G(t)$ and $t \in T_\alpha$. Since the Axiom Schema of Replacement holds for $M$, there exists a $\beta \in M$ such that

$$(\forall t' \in

Since $\{B(t_1)|t_1 \in T\} \subseteq \mathcal{P}(P \times T_\alpha)$, there exists a $\beta \in M$ such that

$$(\forall t_1 \in T)(\exists t_2 \in T_\beta)[B(t_1) = B(t_2)]$$

It is now obvious that we can take $s$ to be $\hat{x}_0^\beta(x_0 \in x_0 \vee x_0 \notin x_0)$.

(9) Axiom of Choice. Here we assume that $M$ satisfies the Axiom of Choice.

Since $M[G]$ satisfies the axioms of ZF with the language containing the predicate $M$, we can carry out every construction of $T, D^G(t), p \vdash t$ for $M$ and $G$ in $M[G]$.

Since $M$ satisfies the Axiom of Choice, we can well order $T_\alpha$ for every $\alpha \in M$. Therefore we can well order $\{D^G(t)|t \in T_\alpha\}$ in $M[G]$. It is then obvious that the Axiom of Choice holds in $M[G]$.

Remark. There are numerous applications of forcing to independence problems in set theory. Here we treat only the first application of Cohen’s original paper, the independence of $V = L$ from ZFC + GCH.

Let $M$ be a countable transitive model of ZF + $V = L$. In $M$, we define $\mathcal{P} = \langle P, \leq \rangle$ as follows (Every notion should be relativized to $M$):

$$P \triangleq \{ \langle p, q \rangle | p \subseteq \omega \wedge q \subseteq \omega \wedge \bar{p} < \omega \wedge \bar{q} < \omega \wedge p \cap q = 0 \}.$$

$$\langle p_1, q_1 \rangle \subseteq \langle p_2, q_2 \rangle \stackrel{\triangle}{=} p_2 \subseteq p_1 \wedge q_

GCH. If we use Theorem 15.44(2), $a \subseteq \omega \wedge V = L_a \rightarrow \text{GCH}$, then we get the result immediately as follows: Obviously $M[G] \models a \subseteq \omega \wedge V = L_a$. Therefore $M[G] \models \text{GCH}$. But we would like to prove this without using the Theorem 15.44(2).

First we will show that the notion of cardinality is the same in $M$ and $M[G]$: Since $M \subseteq M[G]$, an ordinal $\alpha$ is a cardinal in $M$ if $\alpha$ is a cardinal in $M[G]$. To show that $\alpha$ is a cardinal in $M[G]$ if $\alpha$ is so in $M$, let $\beta < \alpha$ and $M[G] \models f: \beta \rightarrow \alpha$, where $f \in T$. Then there exists a $p_0 \in G$ such that

$$p_0 \Vdash (\forall x_0)(\forall x_1)(\forall x_2)(x_1 = f(x_0) \wedge x_2 = f(x_0) \rightarrow x_1 = x_2),$$

where $x_1 = f(x_0)$ is an abbreviation of some formula. From this we have,

$$p_0 \Vdash \gamma_1 = f(\gamma_0) \wedge p_0 \Vdash \gamma_2 = f(\gamma_0) \rightarrow \gamma_1 = \gamma_2.$$

Suppose $\alpha_1 < \alpha$. Then there exists a $\beta_1 < \beta$ such that $M[G] \models \alpha_1 = f(\beta_1)$. Therefore we have

$$(\exists p \in G)(p \leq p_0 \wedge p \Vdash \alpha_1 = f(\beta_1)).$$

Therefore

$$\bar{\alpha} \leq \overline{\{ \langle p, \beta_1 \rangle | p \leq p_0 \wedge (\exists

Bibliography

Bar-Hillel, Y. (Ed.). *Essays on the Foundations of Mathematics*. Jerusalem: Magnes Press, 1966.

Benacerraf, P. and Putnam, H. *Philosophy of Mathematics Selected Readings*. Englewood Cliffs: Prentice-Hall Inc., 1964.

Bernays, P. and Fraenkel, A. A. *Axiomatic Set Theory*. Amsterdam: North-Holland, 1958.

Bernays, P. *Axiomatic Set Theory*. Amsterdam: North-Holland 1968.

Cantor, G. Beiträge zur Begründung der transfiniten Mengenlehre (Erster Artikel) *Math. Ann.* 46, 481–512 (1895); (Zweiter Artikel) *Math. Ann.* 49, 207–246 (1897).

Cantor, G. *Contributions to the Founding of the Theory of Transfinite Numbers*. English translation by Philip E. B. Jourdain. Reprinted by Dover Publications Inc., New York, 1915.

Church, A. *Introduction to Mathematical Logic*. Princeton: Princeton University Press, 1956.

Cohen, P. J. The independency of the continuum hypothesis. *Proc. Nat. Acad. Sci. U.S.* 50, 1143–1148 (1963).

Cohen, P. J. *Set Theory and the Continuum Hypothesis*. Amsterdam: W. A. Benjamin Inc., 1966.

Devlin, K. J. *The Axiom of Constructibility: A Guide for the Mathematician*. Lecture Notes in Mathematics, Vol. 617, New York: Springer-Verlag, 1977.

Fraenkel, A. A. and Bar-Hillel, Y. *Foundations of Set Theory*. Amsterdam: North-Holland, 1958.

Fraenkel, A. A. *Abstract Set Theory*. Amsterdam: North-Holland, 1976.

Gödel, K. *The Consistency of

Problem List

(1) Let $A$ be an infinite set. Prove that the cardinality of the set of all automorphisms of $A$, i.e., one-to-one mappings of $A$ onto $A$, is $\overline{2^A}$. (Hint: Divide $A$ into $A_1, A_2, A_3$ so that $\bar{A}_1 = \bar{A}_2 = \bar{A}_3 = \bar{A}$. For each $B \subseteq A_2$ find an automorphism $\pi$ for which $\pi^* (A_1 \cup B) = A_3 \cup (A_2 - B)$.

(2) Let $A$ be a countable infinite set and $<_1$ be an order relation on $A$ (Definition 6.19). Let $R_0$ be the set of rationals in the interval $(0, 1)$. Find a one-to-one order-preserving map $\tau$ from $A$ into $R_0$. (Hint: Let $A = \{a_0, a_1, \ldots\}$. Define $\tau(a_i)$ assuming that $\tau(a_0), \ldots, \tau(a_{i-1})$ have been defined.

(3) Let $\dot{A}_1$ and $A_2$ be infinite countable sets. Let $<_1$ Or $A_1, <_2$ Or $A_2$, and both structures satisfy

(a) $(\forall x)(\exists y)[y < x]$
(b) $(\forall x)(\exists y)[x < y]$
(c) $(\forall x)(\forall y)(\exists z)[x < y \rightarrow x < z < y]$.

Prove: $(\exists f)f \text{ Isom}_{<_1, <_2}(A_1, A_2)$. (Hint: Let $A_1 = \{a_0, a_1, \ldots\}$ and $A_2 = \{b_0, b_1, \ldots\}$. Define $\tau_1 \text{ Isom}_{<_1, <_2}(A_1, A_2)$ and $\

(5) Let $\mathcal{R}$ be the set of all real numbers and let $f$ be a mapping from $\aleph_1$ into $\mathcal{R}$ that is monotone increasing. Prove: $(\exists \alpha < \aleph_1)(\forall \beta > \alpha)[f(\beta) = f(\alpha)]$. (Hint: $\mathcal{R}$ is separable and hence $\text{cf}(f''\aleph_1) = \aleph_0$).

(6) Let $\mathcal{R}$ be the set of all real numbers and let $f$ be a continuous mapping from $\aleph_1$ into $\mathcal{R}$. Prove: $(\exists \alpha < \aleph_1)(\forall \beta > \alpha)[f(\beta) = f(\alpha)]$.

(7) Let $\mathcal{R}$ be the set of all real numbers and let $f: \aleph_1 \xrightarrow{1-1} \mathcal{R}$. $\forall \alpha, \beta < \aleph_1$ define $\alpha \leq \beta$ iff $\alpha < \beta \wedge f(\alpha) < f(\beta)$. Prove the following:

(a) The relation $\ll$ is a well-founded partial ordering on $\aleph_1$.

(b) If $A \subseteq \aleph_1$, and $(\forall x, y \in A)[x \ll y \vee x = y \vee y \ll x]$ then $A$ is countable.

(c) If $A \subseteq \aleph_1$ and $(\forall x, y \in A)[x = y \vee \neg[x \ll y \vee y \ll x]]$ then $A$ is countable.

(8) Let $A \subseteq [0, 1]$. Then $\forall x \in [0, 1], x$ is a $\kappa$-accumulation point of $A$ iff $\forall N(x)[\overline{N(x) \cap A} \geq \kappa]$.

(Here $N(x)$ is a neighborhood of $x$ in the usual topology on $[0, 1]$.)

(a) Prove that $\{x \in [0,

(16) Find a model $M[G]$ of ZF + AC + $V \neq L$ such that $M$ is a model of ZF + $V = L$ and $G$ is $L$-finite.

(17) If $\vdash^1 \lceil \varphi \rceil \triangleleft (\exists \mathcal{P}) [\mathcal{P} \models \lceil \varphi \rceil]$ and $\vdash^2 \lceil \varphi \rceil \triangleleft (\forall \mathcal{P}) [\mathcal{P} \models \lceil \varphi \rceil)$ what logical rules do $\vdash^1$ and $\vdash^2$ satisfy.

(18) A sentence is called arithmetical if every quantifier in it is restricted to $\omega$. Let $\varphi$ be an arithmetic sentence and let $F$“$\alpha_0$ be a model of ZF. Prove

$$\varphi \leftrightarrow F$$“$\alpha_0 \models \varphi$.$$

(19) A sentence is called a $\mathcal{P}(\omega)$-sentence if every quantifier in it is restricted to $\mathcal{P}(\omega)$. Assuming the existence of the minimal model $M_0$ find a $\mathcal{P}(\omega)$-sentence $\varphi$ such that

$$L \models \varphi \leftrightarrow M_0 \models \varphi$$

is false.

(20) In a forcing model $M$ of $V \neq L$, find $a \subseteq \omega$ such that

(a) $L_a \neq M$,

(b) $a$ and $\omega - a$ are $L$-finite.

Appendix

Let $M$, $SM$, and Consis(ZF) be statements that assert respectively:

(1) There exists a set that is a model of ZF.

(2) There exists a set that is a standard model of ZF.

(3) ZF is consistent.

Furthermore, let Consis(ZF) be so chosen that it is absolute w.r.t. every standard transitive model of ZF.

Theorem. $\neg \vdash_{ZF} M \rightarrow SM$.

Suppose

(1) $\vdash_{ZF} M \rightarrow SM$.

It is known that

(2) $\vdash_{ZF} M \leftrightarrow \text{Consis}(ZF)$.

Consequently, from (1) and (2)

(3) $\text{Consis}(ZF) \vdash_{ZF} SM$.

There exists a minimal standard transitive model of ZF, $M_0$. Clearly

(4) $M_0 \models \text{Consis}(ZF)$

Then relativizing. (3) to $M_0$, using the fact that Consis(ZF) is absolute w.r.t. $M_0$, we have

$M_0 \models SM$.

This is a contradiction. $\square$

Index of Symbols

AC, v
GCH, v
AH, vi
GB, 3
ZF, 3
∈, 3
a₀, a₁, ..., 4
x₀, x₁, ..., 4
¬, 4
∨, ∧, 4
→, ↔, 4
∀, ∃, 4
a, b, c, 4
x, y, z, 4
φ, ψ, η, 5
wff(s), 3, 5
⊢, ⊢_{LA}, 6
a = b, 7
{x|φ(x)}, 11
φ*, 12
A, B, C, ..., 13
A = B, 13
M(A), Pr(A), 13
Ru, 14
(∀ x₁, ..., xₙ)φ(x₁, ..., xₙ), 14
(∃ x₁, ..., xₙ)φ(x₁, ..., xₙ), 14
(∀ x₁, ..., xₙ ∈ A)φ(x₁, ..., xₙ), 14
(∃ x₁, ..., xₙ ∈ A)φ(x₁, ..., xₙ), 14
a₀, ..., aₙ ∈ A, 14
{τ(x₁, ..., xₙ)|φ(x₁, ..., xₙ)}, 14
{a, b}, {a}, 15
〈a, b〉, 15
{a₁, ..., aₙ}, 16
〈a₁, ..., aₙ〉, 16
∪(A), 16
A ∪ B, A ∩ B, 16
A ⊆ B, A ⊂ B, 17
P(a), 17
A − B, 20
{x ∈ a|φ(x)}, 20
0, 20
V, 21
A × B, 23
Aᵃ, A⁻

$$\{A'x | x \in B\}, 27$$
$$\bigcup_{x \in B} A'x, 27$$
$$A \mathcal{F}_n B, 27$$
$$A \mathcal{F}_m_2 B, 27$$
$$F: A \rightarrow B, 27$$
$$F: A \xrightarrow{1-1} B, 27$$
$$F: A \xrightarrow{1-1} B, 27$$
$$[A, R], 29$$
$$a R b, 29$$
$$R \text{ Or } A, 29$$
$$R \text{ Po } A, 29$$
$$R \text{ Fr } A, 30$$
$$E, 30$$
$$R \text{ Wfr } A, 30$$
$$R \text{ We } A, 30$$
$$R \text{ Wfwe } A, 30$$
$$H \text{ Isom}_{R_1, R_2}(A_1, A_2), 32$$
$$I, 33$$
$$\text{Tr}(A), 35$$
$$\text{Ord}(A), 36$$
$$\text{On}, 38$$
$$\alpha, \beta, \gamma, \ldots, 38$$
$$\varphi(\alpha), 39$$
$$(\forall \alpha)\varphi(\alpha), 39$$
$$(\exists \alpha)\varphi(\alpha), 39$$
$$\alpha < \beta, 39$$
$$\alpha \leq \beta, 39$$
$$\max(\alpha, \beta), 39$$
$$\alpha + 1, 41$$
$$K_1, K_2, 42$$
$$\omega, 42$$
$$i, j, k, \ldots, m, n, 42$$
$$\varphi(i), 42$$
$$(\forall i)\varphi(i), 42$$
$$(\exists i)\varphi(i), 42$$
$$\cap

$C' \alpha, C'_a \alpha, 167$
$A^\circ, 186$
$\langle A, F_x \rangle_{x \in I}, 186$
$\hat{\pi}, 186$
$F'x \simeq G'x, 187$
$\mathfrak{A}^\xi, 187$
$\langle I, \leq \rangle, 189$
$\lim_{\rightarrow} \Pi, 190$
$\langle \eta_i, \pi_{ij} \rangle_{i \leq j}, 190$
$[i, \alpha], 190$
$M / \equiv, 190$
$\pi_{i \infty}, 190$
$\alpha, 191$
$\max(\alpha), 191$
$\mathcal{P}_<, 191$
$\mathcal{L}, 194$
$g(\exists^\alpha), 194, 218$
$g(\hat{\alpha}), 194, 218$
$g(s), 194, 218$
$T_\alpha, T, 194, 219$
$E(\varphi), 194, 221$
$\Gamma s^7, 195$
$D(\varphi), 196$
$L_\alpha, L, 196$
$L \models \varphi, 196$
$\check{\alpha}, 199$
$\diamond (\kappa), 200$
$\langle \delta, \alpha, P \rangle, 202$
$S, 205$
$2^{\lambda}, 205$
$I, 207$
$A \prec B, 209$
$\Sigma_1, 212$
$M_0, 215$
$M_0[a], 217$
$M[G], 217, 220$
$\mathcal{L}(M, \mathbf{G}), 218$
$g(\mathbf{k}), g(\mathbf{G}), g(\

Index

A

absolute formula, 121
absolute formula in wider sense, 126
absolute term, 127
absoluteness, 121–142
Abstraction, Axiom of, 10, 18
acceptable map, 202
acceptable triple, 202
addition, cardinal, 95
addition, ordinal, 56
Aleph Hypothesis, vi
algebra, 186
algebra, class contained in, 186
algebra, intersection, 186
algebra, monomorphism of, 187
algebra, universe of, 186
almost universal class, 145
$\mathfrak{A}$-map, medium, 187
$\mathfrak{A}$-map, strong, 187
arithmetic, ordinal, 56–72
auxiliary symbols, 4
Axiom of Abstraction, 10, 18
Axiom of Choice, v, 2, 82–99
Axiom of Constructibility, vi, 162
Axiom of Extensionality, 8, 132
Axiom of Foundation, 20
Axiom of Infinity, 43, 133
Axiom of Pairing, 15, 132
Axiom of Powers, 17, 132
Axiom of Regularity, 20, 133
Axiom of Unions, 16, 132
Axiom Schema of Replacement, 19, 133
Axiom Schema of Separation, 18
axioms, logical, 5–6, 114

B

Begriffsschrift, 2
Benacerraf, Paul, 2
Bernays, Paul (1888–1977), 3
Bernstein, Felix (1878–1956), 86
bound variable, 4
bounded formula, 212
Burali-Forti, Cesari (

character of cofinality, 102
Choice, Axiom of, v, 2, 82–99
class 3, 10–22
class, almost universal, 145
class, constructible, 159
class, converse of, 23
class, domain of, 24
class equality, 13
class, image of, 24
class, infimum of, 45
class, infimum above an ordinal, 45
class intersection, 16, 44, 48
class, $M$-constructible, 150
class of cardinal numbers, 85
class of infinite cardinals, 90
class of limit ordinals, 42
class of ordinal numbers, 38
class of sets, 21
class, one-to-one, 24
class, ordinal, 36
class, proper, 3, 14
class, range of, 24
class, Russell’s, 14
class, single-valued, 24
class, supremum of, 45
class, supremum below an ordinal, 45
class symbol, 10
class, transitive, 35
class union, 16, 48
closed set in ordinal, 200
cofinality, 100–110
cofinality, character of, 102
Cohen, Paul, v, vi, 2, 3, 34, 97, 217
collapsing map, 189
collapsing property, 189
complement, relative, 20
composite functions, 24
conjunction, 4
constant term, 194, 218
Constructibility, Axiom of, vi, 162
constructible class, 159
constructible set, 158
constructible set, order of, 160
Continuum Hypothesis, 2, 105
converse of class, 23
converse of class, second, 143
con

function composition, 24
function, one-to-one, 24, 28
function, ordinal, 49–50
function, strictly monotone ordinal, 49–50
fundamental operations, 144

G

Generalized Continuum Hypothesis (GCH), v, 2, 105
generated subalgebra, 186
generic set, 218
Gödel–Bernays set theory (GB), 3
Gödel, Kurt (1906–1978), v, vi, 2, 3, 185, 215
Gödel’s model, 153–184

H

van Heijenoort, Jean, 2, 10
Hilbert, David (1862–1943), 88

I

image of a class, 24
implication, 4
inaccessible cardinal, 104
inaccessible cardinal, weakly, 104
induced mapping, 186
induction, finite, 43
induction, transfinite, 39
inference, rules of 6, 114
infimum of a class, 45
infimum of a class above an ordinal, 45
infinite set, 91
Infinity, Axiom of, 43, 133
internal models, method of, 215
intersection algebra, 186
intersection of classes, 16, 44, 48
into mapping, 28
isomorphism of relational systems, 32

J

Jensen, Ronald Bjorn, 185

K

κ-direct limit system, 202
Konig, Julius (1849–1913), 109

L

language, 4–6
language, ramified, 194
largest cardinal paradox, 88
largest ordinal paradox, 41–42
lexicographic ordering, 54
limit of direct system, 190

N

negation, 4
von Neumann, John (1903–1957), 3, 35
n-tuple, ordered, 16
n-tuple, unordered, 16
number, cardinal, 1, 82–110
number, ordinal, 35–72

O

one-to-one class, 24
one-to-one into mapping, 28
one-to-one mapping, 28
one-to-one onto mapping, 28
onto mapping, 28
order of constructible set, 160
order, partial, 29
order preserving maps, direct system of, 190
order preserving maps, well founded direct system of, 190
order relation, 29
order type, 189
ordered n-tuple, 16
ordered pair, 15
ordering, lexicographic, 54
ordinal addition, 56
ordinal arithmetic, 56–72
ordinal class, 36
ordinal exponentiation, 67
ordinal function, 49–50
ordinal function, strictly monotone, 49–50
ordinal, limit, 42
ordinal multiplication, 62
ordinal numbers, 35–72
ordinal numbers, Cantor’s notion, 35
ordinal numbers, class of, 38
ordinal numbers, cofinality of, 100–110
ordinal of a formula, 220
ordinal, set closed in, 200
ordinals, maximum of sequence, 191

P

pair, ordered, 15
pair, unordered, 15
Pairing, Axiom of, 15, 132
paradox, Burali-Forti, 42
paradox of the largest cardinal, 88
paradox of the largest ordinal, 41–42
paradox, Russell’s, 3, 10, 11, 14, 18
partial map, 186

partial order, 29
partially ordered structure

S

satisfaction, 112
Schroder, Ernst (1841–1902), 86
Scott, Dana, 9
second converse, 143
Separation, Axiom Schema of, 18
sequence, $\diamond(\kappa)$-, 200
set, Cantor’s notion of, 2
set, closed in ordinal, 200
set, constructible, 158
set, definable, 14
set, dense, 217
set, directed, 189
set, empty, 20
set, equality, 7
set, finite, 91
set, infinite, 91
set, order of constructibility, 160
set, $\mathcal{P}$-generic, 218
set, power, 17
set, rank of, 79
set, singleton, 15
set, stationary, 200
set, supertransitive, 76
set theory, Gödel–Bernays, 3
set theory, Zermelo–Fraenkel, v, 3
set, transitive, 35
set, unbounded, 200
set union, 16, 48
set, well-founded, 77
sets, class of, 21
sets, equivalence of, 83
sets, elementarily equivalent, 202
Shelah, Saharon, 185
Sierpinski, Wacław (1882–1969), v
$\Sigma_1$-elementary embedding, 212
$\Sigma_1$-formula, 212
Silver, Jack, vii, 185
Silver machine, 187
single-valued class, 24
singleton set, 15
singular cardinal, 103
Skolem, Thoralf (1887–1963), 19
Souslin problem, 185
Standard Model Hypothesis, 216
standard structure, 112

well-founded direct system of order preserving maps, 190
well-founded relation, 30
well-founded set, 77
well-ordering relation, 30
Whitehead, Alfred North (1871–1947), 3
Whitehead problem, 185

Z

Zermelo, Ernst (1871–1953), v, 2, 3, 18, 19, 20
Zermelo–Fraenkel set theory (ZF), v, 3, 5
Zermelo–Fraenkel set theory, models of, 111, 139–142, 162
