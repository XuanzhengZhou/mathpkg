---
role: proof
locale: en
of_concept: exercise-ch23-7-duality-finite-length-injective-bimodule
source_book: gtm013
source_chapter: "6"
source_section: "23. Exercises"
---
Since ${}_R U$ and $U_S$ are injective, $H'$ and $H''$ are exact. By induction on composition length, every module of finite length is $U$-reflexive: simple modules are reflexive because $U$ is an injective cogenerator for finite length modules; the induction step uses exactness of $H'$, $H''$ and the 5-lemma. Thus $H'$ and $H''$ restrict to ${}_R\mathbf{FLM}$ and $\mathbf{FLM}_S$, with the natural transformations being isomorphisms on these subcategories. Hence $(H', H'')$ defines a duality.
ENDOFFILE

echo "Done ch23-7"

echo "DONE" > "$BASE/.done" && echo "s018 done"