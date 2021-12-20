
import testingtools
import crawler
import searchdata
import search

output = open('fruits-all-failed.txt', 'w')
success_output = open('fruits-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-643.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-648.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-503.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-650.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-171.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-876.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-876.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-876.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-876.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-687.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-768.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-971.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-983.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-503.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-732.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-732.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-955.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-345.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-900.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-768.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-93.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-169.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-169.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-169.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-169.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-201.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-201.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-201.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-201.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-415.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-839.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-436.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-542.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-842.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-202.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-842.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-842.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-842.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-723.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-879.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-994.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-210.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-994.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-994.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-994.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-704.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-880.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-210.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-880.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-880.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-880.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html\n\n')
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









#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-947.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-135.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-784.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-308.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-478.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-488.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-982.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-195.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-554.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-53.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-369.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-596.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-369.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-369.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-369.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-844.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-844.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-844.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-844.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-588.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-145.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-588.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-588.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-588.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-777.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-777.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-777.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-777.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-420.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-420.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-420.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-420.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-592.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-480.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-898.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-252.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-252.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-252.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-252.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-287.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-588.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-885.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-905.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-264.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-898.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-103.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-585.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-760.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-760.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-307.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-706.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-391.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-945.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-219.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-991.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-979.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-514.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-659.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-617.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-659.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-659.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-659.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-359.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-290.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-339.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-697.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-702.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-946.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-251.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-304.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-564.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-723.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-922.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-952.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html\n\n')
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









#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html
expected = 0.0009202739650743507
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html
expected = 0.0008872686450255169
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html
expected = 0.0009284294092883446
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html
expected = 0.0007712434158247178
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html
expected = 0.0003758122059759636
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-889.html
expected = 0.0004447913394417051
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-889.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-889.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-889.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html
expected = 0.002478508095983867
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html
expected = 0.0012458489133296332
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html
expected = 0.004497487850681179
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html
expected = 0.0007673015823862057
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-299.html
expected = 0.0003556173546590424
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-299.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-299.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-299.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html
expected = 0.00036729490832166744
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html
expected = 0.0018684462661690444
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html
expected = 0.000356610054262596
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html
expected = 0.0010608220218536009
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html
expected = 0.0006361999725165935
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html
expected = 0.0006577440172671755
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html
expected = 0.0006322434664913418
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html
expected = 0.0009028409526749406
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
expected = 0.002015367874487971
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html
expected = 0.0011162008171015532
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html
expected = 0.0012309627758269313
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-785.html
expected = 0.0003734814462863324
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-785.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-785.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-785.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html
expected = 0.001648818169819655
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html
expected = 0.000966278166468746
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html
expected = 0.0014532933976395298
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html
expected = 0.0006742050479240631
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-511.html
expected = 0.0003961526039246388
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-511.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-511.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-511.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html
expected = 0.0012287486952225768
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html
expected = 0.0007767953832920913
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html
expected = 0.0012987615312100504
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html
expected = 0.00039579154012548583
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html
expected = 0.0006309252744503439
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-403.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html
expected = 0.0020313942452800317
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html
expected = 0.0003942269816495904
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html
expected = 0.0009399085924467548
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-413.html
expected = 0.0003991643017063456
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-413.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-413.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-413.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html
expected = 0.0006032178184493058
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html
expected = 0.0003931580649760557
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html
expected = 0.0016719033440833458
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html
expected = 0.0012296498169208452
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html
expected = 0.0009752988894148651
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-936.html
expected = 0.00036299609228322737
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-936.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-936.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-936.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html
expected = 0.0006363698418882312
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html
expected = 0.0011623442282087475
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html
expected = 0.0007015005858129831
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html
expected = 0.0004599400715232119
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html
expected = 0.001965858117378368
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-633.html
expected = 0.0003589243568643016
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-633.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-633.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-633.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html
expected = 0.0008926246602303567
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html\n\n')
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









#Test #153 checking IDF for word banana
expected = 0.066427361738976
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word coconut
expected = 0.05889368905356862
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word pear
expected = 0.06039727964395631
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word peach
expected = 0.05439229681862769
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word apple
expected = 0.06039727964395631
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word apple\n\n')
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









#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word coconut
expected = 0.1590909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word pear
expected = 0.29545454545454547
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word apple
expected = 0.13636363636363635
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word banana
expected = 0.1590909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word peach
expected = 0.2459016393442623
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word coconut
expected = 0.22950819672131148
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word pear
expected = 0.18032786885245902
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word apple
expected = 0.18032786885245902
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word banana
expected = 0.16393442622950818
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-614.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word peach
expected = 0.1919191919191919
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word coconut
expected = 0.15151515151515152
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word pear
expected = 0.21212121212121213
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word apple
expected = 0.1717171717171717
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word banana
expected = 0.2727272727272727
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-667.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word peach
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word coconut
expected = 0.18888888888888888
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word pear
expected = 0.23333333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word apple
expected = 0.2111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word banana
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word apple
expected = 1.0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word peach
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word coconut
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word pear
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word apple
expected = 0.26666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word banana
expected = 0.13333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word peach
expected = 0.24615384615384617
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word coconut
expected = 0.16923076923076924
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word pear
expected = 0.16923076923076924
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word apple
expected = 0.15384615384615385
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word banana
expected = 0.26153846153846155
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-779.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word peach
expected = 0.1414141414141414
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word coconut
expected = 0.25252525252525254
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word pear
expected = 0.25252525252525254
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word apple
expected = 0.16161616161616163
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word banana
expected = 0.1919191919191919
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word peach
expected = 0.23684210526315788
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word coconut
expected = 0.21052631578947367
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word pear
expected = 0.15789473684210525
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word apple
expected = 0.21052631578947367
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word banana
expected = 0.18421052631578946
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word peach
expected = 0.20238095238095238
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word coconut
expected = 0.23809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word pear
expected = 0.13095238095238096
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word apple
expected = 0.23809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word banana
expected = 0.19047619047619047
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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









#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word pear
expected = 0.01648957435463622
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word peach
expected = 0.01209643459154539
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word coconut
expected = 0.01607906631544492
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word banana
expected = 0.014772941820122995
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word apple
expected = 0.019443581172158126
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word pear
expected = 0.020462713910653338
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word peach
expected = 0.016581740885012408
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word coconut
expected = 0.015906547204118424
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word banana
expected = 0.013148590639014034
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word apple
expected = 0.011954999942177122
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-447.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word pear
expected = 0.014316522685958333
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word peach
expected = 0.021160903753249808
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word coconut
expected = 0.01649658869437907
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word banana
expected = 0.011793393274156603
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word apple
expected = 0.013431897262154007
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word pear
expected = 0.01827396823077403
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word peach
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word coconut
expected = 0.015491066507565628
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word banana
expected = 0.02514352852028251
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word apple
expected = 0.00562355473451452
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word pear
expected = 0.018412387411313316
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word peach
expected = 0.01275310366947978
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word coconut
expected = 0.017954010931090607
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word banana
expected = 0.020250685564972566
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word apple
expected = 0.009691629679431265
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word pear
expected = 0.014732441641886168
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word peach
expected = 0.010607367199356812
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word coconut
expected = 0.016233129155728894
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word banana
expected = 0.02338145675925967
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word apple
expected = 0.014732441641886168
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-522.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word pear
expected = 0.010574760777928347
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word peach
expected = 0.009523368112103659
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word coconut
expected = 0.017298914138152523
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word banana
expected = 0.01695605274499107
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word apple
expected = 0.02436158666046443
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word pear
expected = 0.011747453541966586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word peach
expected = 0.015378345348239128
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word coconut
expected = 0.015198585553903321
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word banana
expected = 0.021187033271264474
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word apple
expected = 0.015586614400343306
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-621.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word pear
expected = 0.01726811810008926
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word peach
expected = 0.009123081013215186
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word coconut
expected = 0.014907107967405095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word banana
expected = 0.018992172070464615
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word apple
expected = 0.019204527919815792
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word pear
expected = 0.014052076790036751
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word peach
expected = 0.007479132477413688
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word coconut
expected = 0.025498576704936382
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word banana
expected = 0.017472681626118036
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word apple
expected = 0.014052076790036751
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
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









#Test #291 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177923}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-422.html', 'title': 'N-422', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-585.html', 'title': 'N-585', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-829.html', 'title': 'N-829', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'title': 'N-566', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'title': 'N-423', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'title': 'N-66', 'score': 1.0}]
result = search.search('peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'banana peach banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02041769321332317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015695295563845506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013067418062178126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009905874726749813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008688136060936253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007969433357186957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787973349031283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007654941023042055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00732461099423784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744840464271904}]
result = search.search('banana peach banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'banana peach banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'banana peach banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'banana peach banana peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html', 'title': 'N-170', 'score': 0.9999999961093688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'title': 'N-320', 'score': 0.9999999807750816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-774.html', 'title': 'N-774', 'score': 0.9999990714939916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html', 'title': 'N-712', 'score': 0.9999979284599467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html', 'title': 'N-335', 'score': 0.9999958954433531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-503.html', 'title': 'N-503', 'score': 0.999990457734787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-671.html', 'title': 'N-671', 'score': 0.9999889576033243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html', 'title': 'N-338', 'score': 0.9999876949544175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html', 'title': 'N-600', 'score': 0.9999863590375946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-613.html', 'title': 'N-613', 'score': 0.9999782268660233}]
result = search.search('banana peach banana peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'banana peach banana peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'banana peach banana peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'coconut banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019788328922644025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015477529473221945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01326410473642593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010008138100819788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008392373242279368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008193588606791933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007858972139884408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007464000765966969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007288570443841599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759522278364903}]
result = search.search('coconut banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'coconut banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'coconut banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'coconut banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-376.html', 'title': 'N-376', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html', 'title': 'N-956', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html', 'title': 'N-786', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html', 'title': 'N-479', 'score': 1.0}]
result = search.search('coconut banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'coconut banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'coconut banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'peach coconut coconut apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020046933423907037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014230598295869338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013255701614387537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008874925675016654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007763062792020494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076040482576654085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0074542808417449235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0064978126342053145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006484567701892085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006325276595194216}]
result = search.search('peach coconut coconut apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'peach coconut coconut apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'peach coconut coconut apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'peach coconut coconut apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html', 'title': 'N-444', 'score': 0.9999856660107257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9999667311682621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.9999559566842533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9999214878653702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995746225820269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9993831270986939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html', 'title': 'N-871', 'score': 0.9990931761854721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.998901141002462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-580.html', 'title': 'N-580', 'score': 0.9988415927157747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9987152367869188}]
result = search.search('peach coconut coconut apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'peach coconut coconut apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'peach coconut coconut apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'pear apple apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01939586525346005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014664780051606801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012810493186559208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01031992265721236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00808128588051708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0076875268577402565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0075502844687836395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007516045946558483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074980417969318005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006328134779596567}]
result = search.search('pear apple apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'pear apple apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'pear apple apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'pear apple apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html', 'title': 'N-696', 'score': 0.999991853654877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9999190789081991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.999889688710629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.999860193422854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.999860193422854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.999860193422854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-932.html', 'title': 'N-932', 'score': 0.999860193422854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-159.html', 'title': 'N-159', 'score': 0.9997839010418765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9994493268687997}]
result = search.search('pear apple apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'pear apple apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'pear apple apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'pear coconut peach coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019347699387641467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013806766799249918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013255701614387537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009267232559563321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007641021399423429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00753171605240679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007511337784674179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0069419974256510475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006484567701892085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006253312893407715}]
result = search.search('pear coconut peach coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'pear coconut peach coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'pear coconut peach coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'pear coconut peach coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999820101728686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.9999559566842533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999559566842533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999559566842533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995746225820269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9989287358568217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9987704075251698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9987152367869188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-221.html', 'title': 'N-221', 'score': 0.9987046840029747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9985481984498252}]
result = search.search('pear coconut peach coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'pear coconut peach coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'pear coconut peach coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'coconut coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'coconut coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'coconut coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'coconut coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'coconut coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'coconut coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'peach peach peach apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01907543414471589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014263130441097905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012162066160137779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009054959604917435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008786418071745896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007383940584135772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007298408335267644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.006961828743707071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00632628193874102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00569669627934626}]
result = search.search('peach peach peach apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'peach peach peach apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'peach peach peach apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'peach peach peach apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9999472305746422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'title': 'N-255', 'score': 0.9999292374524209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-635.html', 'title': 'N-635', 'score': 0.9999072851270341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9998549227521191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html', 'title': 'N-851', 'score': 0.9998417395239332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'title': 'N-834', 'score': 0.999771253337013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 0.999698917009812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.9996705041765996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-994.html', 'title': 'N-994', 'score': 0.9996612779863822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9996169853656933}]
result = search.search('peach peach peach apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'peach peach peach apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'peach peach peach apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'apple apple tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020175736424009133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01555920350406321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012095145632340942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010456219975515168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008529230977636661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008299499686541078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007991601838242188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007553904342517641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0074133349948075815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0065445805241273036}]
result = search.search('apple apple tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'apple apple tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'apple apple tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'apple apple tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html', 'title': 'N-343', 'score': 0.9999973891143675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html', 'title': 'N-128', 'score': 0.9999972112327863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999970844681172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html', 'title': 'N-890', 'score': 0.9999792612376112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9999792612376112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-949.html', 'title': 'N-949', 'score': 0.9999561055623829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-702.html', 'title': 'N-702', 'score': 0.9999533089666275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9999409996947595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9999390113125309}]
result = search.search('apple apple tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'apple apple tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'apple apple tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'tomato pear pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'tomato pear pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'tomato pear pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'tomato pear pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato pear pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'tomato pear pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'tomato pear pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'tomato coconut coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato coconut coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'tomato coconut coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'tomato coconut coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'tomato coconut coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato coconut coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'tomato coconut coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'tomato coconut coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'coconut tomato coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02088125479063774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015199898153788811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013171077503324476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008326593738818817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007764859158621026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00738788459647236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007362009600571494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007036260323716333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006479412804423902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'title': 'N-10', 'score': 0.006030143240991654}]
result = search.search('coconut tomato coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #327 checking search results for 'coconut tomato coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'coconut tomato coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'coconut tomato coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html', 'title': 'N-454', 'score': 0.9999999141737868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-977.html', 'title': 'N-977', 'score': 0.9999993132694512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'title': 'N-13', 'score': 0.9999616392948787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9999538929024835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'title': 'N-320', 'score': 0.999953059548306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html', 'title': 'N-236', 'score': 0.9999458712997303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html', 'title': 'N-813', 'score': 0.9999417785621776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html', 'title': 'N-75', 'score': 0.9999292584624077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-856.html', 'title': 'N-856', 'score': 0.9999292584624077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-972.html', 'title': 'N-972', 'score': 0.9999291740883364}]
result = search.search('coconut tomato coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'coconut tomato coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'coconut tomato coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'apple banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019931584714466807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015205070718291025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012712990138140453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009597794542436061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008408311918693288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007724256850635337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007642977358532383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007444383114249996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006656442027448534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0066099916586182}]
result = search.search('apple banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'apple banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'apple banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'apple banana peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html', 'title': 'N-627', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9998475678503425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 'title': 'N-263', 'score': 0.9996978932076122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9996197127893702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.99960490136349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html', 'title': 'N-559', 'score': 0.9995151146679799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'title': 'N-43', 'score': 0.9994814239938961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html', 'title': 'N-708', 'score': 0.9994419507540904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 0.9993962828459813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 0.999025623141714}]
result = search.search('apple banana peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'apple banana peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'apple banana peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'coconut tomato tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut tomato tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'coconut tomato tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'coconut tomato tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'coconut tomato tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut tomato tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'coconut tomato tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'coconut tomato tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'apple coconut apple pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01707119489479063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015583068166739869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012293790852244836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010310482980776015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008516679629020169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008297650118628631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008010960312052012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074682306338264915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007392045291233682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00662933385763199}]
result = search.search('apple coconut apple pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'apple coconut apple pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'apple coconut apple pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'apple coconut apple pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.9999796074784668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-414.html', 'title': 'N-414', 'score': 0.9999796074784668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-921.html', 'title': 'N-921', 'score': 0.9996080960406766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-707.html', 'title': 'N-707', 'score': 0.9994362809476045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html', 'title': 'N-438', 'score': 0.999318648893673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-368.html', 'title': 'N-368', 'score': 0.9991399005244364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9990891600565096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html', 'title': 'N-584', 'score': 0.9990712064712004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.999061351574015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html', 'title': 'N-336', 'score': 0.9989918533678157}]
result = search.search('apple coconut apple pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'apple coconut apple pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'apple coconut apple pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'coconut coconut tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut coconut tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'coconut coconut tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'coconut coconut tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'coconut coconut tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut coconut tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'coconut coconut tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'coconut coconut tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'tomato tomato pear pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato tomato pear pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'tomato tomato pear pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'tomato tomato pear pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'tomato tomato pear pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato tomato pear pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'tomato tomato pear pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'tomato tomato pear pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'pear coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018612780056015833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015356229884649315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013210470870284092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01027015105269429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00858575640006239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008197445386294711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007815144241156325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007600298924495897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00746608521672249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006735084746259515}]
result = search.search('pear coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'pear coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'pear coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'pear coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html', 'title': 'N-745', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html', 'title': 'N-206', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-815.html', 'title': 'N-815', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-469.html', 'title': 'N-469', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html', 'title': 'N-801', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0}]
result = search.search('pear coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'pear coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'pear coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'pear coconut coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01935064404655101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013860953707080344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013269228760935574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009302671676820315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007653846727460788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007566519295726825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00753687798156465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006962838761635281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006519761962961861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006272329674803218}]
result = search.search('pear coconut coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'pear coconut coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'pear coconut coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'pear coconut coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999094165875888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.999858091080985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.999858091080985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.999858091080985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9996307098755277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9992462112385481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.998908558265233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html', 'title': 'N-381', 'score': 0.9988424165495633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9987529243478942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9986205537149403}]
result = search.search('pear coconut coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'pear coconut coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'pear coconut coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'coconut tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'coconut tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'coconut tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'coconut tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'title': 'N-854', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html', 'title': 'N-860', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-119.html', 'title': 'N-119', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html', 'title': 'N-206', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html', 'title': 'N-57', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html', 'title': 'N-341', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}]
result = search.search('coconut tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'coconut tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'coconut tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'banana apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01974097010168522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01546373844615337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013366789310610892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010368545137739396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00857117170809255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008260432530634375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007942399150729383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00786035412788667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007293773302488997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006739717539863654}]
result = search.search('banana apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'banana apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'banana apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'banana apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'title': 'N-66', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}]
result = search.search('banana apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'banana apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'banana apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'pear apple peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015427018071405238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01505978907033273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012810493186559208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00949728797342667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008614534105716299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007996827098673599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0076875268577402565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0072518410013782016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006935605402259333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006528085658892475}]
result = search.search('pear apple peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'pear apple peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'pear apple peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'pear apple peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-422.html', 'title': 'N-422', 'score': 0.9999971960561942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999190789081991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'title': 'N-396', 'score': 0.9998995386697502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9998749069952256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.999860193422854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 0.9997023879661406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html', 'title': 'N-444', 'score': 0.999501822055315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9991799826694631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.9990842733792471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html', 'title': 'N-595', 'score': 0.9990464556114308}]
result = search.search('pear apple peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'pear apple peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'pear apple peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'tomato coconut banana pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018061848959776184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015102091987002318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01326410473642593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009874466377469563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008589336693142408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008205599403988857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007827657805594192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007500361356632108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007464000765966969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006732656533059661}]
result = search.search('tomato coconut banana pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'tomato coconut banana pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'tomato coconut banana pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'tomato coconut banana pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html', 'title': 'N-182', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html', 'title': 'N-625', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-642.html', 'title': 'N-642', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}]
result = search.search('tomato coconut banana pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'tomato coconut banana pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'tomato coconut banana pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'pear apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017694858885956694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015604730243977091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010291542174032615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847983244606652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008316652066202192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007864900509665608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007461735571723743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006745005899958887}]
result = search.search('pear apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'pear apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'pear apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'pear apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'title': 'N-854', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-162.html', 'title': 'N-162', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html', 'title': 'N-449', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html', 'title': 'N-180', 'score': 1.0000000000000002}]
result = search.search('pear apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'pear apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'pear apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'pear coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018768248546204194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015377468170029765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013213519791147264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010080346516550312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00844115569730472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008185777471473926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007831966190257838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007625338299672624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007324906434600333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006738457704715011}]
result = search.search('pear coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'pear coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'pear coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'pear coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-412.html', 'title': 'N-412', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html', 'title': 'N-358', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html', 'title': 'N-914', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 1.0}]
result = search.search('pear coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'pear coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'pear coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'apple apple banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02027898256101624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014733301608030738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012690547180427687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009880586179358048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008012005242701766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076676458264133595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007561604540222131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007506707434369145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007423751567161397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006415929252190506}]
result = search.search('apple apple banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'apple apple banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'apple apple banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'apple apple banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-166.html', 'title': 'N-166', 'score': 0.9999914396372681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9999711489632108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9998838379533882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html', 'title': 'N-215', 'score': 0.9998651350284679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.999852724805757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.999852724805757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9998362273098476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9997925024376171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9994255476867464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9993236172752682}]
result = search.search('apple apple banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'apple apple banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'apple apple banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'coconut peach pear banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019284556521329828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01484352639074853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01252130951017799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009603315051759508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008397799087623288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007740827478291467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076735474808317045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007309335618708797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007058733887200295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00656322859595363}]
result = search.search('coconut peach pear banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'coconut peach pear banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'coconut peach pear banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'coconut peach pear banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 0.9985844167567753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 0.9985734598174079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'title': 'N-793', 'score': 0.9975259725995386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html', 'title': 'N-746', 'score': 0.9967713210393025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html', 'title': 'N-365', 'score': 0.9967645962987144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-727.html', 'title': 'N-727', 'score': 0.9965075276863072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-586.html', 'title': 'N-586', 'score': 0.9963708024902286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html', 'title': 'N-2', 'score': 0.9961656356305847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.995671974237097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'title': 'N-566', 'score': 0.9956132800970796}]
result = search.search('coconut peach pear banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'coconut peach pear banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'coconut peach pear banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'pear coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015220472163379552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01033817851031768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('pear coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'pear coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'pear coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'pear coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}]
result = search.search('pear coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'pear coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'pear coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'banana apple banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.014905143261982234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013170616373923442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012634439894969988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0099529456979292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008843997975543715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007794725317444936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00762240815130804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0071741130946944695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006184118787099936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006165100823085782}]
result = search.search('banana apple banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'banana apple banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'banana apple banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'banana apple banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-609.html', 'title': 'N-609', 'score': 0.9999993535726954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-221.html', 'title': 'N-221', 'score': 0.9999985632659981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9999930315233683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9999839608924712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9999777851701391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html', 'title': 'N-240', 'score': 0.9999665355684827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html', 'title': 'N-137', 'score': 0.9999634241234652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'title': 'N-834', 'score': 0.9999348979871214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-490.html', 'title': 'N-490', 'score': 0.9998664992058665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9998466709858279}]
result = search.search('banana apple banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'banana apple banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'banana apple banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'peach tomato peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02097730703199227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01518601087927951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011781863822818072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008612825577450823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007864898180847195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007459286378420837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007017850058001062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006701709175432194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006543309375740494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006359987259606705}]
result = search.search('peach tomato peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'peach tomato peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'peach tomato peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'peach tomato peach peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html', 'title': 'N-931', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-431.html', 'title': 'N-431', 'score': 0.999978352742665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 0.9999717980849208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html', 'title': 'N-56', 'score': 0.9999526544438386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html', 'title': 'N-31', 'score': 0.9999076868482273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-635.html', 'title': 'N-635', 'score': 0.9998950729061801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9998350711958265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html', 'title': 'N-59', 'score': 0.9997307901085113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-821.html', 'title': 'N-821', 'score': 0.9995938081558656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9995639118940406}]
result = search.search('peach tomato peach peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'peach tomato peach peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'peach tomato peach peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'apple tomato apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020142064363485736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014510144896051007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012856061696853332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01040988475834211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008038505430468494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007737251058321551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0077148723425433585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007495276200856638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007414191723222562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006346238044348001}]
result = search.search('apple tomato apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #373 checking search results for 'apple tomato apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'apple tomato apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'apple tomato apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html', 'title': 'N-894', 'score': 0.9999999982868103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html', 'title': 'N-696', 'score': 0.9999936588039853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-166.html', 'title': 'N-166', 'score': 0.9999936588039853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9999698156920414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9999372860349728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9999372860349728}]
result = search.search('apple tomato apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #374 checking search results for 'apple tomato apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'apple tomato apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'banana apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016637793329136424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014135826149355591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013088367210704503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010278509245218137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008868045586908855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00797930763080684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007976343348693474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007529324810800396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006662876597122568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006477584069226316}]
result = search.search('banana apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #375 checking search results for 'banana apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'banana apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'banana apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'title': 'N-11', 'score': 0.9999999991397696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html', 'title': 'N-587', 'score': 0.9999998933169347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html', 'title': 'N-543', 'score': 0.9999981545014486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html', 'title': 'N-882', 'score': 0.9999969315796817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html', 'title': 'N-599', 'score': 0.99999530749417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html', 'title': 'N-802', 'score': 0.9999907991852149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 0.9999847019162763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html', 'title': 'N-309', 'score': 0.9999580409814697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9999172174973341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-138.html', 'title': 'N-138', 'score': 0.9998942756609119}]
result = search.search('banana apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #376 checking search results for 'banana apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'banana apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #377 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #378 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #379 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #380 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'coconut peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020256173094135237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014366232098515218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013309743643615974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009143008629951137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007862809369385186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007614771299053993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007549054784270825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007288741620261363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0063374001994668415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006322321345814701}]
result = search.search('coconut peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #381 checking search results for 'coconut peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'coconut peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'coconut peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html', 'title': 'N-607', 'score': 0.9999994340598544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9999930487748555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html', 'title': 'N-225', 'score': 0.9999875606420644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9999743197674037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-261.html', 'title': 'N-261', 'score': 0.9999626421405207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html', 'title': 'N-496', 'score': 0.9999556319744893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'title': 'N-46', 'score': 0.9999545671122907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-550.html', 'title': 'N-550', 'score': 0.9999463692722169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 'title': 'N-83', 'score': 0.9999443132110447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-221.html', 'title': 'N-221', 'score': 0.9999199841978885}]
result = search.search('coconut peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #382 checking search results for 'coconut peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'coconut peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'banana apple pear pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.015814412846758313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015514345538073843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012467906587823681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009267381170594434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847663738222064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007964869130552868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007343143639267446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007312787055732194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0070510411435541764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006607105944594496}]
result = search.search('banana apple pear pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #383 checking search results for 'banana apple pear pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'banana apple pear pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'banana apple pear pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999844002956989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html', 'title': 'N-459', 'score': 0.9989642821938735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 0.9981247839273764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-735.html', 'title': 'N-735', 'score': 0.997707844168127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html', 'title': 'N-479', 'score': 0.9970547063583142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html', 'title': 'N-661', 'score': 0.9957690639813204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'title': 'N-472', 'score': 0.9947725472616653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html', 'title': 'N-559', 'score': 0.9944074351406359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html', 'title': 'N-495', 'score': 0.9942151594675754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html', 'title': 'N-902', 'score': 0.9941787980051854}]
result = search.search('banana apple pear pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #384 checking search results for 'banana apple pear pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'banana apple pear pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #385 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #386 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'banana coconut pear peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019454763430388173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014135861452168413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013198778080295782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008946490915209247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007714824741526118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007676979859938586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007555981840239717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007021247065929266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006568232186424489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006350208878748081}]
result = search.search('banana coconut pear peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #387 checking search results for 'banana coconut pear peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'banana coconut pear peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'banana coconut pear peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999804108962645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999519572445278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999519572445278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9983181197922105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9981158954838505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9971509196341481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-935.html', 'title': 'N-935', 'score': 0.9970101876597459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9961768568344856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9959266429584677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9956197872583304}]
result = search.search('banana coconut pear peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #388 checking search results for 'banana coconut pear peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'banana coconut pear peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking search results for 'peach pear coconut peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019176633752347252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014673567512094383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012326043511158022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010283002011436173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008468481788512228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007736429293795832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007625725201510555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0076207070081136035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006969280929208928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006518183898904675}]
result = search.search('peach pear coconut peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #389 checking search results for 'peach pear coconut peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #389 checking search results for 'peach pear coconut peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking search results for 'peach pear coconut peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 0.9999169598141439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9999169598141439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html', 'title': 'N-94', 'score': 0.9995769351034973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-727.html', 'title': 'N-727', 'score': 0.9995755139877083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'title': 'N-793', 'score': 0.9993544559502756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.999348952491462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html', 'title': 'N-170', 'score': 0.9991587989106164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 0.9987127900274513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9987127900274513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 0.9986701697703662}]
result = search.search('peach pear coconut peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #390 checking search results for 'peach pear coconut peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #390 checking search results for 'peach pear coconut peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking search results for 'coconut apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02023091372061026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015578631986166772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012149999467317804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010452055092929994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008552557011320988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008304566378152895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007983375203876219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007552586051267174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007439158084404886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006560695260964112}]
result = search.search('coconut apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #391 checking search results for 'coconut apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #391 checking search results for 'coconut apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking search results for 'coconut apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-702.html', 'title': 'N-702', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9999992807382506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.999997797928232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9999765901609078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9999765901609078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-980.html', 'title': 'N-980', 'score': 0.9999736965722938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html', 'title': 'N-128', 'score': 0.9999733420036785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html', 'title': 'N-343', 'score': 0.9999727800454976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-186.html', 'title': 'N-186', 'score': 0.9999440025632303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html', 'title': 'N-237', 'score': 0.9999310060800397}]
result = search.search('coconut apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #392 checking search results for 'coconut apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #392 checking search results for 'coconut apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking search results for 'banana peach coconut apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019809604079756935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015263544149348473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012521309510177993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009560950687388001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008423796291291122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007714896818881797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007658453957749873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007309335618708799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00676414193740949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006613954698047577}]
result = search.search('banana peach coconut apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #393 checking search results for 'banana peach coconut apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #393 checking search results for 'banana peach coconut apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking search results for 'banana peach coconut apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 0.999104822974355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 0.9986693452124227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 0.9985734598174079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9983871855791302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'title': 'N-793', 'score': 0.9967514835764814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-93.html', 'title': 'N-93', 'score': 0.9957870793445109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-664.html', 'title': 'N-664', 'score': 0.9957539946832892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html', 'title': 'N-459', 'score': 0.9957288677885834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9955641743590472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-598.html', 'title': 'N-598', 'score': 0.9955638495184289}]
result = search.search('banana peach coconut apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #394 checking search results for 'banana peach coconut apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #394 checking search results for 'banana peach coconut apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #395 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #395 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #396 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #396 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking search results for 'banana banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016637793329136424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014135826149355591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013088367210704503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010278509245218137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008868045586908855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00797930763080684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007976343348693474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007529324810800396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006662876597122568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006477584069226316}]
result = search.search('banana banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #397 checking search results for 'banana banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #397 checking search results for 'banana banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking search results for 'banana banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'title': 'N-11', 'score': 0.9999999991397696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html', 'title': 'N-587', 'score': 0.9999998933169347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html', 'title': 'N-543', 'score': 0.9999981545014486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html', 'title': 'N-882', 'score': 0.9999969315796817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html', 'title': 'N-599', 'score': 0.99999530749417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html', 'title': 'N-802', 'score': 0.9999907991852149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 0.9999847019162763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html', 'title': 'N-309', 'score': 0.9999580409814697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9999172174973341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-138.html', 'title': 'N-138', 'score': 0.9998942756609119}]
result = search.search('banana banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #398 checking search results for 'banana banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #398 checking search results for 'banana banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking search results for 'pear peach apple apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019392954747183357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014624218099608217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01278138164494674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010307848262738189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008067717304969422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007670057135477661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007515538492717198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007499494883561093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007493744588608181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006310316340930187}]
result = search.search('pear peach apple apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #399 checking search results for 'pear peach apple apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #399 checking search results for 'pear peach apple apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking search results for 'pear peach apple apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html', 'title': 'N-696', 'score': 0.9999943169129872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.99998588070213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 0.9999725623713581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999722808642152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999566247209449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9999566247209449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999566247209449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-932.html', 'title': 'N-932', 'score': 0.9999566247209449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-159.html', 'title': 'N-159', 'score': 0.9996024755636698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9992987894035339}]
result = search.search('pear peach apple apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #400 checking search results for 'pear peach apple apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #400 checking search results for 'pear peach apple apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking search results for 'banana pear peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015506463350505963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01505098396580987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012642248485302588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009208797964533205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00846124703647274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008011041527026546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007387182275790886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007379252304241546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007284357153592445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006535649468057561}]
result = search.search('banana pear peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #401 checking search results for 'banana pear peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #401 checking search results for 'banana pear peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking search results for 'banana pear peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999957848337058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html', 'title': 'N-579', 'score': 0.9999928712589349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999854317888413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-856.html', 'title': 'N-856', 'score': 0.9999854317888413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-735.html', 'title': 'N-735', 'score': 0.999976372089745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 0.9999713931089299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.9999552267162142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.9999552267162142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html', 'title': 'N-358', 'score': 0.9999201723262089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html', 'title': 'N-657', 'score': 0.9998935245026299}]
result = search.search('banana pear peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #402 checking search results for 'banana pear peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #402 checking search results for 'banana pear peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking search results for 'banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020846239166491965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015625883074666475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012643869829430191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009449574521113814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008419899703797178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007774936676926262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076399872387705485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007321853566747798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007061425110590794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006644539952636677}]
result = search.search('banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #403 checking search results for 'banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #403 checking search results for 'banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking search results for 'banana peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html', 'title': 'N-708', 'score': 0.9999999483480313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-541.html', 'title': 'N-541', 'score': 0.9999993051020479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'title': 'N-139', 'score': 0.9999953203809198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-926.html', 'title': 'N-926', 'score': 0.999995006339741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-246.html', 'title': 'N-246', 'score': 0.9999934793075743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-171.html', 'title': 'N-171', 'score': 0.999992350036811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html', 'title': 'N-769', 'score': 0.9999823543509629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'title': 'N-43', 'score': 0.9999645255953603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-477.html', 'title': 'N-477', 'score': 0.9999619266810669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html', 'title': 'N-754', 'score': 0.999948982298318}]
result = search.search('banana peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #404 checking search results for 'banana peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #404 checking search results for 'banana peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking search results for 'apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017694858885956694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01560473024397709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010291542174032614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008479832446066518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008316652066202192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007864900509665608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007461735571723742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006745005899958886}]
result = search.search('apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #405 checking search results for 'apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #405 checking search results for 'apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking search results for 'apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'title': 'N-854', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html', 'title': 'N-500', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html', 'title': 'N-467', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-591.html', 'title': 'N-591', 'score': 1.0000000000000002}]
result = search.search('apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #406 checking search results for 'apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #406 checking search results for 'apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking search results for 'apple peach pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01850996335347442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015346711874553703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013368782359895913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010262630721324151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008640170335869514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008274019188378917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007948399497703151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007845312095231208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007356090445038332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006736455620521537}]
result = search.search('apple peach pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #407 checking search results for 'apple peach pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #407 checking search results for 'apple peach pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking search results for 'apple peach pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-474.html', 'title': 'N-474', 'score': 0.9995101044564219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html', 'title': 'N-962', 'score': 0.9994867099266312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-724.html', 'title': 'N-724', 'score': 0.9993385585001613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 'title': 'N-649', 'score': 0.9993260436303032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9992399865805257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html', 'title': 'N-468', 'score': 0.9992215462283971}]
result = search.search('apple peach pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #408 checking search results for 'apple peach pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #408 checking search results for 'apple peach pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #409 checking search results for 'coconut pear peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018484747630348165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522247240426872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01326139566662069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009988432926873077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008647974094855031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008207611091114793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0078235729275072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007576358135571884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007492762655316489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067301987686261425}]
result = search.search('coconut pear peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'coconut pear peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'coconut pear peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'coconut pear peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html', 'title': 'N-993', 'score': 0.9995102777828662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html', 'title': 'N-468', 'score': 0.9994883868615442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-514.html', 'title': 'N-514', 'score': 0.9994290045415678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'title': 'N-244', 'score': 0.9992923494604404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html', 'title': 'N-862', 'score': 0.9992607660583946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html', 'title': 'N-552', 'score': 0.9992321563428718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.999219493203456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-893.html', 'title': 'N-893', 'score': 0.9990807780862337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-388.html', 'title': 'N-388', 'score': 0.9989802005451532}]
result = search.search('coconut pear peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'coconut pear peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'coconut pear peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'apple peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015557183105434857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013210470870284092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010098217618014797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008501010640987404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00816592366703186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007875353181678812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007600298924495897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0071958091912974285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006739637373810881}]
result = search.search('apple peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'apple peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'apple peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'apple peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'title': 'N-65', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-571.html', 'title': 'N-571', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html', 'title': 'N-929', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-674.html', 'title': 'N-674', 'score': 1.0}]
result = search.search('apple peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'apple peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'apple peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'banana tomato coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02088125479063774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015199898153788811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013171077503324476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008326593738818817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007764859158621026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00738788459647236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007362009600571494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007036260323716333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006479412804423902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'title': 'N-10', 'score': 0.006030143240991654}]
result = search.search('banana tomato coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'banana tomato coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'banana tomato coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'banana tomato coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html', 'title': 'N-454', 'score': 0.9999999141737868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-977.html', 'title': 'N-977', 'score': 0.9999993132694512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'title': 'N-13', 'score': 0.9999616392948787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9999538929024835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'title': 'N-320', 'score': 0.999953059548306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html', 'title': 'N-236', 'score': 0.9999458712997303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html', 'title': 'N-813', 'score': 0.9999417785621776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html', 'title': 'N-75', 'score': 0.9999292584624077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-856.html', 'title': 'N-856', 'score': 0.9999292584624077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-972.html', 'title': 'N-972', 'score': 0.9999291740883364}]
result = search.search('banana tomato coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'banana tomato coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'banana tomato coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'pear tomato banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018061848959776184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01510209198700232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013264104736425933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009874466377469564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00858933669314241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008205599403988857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007827657805594192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00750036135663211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007464000765966971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006732656533059662}]
result = search.search('pear tomato banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'pear tomato banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'pear tomato banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'pear tomato banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html', 'title': 'N-182', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html', 'title': 'N-625', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-642.html', 'title': 'N-642', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}]
result = search.search('pear tomato banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'pear tomato banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'pear tomato banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522047216337955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010338178510317679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}]
result = search.search('pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'banana banana coconut peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.014765281930912307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0132969775151478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011768353088239718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010241770887999309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008420446117557033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007997978800755264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007797214986359693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0070780974757393995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.006744265664908089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0059593703436190285}]
result = search.search('banana banana coconut peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'banana banana coconut peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'banana banana coconut peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'banana banana coconut peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9998738563803146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-792.html', 'title': 'N-792', 'score': 0.999630760900896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.999570680358618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html', 'title': 'N-941', 'score': 0.9995154275021768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'title': 'N-64', 'score': 0.9984034913568602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-405.html', 'title': 'N-405', 'score': 0.998135347185667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-784.html', 'title': 'N-784', 'score': 0.9973585009959083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.996683675701186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.9946403210987544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html', 'title': 'N-132', 'score': 0.994066692521209}]
result = search.search('banana banana coconut peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'banana banana coconut peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'banana banana coconut peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'banana tomato pear banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016419532475021953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013650695190249057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012542226403149878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010422063678520933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008586684531998933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008045931858400556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007837434329897282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007392939943753259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007160996182493074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006330629506891991}]
result = search.search('banana tomato pear banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'banana tomato pear banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'banana tomato pear banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'banana tomato pear banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9999864212887299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.9999761581277091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-876.html', 'title': 'N-876', 'score': 0.9999735764492649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 0.9999733482839986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9999733482839986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9999583034363221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 0.9999257073466866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 0.9998928181009622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html', 'title': 'N-441', 'score': 0.9998928181009622}]
result = search.search('banana tomato pear banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'banana tomato pear banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'banana tomato pear banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'tomato pear apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018768248546204194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015377468170029766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013213519791147266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010080346516550313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008441155697304721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008185777471473928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00783196619025784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007625338299672626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007324906434600334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006738457704715011}]
result = search.search('tomato pear apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'tomato pear apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'tomato pear apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'tomato pear apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html', 'title': 'N-358', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html', 'title': 'N-914', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-412.html', 'title': 'N-412', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 1.0}]
result = search.search('tomato pear apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'tomato pear apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'tomato pear apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'tomato tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'tomato tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'tomato tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'tomato tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'tomato tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'tomato tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'banana apple peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016835732064973664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014023903227514692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01300367224938558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01028095174640095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008662568930849842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008005211376608657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007951071233879404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0073665534710789975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0067561739943460515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006341499208621315}]
result = search.search('banana apple peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'banana apple peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'banana apple peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'banana apple peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9998691953759775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.999833292533238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9997219231392969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9996452758132504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html', 'title': 'N-194', 'score': 0.9995004564479101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9992380192578275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9991971462334702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.999134113259575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9988486004936428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 'title': 'N-558', 'score': 0.9985527158624662}]
result = search.search('banana apple peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'banana apple peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'banana apple peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020184143788183968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015092137537141847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012868954398378837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009744843107634231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875070202109162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007722609202303772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007721040501782901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007571438704727792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006614922648071249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006382803489133834}]
result = search.search('apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apple peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html', 'title': 'N-538', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html', 'title': 'N-830', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-510.html', 'title': 'N-510', 'score': 0.9999985767888089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html', 'title': 'N-869', 'score': 0.9999919523910138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-783.html', 'title': 'N-783', 'score': 0.99998557507818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-636.html', 'title': 'N-636', 'score': 0.9999823289119689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html', 'title': 'N-710', 'score': 0.9999773367913629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 0.9999736895513718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 0.9999734966387581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html', 'title': 'N-459', 'score': 0.999970286962465}]
result = search.search('apple peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apple peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apple peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'peach banana pear banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019234120498378575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013960035449748005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013056200790894769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010321296325656421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008605528043270657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007919476515056725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007867900816809255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007749245506170972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0070873179266456535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006437156314469493}]
result = search.search('peach banana pear banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'peach banana pear banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'peach banana pear banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'peach banana pear banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'title': 'N-66', 'score': 0.9999789802426594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 0.9999626420849698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.999868662488449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-499.html', 'title': 'N-499', 'score': 0.9997754262471481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html', 'title': 'N-764', 'score': 0.9997740312251633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-242.html', 'title': 'N-242', 'score': 0.9997328378650421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html', 'title': 'N-364', 'score': 0.9997117030761641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html', 'title': 'N-399', 'score': 0.9994583158006273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 0.999375196744474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9985398391881524}]
result = search.search('peach banana pear banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'peach banana pear banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'peach banana pear banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'peach coconut banana tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016720051794452708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014307118292577008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012516994068040268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01036447333121105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008654820159836096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008236348201004207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007844284694584706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007379404630871114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0072543771243070865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006343846477951797}]
result = search.search('peach coconut banana tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'peach coconut banana tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'peach coconut banana tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'peach coconut banana tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-347.html', 'title': 'N-347', 'score': 0.9999962190448477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.999977076498244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 0.9999743758296029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'title': 'N-52', 'score': 0.9999599178459941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9999599178459941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9997977390943792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html', 'title': 'N-995', 'score': 0.9997888707118713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html', 'title': 'N-430', 'score': 0.9997670400556856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html', 'title': 'N-847', 'score': 0.9994272711289885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.999288860371083}]
result = search.search('peach coconut banana tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'peach coconut banana tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'peach coconut banana tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'coconut coconut pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020260748257807604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014010094127690961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013196770135760648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00873955114330248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0077766914187501635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0075831001144581875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0074641097485365375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006960720188886995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006367006288025557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00635788940871841}]
result = search.search('coconut coconut pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'coconut coconut pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'coconut coconut pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'coconut coconut pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999050875494031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9998356616746938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html', 'title': 'N-318', 'score': 0.9998203070436321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9997721313074367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9996826702812037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html', 'title': 'N-872', 'score': 0.9994520843551554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9991823226954788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'title': 'N-81', 'score': 0.9989516167782432}]
result = search.search('coconut coconut pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'coconut coconut pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'coconut coconut pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'peach apple peach peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018364449091234736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013731510951730645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011708758141368401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008667668326361462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008636549521940774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007154263499572134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007026379966151076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.006600965664886904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006129589229175477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0053087823504008175}]
result = search.search('peach apple peach peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'peach apple peach peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'peach apple peach peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'peach apple peach peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-44.html', 'title': 'N-44', 'score': 0.9999887508622035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9999887508622035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9999887508622035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'title': 'N-87', 'score': 0.9998063627210797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.9995585124804789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9992388494569769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html', 'title': 'N-579', 'score': 0.9991753142847519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-860.html', 'title': 'N-860', 'score': 0.9990838421709308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-408.html', 'title': 'N-408', 'score': 0.998959621399194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9988795081856634}]
result = search.search('peach apple peach peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'peach apple peach peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'peach apple peach peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'coconut tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015220472163379552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01033817851031768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('coconut tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'coconut tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'coconut tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'coconut tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}]
result = search.search('coconut tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'coconut tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'coconut tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'banana banana coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.014932008040989913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014316159980228371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011772379726835584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01045987212299529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008845116119544133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00815634208167076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008013525080408099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00721069300336528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.006943721181283599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0062652316984509035}]
result = search.search('banana banana coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'banana banana coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'banana banana coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'banana banana coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-323.html', 'title': 'N-323', 'score': 0.9999837348851419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-427.html', 'title': 'N-427', 'score': 0.9998780614373318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'title': 'N-255', 'score': 0.9998780614373318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html', 'title': 'N-336', 'score': 0.9998664725377957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9998526107881989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9998325817500672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-549.html', 'title': 'N-549', 'score': 0.9998203044388434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9997743815428785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.999761700782963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-534.html', 'title': 'N-534', 'score': 0.9997367805131558}]
result = search.search('banana banana coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'banana banana coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'banana banana coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'apple tomato apple coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019245074094250133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015153836478285958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011243083410955399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010416424056745355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008154818204238063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008135796319001154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008029311846509353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007502318944848251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0069964216807124335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006266785953015933}]
result = search.search('apple tomato apple coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'apple tomato apple coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'apple tomato apple coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'apple tomato apple coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html', 'title': 'N-173', 'score': 0.9999803768102942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'title': 'N-52', 'score': 0.9999327469909752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9999067402319286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-426.html', 'title': 'N-426', 'score': 0.9998824487928732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9998340757831675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 0.9998266780710895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 0.9998167620177637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html', 'title': 'N-29', 'score': 0.9997755998350657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9997755998350657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'title': 'N-681', 'score': 0.9997433753814802}]
result = search.search('apple tomato apple coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'apple tomato apple coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'apple tomato apple coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'banana apple peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020084897468232162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015251101151677566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012674679461812808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009881599871175989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008069422713347318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007543076393083554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007539496239080283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00750805160192678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007401734402155222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00642383124376655}]
result = search.search('banana apple peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'banana apple peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'banana apple peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'banana apple peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-189.html', 'title': 'N-189', 'score': 0.9999456802448436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.99988624514751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9998558006313836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.9998558006313836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9998558006313836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html', 'title': 'N-718', 'score': 0.9998288484239662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 0.9997968921562028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html', 'title': 'N-358', 'score': 0.9997968921562028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9994350397115005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.999068118110069}]
result = search.search('banana apple peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'banana apple peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'banana apple peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'peach banana apple banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0184341205700214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014763291241419391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013102185574481073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01037214921140571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008266007287769323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008198370477229903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007871961261788265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0075079665539855905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007371693540810386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006447894469909399}]
result = search.search('peach banana apple banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'peach banana apple banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'peach banana apple banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'peach banana apple banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html', 'title': 'N-786', 'score': 0.9999833548076876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9999833548076876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999138040031934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html', 'title': 'N-235', 'score': 0.9997528301356864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html', 'title': 'N-964', 'score': 0.9992940698447335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-921.html', 'title': 'N-921', 'score': 0.999255827371336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html', 'title': 'N-825', 'score': 0.9992377563993193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-350.html', 'title': 'N-350', 'score': 0.99911014116358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html', 'title': 'N-262', 'score': 0.9989906450646532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-308.html', 'title': 'N-308', 'score': 0.9989368167740487}]
result = search.search('peach banana apple banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'peach banana apple banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'peach banana apple banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'pear tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'pear tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'pear tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'tomato banana tomato apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01643771392633279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014028513617968698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013043385223583868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010247006709634373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008872625662426128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007960679475086573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007941971812161669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007491814403289155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0066069993668700505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0064468130725565285}]
result = search.search('tomato banana tomato apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'tomato banana tomato apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'tomato banana tomato apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'tomato banana tomato apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html', 'title': 'N-220', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.9999971713478548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-85.html', 'title': 'N-85', 'score': 0.9999902415463718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html', 'title': 'N-223', 'score': 0.9999808679727696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9999700972901993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html', 'title': 'N-985', 'score': 0.9999609339979121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9999546854554082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-998.html', 'title': 'N-998', 'score': 0.9999527202529968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 0.999950611255673}]
result = search.search('tomato banana tomato apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'tomato banana tomato apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'tomato banana tomato apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'tomato coconut apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020175736424009133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01555920350406321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012095145632340942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010456219975515168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008529230977636661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008299499686541078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007991601838242188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007553904342517641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0074133349948075815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0065445805241273036}]
result = search.search('tomato coconut apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'tomato coconut apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'tomato coconut apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'tomato coconut apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html', 'title': 'N-343', 'score': 0.9999973891143675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html', 'title': 'N-128', 'score': 0.9999972112327863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999970844681172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html', 'title': 'N-890', 'score': 0.9999792612376112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9999792612376112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-949.html', 'title': 'N-949', 'score': 0.9999561055623829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-702.html', 'title': 'N-702', 'score': 0.9999533089666275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9999409996947595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9999390113125309}]
result = search.search('tomato coconut apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'tomato coconut apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'tomato coconut apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'pear coconut peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018484747630348162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015222472404268718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013261395666620688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009988432926873077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00864797409485503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008207611091114793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0078235729275072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007576358135571883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007492762655316488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730198768626143}]
result = search.search('pear coconut peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'pear coconut peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'pear coconut peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'pear coconut peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html', 'title': 'N-993', 'score': 0.9995102777828662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html', 'title': 'N-468', 'score': 0.9994883868615441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-514.html', 'title': 'N-514', 'score': 0.9994290045415678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'title': 'N-244', 'score': 0.9992923494604403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html', 'title': 'N-862', 'score': 0.9992607660583945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html', 'title': 'N-552', 'score': 0.9992321563428717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9992194932034559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-893.html', 'title': 'N-893', 'score': 0.9990807780862336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-388.html', 'title': 'N-388', 'score': 0.9989802005451531}]
result = search.search('pear coconut peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'pear coconut peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'pear coconut peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'pear coconut pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015511183070461136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.011738073184960446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011309479088210448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010144921425170006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008827118180622625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008136562944665932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008031156814977887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0073197798892046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.006711000948037673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006446892130223398}]
result = search.search('pear coconut pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #479 checking search results for 'pear coconut pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'pear coconut pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'pear coconut pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html', 'title': 'N-737', 'score': 0.9999984476542482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-687.html', 'title': 'N-687', 'score': 0.9999850847966315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html', 'title': 'N-733', 'score': 0.9999576319094525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 0.9999227550394807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-278.html', 'title': 'N-278', 'score': 0.9998832241203924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.99980705894505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.9997929281013983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9997535225200261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 0.9997392791482778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-799.html', 'title': 'N-799', 'score': 0.9997039169826657}]
result = search.search('pear coconut pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'pear coconut pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'pear coconut pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #489 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #490 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
