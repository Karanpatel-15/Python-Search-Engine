
import testingtools
import crawler
import searchdata
import search

output = open('fruits4-incoming-links-failed.txt', 'w')
success_output = open('fruits4-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')



#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-955.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-108.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-955.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-955.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-955.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-187.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-540.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-984.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-713.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-205.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-985.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-432.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-584.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-584.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-584.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-584.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-31.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-610.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-198.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-198.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-198.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-198.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-933.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-570.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-663.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-811.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-19.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-667.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-827.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-827.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-537.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-537.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-537.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-537.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-708.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-437.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-655.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-797.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-797.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-797.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-797.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html\n\n')
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
