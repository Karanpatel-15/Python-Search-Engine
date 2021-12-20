
import testingtools
import crawler
import searchdata
import search

output = open('tinyfruits-all-failed.txt', 'w')
success_output = open('tinyfruits-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = 0.047437705789256435
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = 0.32242792521306995
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = 0.0819555328928385
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = 0.11939323868209492
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = 0.12476521976591842
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = 0.11896585666418055
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #33 checking IDF for word apple
expected = 0.32192809488736235
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking IDF for word papaya
expected = 0.5145731728297582
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking IDF for word cherry
expected = 0.5145731728297582
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking IDF for word blueberry
expected = 0.32192809488736235
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking IDF for word peach
expected = 0.5145731728297582
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking IDF for word orange
expected = 0.32192809488736235
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking IDF for word banana
expected = 0.0
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking IDF for word coconut
expected = 0.32192809488736235
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking IDF for word apricot
expected = 0.0
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking IDF for word kiwi
expected = 0.32192809488736235
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking IDF for word pear
expected = 0.7369655941662062
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking IDF for word lime
expected = 0.32192809488736235
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking IDF for word fig
expected = 0.7369655941662062
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime
expected = 0.26666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut
expected = 0.03125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot
expected = 0.03125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime
expected = 0.03125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange
expected = 0.09375
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig
expected = 0.15
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana
expected = 0.10810810810810811
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear
expected = 0.13513513513513514
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi
expected = 0.02702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach
expected = 0.10810810810810811
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana
expected = 0.21739130434782608
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut
expected = 0.13043478260869565
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime
expected = 0.044266247441115764
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut
expected = 0.02266030222847964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry
expected = 0.08467816515990254
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi
expected = 0.02266030222847964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach
expected = 0.03622045978643087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry
expected = 0.10363769827780657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi
expected = 0.10363769827780657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime
expected = 0.014291714269269087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut
expected = 0.014291714269269087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya
expected = 0.045006031726892604
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach
expected = 0.045006031726892604
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut
expected = 0.11672149491947882
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya
expected = 0.0991299889868547
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple
expected = 0.06201786293142292
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime
expected = 0.03872609348667805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut
expected = 0.05694192097566775
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry
expected = 0.019766560368774045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear
expected = 0.04525008888053903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya
expected = 0.031595073081303486
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi
expected = 0.03872609348667805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach
expected = 0.031595073081303486
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple
expected = 0.07447019235682993
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime
expected = 0.10978936524490102
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya
expected = 0.13535044877328553
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach
expected = 0.04791160163801364
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime
expected = 0.02445006963027565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut
expected = 0.02445006963027565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear
expected = 0.13476451852905313
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya
expected = 0.03908124238104001
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi
expected = 0.012385909108380427
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach
expected = 0.07620758655640758
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple
expected = 0.06979767743420133
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut
expected = 0.0404119177187868
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya
expected = 0.12401630243933787
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple
expected = 0.07758727832568058
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear
expected = 0.18271404725510207
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach
expected = 0.045006031726892604
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #289 checking search results for 'tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #289 checking search results for 'tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #289 checking search results for 'tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking search results for 'tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #290 checking search results for 'tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #290 checking search results for 'tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking search results for 'coconut apple pear fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.273136941346051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11269778877643445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11175859802859411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043030585413345056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03398059267411853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03385009353234447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03268342898280018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03156680953012927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017039205373130858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01699585040082358}]
result = search.search('coconut apple pear fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'coconut apple pear fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'coconut apple pear fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'coconut apple pear fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.947312043442517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9360546649226147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9301169230025161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8471255743917155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7135693636350084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.706460535143582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3851699624893497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3683067083523651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.36736957972508877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2723562923855873}]
result = search.search('coconut apple pear fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'coconut apple pear fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'coconut apple pear fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04700050552572875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04166740493176235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.990783697140204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9006514341450588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'lime blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25043404352598353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10821792163398258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10666440428093198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058108714191464704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04393390540078169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043825491249772475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038732724583983275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464698}]
result = search.search('lime blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'lime blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'lime blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'lime blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.949642411655075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9472990125221563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9096552966408045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.893387309518794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7767132557159535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7090273486165375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896257}]
result = search.search('lime blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'lime blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'lime blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'banana pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2637331451968811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10940992436469393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047334311598663054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('banana pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'banana pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'banana pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'banana pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9978204217747647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8179599984170057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('banana pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'banana pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'banana pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'tomato orange cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27334194193079353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11318953827718124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04683681160418475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045703366332529576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04409116581499072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.024537204026072217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato orange cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'tomato orange cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'tomato orange cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'tomato orange cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9878897545950132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9873329838558977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9530416350486021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9514455781770661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato orange cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'tomato orange cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'tomato orange cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2821526758257762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1059048539675116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04683681160418476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04409116581499072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0435528580749021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9873329838558978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9530416350486022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9414059778984581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8902121746280713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8750875893870586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'cherry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3052997436712434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1059048539675116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04683681160418476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045703366332529576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9878897545950132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9873329838558978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.946877487331447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8902121746280713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'papaya banana pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09789197951097454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.046918658223838054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04491965701017603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03793211738241752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026485429100261856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026485429100261856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('papaya banana pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'papaya banana pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'papaya banana pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'papaya banana pear tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.946918833084658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5724892093031334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5724892093031334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5724892093031334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('papaya banana pear tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'papaya banana pear tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'papaya banana pear tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'tomato papaya orange cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2948637039317377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10309083647737671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05299708084078069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.04830200317876409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04653871973388704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04448994844629568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0439633104224351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.034861673647887205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato papaya orange cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'tomato papaya orange cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'tomato papaya orange cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'tomato papaya orange cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9810491245221012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9616614218912227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9502780085914954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9145104405484823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8665581820537283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7535438412612129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.4045622994395562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.4045622994395562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato papaya orange cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'tomato papaya orange cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'tomato papaya orange cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'cherry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09884163304040819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09789197951097453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037932117382417516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.027157574678446095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'cherry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'cherry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.830840342027045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8199122545928149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8199122545928149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'kiwi apple coconut apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3122557600208877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09748417116981845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08381617144537605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06691641239511242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03894717105476591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03777409591892747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03777409591892747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03612029567147615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.036028390304748366}]
result = search.search('kiwi apple coconut apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'kiwi apple coconut apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'kiwi apple coconut apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'kiwi apple coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.96845135176967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8210171720316745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7807492727597277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.778762715149899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7045397208543136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896258}]
result = search.search('kiwi apple coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'kiwi apple coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'kiwi apple coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'apricot apricot coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot apricot coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'apricot apricot coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'apricot apricot coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'apricot apricot coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot apricot coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'apricot apricot coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'apricot apricot coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'blueberry apricot orange orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23041966464239808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11165907267238358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09498167379974928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05519424682789035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0472896166273599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04280964991404558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04196370121625199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.036798303860000006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03667562383113479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03053210469505208}]
result = search.search('blueberry apricot orange orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'blueberry apricot orange orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'blueberry apricot orange orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'blueberry apricot orange orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9385808315370457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9253413466347654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8846064647956862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7955364545613371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7954045902280498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7927528305583664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.714639293386669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6734657793032711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.659959119750793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.379028840858723}]
result = search.search('blueberry apricot orange orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'blueberry apricot orange orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'blueberry apricot orange orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'peach banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09754156375709394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04722433043802307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04691865822383806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04316577243726431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'peach banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'peach banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9955019883933407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9330390245149593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'tomato pear blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31166825219109245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11932896648046093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1189018145323858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07756690693417995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.050951997716726274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04019401614880047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03715573029432619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028762236051273562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('tomato pear blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'tomato pear blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'tomato pear blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'tomato pear blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9994616763700905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9994616763700905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9666292148396662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8688037651433277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7832531037523557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('tomato pear blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'tomato pear blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'tomato pear blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #327 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'banana papaya peach pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27272251097834893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10109565683306951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0989453798309917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.053553337999504506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0454564870387283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03741123638272974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.025891020796039214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02589102079603921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.021949407447519186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana papaya peach pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #329 checking search results for 'banana papaya peach pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'banana papaya peach pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'banana papaya peach pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9582353590342298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8497871546324804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8458402317296982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8287352024552315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8086532808180863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6534438384962798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5596409243537206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5596409243537205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana papaya peach pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'banana papaya peach pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'banana papaya peach pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'apple kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038888417384739506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('apple kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'apple kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'apple kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8197786283658526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}]
result = search.search('apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'orange lime fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24940553762330134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11718243351592351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11233183583114192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043177826742497115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04240108680922134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.030589983315464014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.027213437080599274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.027213437080599274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.026530951176359046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange lime fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'orange lime fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'orange lime fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'orange lime fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9850089496409771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.940855923426659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9332995813534118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9165101523978954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7735233772275982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.644845335720092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5882252848430846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5882252848430846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.323723734565301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange lime fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'orange lime fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'orange lime fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'tomato peach kiwi cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30825399412837273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09107093102104816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07693004853215028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06251414875134181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05047530419858152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045090337376498035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0410999447171166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029916678785502596}]
result = search.search('tomato peach kiwi cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'tomato peach kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'tomato peach kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'tomato peach kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9560400015745203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9505168225633284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8883856389274792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.762781310117068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.762781310117068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.40456229943955613}]
result = search.search('tomato peach kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'tomato peach kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'tomato peach kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'papaya kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3063711312724565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0996534628802813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08267389077226897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07534196181460875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07480528573223755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0405830870382606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.026543893578995635}]
result = search.search('papaya kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'papaya kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'papaya kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'papaya kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.950200362049898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.912754552277144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8555027348614265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8376643994720712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6310404395279009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5737529337108415}]
result = search.search('papaya kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'papaya kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'papaya kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'blueberry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07116834968915606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04414631023537236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'blueberry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'blueberry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8683776088944807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'pear fig tomato apricot fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3090727682292671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11444789952032623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11403821992051827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044347363087998935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040675908593195795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.022600082116176423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear fig tomato apricot fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'pear fig tomato apricot fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'pear fig tomato apricot fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'pear fig tomato apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9585794035210277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9585794035210277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9585794035210277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9585794035210277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.879219991492415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.476416001578534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear fig tomato apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'pear fig tomato apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'pear fig tomato apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'cherry cherry tomato fig banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3079037075953829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11403608287243269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07319868520591948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04417962020757703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03747644323107103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03654890732618667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03654890732618667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028363724314700238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry cherry tomato fig banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'cherry cherry tomato fig banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'cherry cherry tomato fig banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'cherry cherry tomato fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9585614399796764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9549535989846752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9549535989846752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7900138214432493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7900138214432493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7900138214432493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6130890326279161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6130890326279161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry cherry tomato fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'cherry cherry tomato fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'cherry cherry tomato fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'lime fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30948479568917386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11473564072080805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11166377113686467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04636687542255846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045654220977607574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04363367322132315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.037403839749227376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01762941786812988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'lime fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'lime fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'lime fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9868274653916285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9609894327962027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9598572936406086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9431528176079137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9386203257634804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4563918801935559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'lime fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'lime fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'blueberry coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2999372132854783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11310109710537064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09809262118059654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058108714191464704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04123605518358694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038732724583983275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464698}]
result = search.search('blueberry coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'blueberry coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'blueberry coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'blueberry coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9472990125221563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9302457691506432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8913277008828474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8245443182701955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7090273486165375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896257}]
result = search.search('blueberry coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'blueberry coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'blueberry coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'papaya peach peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29622029211510004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11090179834009874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05401810099427488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047226350272653345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.04406315335085425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04297328599924992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04297328599924992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017135348673580294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017135348673580294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya peach peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'papaya peach peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'papaya peach peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'papaya peach peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9955445670677657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9288783817599077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9288783817599077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9288783817599077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.918717855841267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6591147551307683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.37038486996514214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.37038486996514214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.37038486996514214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya peach peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'papaya peach peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'papaya peach peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'peach blueberry kiwi cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3093505814873631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09092799496834543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08170855750432897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06559772886990725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04179924560555587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04086346679514825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037029703382255134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.027733094871663748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.027733094871663748}]
result = search.search('peach blueberry kiwi cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'peach blueberry kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'peach blueberry kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'peach blueberry kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9594410325437385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8832741091858685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8811396948927165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8004063490829838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8004063490829838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7615841229540384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6868235962439012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5994578186558659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5994578186558659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}]
result = search.search('peach blueberry kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'peach blueberry kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'peach blueberry kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'orange banana apricot tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10688190287446392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044026277828701735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange banana apricot tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'orange banana apricot tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'orange banana apricot tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'orange banana apricot tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9516390649100088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8984250260658612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange banana apricot tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'orange banana apricot tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'orange banana apricot tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'apple cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26418456595817313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11555335018456395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045037689905185516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04395164122282064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0392205188940866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'apple cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'apple cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'apple cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9713152447659877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9500257759078112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9494069992606079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8477613772137168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.819360065613399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'apple cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'apple cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'fig peach papaya blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10145884058201403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1010956568330695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0535533379995045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03791855372486537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037411236382729744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03703295495584969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.030296727558959683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021949407447519186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021949407447519186}]
result = search.search('fig peach papaya blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'fig peach papaya blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'fig peach papaya blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'fig peach papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8497871546324803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8497871546324803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8196190727244792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8086532808180864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6534438384962797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6386634230068775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2968211415435331}]
result = search.search('fig peach papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'fig peach papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'fig peach papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'blueberry kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0400580483740508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'blueberry kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'blueberry kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'blueberry kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.865864787505379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'blueberry kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'blueberry kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'coconut coconut pear coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3151389221165549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10899982209152681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09256134608628935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03689180722308935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03475633712669164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03322334564230769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03322334564230769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032605532847986674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.031121843066221663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.022830674573934957}]
result = search.search('coconut coconut pear coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #373 checking search results for 'coconut coconut pear coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'coconut coconut pear coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'coconut coconut pear coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9773933877107629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9129480303466566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7780496747699095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7776895321831628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7181309694915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7181309694915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7047767906039584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6727064629230906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2785739262264008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2785739262264008}]
result = search.search('coconut coconut pear coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #374 checking search results for 'coconut coconut pear coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'coconut coconut pear coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'kiwi apricot apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038888417384739506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('kiwi apricot apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #375 checking search results for 'kiwi apricot apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'kiwi apricot apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'kiwi apricot apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8197786283658526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}]
result = search.search('kiwi apricot apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #376 checking search results for 'kiwi apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'kiwi apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'apricot coconut coconut banana apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot coconut coconut banana apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #377 checking search results for 'apricot coconut coconut banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'apricot coconut coconut banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'apricot coconut coconut banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot coconut coconut banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #378 checking search results for 'apricot coconut coconut banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'apricot coconut coconut banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'coconut orange tomato kiwi papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26392651741831913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1025240051065912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07298115934428404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0617849685502975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04644316368055327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04011355073825715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0399512944849101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032178478729585354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.026436157620650828}]
result = search.search('coconut orange tomato kiwi papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #379 checking search results for 'coconut orange tomato kiwi papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'coconut orange tomato kiwi papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'coconut orange tomato kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9790347764050511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8670644850628043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8635572753501922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8617935261543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8185597362384435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7538840438153803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6955459084593757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6112671048199718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5714241938828836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
result = search.search('coconut orange tomato kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #380 checking search results for 'coconut orange tomato kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'coconut orange tomato kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #381 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #382 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'peach tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11320752984200066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03798447959373376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #383 checking search results for 'peach tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'peach tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'peach tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8210440769559838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #384 checking search results for 'peach tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'peach tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #385 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #386 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'peach papaya apricot coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2897080601905067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09556310627872887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09090486711462029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06848275437523192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044915361649018444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03520240304770592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03174404655708439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.031177162338200427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach papaya apricot coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #387 checking search results for 'peach papaya apricot coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'peach papaya apricot coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'peach papaya apricot coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9468282856796746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8985203747443992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.835608676534103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8004063490829838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.764125688358035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.760908792908782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6861555478203457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6739022028959814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach papaya apricot coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #388 checking search results for 'peach papaya apricot coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'peach papaya apricot coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking search results for 'coconut fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2897566377186737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10838102249596974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04636687542255846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043600173718373186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.041518259392866914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030457382201234822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.023693410736114057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01719309262899024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01719309262899024}]
result = search.search('coconut fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #389 checking search results for 'coconut fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #389 checking search results for 'coconut fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking search results for 'coconut fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9424287174287822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9110262854821454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8986710364097462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8974276158217794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.49946367223939564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3716330200800424}]
result = search.search('coconut fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #390 checking search results for 'coconut fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #390 checking search results for 'coconut fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking search results for 'papaya cherry coconut fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2747242896143676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11171655897866428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07130312195395731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040504519209152025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03948905626491672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03441258047252366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03261230015414683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03131727769645781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02531893917367504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya cherry coconut fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #391 checking search results for 'papaya cherry coconut fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #391 checking search results for 'papaya cherry coconut fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking search results for 'papaya cherry coconut fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9390640483850778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8755153668634262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8520486847807046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8324402626119431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7438365793590537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7049230676281317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5972123944456701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5472752362463347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.38212524024957445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya cherry coconut fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #392 checking search results for 'papaya cherry coconut fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #392 checking search results for 'papaya cherry coconut fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking search results for 'orange peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2948637039317377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08633886429861432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07505800504193834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05299708084078069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04639549421980224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04233866345123355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.033631917224947495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.033460723931863556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #393 checking search results for 'orange peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #393 checking search results for 'orange peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking search results for 'orange peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9780298909461547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9151608558197205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9145104405484823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7269623469784852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7257449046269937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7232619609048967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6286621074229607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #394 checking search results for 'orange peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #394 checking search results for 'orange peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking search results for 'cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #395 checking search results for 'cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #395 checking search results for 'cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking search results for 'cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #396 checking search results for 'cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #396 checking search results for 'cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking search results for 'tomato orange lime blueberry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2774273497389862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10531799280780524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07838652563184757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045019339745714544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.042703470244920536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.042216807977369986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.037009704575228335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.035271789361041334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.032206883039731404}]
result = search.search('tomato orange lime blueberry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #397 checking search results for 'tomato orange lime blueberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #397 checking search results for 'tomato orange lime blueberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking search results for 'tomato orange lime blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9731043479344058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8899420255465039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8852791528673575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8604321401617244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7999740698407469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.76240859551751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6961598747649528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6565407429860012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5210565868781275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
result = search.search('tomato orange lime blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #398 checking search results for 'tomato orange lime blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #398 checking search results for 'tomato orange lime blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking search results for 'cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27334194193079353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11318953827718124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04683681160418476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045703366332529576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04409116581499072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #399 checking search results for 'cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #399 checking search results for 'cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking search results for 'cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9878897545950132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9873329838558978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9530416350486022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9514455781770661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #400 checking search results for 'cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #400 checking search results for 'cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking search results for 'kiwi orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04508149302055014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044057724095804975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044026277828701735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('kiwi orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #401 checking search results for 'kiwi orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #401 checking search results for 'kiwi orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking search results for 'kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9516390649100088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.950330381086011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #402 checking search results for 'kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #402 checking search results for 'kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #403 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #403 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #404 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #404 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking search results for 'cherry pear pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3086973645975839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10867452409460727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08545931038891283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04216380160301393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04211024054297385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.025783348793270624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0147606889638464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0147606889638464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry pear pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #405 checking search results for 'cherry pear pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #405 checking search results for 'cherry pear pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking search results for 'cherry pear pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9574151010449468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9102234372247154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9102234372247153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8888246364680452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7183515740163101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5573135669416232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.31905600327231876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.31905600327231876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry pear pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #406 checking search results for 'cherry pear pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #406 checking search results for 'cherry pear pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking search results for 'cherry apricot orange blueberry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2848440328131797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1122325572259385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07558698914880897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04530401755059417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04137726685004366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04087089852330702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03840060984443414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.029194221565955414}]
result = search.search('cherry apricot orange blueberry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #407 checking search results for 'cherry apricot orange blueberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #407 checking search results for 'cherry apricot orange blueberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking search results for 'cherry apricot orange blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9792577302641667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9434014125813514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8834347478585991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8722442656452133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6330927109706134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.631040439527901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('cherry apricot orange blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #408 checking search results for 'cherry apricot orange blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #408 checking search results for 'cherry apricot orange blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #409 checking search results for 'peach apricot peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2740541731498867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11631809701132828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05544746479862905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04742711474265921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04507204503958864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.039357473416394735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.03872916154670821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach apricot peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'peach apricot peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'peach apricot peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'peach apricot peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9997767377991618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9742435861133247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9742435861133247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8507216836482423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8499703397861199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6765554788244712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.3255485450420766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach apricot peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'peach apricot peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'peach apricot peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'apricot apricot pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28487235510929493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04616272400490676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04239520044987674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot apricot pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'apricot apricot pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'apricot apricot pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'apricot apricot pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9731230302322413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8835225885631427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot apricot pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'apricot apricot pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'apricot apricot pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'coconut cherry papaya fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2945517018360109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09760885871482787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08785043567167074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04143634335617225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04010714846604452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03550204784682146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03273323224010809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03178957430383981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.031292219106376314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.030921805720703657}]
result = search.search('coconut cherry papaya fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'coconut cherry papaya fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'coconut cherry papaya fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'coconut cherry papaya fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9135427759284882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8669260983391882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.820477920739564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7358074597975156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6900256177127652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6871396415136248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6763891838691284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6683826054038039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5055954356413327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2845508380735398}]
result = search.search('coconut cherry papaya fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'coconut cherry papaya fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'coconut cherry papaya fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'orange coconut lime banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2896082275162753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09100002937522739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08499155452947675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04529846465857546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.040035977731956975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.040035977731956975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03895846506644128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03524903693480346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0267982252998087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange coconut lime banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'orange coconut lime banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'orange coconut lime banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'orange coconut lime banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9549042034160627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.898210746866586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8653877250272415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8653877250272415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8420970178402813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7649256007301681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7118623756893087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5792503778035082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.43009953923298355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange coconut lime banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'orange coconut lime banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'orange coconut lime banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'banana blueberry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11434339965985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.049943869505471396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04347110321931072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana blueberry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'banana blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'banana blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'banana blueberry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana blueberry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'banana blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'banana blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'cherry peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04700050552572875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04166740493176235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'cherry peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'cherry peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'cherry peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.990783697140204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9006514341450588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'cherry peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'cherry peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'fig papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3096450787714189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11424938467580438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07495586913181805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06379167307753707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03692405518506568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03601019079492299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03601019079492299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.029044614692774674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029044614692774674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'fig papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'fig papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'fig papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9603544065446447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9603544065446447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7783693281690731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7783693281690731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7783693281690731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7783693281690731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6278066493480504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6278066493480504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6278066493480504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'fig papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'fig papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'lime blueberry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2999372132854783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11310109710537064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09809262118059654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058108714191464704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04123605518358695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038732724583983275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464698}]
result = search.search('lime blueberry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'lime blueberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'lime blueberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'lime blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9472990125221563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9302457691506432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8913277008828477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8245443182701955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7090273486165375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896257}]
result = search.search('lime blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'lime blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'lime blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'apricot orange blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11788333578620874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407020069458892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04414631023537236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044057724095804975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('apricot orange blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'apricot orange blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'apricot orange blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'apricot orange blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9909005751034301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9554159176326601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}]
result = search.search('apricot orange blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'apricot orange blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'apricot orange blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'pear apple papaya coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2703726323399969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11324236838683342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09529686168098306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.046527430698002775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04445598746798282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03569540880157311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.030800156205081638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03016790175518315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01478179670654882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear apple papaya coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'pear apple papaya coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'pear apple papaya coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'pear apple papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9518896560926424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9371445504864845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8385521575444392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7981763685523883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7715652362363523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6657531205369769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6520867816330248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5677155532481257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.31951225243800674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear apple papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'pear apple papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'pear apple papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'kiwi banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038888417384739506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('kiwi banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'kiwi banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'kiwi banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'kiwi banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8197786283658526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}]
result = search.search('kiwi banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'kiwi banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'kiwi banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'banana cherry coconut banana lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29146176752337377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09798997668236749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07911422423869519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04662125500931216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04385438269286965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04087089852330702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03840060984443414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana cherry coconut banana lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'banana cherry coconut banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'banana cherry coconut banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'banana cherry coconut banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9827889910281205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9479235083289531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9039594425041416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8236815119061913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6626357163268721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana cherry coconut banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'banana cherry coconut banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'banana cherry coconut banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'fig apple papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26808046481989806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11484400132389777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09215920395027943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04910121087540568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037669988833599816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03571072686011265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029412029356386274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.026447398367723824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig apple papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'fig apple papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'fig apple papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'fig apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9653526191811652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8314430725649539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.814246280102451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7718963399231442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7718963399231442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5991201465263888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5575184956291365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'fig apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'fig apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'fig apple tomato banana kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2724069507952475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11084226110397839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10577410203077764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04636687542255846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04363367322132316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043073242983367205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0415009294599691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.02043852552873653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01719309262899024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01719309262899024}]
result = search.search('fig apple tomato banana kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'fig apple tomato banana kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'fig apple tomato banana kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'fig apple tomato banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9431528176079138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9283797167033472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8970530249648827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.889113103513045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8448615318143827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5255684572228688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4308497889745206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3716330200800424}]
result = search.search('fig apple tomato banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'fig apple tomato banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'fig apple tomato banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'blueberry tomato tomato kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0400580483740508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry tomato tomato kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'blueberry tomato tomato kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'blueberry tomato tomato kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'blueberry tomato tomato kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.865864787505379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry tomato tomato kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'blueberry tomato tomato kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'blueberry tomato tomato kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'papaya kiwi orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2697124020714999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10326081077386107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06865223963796284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06823094668999653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.058459268792147315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046240157462122934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03965991348451094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02919422156595541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02917338414622765}]
result = search.search('papaya kiwi orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'papaya kiwi orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'papaya kiwi orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'papaya kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9747553489948766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8679869474259994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8572590017638744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8365044742736408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8325361849481518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6310404395279009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6305900334612783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5750094427102465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4685542084711366}]
result = search.search('papaya kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'papaya kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'papaya kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'pear peach blueberry kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074058851342928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11579063073579636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09144866303976223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05370168318579823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.048353063690220584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04289785473509124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04162626000797164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028183221029823312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear peach blueberry kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'pear peach blueberry kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'pear peach blueberry kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'pear peach blueberry kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9698256954408354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9534096183857209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9042986801610172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8997620762721463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7686967135276934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6091874087408865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5899914500396813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.43042190192548907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear peach blueberry kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'pear peach blueberry kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'pear peach blueberry kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'lime apple apricot peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.275744302573069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10547613571113809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06802182654871261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06727991414163317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045222679397635676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03871846108947347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime apple apricot peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'lime apple apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'lime apple apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'lime apple apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9533066290882387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.855212222672242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8369092715332921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8209319342673969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5717760410932535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime apple apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'lime apple apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'lime apple apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'peach kiwi kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3220475911172817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11478182632914861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.09272905062366474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07879010442347066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04447675623105992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04447675623105992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03698262211581106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach kiwi kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'peach kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'peach kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'peach kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.998820405845626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9613762688419486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9613762688419485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9613762688419485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9613762688419485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7796039353190387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7432283676303445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'peach kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'peach kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'fig blueberry pear banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11594525958169101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11553022000696625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04542188940405291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03682153407668069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03391641544535641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03204943318149185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.024187257096552783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig blueberry pear banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'fig blueberry pear banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'fig blueberry pear banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'fig blueberry pear banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9818055600135069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9711208177409045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9711208177409045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7331118475447582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6756109438317381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig blueberry pear banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'fig blueberry pear banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'fig blueberry pear banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'apple coconut peach apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2778089544556317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10547613571113809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07240236553680192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06802182654871261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045222679397635676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040870898523307025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040870898523307025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029313776144673936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029239189453267648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple coconut peach apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'apple coconut peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'apple coconut peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'apple coconut peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9533066290882387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8616156751064514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6336246418068234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6320124317185489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5717760410932535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple coconut peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'apple coconut peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'apple coconut peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'fig peach coconut banana lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29156017083108854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0991134067964434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04273754914363994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.040740997928993335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040271216332424066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03091893399397532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01478179670654882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01478179670654882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig peach coconut banana lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'fig peach coconut banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'fig peach coconut banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'fig peach coconut banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9237828703539614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9042646372469658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8704724665229965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8331248105599148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6517797072930487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4971110124104067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.31951225243800674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.31951225243800674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig peach coconut banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'fig peach coconut banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'fig peach coconut banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0400580483740508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.865864787505379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'cherry papaya tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2948637039317377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10309083647737671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05299708084078069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.04830200317876408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04653871973388704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04448994844629568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0439633104224351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.034861673647887205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry papaya tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'cherry papaya tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'cherry papaya tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'cherry papaya tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9810491245221012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9616614218912227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9502780085914954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9145104405484823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8665581820537283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7535438412612129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.40456229943955613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.40456229943955613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry papaya tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'cherry papaya tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'cherry papaya tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26418456595817313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11280229029007091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07723371404100288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04160041608432924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9481904594567138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9423856000300839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8769483134184535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8193600656133991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'kiwi orange lime blueberry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28434795988915273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.09918539511639447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09088584833417988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0740580469383203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05367497006732264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040650258527662464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03661828138456368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0364895248142197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.018278987956211492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.018278987956211492}]
result = search.search('kiwi orange lime blueberry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'kiwi orange lime blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'kiwi orange lime blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'kiwi orange lime blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8818961933934449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8786655588766489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.794976318740782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7887302535163824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7719235316151586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7612311160783495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6549279612092292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6225151401832291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3951049206074428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3951049206074428}]
result = search.search('kiwi orange lime blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'kiwi orange lime blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'kiwi orange lime blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'papaya apple lime peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3046610814981995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09989485369713466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07297514855820389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06641992574419832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045872085745830654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03794952715787342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03500242875653696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03500242875653695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02678791207982221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya apple lime peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'papaya apple lime peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'papaya apple lime peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'papaya apple lime peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.966996295091059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9448966968257181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8396934759114967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8202885712666799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8104385805293479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7565862983251039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7565862983251038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6112167603771332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5790274549604202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya apple lime peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'papaya apple lime peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'papaya apple lime peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'fig apricot fig blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3091567317468595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10446413428261415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08629119885082358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04604009976676315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04447982315049945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.028004696575407256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.018395670168704376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.010647827650638752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.010384295639500628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.010384295639500628}]
result = search.search('fig apricot fig blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #475 checking search results for 'fig apricot fig blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'fig apricot fig blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'fig apricot fig blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9951683324417433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9614425610767574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9588398137120397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8781018118290681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7227477854134502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2244591611985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2244591611985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2244591611985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.2244591611985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.2244591611985216}]
result = search.search('fig apricot fig blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'fig apricot fig blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'fig apricot fig blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'banana fig peach fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31298073263927795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1158949966576391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11104929287373869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04590060475603996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045886444878533376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.029396966707304083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.017015625529286444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana fig peach fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'banana fig peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'banana fig peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'banana fig peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9921531127113647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9918470433988049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9706998313885219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9706998313885219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9334551608972235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana fig peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'banana fig peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'banana fig peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #479 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'fig papaya fig tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31298073263927795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11548013700491112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11144823482403551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04318502441698619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04318502441698619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.029396966707304083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.017015625529286444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01659449155119871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01659449155119871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig papaya fig tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'fig papaya fig tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'fig papaya fig tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'fig papaya fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9706998313885219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9706998313885219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9334551608972235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9334551608972235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9334551608972235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.358694107275738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig papaya fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'fig papaya fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'fig papaya fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'fig peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26808046481989806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11240130079047002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09597004548480667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0521030997012669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.042498918502119565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04059977386856608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.02965772512796838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.015599488437619373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.015599488437619373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'fig peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'fig peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'fig peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9414377399524093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9186248090379698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.87757432027679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.831443072564954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8067024285439564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6251930744653588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'fig peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'fig peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'banana peach papaya apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07396757065598898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04515414587212143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana peach papaya apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'banana peach papaya apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'banana peach papaya apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'banana peach papaya apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9518619233552358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.902532971784904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana peach papaya apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'banana peach papaya apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'banana peach papaya apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
