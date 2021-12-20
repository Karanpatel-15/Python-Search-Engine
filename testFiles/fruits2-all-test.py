
import testingtools
import crawler
import searchdata
import search

output = open('fruits2-all-failed.txt', 'w')
success_output = open('fruits2-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-132.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-408.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-872.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-872.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-996.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-220.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-504.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-244.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-454.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-554.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-504.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-504.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-504.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-178.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-456.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-573.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-314.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-314.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-314.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-314.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-632.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-422.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-343.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-607.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-674.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-835.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-214.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-214.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-214.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-214.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-731.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-684.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-522.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-731.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-731.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-731.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-611.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-611.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-611.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-611.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-911.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-484.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-632.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-719.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-760.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-876.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-876.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-876.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-876.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-386.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-507.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-503.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-245.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-842.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-243.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-703.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-703.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-703.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-703.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-346.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-530.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-554.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-744.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-681.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-167.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-358.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-981.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-808.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-501.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-169.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-511.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-904.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-904.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-904.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-904.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-380.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-383.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-380.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-380.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-380.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-97.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-541.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-220.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-188.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-188.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-188.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-188.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-74.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-230.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-659.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-680.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-724.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-693.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-701.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-243.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-701.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-196.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-391.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-289.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-750.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-391.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-391.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-391.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-378.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-378.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-378.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-378.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-882.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-912.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-882.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-882.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-882.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-511.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-178.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-138.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-743.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-955.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-474.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-402.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-474.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-474.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-474.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-436.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-241.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-436.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-436.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-436.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-137.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-891.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-137.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-137.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-137.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-526.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-241.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-132.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-207.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-207.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-207.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-207.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-475.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-927.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-704.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-475.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-475.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-475.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-646.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-646.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-646.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-646.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-158.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-519.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-956.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-779.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-134.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-630.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-915.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-915.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-915.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-915.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-141.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-769.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-735.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-227.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-735.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-735.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-735.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html
expected = 0.0009961028115036638
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html
expected = 0.0003438218019261909
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-730.html
expected = 0.0006473858218226792
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-730.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-730.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-730.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html
expected = 0.0006433929373533065
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html
expected = 0.0006117346950115209
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html
expected = 0.0006042969063994933
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html
expected = 0.000645074407619179
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html
expected = 0.00035408157577578194
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html
expected = 0.0003544590493815487
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html
expected = 0.0006340651756395578
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-957.html
expected = 0.0004199326969020273
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-957.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-957.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-957.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-761.html
expected = 0.00036417787580021743
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-761.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-761.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-761.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html
expected = 0.002591397446719917
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html
expected = 0.000879736277125831
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-654.html
expected = 0.0003438218019261909
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-654.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-654.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-654.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-267.html
expected = 0.0012442784194328464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-267.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-267.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-267.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html
expected = 0.0018105112701118557
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html
expected = 0.0020006686145882927
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-616.html
expected = 0.0003499613731749362
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-616.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-616.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-616.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-421.html
expected = 0.0006463822340917242
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-421.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-421.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-421.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html
expected = 0.000393964040496451
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html
expected = 0.0003833181923609193
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html
expected = 0.0011096996318792093
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html
expected = 0.0008697562775437425
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-376.html
expected = 0.0006224139820615838
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-376.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-376.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-376.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html
expected = 0.0014202866849949546
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html
expected = 0.0006237444462155389
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-254.html
expected = 0.0005983631397501793
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-254.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-254.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-254.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html
expected = 0.0011525972776167117
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html
expected = 0.000861825702940806
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-284.html
expected = 0.0009027387253613386
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-284.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-284.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-284.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html
expected = 0.0006087499710119376
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html
expected = 0.0004098880150877093
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html
expected = 0.0011165864028038171
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-722.html
expected = 0.0003570099185522668
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-722.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-722.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-722.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html
expected = 0.0009168826188400945
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html
expected = 0.0005948213116597534
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html
expected = 0.0003551391323545657
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-555.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html
expected = 0.001484414928024238
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html
expected = 0.0007259920219029112
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-489.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html
expected = 0.0003833181923609193
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html
expected = 0.0008612796994556053
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html
expected = 0.0006169524242927133
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-811.html
expected = 0.0003967163025833065
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-811.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-811.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-811.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html
expected = 0.0017299892230959381
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-940.html
expected = 0.0009352138171428194
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-940.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-940.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-940.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html
expected = 0.0036697700843585515
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
expected = 0.0008950906241345888
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html
expected = 0.000653761986141421
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-784.html
expected = 0.0009663933779912379
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-784.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-784.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-784.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #153 checking IDF for word pear
expected = 0.052894948432125555
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apple
expected = 0.05439229681862769
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word coconut
expected = 0.05739166388833648
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word banana
expected = 0.052894948432125555
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word peach
expected = 0.05139915250664415
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word pear
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word apple
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word peach
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word coconut
expected = 0.3076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-734.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word pear
expected = 0.26153846153846155
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word banana
expected = 0.16923076923076924
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word apple
expected = 0.2153846153846154
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word peach
expected = 0.16923076923076924
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word coconut
expected = 0.18461538461538463
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word pear
expected = 0.17582417582417584
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word banana
expected = 0.18681318681318682
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word apple
expected = 0.24175824175824176
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word peach
expected = 0.25274725274725274
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word coconut
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word pear
expected = 0.13541666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word banana
expected = 0.21875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word apple
expected = 0.2604166666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word peach
expected = 0.17708333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word coconut
expected = 0.20833333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-933.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word pear
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word banana
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word apple
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word peach
expected = 0.21428571428571427
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word coconut
expected = 0.21428571428571427
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word pear
expected = 0.17307692307692307
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word banana
expected = 0.11538461538461539
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word apple
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word coconut
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word pear
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word banana
expected = 0.24489795918367346
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word apple
expected = 0.20408163265306123
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word peach
expected = 0.1836734693877551
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word coconut
expected = 0.22448979591836735
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word pear
expected = 0.24096385542168675
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word banana
expected = 0.1686746987951807
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word apple
expected = 0.20481927710843373
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word peach
expected = 0.24096385542168675
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word coconut
expected = 0.14457831325301204
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word pear
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word banana
expected = 0.19047619047619047
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word apple
expected = 0.38095238095238093
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word peach
expected = 0.23809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word coconut
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word pear
expected = 0.15053763440860216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word banana
expected = 0.17204301075268819
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word apple
expected = 0.23655913978494625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word peach
expected = 0.22580645161290322
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word coconut
expected = 0.21505376344086022
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word coconut
expected = 0.007204426192163225
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word pear
expected = 0.01274811099497782
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word apple
expected = 0.02940275584984526
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word peach
expected = 0.006452180952521823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word banana
expected = 0.01274811099497782
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word coconut
expected = 0.018475989017987995
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word pear
expected = 0.011763435658286957
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word apple
expected = 0.017510408491368753
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word peach
expected = 0.011430781980593952
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word banana
expected = 0.011763435658286957
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word coconut
expected = 0.02110473897711014
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word pear
expected = 0.013501808773965762
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word apple
expected = 0.015976714781553193
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word peach
expected = 0.008999308332265378
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word banana
expected = 0.0114109579887073
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word coconut
expected = 0.016171304712786553
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word pear
expected = 0.012402027500255569
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word apple
expected = 0.020232236146893463
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word peach
expected = 0.010805012001753465
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word banana
expected = 0.011119454791931986
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word coconut
expected = 0.017683651211937695
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word pear
expected = 0.010189951463465836
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word apple
expected = 0.013681771275836127
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word peach
expected = 0.009901793740815552
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word banana
expected = 0.019178125652085806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word coconut
expected = 0.018220831130758352
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word pear
expected = 0.010920208517406584
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word apple
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word peach
expected = 0.015397144612199315
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word banana
expected = 0.011930968721824049
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word coconut
expected = 0.017643834587520443
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word pear
expected = 0.018539533810117192
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word apple
expected = 0.016721743592769678
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word peach
expected = 0.007905463925462002
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word banana
expected = 0.009831401329500332
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word coconut
expected = 0.015859108984895787
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word pear
expected = 0.01248677074027039
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word apple
expected = 0.01284024581822718
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word peach
expected = 0.015551469959112848
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word banana
expected = 0.013913191332453308
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word coconut
expected = 0.014127565687120784
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word pear
expected = 0.01667260579141209
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word apple
expected = 0.011046633023062394
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word peach
expected = 0.018251579942861376
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word banana
expected = 0.00996779328679376
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word coconut
expected = 0.014228972520225284
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word pear
expected = 0.017976348377239947
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word apple
expected = 0.011392649632950388
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word peach
expected = 0.011761086769168386
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word banana
expected = 0.015096335649132837
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-477.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
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


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #291 checking search results for 'tomato apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'tomato apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'tomato apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'tomato apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'tomato apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'tomato apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'tomato banana banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01460418145865464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011341918522567279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010619364342611999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00982783343037611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00940685855880851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009003992010225568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00895125276263384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007766749348386874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007609340945087184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007396743550699649}]
result = search.search('tomato banana banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'tomato banana banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'tomato banana banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'tomato banana banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html', 'title': 'N-449', 'score': 0.9999996424209996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-509.html', 'title': 'N-509', 'score': 0.9999976933001928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html', 'title': 'N-485', 'score': 0.9999976887500056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html', 'title': 'N-871', 'score': 0.9999954265857062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9999910474555675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html', 'title': 'N-800', 'score': 0.999984369084765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.9999785868338457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html', 'title': 'N-790', 'score': 0.9999697154805854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999627731843339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-434.html', 'title': 'N-434', 'score': 0.9999317885459306}]
result = search.search('tomato banana banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'tomato banana banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'tomato banana banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'peach apple banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015308099512549434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011755002128742413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010760933399560926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010319186143919697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010294891389279024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009338517799835138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008288573039892621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0076922558838949965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007626783615365797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074137476204403}]
result = search.search('peach apple banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'peach apple banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'peach apple banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'peach apple banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 0.9999717949947918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-599.html', 'title': 'N-599', 'score': 0.9998263196165378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9996489517362085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-336.html', 'title': 'N-336', 'score': 0.9993721928558164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-448.html', 'title': 'N-448', 'score': 0.9993476204580279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-454.html', 'title': 'N-454', 'score': 0.9991400435734373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-602.html', 'title': 'N-602', 'score': 0.9989389645053885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-950.html', 'title': 'N-950', 'score': 0.9989333009704168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html', 'title': 'N-824', 'score': 0.9989324659750758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html', 'title': 'N-110', 'score': 0.9988553058317361}]
result = search.search('peach apple banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'peach apple banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'peach apple banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'pear tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00913551662149082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074999419284363135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605518}]
result = search.search('pear tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'pear tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'pear tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'pear tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html', 'title': 'N-890', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}]
result = search.search('pear tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'pear tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'pear tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'banana peach coconut peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013815520723623884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011108572972187761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010570184961328381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009980629398751722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009960482883737413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009460769132192893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008821413053481329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007423745265845101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006777992233639497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0066403227029770764}]
result = search.search('banana peach coconut peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'banana peach coconut peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'banana peach coconut peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'banana peach coconut peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999332303387874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.998917904535495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9986380857949216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9985090600748486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9964543734868033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html', 'title': 'N-419', 'score': 0.9963363988727842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9956355149898338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-540.html', 'title': 'N-540', 'score': 0.9951978268310447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-558.html', 'title': 'N-558', 'score': 0.9949893462258304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9948201179263864}]
result = search.search('banana peach coconut peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'banana peach coconut peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'banana peach coconut peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'apple apple banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016568716386636952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011680811395381704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011617433494753051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009952300364999937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009857185184309497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009522658567342964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008793328256998132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0075897250718065905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006839052805482695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006558178298545398}]
result = search.search('apple apple banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'apple apple banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'apple apple banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'apple apple banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 0.9999722162695387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999516618034076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html', 'title': 'N-544', 'score': 0.9999180400392951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999180400392951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html', 'title': 'N-567', 'score': 0.9998110050235314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9996545502136515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.999506538493108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9989389454405911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html', 'title': 'N-563', 'score': 0.9985949733487115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.998351732477799}]
result = search.search('apple apple banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'apple apple banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'apple apple banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'apple apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841191379828556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01199134932809723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011798973355287852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01158476561985825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010711607372568214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01011938684436538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009079051557281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007608689318007255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007237080178135317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006561103035845456}]
result = search.search('apple apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'apple apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'apple apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'apple apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999993684453062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html', 'title': 'N-563', 'score': 0.9999989069830075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html', 'title': 'N-539', 'score': 0.9999980092064268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html', 'title': 'N-645', 'score': 0.9999970396372632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html', 'title': 'N-567', 'score': 0.9999965212980642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html', 'title': 'N-18', 'score': 0.9999919601256966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-678.html', 'title': 'N-678', 'score': 0.9999841608388886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-638.html', 'title': 'N-638', 'score': 0.9999840182067132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html', 'title': 'N-384', 'score': 0.9999810635007813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'title': 'N-629', 'score': 0.9999762396805963}]
result = search.search('apple apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'apple apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'apple apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'banana pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01670941806909784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071491793215802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011848532967550791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011012325687601347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010430880092533866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.0100485896996318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008988847823103913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007739110753157671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007492835360319172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006700433037127445}]
result = search.search('banana pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'banana pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'banana pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'banana pear tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html', 'title': 'N-463', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'title': 'N-445', 'score': 1.0000000000000002}]
result = search.search('banana pear tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'banana pear tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'banana pear tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'pear tomato tomato coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017229531486511136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012023882482142177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011705469401483247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011540466614666291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009939785691461454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00989199677258067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007882867905364015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007818172212497523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007428054995000698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006215288195668343}]
result = search.search('pear tomato tomato coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'pear tomato tomato coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'pear tomato tomato coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'pear tomato tomato coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.9999951396893352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-252.html', 'title': 'N-252', 'score': 0.9999951396893352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html', 'title': 'N-127', 'score': 0.9999932723897959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-916.html', 'title': 'N-916', 'score': 0.9999900789790983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html', 'title': 'N-544', 'score': 0.9999900789790983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html', 'title': 'N-726', 'score': 0.9999844939350494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-781.html', 'title': 'N-781', 'score': 0.9999821828104631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html', 'title': 'N-697', 'score': 0.9999770160259884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html', 'title': 'N-668', 'score': 0.9999752008103824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-190.html', 'title': 'N-190', 'score': 0.9999724258407627}]
result = search.search('pear tomato tomato coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'pear tomato tomato coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'pear tomato tomato coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'coconut apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018155422472989447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012135615749216592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011945735836534152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011529346327257812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010927471730758476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00992315666944262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007991416549650202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007346464886527882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007211855160279439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006021675981018596}]
result = search.search('coconut apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'coconut apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'coconut apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-849.html', 'title': 'N-849', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html', 'title': 'N-642', 'score': 0.9999999505477939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'title': 'N-88', 'score': 0.9999997272259222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9999996040558455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-886.html', 'title': 'N-886', 'score': 0.9999995427334912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html', 'title': 'N-441', 'score': 0.9999951977319469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html', 'title': 'N-411', 'score': 0.9999941804094368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9999904324585521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-366.html', 'title': 'N-366', 'score': 0.9999818215869007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-490.html', 'title': 'N-490', 'score': 0.9999761345368776}]
result = search.search('coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'tomato pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'tomato pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'tomato pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'tomato pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'tomato pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'tomato pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'peach pear tomato coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016544743194866922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012096045075694437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656252381931626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011186199528798868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010782133225058948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010112747489637223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008902579410935248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0077403903079628035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007203921054599602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006782981161312071}]
result = search.search('peach pear tomato coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'peach pear tomato coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'peach pear tomato coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'peach pear tomato coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-81.html', 'title': 'N-81', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html', 'title': 'N-226', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-401.html', 'title': 'N-401', 'score': 1.0}]
result = search.search('peach pear tomato coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'peach pear tomato coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'peach pear tomato coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'pear apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00913551662149082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074999419284363135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605518}]
result = search.search('pear apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'pear apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'pear apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'pear apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html', 'title': 'N-890', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}]
result = search.search('pear apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'pear apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'pear apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #329 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'banana coconut coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018413884892511202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157352786391951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011602461030633612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01150200383979258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01076111780331539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009988305498192547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008116343210390104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00693117179229023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006197430981442359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006183474173711641}]
result = search.search('banana coconut coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'banana coconut coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'banana coconut coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'banana coconut coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html', 'title': 'N-662', 'score': 0.9999985331658363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-886.html', 'title': 'N-886', 'score': 0.9999950127345395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html', 'title': 'N-37', 'score': 0.9999934943029772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.9999834639066093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html', 'title': 'N-411', 'score': 0.999888008223819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-358.html', 'title': 'N-358', 'score': 0.9998851695953119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html', 'title': 'N-105', 'score': 0.9998341238269666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html', 'title': 'N-365', 'score': 0.9998094294604977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-99.html', 'title': 'N-99', 'score': 0.9998014656458537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-564.html', 'title': 'N-564', 'score': 0.9997803042706872}]
result = search.search('banana coconut coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'banana coconut coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'banana coconut coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'coconut tomato apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016732641273120536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011704507637273046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011696140257387163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011190958395635414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01092315549960318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010113972855512536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008928495257767032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007852915150706486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00742168295495411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007197966155296847}]
result = search.search('coconut tomato apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'coconut tomato apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'coconut tomato apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'coconut tomato apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-534.html', 'title': 'N-534', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html', 'title': 'N-61', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html', 'title': 'N-403', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html', 'title': 'N-888', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html', 'title': 'N-672', 'score': 1.0}]
result = search.search('coconut tomato apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'coconut tomato apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'coconut tomato apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'peach peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015275702619357064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012131426519985538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010829113102607224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01025896274038732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009929737981517944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009888568427557124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009065150261828974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007397560448250057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00730132920243378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006431186371832145}]
result = search.search('peach peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'peach peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'peach peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'peach peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html', 'title': 'N-887', 'score': 0.9999999214035166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-230.html', 'title': 'N-230', 'score': 0.9999998103886395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9999958443242492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html', 'title': 'N-805', 'score': 0.9999942094136727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'title': 'N-1', 'score': 0.9999934638575094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.9999934638575094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-369.html', 'title': 'N-369', 'score': 0.9999773626378128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.999954537558482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-358.html', 'title': 'N-358', 'score': 0.9999353338907572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999353338907572}]
result = search.search('peach peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'peach peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'peach peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'apple apple apple banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018208242235240354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011514811012056723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011099275205707124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00985743244759285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009800608139956861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009653372933740424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00843433331760543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0072368796350159624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0067083712467304836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006164642614799608}]
result = search.search('apple apple apple banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'apple apple apple banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'apple apple apple banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'apple apple apple banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9997285651950937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-552.html', 'title': 'N-552', 'score': 0.9996480860706939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html', 'title': 'N-319', 'score': 0.998602538080594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-543.html', 'title': 'N-543', 'score': 0.9982288717653746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9968659058349725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.9966756237150385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html', 'title': 'N-870', 'score': 0.9955761456383451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-480.html', 'title': 'N-480', 'score': 0.9941170445337266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html', 'title': 'N-919', 'score': 0.9937483073536718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-308.html', 'title': 'N-308', 'score': 0.9920790415183427}]
result = search.search('apple apple apple banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'apple apple apple banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'apple apple apple banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'peach peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'peach peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'peach peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'peach peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'peach peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'peach peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'apple apple banana peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016665109467231376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011326608000369474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011260163869828175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010352567297512234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01023577548520087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009774156728599668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880954898124663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007657702116213575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00707531271403659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006805817422216947}]
result = search.search('apple apple banana peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'apple apple banana peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'apple apple banana peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'apple apple banana peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 0.9999978998960868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 0.9999773389798088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html', 'title': 'N-298', 'score': 0.9990178090825302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9987228888761215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-678.html', 'title': 'N-678', 'score': 0.9986562134268162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html', 'title': 'N-429', 'score': 0.9982314756116819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html', 'title': 'N-18', 'score': 0.9981862043235759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html', 'title': 'N-645', 'score': 0.9981293087742303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html', 'title': 'N-785', 'score': 0.9975629756555439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html', 'title': 'N-233', 'score': 0.9964686122282016}]
result = search.search('apple apple banana peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'apple apple banana peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'apple apple banana peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'peach pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0153367109130787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011815580312580499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011386442498910248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011385532086944958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010516463499601194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010084310069385542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009029954973510753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007689115353880961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623426302802696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006869536972819043}]
result = search.search('peach pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'peach pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'peach pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'peach pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 1.0}]
result = search.search('peach pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'peach pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'peach pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'tomato banana coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017189970231673745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01208706964257492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011693076294116908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011206269293521722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010832104155960764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009982414809500503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00910552204361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850441844377493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007288029773052713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006736919019056488}]
result = search.search('tomato banana coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'tomato banana coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'tomato banana coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'tomato banana coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}]
result = search.search('tomato banana coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'tomato banana coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'tomato banana coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'banana peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0153367109130787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011815580312580497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011386442498910248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011385532086944958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010516463499601194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010084310069385542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009029954973510753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007689115353880962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623426302802697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006869536972819044}]
result = search.search('banana peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'banana peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'banana peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'banana peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 1.0}]
result = search.search('banana peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'banana peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'banana peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01832996118432234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012058969554624502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011874122316225049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011507913713472501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010891862743686864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010171409367176289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880626423413049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785054050421375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007426245523254142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007052512952506606}]
result = search.search('apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 1.0}]
result = search.search('apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'coconut tomato pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017269802677133614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012033074052391672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011717815525706152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011564082078209989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009969102234809535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009906813386835394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007885505025032618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007847518188321648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007427269770432032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006224576622147615}]
result = search.search('coconut tomato pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'coconut tomato pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'coconut tomato pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'coconut tomato pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-781.html', 'title': 'N-781', 'score': 0.9999999649802968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html', 'title': 'N-726', 'score': 0.9999997787202023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'title': 'N-100', 'score': 0.9999801550746676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.9999733432851377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.9999562712584065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-252.html', 'title': 'N-252', 'score': 0.9999562712584065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-923.html', 'title': 'N-923', 'score': 0.9999561866734799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html', 'title': 'N-127', 'score': 0.9999509731214115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-916.html', 'title': 'N-916', 'score': 0.9999428779221323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html', 'title': 'N-544', 'score': 0.9999428779221323}]
result = search.search('coconut tomato pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'coconut tomato pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'coconut tomato pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'pear apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018235792007146014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012008762783274146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011827386588722621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011628019812426128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010678945319733074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010171828043119663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008909680542167026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007644888773366838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007204370179428233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006739849382670107}]
result = search.search('pear apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'pear apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'pear apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'pear apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html', 'title': 'N-815', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-802.html', 'title': 'N-802', 'score': 1.0}]
result = search.search('pear apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'pear apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'pear apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'apple tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018329961184322344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012058969554624505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011874122316225049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011507913713472503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010891862743686866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01017140936717629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00888062642341305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850540504213752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007426245523254142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007052512952506607}]
result = search.search('apple tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'apple tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'apple tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'apple tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html', 'title': 'N-265', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html', 'title': 'N-203', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html', 'title': 'N-80', 'score': 1.0000000000000002}]
result = search.search('apple tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'apple tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'apple tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'coconut apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018155422472989447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012135615749216592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011945735836534152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011529346327257812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010927471730758476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00992315666944262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007991416549650202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007346464886527882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007211855160279439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006021675981018596}]
result = search.search('coconut apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'coconut apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'coconut apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-849.html', 'title': 'N-849', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html', 'title': 'N-642', 'score': 0.9999999505477939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'title': 'N-88', 'score': 0.9999997272259222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9999996040558455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-886.html', 'title': 'N-886', 'score': 0.9999995427334912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html', 'title': 'N-441', 'score': 0.9999951977319469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html', 'title': 'N-411', 'score': 0.9999941804094368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9999904324585521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-366.html', 'title': 'N-366', 'score': 0.9999818215869007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-490.html', 'title': 'N-490', 'score': 0.9999761345368776}]
result = search.search('coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'apple pear tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01726048303719182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012087131638543018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011778013264012399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011015130730046984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010427641032306225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010076040068669854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009033494987624435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007608390862673099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076039115857431915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006907982710612904}]
result = search.search('apple pear tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'apple pear tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'apple pear tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'apple pear tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-85.html', 'title': 'N-85', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-966.html', 'title': 'N-966', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0}]
result = search.search('apple pear tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'apple pear tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'apple pear tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'peach banana tomato coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01331174176348832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011224935255367547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010379949215416696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010258241641913989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009577140150878558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009409085190558384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009074483222626937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007394149459997728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007165631652731779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006642474004003138}]
result = search.search('peach banana tomato coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'peach banana tomato coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'peach banana tomato coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'peach banana tomato coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9999606858554255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.999942011365753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9999402434782831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999359806010701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.9998283475981268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-493.html', 'title': 'N-493', 'score': 0.9991795560866381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9991417448719913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9991146825873221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9990031532275027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9988295109639755}]
result = search.search('peach banana tomato coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'peach banana tomato coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'peach banana tomato coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'banana peach coconut peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013815520723623884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011108572972187761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010570184961328381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009980629398751722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009960482883737413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009460769132192893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008821413053481329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007423745265845101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006777992233639497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0066403227029770764}]
result = search.search('banana peach coconut peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'banana peach coconut peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'banana peach coconut peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'banana peach coconut peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999332303387874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.998917904535495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9986380857949216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9985090600748486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9964543734868033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html', 'title': 'N-419', 'score': 0.9963363988727842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9956355149898338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-540.html', 'title': 'N-540', 'score': 0.9951978268310447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-558.html', 'title': 'N-558', 'score': 0.9949893462258304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9948201179263864}]
result = search.search('banana peach coconut peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'banana peach coconut peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'banana peach coconut peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'tomato pear tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009135516621490822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007499941928436314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605519}]
result = search.search('tomato pear tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'tomato pear tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'tomato pear tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'tomato pear tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-155.html', 'title': 'N-155', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-637.html', 'title': 'N-637', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'title': 'N-438', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html', 'title': 'N-815', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-690.html', 'title': 'N-690', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}]
result = search.search('tomato pear tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'tomato pear tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'tomato pear tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'banana coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014717912590507632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011384865984488542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010673085992621907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009877931319644526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009484924179354858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00905198629634451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008969561317055971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007780832902138458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0075888483482094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007403386567966819}]
result = search.search('banana coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #373 checking search results for 'banana coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'banana coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'banana coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999987658138942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html', 'title': 'N-790', 'score': 0.9999970786867334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.9999933183407246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html', 'title': 'N-800', 'score': 0.9999893806576247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9999879317118892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-26.html', 'title': 'N-26', 'score': 0.9999839571016191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-273.html', 'title': 'N-273', 'score': 0.9999821956388584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9999821895091083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html', 'title': 'N-485', 'score': 0.9999676006661705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-509.html', 'title': 'N-509', 'score': 0.9999675836194201}]
result = search.search('banana coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #374 checking search results for 'banana coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'banana coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'apple peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007425906454159637}]
result = search.search('apple peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #375 checking search results for 'apple peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'apple peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'apple peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html', 'title': 'N-221', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html', 'title': 'N-288', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-504.html', 'title': 'N-504', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html', 'title': 'N-791', 'score': 1.0000000000000002}]
result = search.search('apple peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #376 checking search results for 'apple peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'apple peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018360784037711454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01214854351680189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011970665248063199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011805065245497246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010863492977125766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01017146667552604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00882484634182096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007696979456803251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007107180944381106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006389944373751743}]
result = search.search('coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #377 checking search results for 'coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html', 'title': 'N-103', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'title': 'N-629', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html', 'title': 'N-695', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'title': 'N-86', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}]
result = search.search('coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #378 checking search results for 'coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'tomato banana pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013888914418639717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011890932003911149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011146791502932834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009195366514186908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009141530490172405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009036978279287632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008174185126985095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007889721213387968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0073288206146943065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007049780559352313}]
result = search.search('tomato banana pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #379 checking search results for 'tomato banana pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'tomato banana pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'tomato banana pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9999970030868942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-475.html', 'title': 'N-475', 'score': 0.9999961383389033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-434.html', 'title': 'N-434', 'score': 0.9999372860349729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'title': 'N-486', 'score': 0.9999245614309628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9999146001589577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 0.9999104999987424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-621.html', 'title': 'N-621', 'score': 0.9999067882723824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html', 'title': 'N-949', 'score': 0.9998978076422678}]
result = search.search('tomato banana pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #380 checking search results for 'tomato banana pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'tomato banana pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #381 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #382 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'tomato pear peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015301308519085552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012059932348321737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011878287038614087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01112813974300807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010702930743517075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010128703443780338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.0091355255609854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007685795518032403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0076534469738927255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007180176917700487}]
result = search.search('tomato pear peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #383 checking search results for 'tomato pear peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'tomato pear peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'tomato pear peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'title': 'N-100', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html', 'title': 'N-372', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html', 'title': 'N-55', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 1.0000000000000002}]
result = search.search('tomato pear peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #384 checking search results for 'tomato pear peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'tomato pear peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #385 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #386 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #387 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #388 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking search results for 'apple apple coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017072370384591928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011306152846747164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011229926652212924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009996256082859603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009933408310245539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009634756376382917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009128029307577754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00776901590605865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007745377924439761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007069711819600528}]
result = search.search('apple apple coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #389 checking search results for 'apple apple coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #389 checking search results for 'apple apple coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking search results for 'apple apple coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-519.html', 'title': 'N-519', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-273.html', 'title': 'N-273', 'score': 0.9999999981893295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-619.html', 'title': 'N-619', 'score': 0.9999989783949955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html', 'title': 'N-741', 'score': 0.999998899228198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-56.html', 'title': 'N-56', 'score': 0.9999966064497715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-141.html', 'title': 'N-141', 'score': 0.9999853518153952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-389.html', 'title': 'N-389', 'score': 0.9999811094223305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 0.9999640067842379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html', 'title': 'N-506', 'score': 0.9999637525215468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999637525215468}]
result = search.search('apple apple coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #390 checking search results for 'apple apple coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #390 checking search results for 'apple apple coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking search results for 'pear tomato banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018207167488199234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012011360998473119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011612318540863212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011296445780915997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010999050529491735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010106344455871653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009091933584354983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007815795943208546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006502800204459808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006292904416668935}]
result = search.search('pear tomato banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #391 checking search results for 'pear tomato banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #391 checking search results for 'pear tomato banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking search results for 'pear tomato banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-971.html', 'title': 'N-971', 'score': 0.9999993963364374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'title': 'N-187', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html', 'title': 'N-331', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-523.html', 'title': 'N-523', 'score': 0.999978678716226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html', 'title': 'N-707', 'score': 0.9999708062129199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html', 'title': 'N-185', 'score': 0.9999519992610578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html', 'title': 'N-38', 'score': 0.9999461794838154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9999372860349729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html', 'title': 'N-118', 'score': 0.9999146001589577}]
result = search.search('pear tomato banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #392 checking search results for 'pear tomato banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #392 checking search results for 'pear tomato banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking search results for 'banana tomato pear peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01624940882459001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011766120885263576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011588140702089453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011322121871412355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010654497877652883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049697372224269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008919887223453014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007701769332636736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007051419709970935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0070223136009438724}]
result = search.search('banana tomato pear peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #393 checking search results for 'banana tomato pear peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #393 checking search results for 'banana tomato pear peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking search results for 'banana tomato pear peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-312.html', 'title': 'N-312', 'score': 0.9995094623388827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html', 'title': 'N-371', 'score': 0.9993776306845847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-674.html', 'title': 'N-674', 'score': 0.9993258773950364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-823.html', 'title': 'N-823', 'score': 0.9992055180793323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-140.html', 'title': 'N-140', 'score': 0.9990716118013632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-224.html', 'title': 'N-224', 'score': 0.9990375572796262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-769.html', 'title': 'N-769', 'score': 0.9986594627391125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-500.html', 'title': 'N-500', 'score': 0.9986508027867084}]
result = search.search('banana tomato pear peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #394 checking search results for 'banana tomato pear peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #394 checking search results for 'banana tomato pear peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking search results for 'pear banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0153367109130787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011815580312580497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01138644249891025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011385532086944958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010516463499601194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01008431006938554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009029954973510753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007689115353880962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623426302802697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006869536972819044}]
result = search.search('pear banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #395 checking search results for 'pear banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #395 checking search results for 'pear banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking search results for 'pear banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'title': 'N-317', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 1.0}]
result = search.search('pear banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #396 checking search results for 'pear banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #396 checking search results for 'pear banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #397 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #397 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #398 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #398 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking search results for 'pear tomato banana apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014812835040978602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011735721099195264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0108785601924025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009615852724359095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009386629523108918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00919003635293167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008221453064515128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007568079533865023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0073216751346393645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007174791684993745}]
result = search.search('pear tomato banana apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #399 checking search results for 'pear tomato banana apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #399 checking search results for 'pear tomato banana apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking search results for 'pear tomato banana apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9999712596524744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9999550163542428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html', 'title': 'N-738', 'score': 0.9999550163542428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.999937642565161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-307.html', 'title': 'N-307', 'score': 0.9998842184673279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9998183984969558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html', 'title': 'N-949', 'score': 0.9997468811222266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-244.html', 'title': 'N-244', 'score': 0.9990901699871962}]
result = search.search('pear tomato banana apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #400 checking search results for 'pear tomato banana apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #400 checking search results for 'pear tomato banana apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking search results for 'tomato banana coconut peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015950288416089305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011690815592633566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011502020040922434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01113832501822201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010883759362484771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010016937474234483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008943575371658545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007853500422846422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007250503455500903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007091128207558298}]
result = search.search('tomato banana coconut peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #401 checking search results for 'tomato banana coconut peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #401 checking search results for 'tomato banana coconut peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking search results for 'tomato banana coconut peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html', 'title': 'N-990', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-543.html', 'title': 'N-543', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-683.html', 'title': 'N-683', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}]
result = search.search('tomato banana coconut peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #402 checking search results for 'tomato banana coconut peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #402 checking search results for 'tomato banana coconut peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking search results for 'banana coconut pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017576932569916867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012034717754105927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011761272137958339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011271308444908661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010590648791111996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01007683842354837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008923449297282157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00767666184920395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007044560381228675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007016633486905639}]
result = search.search('banana coconut pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #403 checking search results for 'banana coconut pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #403 checking search results for 'banana coconut pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking search results for 'banana coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html', 'title': 'N-906', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-659.html', 'title': 'N-659', 'score': 0.9997141347973468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'title': 'N-143', 'score': 0.9995199820484125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-872.html', 'title': 'N-872', 'score': 0.9995095198937006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 0.9993868816300769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-208.html', 'title': 'N-208', 'score': 0.9992131950654207}]
result = search.search('banana coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #404 checking search results for 'banana coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #404 checking search results for 'banana coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking search results for 'apple coconut pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016804521908667526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011396351122753147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011388978379973753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010110612860576832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009671106295394848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009608899201728359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008783806596023448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007763824206071662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007092500988530669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006410653171392187}]
result = search.search('apple coconut pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #405 checking search results for 'apple coconut pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #405 checking search results for 'apple coconut pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking search results for 'apple coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-273.html', 'title': 'N-273', 'score': 0.999999997728659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999506574415822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-698.html', 'title': 'N-698', 'score': 0.9999454280965998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-434.html', 'title': 'N-434', 'score': 0.9999161805574814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9996463218704227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9996463218704227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-213.html', 'title': 'N-213', 'score': 0.9995037205695662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-94.html', 'title': 'N-94', 'score': 0.9993509174484274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-945.html', 'title': 'N-945', 'score': 0.9993387005486992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html', 'title': 'N-432', 'score': 0.9983338716797951}]
result = search.search('apple coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #406 checking search results for 'apple coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #406 checking search results for 'apple coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011738492510397939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #407 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #407 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking search results for 'peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-355.html', 'title': 'N-355', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html', 'title': 'N-221', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}]
result = search.search('peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #408 checking search results for 'peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #408 checking search results for 'peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #409 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'pear coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018360784037711454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01214854351680189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011970665248063199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011805065245497246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010863492977125766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01017146667552604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00882484634182096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007696979456803251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007107180944381106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006389944373751743}]
result = search.search('pear coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'pear coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'pear coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'pear coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html', 'title': 'N-103', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'title': 'N-629', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html', 'title': 'N-695', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'title': 'N-86', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}]
result = search.search('pear coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'pear coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'pear coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'pear pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018178970027312957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011992373529565465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011636228763440165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011338877964326245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010993852828798846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01011789441553375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009100526464519582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007823602269408111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006546350227536887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006303801165849845}]
result = search.search('pear pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'pear pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'pear pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'pear pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html', 'title': 'N-707', 'score': 0.9999976808004866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-895.html', 'title': 'N-895', 'score': 0.9999888936044248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'title': 'N-191', 'score': 0.9999777728504009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-91.html', 'title': 'N-91', 'score': 0.9999684376099143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-971.html', 'title': 'N-971', 'score': 0.9999621891165986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html', 'title': 'N-794', 'score': 0.9999581812655921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-366.html', 'title': 'N-366', 'score': 0.9999519587293255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html', 'title': 'N-83', 'score': 0.9999384033950172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-521.html', 'title': 'N-521', 'score': 0.9999384033950172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html', 'title': 'N-624', 'score': 0.9999228021517261}]
result = search.search('pear pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'pear pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'pear pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'banana tomato tomato peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015207125440201232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012136441623446709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010815719945698816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010215966998548156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009914622884552303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009844721514642966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009057287284405646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007379780444118979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007281244434528949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0064063913905660136}]
result = search.search('banana tomato tomato peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'banana tomato tomato peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'banana tomato tomato peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'banana tomato tomato peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'title': 'N-1', 'score': 0.9999954558677588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.9999954558677588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-358.html', 'title': 'N-358', 'score': 0.9999887555335913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999887555335913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9999828349796642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-230.html', 'title': 'N-230', 'score': 0.9999819133773974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-887.html', 'title': 'N-887', 'score': 0.9999805701574657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9999706275466935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9999706275466935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9999678602251196}]
result = search.search('banana tomato tomato peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'banana tomato tomato peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'banana tomato tomato peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'banana peach tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01142048412238662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936173}]
result = search.search('banana peach tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'banana peach tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'banana peach tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'banana peach tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}]
result = search.search('banana peach tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'banana peach tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'banana peach tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'coconut peach apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01654902658801003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011295609874491807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011163290477094563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010295666790262229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010127650055266932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009725873145471567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00885115492204368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007753564628571811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007245967126547626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0070976725710042605}]
result = search.search('coconut peach apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'coconut peach apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'coconut peach apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'coconut peach apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-519.html', 'title': 'N-519', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-141.html', 'title': 'N-141', 'score': 0.9999817946701273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999550313155904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 0.999954904784063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9999167234206503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 0.9999016587167374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html', 'title': 'N-90', 'score': 0.9997559879650516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-94.html', 'title': 'N-94', 'score': 0.9997015526398223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9996933720996686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html', 'title': 'N-457', 'score': 0.999489578573339}]
result = search.search('coconut peach apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'coconut peach apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'coconut peach apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'tomato peach pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0153367109130787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011815580312580499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011386442498910248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011385532086944958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010516463499601194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010084310069385542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009029954973510753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007689115353880961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623426302802696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006869536972819043}]
result = search.search('tomato peach pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'tomato peach pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'tomato peach pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'tomato peach pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 1.0}]
result = search.search('tomato peach pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'tomato peach pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'tomato peach pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'peach banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0153367109130787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011815580312580497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011386442498910248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011385532086944958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010516463499601194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010084310069385542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009029954973510753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007689115353880962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623426302802697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006869536972819044}]
result = search.search('peach banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'peach banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'peach banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 1.0}]
result = search.search('peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'tomato peach peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012502145372137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01130066565997112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010259343688083605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.009901707919397337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009255454006501889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009127504306337577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009026763117425842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007665693820904021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007567206236204477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006996901830199285}]
result = search.search('tomato peach peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'tomato peach peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'tomato peach peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'tomato peach peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-956.html', 'title': 'N-956', 'score': 0.9999988383862862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9999955050970698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html', 'title': 'N-294', 'score': 0.9999809249283204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-289.html', 'title': 'N-289', 'score': 0.9999792474211298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.9999780176601084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-425.html', 'title': 'N-425', 'score': 0.9999761928857072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html', 'title': 'N-556', 'score': 0.9999577190458988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.9999508743447423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'title': 'N-524', 'score': 0.999942313833869}]
result = search.search('tomato peach peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'tomato peach peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'tomato peach peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018360784037711454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01214854351680189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011970665248063199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011805065245497246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010863492977125766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01017146667552604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00882484634182096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007696979456803251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007107180944381106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006389944373751743}]
result = search.search('coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html', 'title': 'N-103', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'title': 'N-629', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html', 'title': 'N-695', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'title': 'N-86', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}]
result = search.search('coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'coconut peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015950288416089302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011690815592633564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01150202004092243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01113832501822201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01088375936248477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010016937474234483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008943575371658545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007853500422846422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007250503455500902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007091128207558297}]
result = search.search('coconut peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'coconut peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'coconut peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'coconut peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html', 'title': 'N-813', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-816.html', 'title': 'N-816', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html', 'title': 'N-990', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-891.html', 'title': 'N-891', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html', 'title': 'N-147', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-178.html', 'title': 'N-178', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-543.html', 'title': 'N-543', 'score': 1.0}]
result = search.search('coconut peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'coconut peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'coconut peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01832996118432234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012058969554624502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011874122316225049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011507913713472501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010891862743686864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010171409367176289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880626423413049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785054050421375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007426245523254142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007052512952506606}]
result = search.search('apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 1.0}]
result = search.search('apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'pear tomato tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear tomato tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'pear tomato tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'pear tomato tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'pear tomato tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear tomato tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'pear tomato tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'pear tomato tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'apple pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016605809898409755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01185342793117493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011678734124419285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009810855861162298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009767110846715329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00928130955489444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008740746831858092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007886655144883693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007428471031853662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006636882362239696}]
result = search.search('apple pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'apple pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'apple pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'apple pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999993684453062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html', 'title': 'N-818', 'score': 0.9999966897964376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-451.html', 'title': 'N-451', 'score': 0.9999940129918854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9999937621283271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-825.html', 'title': 'N-825', 'score': 0.999992732732806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9999919601256966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html', 'title': 'N-310', 'score': 0.9999792494791696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.9999750845059309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html', 'title': 'N-232', 'score': 0.999973858082214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html', 'title': 'N-150', 'score': 0.9999639555475149}]
result = search.search('apple pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'apple pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'apple pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'banana pear banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015435224182086779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011544793168066577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01088946238634837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009943811825314373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009675314910414111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009253509915416796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008356332337667761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00760751015055106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0073111997092523626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006932983671548411}]
result = search.search('banana pear banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'banana pear banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'banana pear banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'banana pear banana coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9999519225334927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-802.html', 'title': 'N-802', 'score': 0.9987523464811388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html', 'title': 'N-643', 'score': 0.9972184394952537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9968049295037659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-565.html', 'title': 'N-565', 'score': 0.996582924171619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.996410362861612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html', 'title': 'N-861', 'score': 0.9962030546953782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html', 'title': 'N-949', 'score': 0.9956406215967645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html', 'title': 'N-888', 'score': 0.9955433398802092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-750.html', 'title': 'N-750', 'score': 0.9949572009177541}]
result = search.search('banana pear banana coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'banana pear banana coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'banana pear banana coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01832996118432234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012058969554624502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011874122316225049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011507913713472501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010891862743686864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010171409367176289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880626423413049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785054050421375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007426245523254142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007052512952506606}]
result = search.search('coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 1.0}]
result = search.search('coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01142048412238662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936172}]
result = search.search('banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}]
result = search.search('banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'banana peach pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012725479786283718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011097175457490055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010585644293791998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.00994880848982061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009787655790402573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009580873100392875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00878916783117194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00737305682158313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00705147151267853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00647432061215487}]
result = search.search('banana peach pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'banana peach pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'banana peach pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'banana peach pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.999991516198713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999156150692685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9998238478711104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9990842520090095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.998975335421906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'title': 'N-274', 'score': 0.9988237143955351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9986698424960752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html', 'title': 'N-598', 'score': 0.9986233599542476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9986135568622674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9985677643254509}]
result = search.search('banana peach pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'banana peach pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'banana peach pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'tomato peach pear peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012642635058430517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011076919002424022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010541360362477898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009899825025152393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00975738639114938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00955673209329576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008772800109415224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007358061623320024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007026721179898089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006456569031867734}]
result = search.search('tomato peach pear peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'tomato peach pear peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'tomato peach pear peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'tomato peach pear peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.9999940747956816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999852596766301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999371862791988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9990350757829686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9989437712759781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9989286353298223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.998801582346434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.998664456744124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'title': 'N-274', 'score': 0.9985173893767438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9983441482178604}]
result = search.search('tomato peach pear peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'tomato peach pear peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'tomato peach pear peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'pear banana peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013716873586519334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011914959976089996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01116703508193692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009737275597155278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009418037712933846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00934004734065954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008239589770669228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007772965346398519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007332479304237139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007200403401611276}]
result = search.search('pear banana peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'pear banana peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'pear banana peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'pear banana peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 0.999972006969876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html', 'title': 'N-68', 'score': 0.9998572727405421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-342.html', 'title': 'N-342', 'score': 0.9995078288562562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html', 'title': 'N-110', 'score': 0.9992166603405139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-422.html', 'title': 'N-422', 'score': 0.9991256479488525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-469.html', 'title': 'N-469', 'score': 0.999000119846273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 0.9986452849440577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-724.html', 'title': 'N-724', 'score': 0.9985359494176886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-621.html', 'title': 'N-621', 'score': 0.9981403127918709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'title': 'N-100', 'score': 0.998048760939508}]
result = search.search('pear banana peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'pear banana peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'pear banana peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00902725649960236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'title': 'N-111', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'title': 'N-398', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-982.html', 'title': 'N-982', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0}]
result = search.search('banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'tomato pear tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato pear tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'tomato pear tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'tomato pear tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'tomato pear tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato pear tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'tomato pear tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'tomato pear tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'pear apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016605809898409755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01185342793117493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011678734124419285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009810855861162298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009767110846715329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00928130955489444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008740746831858092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007886655144883693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007428471031853662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006636882362239696}]
result = search.search('pear apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'pear apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'pear apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'pear apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999993684453062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html', 'title': 'N-818', 'score': 0.9999966897964376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-451.html', 'title': 'N-451', 'score': 0.9999940129918854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9999937621283271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-825.html', 'title': 'N-825', 'score': 0.999992732732806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9999919601256966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html', 'title': 'N-310', 'score': 0.9999792494791696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.9999750845059309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html', 'title': 'N-232', 'score': 0.999973858082214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html', 'title': 'N-150', 'score': 0.9999639555475149}]
result = search.search('pear apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'pear apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'pear apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #475 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'coconut coconut apple banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018321012778377863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011821115997590843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011794584328891907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011571501199805566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010817337655538719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010137752952067964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008769297226775387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0075327933900048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006699889439255687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006357445238850664}]
result = search.search('coconut coconut apple banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'coconut coconut apple banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'coconut coconut apple banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'coconut coconut apple banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html', 'title': 'N-544', 'score': 0.9999936380596506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-907.html', 'title': 'N-907', 'score': 0.9999552081044815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 0.9999501917853332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-467.html', 'title': 'N-467', 'score': 0.9997014217308223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 0.9993311270143713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-122.html', 'title': 'N-122', 'score': 0.9990515821989797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-374.html', 'title': 'N-374', 'score': 0.9990130261439104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-914.html', 'title': 'N-914', 'score': 0.9989063253142737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-459.html', 'title': 'N-459', 'score': 0.9985419788678975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html', 'title': 'N-166', 'score': 0.9985302623989034}]
result = search.search('coconut coconut apple banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'coconut coconut apple banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'coconut coconut apple banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'apple coconut peach banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016665109467231376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011326608000369474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011260163869828173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010352567297512232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010235775485200868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009774156728599668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880954898124661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007657702116213575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0070753127140365905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006805817422216947}]
result = search.search('apple coconut peach banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #479 checking search results for 'apple coconut peach banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'apple coconut peach banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'apple coconut peach banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 0.9999978998960867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 0.9999773389798088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html', 'title': 'N-298', 'score': 0.9990178090825302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9987228888761214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-678.html', 'title': 'N-678', 'score': 0.9986562134268162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html', 'title': 'N-429', 'score': 0.9982314756116819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html', 'title': 'N-18', 'score': 0.9981862043235759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html', 'title': 'N-645', 'score': 0.9981293087742302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html', 'title': 'N-785', 'score': 0.9975629756555441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html', 'title': 'N-233', 'score': 0.9964686122282018}]
result = search.search('apple coconut peach banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'apple coconut peach banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'apple coconut peach banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00913551662149082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074999419284363135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605518}]
result = search.search('apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html', 'title': 'N-890', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}]
result = search.search('apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'banana coconut apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01424250116337328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01131694654467735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010577270982676771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010482622537857518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009906323241415655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00946446931968738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008866737348379394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007398983372786145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007262445784115094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006777079068398422}]
result = search.search('banana coconut apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'banana coconut apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'banana coconut apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'banana coconut apple peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999395191314641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.998921517252274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9980620077490978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9978835810356514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9976482473570288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9962892926678882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9955289709631839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9949772431926911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9948581986819997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9936019352659156}]
result = search.search('banana coconut apple peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'banana coconut apple peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'banana coconut apple peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'peach coconut coconut pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016902786750462723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01190233961781621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011596018309841201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011385384781893245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01023956164381349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009884914262602863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008031649568333956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074063800088829635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007171431719960009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006066380395374706}]
result = search.search('peach coconut coconut pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'peach coconut coconut pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'peach coconut coconut pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'peach coconut coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-807.html', 'title': 'N-807', 'score': 0.9994210213577843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'title': 'N-370', 'score': 0.9991535850333183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-250.html', 'title': 'N-250', 'score': 0.9984191317539458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.9979543565223004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9975351704220942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-153.html', 'title': 'N-153', 'score': 0.9973813739227535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html', 'title': 'N-668', 'score': 0.9972027152840619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html', 'title': 'N-639', 'score': 0.9965022559136747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9957553606425185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-584.html', 'title': 'N-584', 'score': 0.9954308789018664}]
result = search.search('peach coconut coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'peach coconut coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'peach coconut coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'peach banana banana apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014537322287624256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011749505255058038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010838515541556718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009989448200635033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009642519854567258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009339271267480883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008319747430613644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007600020395402309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007331386381047729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007279761257264664}]
result = search.search('peach banana banana apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #489 checking search results for 'peach banana banana apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'peach banana banana apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'peach banana banana apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html', 'title': 'N-110', 'score': 0.9984649389761742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 0.9981416482982833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-448.html', 'title': 'N-448', 'score': 0.9975332276386552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9972072255850185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-950.html', 'title': 'N-950', 'score': 0.9968525770092831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html', 'title': 'N-976', 'score': 0.9963941514302431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'title': 'N-52', 'score': 0.9962502264042518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.9958082299155496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html', 'title': 'N-888', 'score': 0.9956557191577741}]
result = search.search('peach banana banana apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #490 checking search results for 'peach banana banana apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'peach banana banana apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
