---
role: proof
locale: en
of_concept: translation-between-l1ar-and-sar
source_book: gtm053
source_chapter: "I"
source_section: "10"
---

**(a) Translation from $\mathrm{L}_1\mathrm{Ar}$ to SAr.** We denote the translation of $P$ by "$P$".

*Atomic formulas:* The alphabet of SAr lacks addition ($+$) but has multiplication ($\cdot$) and exponentiation ($\uparrow$). In place of $z = x + y$ we can write $2^z = 2^x \cdot 2^y$, which is expressible using $\cdot$ and $\uparrow$. Specifically, we use the formula

$$“z = x + y” = ((\bar{1}\bar{1}) \uparrow (z)) = ((\bar{1}\bar{1}) \uparrow (x)) \cdot ((\bar{1}\bar{1}) \uparrow (y))$$

where $\bar{1}\bar{1}$ represents the constant $2$. All other atomic formulas ($t_1 = t_2$, $t_1 = t_2 \cdot t_3$, $t_1 = t_2 \uparrow t_3$) are translated similarly by replacing terms.

*Inductive step:* The translation respects the logical connectives and quantifiers:

- “$\neg Q$” = $\neg$“$Q$”
- “$Q_1 \land Q_2$” = “$Q_1$” $\land$ “$Q_2$”
- “$\forall x_k Q$” = $\forall x_k$ “$Q$”
- “$\exists x_k Q$” = “$\neg \forall x_k \neg Q$”

Both the formula and its translation are true at a point $\xi$ if and only if $Q$ (and "$Q$") are true at all variations $\xi'$ of $\xi$ along $x_k$. They have the same free variables by induction.

**(b) Translation from SAr to $\mathrm{L}_1\mathrm{Ar}$.** Again denote the translation by "$P$".

The subtle point is translating $x_1 = x_2 \uparrow x_3$. It is shown in Part II of the book that exponentiation is definable in $\mathrm{L}_1\mathrm{Ar}$: there exists a formula $\exists x_4 \cdots \exists x_n \, p(x_1, x_2, x_3, x_4, \ldots, x_n)$ with $p$ atomic in $\mathrm{L}_1\mathrm{Ar}$ that expresses $x_1 = x_2^{x_3}$. We take such a translation "$x_1 = x_2 \uparrow x_3$" once and for all.

*Translation of $Fl_0$ formulas:* 

- “$t_1 = t_2$” for $t_i$ among variables and numerals $\bar{1}, \bar{1}\bar{1}, \ldots$ is straightforward (replace $x'\cdots'$ with $x_k$, and $\bar{1}\cdots\bar{1}$ with $(\cdots(\bar{1} + \bar{1}) + \bar{1}) + \cdots)$).
- “$x_k = t_1 \cdot t_2$” becomes $\exists x_i \exists x_j (“x_i = t_1” \land “x_j = t_2” \land x_k = x_i \cdot x_j)$.
- The connective $\downarrow$ (conjunction of negations) is translated as: “$(P_1) \downarrow (P_2)$” = $\neg$“$P_1$” $\land$ $\neg$“$P_2$”.

*Class terms and satisfaction:* The class term $x_k(P)$ in SAr names the set $\{x_k \mid P\}$, and $x_k(P)\bar{m}$ says that $\bar{m}$ belongs to this set. In $\mathrm{L}_1\mathrm{Ar}$ this is expressed by substituting $\bar{m}$ for $x_k$ in the translation of $P$: “$x_k(P)\bar{m}$” = “$P$”$(\bar{m}/x_k)$. The induction on rank $i$ shows that the translation preserves truth values and free variables at every level.

Since the translations preserve truth values and free variables, the classes of definable sets in $\bigcup_{r \geqslant 1} N^r$ coincide for $\mathrm{L}_1\mathrm{Ar}$ and SAr.
