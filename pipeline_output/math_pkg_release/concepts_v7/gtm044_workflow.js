export const meta = {
  name: 'v7-extract-gtm044',
  description: 'GTM044: 19 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s001_2.2_Draw_figures_corresponding_to_Figures.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s002_3.1_Suppose_that_curves.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s003_2_Sometimes_there_is_given_just_one_function.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s004_3.2_Find_functions.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s005_4.1_Show_that_the_product_of_distinct_irreducible_polynomial.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s006_6.2_Redo_Exercise.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s007_8.1_Prove_Lemma.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s008_2.2_Let_the_set.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s009_4.4_Show_that_decompositions_in_Theorem.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s010_6.1_Prove_that_a_module.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s011_8.5_Find_an_irreducible_curve.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s012_10.1_In_this_exercise_we_look_at_properties_of_Diagram.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s013_11.2_With_notation_and_assumptions_as_in.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s014_3.1_Is_the_assumption_that_V_is_irreducible_in_Theorems.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s015_4.3_Show_that_a_pure.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s016_7.3_Using_Exercise.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s017_2.1_Prove_that_for_ord_in_Definition.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM044)Elementary Algebraic Geometry/s018_3.2_Use_Theorem.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm044'
var BOOK_SLUG = 'gtm044'

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
