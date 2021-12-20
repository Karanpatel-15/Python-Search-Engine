
import testingtools
import crawler
import searchdata
import search

output = open('fruits3-incoming-links-failed.txt', 'w')
success_output = open('fruits3-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')



#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-969.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-505.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-622.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-106.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-106.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-106.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-106.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-504.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-888.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-539.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-766.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-766.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-766.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-766.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-688.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-741.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-741.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-741.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-741.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-678.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-716.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-716.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-716.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-716.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-163.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-46.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-296.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-197.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-637.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-662.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-591.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-591.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-591.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-591.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html\n\n')
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
