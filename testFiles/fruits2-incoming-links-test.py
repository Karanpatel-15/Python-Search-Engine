
import testingtools
import crawler
import searchdata
import search

output = open('fruits2-incoming-links-failed.txt', 'w')
success_output = open('fruits2-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')



#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-985.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-985.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-985.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-985.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-210.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-158.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-210.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-210.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-210.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-169.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-334.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-982.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-334.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-334.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-334.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-433.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-433.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-433.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-433.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-617.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-617.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-617.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-617.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-405.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-405.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-405.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-405.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-637.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-702.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-714.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-617.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-775.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-622.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-775.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-775.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-775.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-731.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-96.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-224.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-96.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-96.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-96.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-222.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-222.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-222.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-222.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-289.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-146.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-614.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-480.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-910.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-853.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-910.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-910.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-910.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-713.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-282.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-282.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-282.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-282.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-693.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-693.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-693.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-693.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-806.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-806.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-806.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-806.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-534.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-852.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-219.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-219.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-219.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-219.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-199.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-199.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-199.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-199.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-883.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
