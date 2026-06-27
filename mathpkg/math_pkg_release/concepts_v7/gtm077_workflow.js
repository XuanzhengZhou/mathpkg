export const meta = {
  name: 'v7-extract-gtm077',
  description: 'GTM077: 31 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s001_1_Algebraic_number_theory.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s002_3_Integral_Polynomials_Functional_Congruences_and_Divisibili.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s003_4_Congruences_of_the_First_Degree.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s004_5_The_General_Group_Concept_and_Calculation_with_Elements_of.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s005_6_Subgroups_and_Division_of_a_Group_by_a_Subgroup.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s006_7_Abelian_Groups_and_the_Product_of_Two_Abelian_Groups.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s007_10_Characters_of_Abelian_Groups.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s008_12_Groups_of_Integers_under_Addition_and_Multiplication.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s009_13_Structure_of_the_Group_Ren_of_the_Residue_Classes_mod.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s010_16_Quadratic_Residue_Characters_mod_n.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s011_17_Number_Fields_Polynomials_over_Number_Fields_and_Irreduci.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s012_19_Algebraic_Number_Fields_over_k.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s013_21_Definition_of_Algebraic_Integers_Divisibility_and_Units.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s014_II_The_set_of_integers_in.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s015_27_Congruences_and_Residue_Classes_Modulo_Ideals_and_the_Gro.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s016_29_First_Type_of_Decomposition_Laws_for_Rational_Primes_Deco.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s017_30_Second_Type_of_Decomposition_Theorem_for_Rational_Primes.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s018_37_Relative_Fields_and_Relations_between_Ideals_in_Different.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s019_38_Relative_Norms_of_Numbe.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s020_39_Decomposition_Laws_in_the_Relative_Fields_Ksqrtlmu.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s021_40_The_Density_of_the_Ideals_in_a_Class.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s022_43_The_Distribution_of_Prime_Ideals_of_Degree_1_in_Particula.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s023_44_Summary_and_the_System_of_Ideal_Classes.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s024_46_The_Quadratic_Reciprocity_Law_and_a_New_Formulation_of_th.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s025_50_Determination_of_the_Class_Number_of_ksqrtd_without_U.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s026_51_Determination_of_the_Class_Number_with_the_Help_of_the_Ze.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s027_52_Gauss_Sums_and_the_Final_Formula_for_the_Class_Number.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s028_54_Quadratic_Residue_Characters_and_Gauss_Sums_in_Arbitrary.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s029_56_Reciprocity_between_Gauss_Sums_in_Totally_Real_Fields.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s030_57_Reciprocity_between_Gauss_Sums_in_Arbitrary_Algebraic_Num.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM077)Lectures on the Theory of Algebraic Numbers/s031_6_We_regard_two_nonzero_ideals.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm077'
var BOOK_SLUG = 'gtm077'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
