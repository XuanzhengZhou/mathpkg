---
role: proof
locale: en
of_concept: theorem-24-5
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
By the definition of #. (See Remark following Theorem 22.9.)

$$\#([p]_{P_\beta}) = \inf \{b \in B_\alpha \mid [p]_{P_\beta} \leq i(b)\}$$
$$= \inf \{b \in B_\alpha \mid [p]

It is clear that $P_\alpha$ and $P'_\alpha \triangleq \langle \Delta_\alpha, \leq \rangle$ form an $\aleph_\alpha$-Easton pair and $P \simeq P_\alpha \times P'_\alpha$. Therefore by Theorem 23.45 $B$ satisfies the SL. Consequently, by Theorem 23.30 $V^{(B)}$ satisfies $ZF + AC$. Furthermore, by Theorem 23.46 $B$ is $(\aleph_\alpha, \aleph_\beta)$-splitable. Hence by Corollary 23.34 cardinals are absolute, i.e.,

$$(\forall \alpha) [\llbracket \text{Card} (\aleph_\alpha) \rrbracket = 1].$$

Using only the properties 1 and 2 of $G$ stated at the beginning of this section one can prove

$$\llbracket 2^{\aleph_\alpha} \rrbracket = (\aleph_{G(\alpha)})^\vee = 1 \quad \text{for} \quad \alpha \in \text{Reg}.$$

In order to determine $\overline{2^{\aleph_\alpha}}$ even in the case $\alpha \notin \text{Reg}$, we require that in this case $\aleph_{G(\alpha)}$ be the least cardinal which is not cofinal with $\aleph_\alpha$ and which is greater than or equal to $\aleph_{G(\beta)}$ for each $\beta < \alpha$. Then it will turn out that in $V^{(B)}$, $\overline{2^{\aleph_\alpha}} = \aleph_{G(\alpha)}$, i.e., $\overline{2^{\aleph_\alpha}}$ is the least cardinal allowed by König’s Theorem. Thus we obtain in general

$$(\forall \alpha) [\llbracket 2^{\aleph_\alpha} \rrbracket = (\aleph_{G(\alpha)})^\vee = 1 \quad \text{in} \quad V^{(B)}.$$

We shall prove this statement by a forcing argument. Thus, let $M$ be a transitive countable structure such that $\

Proof.

1. $\overline{2^{\aleph_{\alpha}}} \geq \aleph_{G(\alpha)}$ in $M[h_0]$:
Consider first the case $\alpha \in \text{Reg.}$ Let
$$a_{\eta} = \{\gamma \in \aleph_{\alpha} \mid (\exists p \in P)[\langle 1, \gamma, \alpha, \eta \rangle \in p \land h_0(p) = 1]\}.$$
Then, as in the proof of Theorem 11.10,
$$(\forall \eta < \aleph_{G(\alpha)})[a_{\eta} \subseteq \aleph_{\alpha}].$$
and
$$(\forall \eta, \eta' < \aleph_{G(\alpha)})[\eta \neq \eta \rightarrow a_{\eta} \neq a_{\eta'}].$$
Since $(\forall \eta < \aleph_{G(\alpha)})[a_{\eta} \in M[h_0]]$, this proves 1.
Now suppose $\alpha \notin \text{Reg.}$ Then $\overline{2^{\aleph_{\alpha}}} \geq \overline{2^{\aleph_{\beta}}} \geq \aleph_{G(\beta)}$ for each $\beta < \alpha$, $\beta \in \text{Reg.}$, hence $\overline{2^{\aleph_{\alpha}}} \geq \aleph_{G(\alpha)}$ by our additional requirement on $G$ that $\aleph_{G(\alpha)}$ is the smallest cardinal greater than or equal to $\aleph_{G(\beta)}$ for all $\beta < \alpha$ that are not cofinal with $\aleph_{\alpha}$.

2. $\overline{2^{\aleph_{\alpha}}} \leq \aleph_{G(\alpha)}$ in $M[h_0]$.
Define $\sum$ in $M$ as follows:
$$\sum = \{\langle \Lambda, S \rangle \mid \Lambda \subseteq \Gamma_{\alpha} \land \Lambda \in M \land S \subseteq \Lambda \times \aleph_{\alpha} \land S \in M\}.$$
We first show that $\overline{\sum

for the same $S$. We must then show that $h(w_0) = h(w_1)$. Note that $h(w_0), h(w_1) \subseteq \aleph_\alpha$. Suppose

$$\gamma \in h(w_0) \land \gamma \notin h(w_1) \quad \text{for some} \quad \gamma \in \aleph_\alpha.$$

Then since this is true in $M[h_0]$, we have from the definition of $h$ (see the proof of Theorem 23.24)

$$h_0(\bar{q}_0 \cdot \bar{q}_1 \cdot [\check{\gamma} \in w_0] \cdot [\check{\gamma} \notin w_1]) = 1$$

and by (ii):

$[\exists p \in \Lambda)[p \cdot \bar{q}_0 \cdot \bar{q}_1 \cdot [\check{\gamma} \in w_0] \cdot [\check{\gamma} \notin w_1]] > 0 \land [p \cdot \bar{q}_0 \leq [\check{\gamma} \in w_0] \lor p \cdot \bar{q}_0 \leq [\check{\gamma} \notin w_0]]].$$

We must have $p \cdot \bar{q}_0 \leq [\check{\gamma} \in w_0]$, therefore by (iii)

$$\langle p, \gamma \rangle \in S.$$

But by hypothesis, $w_0, \bar{q}_0$ and $w_1, \bar{q}_1$ satisfy (i)–(iv) for the same $S$. Hence

$$p \cdot \bar{q}_1 \leq [\check{\gamma} \in w_1].$$

This is a contradiction.

To prove that $K$ is onto suppose $h(u) \subseteq \aleph_\alpha$. Then $h_0([\check{u} \subseteq (\aleph_\alpha)^\vee]) = 1$, so by Lemma 24.6 there are $p, \Lambda \in M$ such that $h_0(p) =

Bibliography

Bar-Hillel, Y. (Ed.): Essays on the foundations of mathematics. Jerusalem: Magnes Press 1966.

Benacerraf, P., Putnam, H.: Philosophy of mathematics selected readings. Englewood Cliffs: Prentice-Hall Inc. 1964.

Bernays, P., Fraenkel, A. A.: Axiomatic set theory. Amsterdam: North-Holland 1958.

Birkhoff, G., MacLane, S.: A survey of modern algebra. Macmillan 1965.

Church, A.: Introduction to mathematical logic. Princeton: Princeton University Press 1956.

Cohen, P.: The independency of the continuum hypothesis. Proc. Nat. Acad. Sci. U.S. 50, 1143–1148 (1963).

Set theory and the continuum hypothesis. New York: W. A. Benjamin Inc. 1966.

Fraenkel, A. A., Bar-Hillel, Y.: Foundations of set theory. Amsterdam: North-Holland 1958.

Gödel, K.: The consistency of the continuum hypothesis. Princeton: Princeton University Press 1940.

What is Cantor’s continuum problem? Am. Math. Monthly 54, 515–525 (1947).

Halmos, Paul R.: Lectures on Boolean algebras. D. van Nostrand Co. Inc. 1963.

van Heijenoort, J.: From Frege to Godel. Cambridge: Harvard University Press 1967.

Jeck, Thomas: Lectures in set theory. New York: Springer-Verlag 1971.

Moore, T. O.: Elementary general topology. Prentice-Hall 1964.

Quine, W. V.: Set theory and its logic. Cambridge: Belknap Press 1969.

Rosser, J. Barkley: Boolean valued models of set theory. Academic Press 1969.

Rubin, J. E.: Set theory for the mathematician. San Francisco: Holden-Day 1967.

Schoenfield, J. R

Problem List

by Paul E. Cohen

Section 1

1. Prove, for a Boolean algebra $\langle B, +, \cdot, -, 0, 1 \rangle$, that
   i) $(\forall a)(\forall b)[a + b = a \rightarrow b - a = 0]$, and
   ii) $(\forall a)(\forall b)[ab = a \rightarrow a - b = 0]$.

2. If $\langle B, +, \cdot, -, 0, 1 \rangle$ is a Boolean algebra, prove that $\langle B, \cdot, +, -, 1, 0 \rangle$ is a Boolean algebra.

3. Let $\langle B, +, \cdot, -, 0, 1 \rangle$ be a Boolean algebra and let $\leq$ be the natural order on $B$. Show that $+, \cdot, -, 0, 1$ can be defined in $\langle B, \leq \rangle$.

4. Give a partial order structure in which there is a $p$ such that $[p]$ is not regular open.

5. Which sets are regular open in a linear order structure?

Section 2

6. Show that in Definition 2.2, condition 3 may be replaced by
   $3'$. $S \in A \land S \subseteq P \land S^- = P \land S$ is open $\rightarrow G \cap S \neq 0$.

7. If $\langle P, \leq \rangle$ is a partial order structure, if $M$ is a model of $ZF$, if $Q$ is a dense subset of $P$, if $Q \in M$, and if $G$ is $\langle P, \leq \rangle$-generic over $M$, then $Q \cap G$ is $\langle Q, \leq \rangle$-generic over $M$.

8. Let $P = \langle P, \leq \rangle$ be a partial order structure with
   $P = \{p \mid (\exists d \subseteq \omega)[d \text{ if finite } \land p:d \rightarrow 2]\}$ and $p \leq q$

Section 4

11. Show that the Boolean algebra of regular open sets for the partial order structure of Exercise 8 does not satisfy the $(\omega, 2)$-DL.

Section 5

12. Show that if $P$ is a partial order structure, if $A$ is a set and if $G$ is $P$-generic over $A$, then $G$ is a filter for $P$. Thus $G$ is sometimes referred to as a $P$-generic filter.

Section 7

13. We say that mathematical induction holds in a model $M$ of Godel-Bernays set theory $(GB)$ if for every formula $\varphi$ of the language of $GB$,

$$[\varphi(0) \wedge (\forall n)[\varphi(n) \rightarrow \varphi(n + 1)]] \rightarrow (\forall n)[\varphi(n)]$$

is true in $M$. Show that if $M$ is a standard model of $GB$, then $M$ satisfies mathematical induction.

14. Let the strong Löwenheim-Skölen Theorem be the statement that every structure for a language $\mathcal{L}$ (which is a sequence of classes) has an elementary substructure of power $\overline{\mathcal{L}}$. Show that if “$GB +$ there is a standard model of $ZF$ which is a set” is consistent, then the strong Löwenheim-Skölem Theorem is not a Theorem of $GB +$ mathematical induction. (Hint: Look at the minimal model.) We remark that the strong Löwenheim-Skölem Theorem may be proven in Morse-Kelly set theory, which has stronger comprehension axioms than does $GB$.

15. Give a construction for $M[K]$ that does not presuppose that $K \subseteq M$.

Section 8

16. What is the relationship between the sets in $L[K; F]$ of rank not more than $\alpha$ and $\{D_{\alpha}(t) \mid t \in T_{\alpha}\}$?

Section 9

17. In view of the fact that $V[F] \subseteq V$, discuss the statement “$V[F]$ is an extension of $V$.”

Section 10

18. Show that

Section 11

19. Prove that the partial order structure $P$ of Definition 11.1 is isomorphic to the partial order structure of Exercise 8. What relationship is there between the set $a$ in Theorem 11.3 and the function $\bigcup G$ of Exercise 8?

20. Why is Corollary 11.4 not a proof that if $ZF$ is consistent then so is $ZF + AC + GCH + V \neq L$?

21. Refer to Theorem 11.6. Show that $M[G_1]$ and $M[G_2]$ are not necessarily elementarily equivalent in the language $\mathcal{L}_0(C(M) \cup \{G(\cdot)\})$.

22. Show that the partial order structure of Theorem 11.10 is isomorphic to the structure $\langle Q, \leq \rangle$ where

$$Q = \{q \mid (\exists d)[d \subseteq \overline{\alpha \times \omega} \land \bar{d} < \lambda_0 \land q:d \rightarrow 2]\}$$

and $q_1 \leq q_2$ iff $q_1 \supseteq q_2$ (cf. Definition 11.1 and Exercises 8 and 19).

Section 12

23. Show that the partial order structure of Theorem 11.1 is isomorphic to the strong product of copies of the partial order structure of Exercise 8 or 19.

24. In courses in naive set theory a finite set is sometimes defined as a set that is equinumerous with none of its proper subsets. Show that this is a satisfactory definition only if the Axiom of Choice is assumed.

Section 13

25. In view of the fact that $V^{(B)} \subseteq V$, discuss the statement “$V^{(B)}$ is an extension of $V$.” (cf. Exercise 16.)

26. Suppose $\langle K, \leq \rangle$ is a partial order structure and $B$ is the Boolean algebra of regular open sets of $B$. Let $f_0: K \rightarrow B$ be defined by $f_0

29. If $P$ is a partial order structure, then we say that $P$ satisfies the $\gamma$-chain condition (where $\gamma$ is a cardinal) if $\overline{S} \leq \gamma$ for every $S \subseteq |P|$ such that $(\forall p, q \in S) [\neg \text{Comp}(p, q)]$. Show that if $M$ is a countable standard transitive model of $ZFC$, if $P \in M$, if $G$ is $P$-generic over $M$, and if $\alpha > \gamma$ is a cardinal in $M$, then $\alpha$ is a cardinal in $M[G]$. Give two proofs of this, one using Theorem 17.4 (see Exercise 10), and the other based on Theorems 10.4 and 10.6.

Section 18

30. Suppose $P$ is a partial order structure such that whenever $\langle p_i | i < \omega \rangle$ is a sequence with $p_0 \geq p_1 > \cdots$, then $(\exists p \in |P|)(\forall i \in \omega)[p \leq p_i]$. Let $B$ be the Boolean algebra of regular open sets of $P$. Then $B$ satisfies the $(\omega, 2)$-DL.

31. Use the result of Exercise 30 to show that if $M$ is a countable standard transitive model of $ZFC$ if $P \in M$ has the property of Exercise 30, and if $G$ is $P$-generic over $M$, then $\mathcal{P}(\omega)$ is the same in $M$ and $M[G]$.

32. Give a direct proof of Exercise 31 based on Theorems 10.4 and 10.6. Can the proof be generalized to give a stronger theorem?

Section 20

33. Give a proof for the remark after Definition 20.1.

34. Give a condition on a partial order structure such that its Boolean algebra of regular open sets satisfies the $(\omega, \omega_\alpha)$-WDL. Can you find an equivalent condition?

Section 22

35

Subject Index

absolute class, 66
absolute formula, 66
absorption laws, 4
abstraction operator, 79
abstraction terms, 79
(ℓα, ℓβ)-splitable, 212
ℓα-bounded, 215
ℓα-Easton pair, 215
(α, β)-distributive law, 47
associated partial order structure, 52
associative laws, 3
atom, 132
atomic topological space, 191
