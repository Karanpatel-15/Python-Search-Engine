
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-page-rank-failed.txt', 'w')
success_output = open('fruits5-page-rank-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html
expected = 0.00038490658145333347
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html
expected = 0.0020205479118357013
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html
expected = 0.0004174295277328994
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html
expected = 0.0023263904203868853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html
expected = 0.0004674471026569333
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html
expected = 0.0003840776780762749
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html
expected = 0.00035714372225053464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html
expected = 0.0019806821469571935
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html
expected = 0.0033233711995765565
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html
expected = 0.0006324540946060254
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html
expected = 0.00037195478970996314
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html
expected = 0.0006555769979858365
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html
expected = 0.00035451373937112806
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html
expected = 0.0006625550943026569
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html
expected = 0.0008753256038677005
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html
expected = 0.0009423859946335992
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html
expected = 0.0003804539804548974
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html
expected = 0.0016707754782408154
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html
expected = 0.001498325780401488
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html
expected = 0.0007756732301099296
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html
expected = 0.0018141864531675098
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html
expected = 0.0014179444854222146
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html
expected = 0.00038659090589926004
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html
expected = 0.0012107555388991618
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
expected = 0.0011430871085981325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html
expected = 0.0009550835657134184
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html
expected = 0.0006511855068961516
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html
expected = 0.0003673105649758189
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html
expected = 0.0007751211185293035
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html
expected = 0.00035974551095579625
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html
expected = 0.00038827248057796143
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html
expected = 0.0017552412034235413
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html
expected = 0.000360004864997057
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html
expected = 0.0006890810517363664
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html
expected = 0.0009071095306778685
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html
expected = 0.0004044760337651851
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html
expected = 0.0020368702002525113
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html
expected = 0.0003876732732876885
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html
expected = 0.0014223148503289226
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html
expected = 0.0006208436121706209
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html
expected = 0.0004862742995016652
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html
expected = 0.0003844873028720965
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html
expected = 0.001586901988068157
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html
expected = 0.0004608941199525589
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html
expected = 0.00045156319709767736
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html
expected = 0.00041408813686226947
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
expected = 0.0006749273702981862
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-713.html
expected = 0.00041143967946875577
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-713.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-713.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-713.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-686.html
expected = 0.00035485324890770757
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-686.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-686.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-686.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html
expected = 0.0003717766383383526
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html\n\n')
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
