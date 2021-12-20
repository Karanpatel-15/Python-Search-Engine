
import testingtools
import crawler
import searchdata
import search

output = open('fruits2-page-rank-failed.txt', 'w')
success_output = open('fruits2-page-rank-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')



#Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html
expected = 0.002735186646447709
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html
expected = 0.0014623420498163333
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html
expected = 0.0006061142126516885
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html
expected = 0.0006012946580696521
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html
expected = 0.0008404099320985172
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html
expected = 0.0007259920219029112
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-943.html
expected = 0.0003759107288599937
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-943.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-943.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-943.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-466.html
expected = 0.0003593566498590439
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-466.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-466.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-466.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html
expected = 0.0013835381417722232
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html
expected = 0.0006374274676556428
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-733.html
expected = 0.00062309471067122
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-733.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-733.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-733.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html
expected = 0.0006343195152163438
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html
expected = 0.0004937605626209321
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-855.html
expected = 0.0006363277068834551
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-855.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-855.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-855.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-124.html
expected = 0.0003549635139768133
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-124.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-124.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-124.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html
expected = 0.000369923576275234
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-627.html
expected = 0.0006419317249881176
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-627.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-627.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-627.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html
expected = 0.0016737005463212428
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html
expected = 0.00035774184996753544
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html
expected = 0.00163735143129181
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-798.html
expected = 0.0003708789953978746
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-798.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-798.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-798.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html
expected = 0.001150868906976493
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html
expected = 0.0008695613254074448
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html
expected = 0.0006237649049023903
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html
expected = 0.011877960885945333
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html
expected = 0.0006029702859546521
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html
expected = 0.0010896356490712915
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html
expected = 0.0010027835412171212
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html
expected = 0.0011093319402238472
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html
expected = 0.00037830071395642147
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html
expected = 0.0006086285925394773
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html
expected = 0.0020062809624722395
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html
expected = 0.0008961985902299828
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-269.html
expected = 0.0010867884458476116
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-269.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-269.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-269.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html
expected = 0.0006180974186630668
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
expected = 0.0015607476940509178
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html
expected = 0.0012837173525721448
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html
expected = 0.00035261020331693165
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html
expected = 0.000359671428802781
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-582.html
expected = 0.00034953516000574075
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-582.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-582.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-582.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-446.html
expected = 0.00038470442317922954
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-446.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-446.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-446.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html
expected = 0.0006062563401124724
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html
expected = 0.00035077368590988333
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html
expected = 0.002571518197319439
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-493.html
expected = 0.0008035310195140911
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-493.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-493.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-493.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html
expected = 0.0015139225091534555
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html
expected = 0.010180760971221083
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-728.html
expected = 0.0003570099185522668
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-728.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-728.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-728.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html
expected = 0.0003673691517879539
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html
expected = 0.00044965426790029555
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
