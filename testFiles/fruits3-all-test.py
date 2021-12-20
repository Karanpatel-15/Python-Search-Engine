
import testingtools
import crawler
import searchdata
import search

output = open('fruits3-all-failed.txt', 'w')
success_output = open('fruits3-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-424.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-488.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-908.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-261.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-352.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-301.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-696.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-531.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-839.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-889.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-603.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-219.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-31.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-578.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-519.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-324.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-693.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-960.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-723.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-603.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-688.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-915.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-444.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-871.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-163.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-877.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-296.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-308.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html\n\n')
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









#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-629.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-284.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-656.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-559.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-559.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-559.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-559.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-390.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-751.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-729.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-784.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-955.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-955.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-955.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-955.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-473.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-216.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-216.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-216.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-216.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-515.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-98.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-436.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-533.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-533.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-533.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-533.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html\n\n')
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









#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html
expected = 0.0011854666347631696
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html
expected = 0.0006368995031401394
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html
expected = 0.0038002103646793597
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html
expected = 0.0003784444439070059
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html
expected = 0.0016278305840346512
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-799.html
expected = 0.0004131535133187784
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-799.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-799.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-799.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html
expected = 0.0003561115931946534
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html
expected = 0.0003626687511863686
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
expected = 0.00037693240088667256
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html
expected = 0.0017417967188590251
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html
expected = 0.00038364333009110275
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html
expected = 0.0015945138999127906
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-788.html
expected = 0.00039046570235386316
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-788.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-788.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-788.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html
expected = 0.0003869814897785985
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html
expected = 0.0006900715729351567
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html
expected = 0.0013250777446013973
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html
expected = 0.0007745415873169228
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html
expected = 0.0006771730653497886
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html
expected = 0.00037667695858446874
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html
expected = 0.0003784444439070059
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html
expected = 0.000707629201258527
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html
expected = 0.00037768109203818235
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html
expected = 0.0009115058683915625
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html
expected = 0.0015581909124060059
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html
expected = 0.0023039914057898228
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html
expected = 0.00037125059693324144
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html
expected = 0.0006469758285861584
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-251.html
expected = 0.0017376377802949309
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-251.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-251.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-251.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html
expected = 0.0003531001525702337
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html
expected = 0.0007555388807594921
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html
expected = 0.004005390789576159
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html
expected = 0.0011499775664680408
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html
expected = 0.0020021102564865166
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html
expected = 0.0004419685283497025
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html
expected = 0.0007854375630519505
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html
expected = 0.0006094695450172534
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html
expected = 0.00038854970381783786
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html
expected = 0.00039587895391958276
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html
expected = 0.0006199754501833211
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html
expected = 0.00034863440432348014
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
expected = 0.002464267287149932
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html
expected = 0.00037893100807835346
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html
expected = 0.0004075884017553431
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html
expected = 0.00035403699436723136
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html
expected = 0.0011273839630878246
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html
expected = 0.00036526370046091936
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html
expected = 0.0012686147755100498
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html
expected = 0.0006806238950027231
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-745.html
expected = 0.0006399261204125181
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-745.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html
expected = 0.0003889483227215651
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html\n\n')
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









#Test #153 checking IDF for word kiwi
expected = 0.15842936260448298
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apricot
expected = 0.16650266314016507
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word lime
expected = 0.20922796213800016
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word peach
expected = 0.1600404125104682
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word papaya
expected = 0.1762506396917273
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word orange
expected = 0.16812275880832706
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word banana
expected = 0.15842936260448298
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word cherry
expected = 0.1600404125104682
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word apple
expected = 0.1729939903610231
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word pear
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word cherry
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word lime
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word peach
expected = 0.26666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word blueberry
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word fig
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word coconut
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word pear
expected = 0.1282051282051282
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word cherry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word lime
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word peach
expected = 0.02564102564102564
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apple
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word blueberry
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig
expected = 0.02
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word coconut
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word banana
expected = 0.12
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word fig
expected = 0.0851063829787234
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word coconut
expected = 0.0425531914893617
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word pear
expected = 0.0851063829787234
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word banana
expected = 0.10638297872340426
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word cherry
expected = 0.0425531914893617
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apricot
expected = 0.14893617021276595
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word lime
expected = 0.0425531914893617
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word peach
expected = 0.02127659574468085
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word blueberry
expected = 0.1276595744680851
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word fig
expected = 0.14457831325301204
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word coconut
expected = 0.04819277108433735
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word pear
expected = 0.07228915662650602
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word banana
expected = 0.04819277108433735
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word cherry
expected = 0.07228915662650602
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apricot
expected = 0.060240963855421686
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word lime
expected = 0.08433734939759036
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word peach
expected = 0.08433734939759036
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apple
expected = 0.060240963855421686
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word blueberry
expected = 0.0963855421686747
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word fig
expected = 0.06153846153846154
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word coconut
expected = 0.1076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word pear
expected = 0.09230769230769231
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word banana
expected = 0.06153846153846154
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word cherry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apricot
expected = 0.03076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word lime
expected = 0.09230769230769231
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word peach
expected = 0.12307692307692308
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apple
expected = 0.046153846153846156
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word blueberry
expected = 0.046153846153846156
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word fig
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word coconut
expected = 0.10294117647058823
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word pear
expected = 0.04411764705882353
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word banana
expected = 0.10294117647058823
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word cherry
expected = 0.07352941176470588
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apricot
expected = 0.1323529411764706
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word lime
expected = 0.10294117647058823
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word peach
expected = 0.07352941176470588
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apple
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word blueberry
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-796.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word banana
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word cherry
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word lime
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word peach
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word fig
expected = 0.043010752688172046
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word coconut
expected = 0.043010752688172046
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word pear
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word banana
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word cherry
expected = 0.043010752688172046
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apricot
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word lime
expected = 0.10752688172043011
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word peach
expected = 0.053763440860215055
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apple
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word blueberry
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word fig
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word coconut
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word pear
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word banana
expected = 0.12
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word cherry
expected = 0.12
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word lime
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word peach
expected = 0.12
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apple
expected = 0.16
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple
expected = 0.07179899314970742
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi
expected = 0.06575412646770577
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word lime
expected = 0.036084959955732146
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word fig
expected = 0.028716247439110307
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word pear
expected = 0.003967411478103978
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word banana
expected = 0.010632859271580456
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apple
expected = 0.01536346947207686
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word papaya
expected = 0.019419809736613006
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word peach
expected = 0.010740983590508625
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word kiwi
expected = 0.010632859271580456
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word cherry
expected = 0.01421307171868756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apricot
expected = 0.028716247439110307
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word lime
expected = 0.02746002623956176
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word fig
expected = 0.019227264232435187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word pear
expected = 0.020164792924428732
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word banana
expected = 0.01829498195117974
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apple
expected = 0.022704515524875027
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word papaya
expected = 0.01182891995246303
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word peach
expected = 0.01848102151144756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word kiwi
expected = 0.01829498195117974
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word cherry
expected = 0.023500556361826408
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apricot
expected = 0.013888987511763456
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word lime
expected = 0.010592390099478924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word fig
expected = 0.008429375990478289
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apple
expected = 0.03332644075666537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word papaya
expected = 0.025880888626255386
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word peach
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word kiwi
expected = 0.0232639875569638
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word cherry
expected = 0.030830997742012325
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apricot
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word lime
expected = 0.05128438841689243
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word pear
expected = 0.026542992389967886
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apple
expected = 0.009076548331433825
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word papaya
expected = 0.009247416319315837
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word peach
expected = 0.008396907523217388
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word kiwi
expected = 0.045866348831981534
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word cherry
expected = 0.008396907523217388
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apricot
expected = 0.017165341130945092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word lime
expected = 0.03602507459825138
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word fig
expected = 0.013165627148711207
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word pear
expected = 0.013807588118862324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word banana
expected = 0.024403449610227265
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apple
expected = 0.01032882176651443
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word papaya
expected = 0.023909298039215904
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word peach
expected = 0.012654646839282212
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word kiwi
expected = 0.015554657231997495
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word cherry
expected = 0.018731037247269103
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apricot
expected = 0.013165627148711207
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word lime
expected = 0.02416106287413996
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word fig
expected = 0.016906351815929928
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word pear
expected = 0.015272883446625196
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word banana
expected = 0.016086604812501657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apple
expected = 0.024730866888981986
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word papaya
expected = 0.015415381719628314
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word peach
expected = 0.016250187640487287
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word kiwi
expected = 0.009330489618183493
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word cherry
expected = 0.016250187640487287
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apricot
expected = 0.007391739100944854
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word lime
expected = 0.04319529637411157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word fig
expected = 0.009065701041806217
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word pear
expected = 0.009507748060923542
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word banana
expected = 0.0169385076092213
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apple
expected = 0.009419139424346069
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word papaya
expected = 0.027766750846718695
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word peach
expected = 0.04794175108045175
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word kiwi
expected = 0.0169385076092213
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apricot
expected = 0.017801666182273038
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word lime
expected = 0.02416106287413996
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word fig
expected = 0.019227264232435187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word banana
expected = 0.051002862877480334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apple
expected = 0.019976864637262157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word peach
expected = 0.05152150510448261
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word kiwi
expected = 0.01829498195117974
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word lime
expected = 0.015482990852508524
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word pear
expected = 0.012922084844447151
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word banana
expected = 0.03350846057407129
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apple
expected = 0.024978586583758202
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word papaya
expected = 0.013042649817025421
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word peach
expected = 0.011843083580276532
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word cherry
expected = 0.011843083580276532
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apricot
expected = 0.012321293884309515
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))









#Test #409 checking search results for 'orange peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017698994093024237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013278713200815527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012866065384460858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009864564726963024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008342655060050531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006952768947323818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006435203416657625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('orange peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'orange peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'orange peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'orange peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html', 'title': 'N-81', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'title': 'N-709', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html', 'title': 'N-982', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html', 'title': 'N-363', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html', 'title': 'N-196', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-889.html', 'title': 'N-889', 'score': 1.0000000000000002}]
result = search.search('orange peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'banana papaya peach papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01790696284096535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014161965719320711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011499422137422473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010080906355177124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009692911719615884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007741859239893233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007442078664285085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006397890768738597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005891059250085086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005645634238912236}]
result = search.search('banana papaya peach papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'banana papaya peach papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'banana papaya peach papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'banana papaya peach papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9999091286624014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9997351887885918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html', 'title': 'N-831', 'score': 0.9996159799192317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9995963749928165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-345.html', 'title': 'N-345', 'score': 0.9995411684192026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html', 'title': 'N-860', 'score': 0.9995282732921636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9994435742858131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 0.9994348651396695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html', 'title': 'N-724', 'score': 0.9994184472975944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'title': 'N-27', 'score': 0.9994032440215338}]
result = search.search('banana papaya peach papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'banana papaya peach papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'banana papaya peach papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'tomato coconut fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014716192100639885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013460649485539591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01068057561879902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00981771128384917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007227621524962007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0057990629024355185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005604833509617134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005399117986852951}]
result = search.search('tomato coconut fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'tomato coconut fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'tomato coconut fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'tomato coconut fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html', 'title': 'N-61', 'score': 1.0000000000000002}]
result = search.search('tomato coconut fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'tomato coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'tomato coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014047325222444194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013328542958131748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010428059197353042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009433033776199723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008329941991833546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007759985252067017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006286194236918289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0057468405909061725}]
result = search.search('coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}]
result = search.search('coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'blueberry papaya coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014750615715829812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014559034313732613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012719281621473892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010627538908750504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009083558148257828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007691646978509927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00751626987327812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006865251080095596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005688840746678425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005360372281589691}]
result = search.search('blueberry papaya coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'blueberry papaya coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'blueberry papaya coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'blueberry papaya coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html', 'title': 'N-850', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-647.html', 'title': 'N-647', 'score': 0.9987211336998646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9984365036795587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.998318642107381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-637.html', 'title': 'N-637', 'score': 0.9983145531625747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html', 'title': 'N-273', 'score': 0.9980183401196207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-695.html', 'title': 'N-695', 'score': 0.9979852450926077}]
result = search.search('blueberry papaya coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'blueberry papaya coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'blueberry papaya coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'lime banana orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017431560267035868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015565319151656883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012204027717322945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010372644396160906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008662356532712332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007720712728308277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006867141747518873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006334286228212469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006213102012261031}]
result = search.search('lime banana orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'lime banana orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'lime banana orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'lime banana orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'title': 'N-761', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-994.html', 'title': 'N-994', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html', 'title': 'N-437', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 1.0000000000000002}]
result = search.search('lime banana orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'lime banana orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'lime banana orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'pear pear papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019904321923022963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01568313024970317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013494782279552706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010371377726927766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008104460903046663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00791927158773338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0067213744466415575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.00628033417404254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005287695668871452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 0.005206147972724975}]
result = search.search('pear pear papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'pear pear papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'pear pear papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'pear pear papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.9998640365816137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.999856427381886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-156.html', 'title': 'N-156', 'score': 0.9997430487788386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 0.9997430487788386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-307.html', 'title': 'N-307', 'score': 0.9996436652473737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9995996558626308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 0.9995101959545559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.99949638889677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9994585950720959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-609.html', 'title': 'N-609', 'score': 0.9994470848646031}]
result = search.search('pear pear papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'pear pear papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'pear pear papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'coconut blueberry banana fig apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014972665442686016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013048575941482767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.012636281273890635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010390384697548135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009215198052410502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007600937969841044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007501430151042598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006745960365777852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005649430840664905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005190775335897571}]
result = search.search('coconut blueberry banana fig apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'coconut blueberry banana fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'coconut blueberry banana fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'coconut blueberry banana fig apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9985424039250388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9981498376084282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html', 'title': 'N-813', 'score': 0.9974917589108482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.9951137467930292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html', 'title': 'N-428', 'score': 0.9949752305339566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9948579845743298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9948559008209277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html', 'title': 'N-260', 'score': 0.9945126744764403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-150.html', 'title': 'N-150', 'score': 0.9933459107031103}]
result = search.search('coconut blueberry banana fig apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'coconut blueberry banana fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'coconut blueberry banana fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'lime papaya blueberry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01732516673402734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015301126088774241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012939346200531962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010585230035181192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009457474406135402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008036976494496112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006753505601107101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006422434357272395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006311937548644516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005313650862361177}]
result = search.search('lime papaya blueberry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'lime papaya blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'lime papaya blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'lime papaya blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'title': 'N-189', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html', 'title': 'N-641', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9986680573326812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.998250706161613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9982098495276289}]
result = search.search('lime papaya blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'lime papaya blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'lime papaya blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'title': 'N-69', 'score': 0.005896359403508087}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'fig cherry blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015691220399340147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01273542120136617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011276108183173582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010352906031542236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009900952345510517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008999027611535601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007782472410967127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007326969523757739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005630563985415976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005529722873577924}]
result = search.search('fig cherry blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'fig cherry blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'fig cherry blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'fig cherry blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html', 'title': 'N-14', 'score': 0.9996148612747643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.999579505762267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-751.html', 'title': 'N-751', 'score': 0.9995409579619132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 0.9995409579619132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-308.html', 'title': 'N-308', 'score': 0.9995257991269071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html', 'title': 'N-898', 'score': 0.9995113559282769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.9994975833651457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9994598843324951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html', 'title': 'N-575', 'score': 0.9994598843324951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html', 'title': 'N-806', 'score': 0.9994248228140123}]
result = search.search('fig cherry blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'fig cherry blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'fig cherry blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'cherry coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015525909189760595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014781805689361162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012744408264353147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010296392498062067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00870883828600775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008363579089345773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008186396534831426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007050621806549849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005604204960917585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005435011650916337}]
result = search.search('cherry coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'cherry coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'cherry coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'cherry coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html', 'title': 'N-93', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html', 'title': 'N-931', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'title': 'N-136', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html', 'title': 'N-922', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 1.0000000000000002}]
result = search.search('cherry coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'cherry coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'cherry coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'banana fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01480128877647665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.0131204140910477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010222888724116818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00860663718127972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008344377721569143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007641928784415648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005997574352003075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00598630794335006}]
result = search.search('banana fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'banana fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'banana fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html', 'title': 'N-914', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-624.html', 'title': 'N-624', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html', 'title': 'N-410', 'score': 1.0000000000000002}]
result = search.search('banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'coconut lime peach kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015906454209985158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01403556330557281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012319959477300288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010614272452023543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009222178744336524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0076521710195262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007416097258868427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006293836397403531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005964215529969061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0059222316400902066}]
result = search.search('coconut lime peach kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'coconut lime peach kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'coconut lime peach kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'coconut lime peach kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html', 'title': 'N-166', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-878.html', 'title': 'N-878', 'score': 0.9993112910056495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-473.html', 'title': 'N-473', 'score': 0.998061517253373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-44.html', 'title': 'N-44', 'score': 0.9963104095645822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9957789929977902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 0.9956685295554257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9952249985412603}]
result = search.search('coconut lime peach kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'coconut lime peach kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'coconut lime peach kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0}]
result = search.search('blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'lime coconut orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016778010008256673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015546349031161963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01258063324857477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010271209133599107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009373053426082174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00879097476831529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007622705446222359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006934877179872777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005731420307373523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005600585707237469}]
result = search.search('lime coconut orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'lime coconut orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'lime coconut orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'lime coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-826.html', 'title': 'N-826', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'title': 'N-68', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html', 'title': 'N-398', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-174.html', 'title': 'N-174', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-480.html', 'title': 'N-480', 'score': 1.0000000000000002}]
result = search.search('lime coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'lime coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'lime coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'coconut kiwi cherry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015053722824885237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.0127668392434767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01126059956793807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011023643669661585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010202917444977908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008209176212504563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007075781124719695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006951796558975019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005812873448094358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005299780985789006}]
result = search.search('coconut kiwi cherry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'coconut kiwi cherry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'coconut kiwi cherry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'coconut kiwi cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html', 'title': 'N-385', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-365.html', 'title': 'N-365', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html', 'title': 'N-649', 'score': 0.9999999999999998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9984501397823171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9979731819681907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-818.html', 'title': 'N-818', 'score': 0.9979468272731778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 0.9973765271439233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html', 'title': 'N-718', 'score': 0.9964667344758036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html', 'title': 'N-445', 'score': 0.9964489990631793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9961027278033404}]
result = search.search('coconut kiwi cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'coconut kiwi cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'coconut kiwi cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'papaya tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('papaya tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'papaya tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('papaya tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02015678971628877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013469314021595161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009905549161149855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00806635754175052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006685930958774131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006229262606774017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006044508323419388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005389588078832613}]
result = search.search('blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html', 'title': 'N-919', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html', 'title': 'N-814', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-770.html', 'title': 'N-770', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html', 'title': 'N-856', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-792.html', 'title': 'N-792', 'score': 1.0000000000000002}]
result = search.search('blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'peach blueberry fig pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01655857526303787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014072204087228986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013059408769339843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010620463956293312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009405107114780084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007448313946838984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007049473240040845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005832803950018687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005700202145169931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005575911032637299}]
result = search.search('peach blueberry fig pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'peach blueberry fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'peach blueberry fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'peach blueberry fig pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9984742589864112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9984053466665231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9983112624366861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html', 'title': 'N-335', 'score': 0.998295929223835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 0.9975873452344548}]
result = search.search('peach blueberry fig pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'peach blueberry fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'peach blueberry fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'pear apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019982898567903012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015551288310342833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012680161398007487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010621089353284952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007532286378471528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006340734760716107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006216363448301495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006128309208708313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005416565006152094}]
result = search.search('pear apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'pear apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'pear apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'pear apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'title': 'N-50', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html', 'title': 'N-363', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html', 'title': 'N-683', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-201.html', 'title': 'N-201', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 1.0000000000000002}]
result = search.search('pear apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'lime cherry fig cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014561387852223877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.012058951231636864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012007438765102102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.0090313513713891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008723176025161409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00809224588224192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0065805625277710845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006478007081737823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006141762431114227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006132263116519761}]
result = search.search('lime cherry fig cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'lime cherry fig cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'lime cherry fig cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'lime cherry fig cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-576.html', 'title': 'N-576', 'score': 0.9999844036429268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-657.html', 'title': 'N-657', 'score': 0.9998758712180279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9996868014928849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9996301839445249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'title': 'N-274', 'score': 0.9962668518357511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9960149259601626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html', 'title': 'N-371', 'score': 0.9956454852339639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'title': 'N-80', 'score': 0.9954126346447433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9950921260121977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-968.html', 'title': 'N-968', 'score': 0.9950843045245795}]
result = search.search('lime cherry fig cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'lime cherry fig cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'lime cherry fig cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014690733564521666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013390048489155789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012056010358577845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010995156483129273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010680664594820453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009209949258010617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007747166471037373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006373897310994583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006291412496189925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html', 'title': 'N-445', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html', 'title': 'N-590', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 1.0000000000000002}]
result = search.search('coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018441350764611456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01294063939903812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012705017796983152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01065962688062907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00624249230939875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006052717455158258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00552086020011209}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #475 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'title': 'N-27', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 1.0000000000000002}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'cherry blueberry papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017767092890500366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015302756459583311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013364245329861505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010271866497534947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008155458850744158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008071425571539833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006295875623269535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00623292710876038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005413008925774072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005343259933572169}]
result = search.search('cherry blueberry papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'cherry blueberry papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'cherry blueberry papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'cherry blueberry papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'title': 'N-562', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'title': 'N-738', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9980073343824509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html', 'title': 'N-641', 'score': 0.9979850138151546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 0.9979791415585204}]
result = search.search('cherry blueberry papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'cherry blueberry papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'cherry blueberry papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'coconut pear tomato banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01409210240026215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012992975473000072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.012936123087784837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010549041515143912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009395159201549763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007681103788606516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0074561872493363966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006179164158047488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006099223590345461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005362412851577407}]
result = search.search('coconut pear tomato banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #479 checking search results for 'coconut pear tomato banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'coconut pear tomato banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'coconut pear tomato banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'title': 'N-676', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-640.html', 'title': 'N-640', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9986681433327556}]
result = search.search('coconut pear tomato banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'coconut pear tomato banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'coconut pear tomato banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'tomato lime apricot pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019265187711196383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015633141126780912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012095180001512216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010649582195330607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009086588796785639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00733025574988198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0069334359287806045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005685674831691057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005657473977511697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.00541125268331486}]
result = search.search('tomato lime apricot pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'tomato lime apricot pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'tomato lime apricot pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'tomato lime apricot pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'title': 'N-326', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-466.html', 'title': 'N-466', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html', 'title': 'N-946', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 1.0}]
result = search.search('tomato lime apricot pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'tomato lime apricot pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'tomato lime apricot pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'apple peach tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017860557589908167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014214580111025575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013176205823465932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010480397220105806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008729874563922829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0070761558534509685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006789250538974509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006111647117928612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006018793635977449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00587743012980521}]
result = search.search('apple peach tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'apple peach tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'apple peach tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'apple peach tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-86.html', 'title': 'N-86', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'title': 'N-133', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-382.html', 'title': 'N-382', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 1.0000000000000002}]
result = search.search('apple peach tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'apple peach tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'apple peach tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #489 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #490 checking search results for 'coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #491 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #491 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #491 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #492 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #492 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #492 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #493 checking search results for 'fig fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015691547123573322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013009583874932267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.01110255087924463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01055624634910419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.009682509382080214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008716035192164373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007781447303538833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007091908801085712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0061678922233693225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005669041473510388}]
result = search.search('fig fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #493 checking search results for 'fig fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #493 checking search results for 'fig fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #494 checking search results for 'fig fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html', 'title': 'N-860', 'score': 0.9999961345627825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'title': 'N-821', 'score': 0.9999945109336483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html', 'title': 'N-631', 'score': 0.9999630622903871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.999923433056858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9999218632342693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9999069909647824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-992.html', 'title': 'N-992', 'score': 0.9999018004096191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html', 'title': 'N-14', 'score': 0.9998974492853976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.999889143820081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html', 'title': 'N-267', 'score': 0.9998853874725792}]
result = search.search('fig fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #494 checking search results for 'fig fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #494 checking search results for 'fig fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #495 checking search results for 'coconut pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015192183134745425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013368033979558703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011945231179824822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010532155346072759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009271235455673666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007652103155332945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007017403664539235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006014849678666435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00543441348967106}]
result = search.search('coconut pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #495 checking search results for 'coconut pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #495 checking search results for 'coconut pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #496 checking search results for 'coconut pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html', 'title': 'N-525', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'title': 'N-602', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-640.html', 'title': 'N-640', 'score': 1.0000000000000002}]
result = search.search('coconut pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #496 checking search results for 'coconut pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #496 checking search results for 'coconut pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #497 checking search results for 'coconut tomato pear kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015363231980963645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015062721858567229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012350163228122175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010597306148109468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008899222043851037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008802144234157813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007745761835191219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0071655105652564275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006318548930118936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('coconut tomato pear kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #497 checking search results for 'coconut tomato pear kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #497 checking search results for 'coconut tomato pear kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #498 checking search results for 'coconut tomato pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-192.html', 'title': 'N-192', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html', 'title': 'N-754', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html', 'title': 'N-850', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 1.0}]
result = search.search('coconut tomato pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #498 checking search results for 'coconut tomato pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #498 checking search results for 'coconut tomato pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #499 checking search results for 'tomato papaya kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016318574200614822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014039277899028767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012529115225900427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010523963452668332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009585638791585721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007699993828635363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007449213525731298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006925858951993234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006518091009967331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006297448657263517}]
result = search.search('tomato papaya kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #499 checking search results for 'tomato papaya kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #499 checking search results for 'tomato papaya kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #500 checking search results for 'tomato papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html', 'title': 'N-329', 'score': 1.0000000000000002}]
result = search.search('tomato papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #500 checking search results for 'tomato papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #500 checking search results for 'tomato papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #501 checking search results for 'lime orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.020241696321958474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015690608694266125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012180764506977375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010277790478155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009291123053895204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007714659420544837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007214714129025139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006914626305400278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006600724035738475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006520120568159997}]
result = search.search('lime orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #501 checking search results for 'lime orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #501 checking search results for 'lime orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #502 checking search results for 'lime orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-471.html', 'title': 'N-471', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html', 'title': 'N-710', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html', 'title': 'N-892', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-174.html', 'title': 'N-174', 'score': 1.0000000000000002}]
result = search.search('lime orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #502 checking search results for 'lime orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #502 checking search results for 'lime orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #503 checking search results for 'lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01591513148992107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015458374651140826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012772107716990921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010522734017794648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009861524839444932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008139688309713495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007662519672437822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007172227435151036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006396538699847119}]
result = search.search('lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #503 checking search results for 'lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #503 checking search results for 'lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #504 checking search results for 'lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html', 'title': 'N-56', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 1.0000000000000002}]
result = search.search('lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #504 checking search results for 'lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #504 checking search results for 'lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #505 checking search results for 'tomato peach tomato apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01936597441396615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013253250692357417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010416071883689041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00754299623587247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006342027739056718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00587311614316463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00556536653497155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005460789415174649}]
result = search.search('tomato peach tomato apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #505 checking search results for 'tomato peach tomato apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #505 checking search results for 'tomato peach tomato apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #506 checking search results for 'tomato peach tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'title': 'N-80', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-987.html', 'title': 'N-987', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'title': 'N-38', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html', 'title': 'N-247', 'score': 1.0}]
result = search.search('tomato peach tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #506 checking search results for 'tomato peach tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #506 checking search results for 'tomato peach tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #507 checking search results for 'orange apple papaya orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017897650647184005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013854430971101032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013388145199402509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009041580198511697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.008875401778909123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00825136175114959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006699836153526721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0066345733600494255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00610547565665336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.005864041165482271}]
result = search.search('orange apple papaya orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #507 checking search results for 'orange apple papaya orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #507 checking search results for 'orange apple papaya orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #508 checking search results for 'orange apple papaya orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 0.999839551037265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-609.html', 'title': 'N-609', 'score': 0.9996409941726199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9993302092316133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-529.html', 'title': 'N-529', 'score': 0.9984903839365005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9982075074297314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html', 'title': 'N-108', 'score': 0.998183116363317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-116.html', 'title': 'N-116', 'score': 0.9977702391564665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.9976642098179639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html', 'title': 'N-924', 'score': 0.9961576810457837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-307.html', 'title': 'N-307', 'score': 0.9944434349116}]
result = search.search('orange apple papaya orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #508 checking search results for 'orange apple papaya orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #508 checking search results for 'orange apple papaya orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #509 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #509 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #509 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #510 checking search results for 'apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #510 checking search results for 'apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #510 checking search results for 'apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #511 checking search results for 'papaya fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014459193573518951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01440448834068803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013256742062442607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009988006707605168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009564608091542814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009237240157705223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006958484441660632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006948114764510304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006431263622379831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('papaya fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #511 checking search results for 'papaya fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #511 checking search results for 'papaya fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #512 checking search results for 'papaya fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'title': 'N-222', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-327.html', 'title': 'N-327', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 1.0}]
result = search.search('papaya fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #512 checking search results for 'papaya fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #512 checking search results for 'papaya fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #513 checking search results for 'apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017694252475683084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015487823074951505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013089761444053502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010627916211932417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00987532778280757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0081279191633383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007383794305958331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.007267027893053541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006056788868214248}]
result = search.search('apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #513 checking search results for 'apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #513 checking search results for 'apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #514 checking search results for 'apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html', 'title': 'N-840', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html', 'title': 'N-494', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html', 'title': 'N-606', 'score': 1.0000000000000002}]
result = search.search('apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #514 checking search results for 'apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #514 checking search results for 'apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #515 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02022519327345739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01574050270777139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010316979986851422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.010277232389174969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010268560027568588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009584031976292023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007190977168311921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00628175748090317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006202152161289179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005165781004097482}]
result = search.search('orange tomato kiwi blueberry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #515 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #515 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #516 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html', 'title': 'N-429', 'score': 0.999873197183419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-355.html', 'title': 'N-355', 'score': 0.9997303409675203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html', 'title': 'N-306', 'score': 0.9997070699913149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9996961638159344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'title': 'N-154', 'score': 0.999694037769782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 0.9996857111669679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.9996709851416795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9996660733678114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 0.9996479806879356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9995881386932044}]
result = search.search('orange tomato kiwi blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #516 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #516 checking search results for 'orange tomato kiwi blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #517 checking search results for 'apple peach tomato cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.020339578018588912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013882441746158896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01333922853350601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.0101017420996002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0074385870897347795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006866987116568782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006667990925813613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0065321012838571385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006470863533368393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0060118408228134355}]
result = search.search('apple peach tomato cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #517 checking search results for 'apple peach tomato cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #517 checking search results for 'apple peach tomato cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #518 checking search results for 'apple peach tomato cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html', 'title': 'N-526', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'title': 'N-175', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html', 'title': 'N-993', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-889.html', 'title': 'N-889', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html', 'title': 'N-726', 'score': 1.0000000000000002}]
result = search.search('apple peach tomato cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #518 checking search results for 'apple peach tomato cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #518 checking search results for 'apple peach tomato cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #519 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #519 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #519 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #520 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #520 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #520 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #521 checking search results for 'banana fig papaya lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014731342121052917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013501852213312668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012374447999006105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010455113348930787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009280933791516113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008036454457175381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006827099910714505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006280670491274589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005917373573730895}]
result = search.search('banana fig papaya lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #521 checking search results for 'banana fig papaya lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #521 checking search results for 'banana fig papaya lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #522 checking search results for 'banana fig papaya lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'title': 'N-58', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html', 'title': 'N-550', 'score': 0.9989856728816388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9984246730945336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.9980043822939666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9977979717993399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.9974562747918607}]
result = search.search('banana fig papaya lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #522 checking search results for 'banana fig papaya lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #522 checking search results for 'banana fig papaya lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #523 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #523 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #523 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #524 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #524 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #524 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #525 checking search results for 'cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #525 checking search results for 'cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #525 checking search results for 'cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #526 checking search results for 'cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #526 checking search results for 'cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #526 checking search results for 'cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #527 checking search results for 'cherry fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015290580843955655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01500849591647543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013461532791907215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010060182047999484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009249827597276453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00803866805069972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007829696439426903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007355109130705998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005970512006828934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.0053199650741708225}]
result = search.search('cherry fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #527 checking search results for 'cherry fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #527 checking search results for 'cherry fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #528 checking search results for 'cherry fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html', 'title': 'N-414', 'score': 1.0000000000000002}]
result = search.search('cherry fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #528 checking search results for 'cherry fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #528 checking search results for 'cherry fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #529 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #529 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #529 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #530 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #530 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #530 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #531 checking search results for 'apricot pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01644689398558041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015380568398491083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012886900512789262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01034288983450889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009381059434250742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00709904772733336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006969296500531335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006542000541762488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006061130742942323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005842917620633992}]
result = search.search('apricot pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #531 checking search results for 'apricot pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #531 checking search results for 'apricot pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #532 checking search results for 'apricot pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html', 'title': 'N-874', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html', 'title': 'N-780', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html', 'title': 'N-950', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-702.html', 'title': 'N-702', 'score': 1.0000000000000004}]
result = search.search('apricot pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #532 checking search results for 'apricot pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #532 checking search results for 'apricot pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #533 checking search results for 'peach pear orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01780049108113397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013925654047816066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012926262830151728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010329830057483587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009393484151223222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007396430517857162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00618348059154692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005929055483109864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005928839592395886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005737470819528088}]
result = search.search('peach pear orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #533 checking search results for 'peach pear orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #533 checking search results for 'peach pear orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #534 checking search results for 'peach pear orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html', 'title': 'N-918', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'title': 'N-584', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html', 'title': 'N-452', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html', 'title': 'N-67', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html', 'title': 'N-281', 'score': 0.9988331781061921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-588.html', 'title': 'N-588', 'score': 0.9986878852903234}]
result = search.search('peach pear orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #534 checking search results for 'peach pear orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #534 checking search results for 'peach pear orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #535 checking search results for 'kiwi banana pear cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015400210545375862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015245614483098918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012368735496586701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010050232937150884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007613358392489502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007243976726772582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0070252285090660034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.006875147823324078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0058184786409247536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005704198123157566}]
result = search.search('kiwi banana pear cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #535 checking search results for 'kiwi banana pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #535 checking search results for 'kiwi banana pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #536 checking search results for 'kiwi banana pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html', 'title': 'N-975', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html', 'title': 'N-949', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.9985983336510615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998404598011428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 0.9979994536075144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html', 'title': 'N-317', 'score': 0.9979784589062901}]
result = search.search('kiwi banana pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #536 checking search results for 'kiwi banana pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #536 checking search results for 'kiwi banana pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #537 checking search results for 'lime apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017694252475683084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015487823074951505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013089761444053502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010627916211932417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00987532778280757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0081279191633383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007383794305958331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.007267027893053541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006056788868214248}]
result = search.search('lime apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #537 checking search results for 'lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #537 checking search results for 'lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #538 checking search results for 'lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html', 'title': 'N-840', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html', 'title': 'N-494', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html', 'title': 'N-606', 'score': 1.0000000000000002}]
result = search.search('lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #538 checking search results for 'lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #538 checking search results for 'lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #539 checking search results for 'blueberry fig tomato cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015290580843955652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01500849591647543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013461532791907215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010060182047999484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009249827597276451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008038668050699718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007829696439426903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0073551091307059975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005970512006828933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005319965074170822}]
result = search.search('blueberry fig tomato cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #539 checking search results for 'blueberry fig tomato cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #539 checking search results for 'blueberry fig tomato cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #540 checking search results for 'blueberry fig tomato cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html', 'title': 'N-459', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html', 'title': 'N-247', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 1.0}]
result = search.search('blueberry fig tomato cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #540 checking search results for 'blueberry fig tomato cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #540 checking search results for 'blueberry fig tomato cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #541 checking search results for 'pear apple orange tomato apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01866076909217156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01543207451673278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012913402252588599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010449976865115595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00868124011734018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0075822774198518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006100437214105084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005885931662586426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005806965646326427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005675700700090931}]
result = search.search('pear apple orange tomato apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #541 checking search results for 'pear apple orange tomato apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #541 checking search results for 'pear apple orange tomato apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #542 checking search results for 'pear apple orange tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html', 'title': 'N-477', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-909.html', 'title': 'N-909', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 0.998916215771648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html', 'title': 'N-789', 'score': 0.9988317213505598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9980279473714817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9979750230719945}]
result = search.search('pear apple orange tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #542 checking search results for 'pear apple orange tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #542 checking search results for 'pear apple orange tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #543 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #543 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #543 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #544 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #544 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #544 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #545 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #545 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #545 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #546 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #546 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #546 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #547 checking search results for 'coconut tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014047325222444196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013328542958131748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010428059197353044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009433033776199723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008329941991833546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007759985252067018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006286194236918289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005746840590906174}]
result = search.search('coconut tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #547 checking search results for 'coconut tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #547 checking search results for 'coconut tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #548 checking search results for 'coconut tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}]
result = search.search('coconut tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #548 checking search results for 'coconut tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #548 checking search results for 'coconut tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #549 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #549 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #549 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #550 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #550 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #550 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #551 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #551 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #551 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #552 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #552 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #552 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #553 checking search results for 'peach peach orange kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014632832038459533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01112475654501858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01063450698867505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.00989705314785758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0074557915804320815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007350347807721781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006848561321723527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006518420543656779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0062749180360668535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0061994317665791405}]
result = search.search('peach peach orange kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #553 checking search results for 'peach peach orange kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #553 checking search results for 'peach peach orange kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #554 checking search results for 'peach peach orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9999736294776225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9999628115332971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9998977078382292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9998933948074946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html', 'title': 'N-506', 'score': 0.9996452545633578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 0.9995679797693955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 0.9995194919940746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9995145316492478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9995106202074778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-441.html', 'title': 'N-441', 'score': 0.9994775496049787}]
result = search.search('peach peach orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #554 checking search results for 'peach peach orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #554 checking search results for 'peach peach orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #555 checking search results for 'blueberry cherry pear cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01620073234154308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014942135080306684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012303130617077456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.008911705301020163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008813739970561105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00846457989041663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.006380669108849353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006169430418726276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.005547917759368912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005218115230971018}]
result = search.search('blueberry cherry pear cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #555 checking search results for 'blueberry cherry pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #555 checking search results for 'blueberry cherry pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #556 checking search results for 'blueberry cherry pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'title': 'N-528', 'score': 0.9998792868060092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html', 'title': 'N-524', 'score': 0.999669913187851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.9996359721800119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.999572212260031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-86.html', 'title': 'N-86', 'score': 0.9994635364933151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html', 'title': 'N-181', 'score': 0.9994635364933151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'title': 'N-43', 'score': 0.9994546716154714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-402.html', 'title': 'N-402', 'score': 0.9994504389687007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9994379176098592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html', 'title': 'N-257', 'score': 0.9994379176098592}]
result = search.search('blueberry cherry pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #556 checking search results for 'blueberry cherry pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #556 checking search results for 'blueberry cherry pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #557 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #557 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #557 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #558 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #558 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #558 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #559 checking search results for 'orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015186213758782494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014451716135987839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01337229503184508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009632505084288184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009429031516393818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007409668336084355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006492160104049185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.005958482836424054}]
result = search.search('orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #559 checking search results for 'orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #559 checking search results for 'orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #560 checking search results for 'orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-255.html', 'title': 'N-255', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'title': 'N-232', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-190.html', 'title': 'N-190', 'score': 1.0000000000000002}]
result = search.search('orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #560 checking search results for 'orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #560 checking search results for 'orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #561 checking search results for 'kiwi apricot pear orange cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018210873971221255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015380871299897599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012444525627500171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009898758486644267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008332364462057732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007549298805430012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007105182662534984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005819801815959031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005708079668440355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.0052091719055653496}]
result = search.search('kiwi apricot pear orange cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #561 checking search results for 'kiwi apricot pear orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #561 checking search results for 'kiwi apricot pear orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #562 checking search results for 'kiwi apricot pear orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9986583347767437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9984883165658149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'title': 'N-364', 'score': 0.9964966885783098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9959105293364443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9952095647156989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9947089401042004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9945643830037426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9941780752067887}]
result = search.search('kiwi apricot pear orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #562 checking search results for 'kiwi apricot pear orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #562 checking search results for 'kiwi apricot pear orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #563 checking search results for 'peach papaya cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013567804228147186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013341369618039365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010212955534614578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007852770124571244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006686449203842862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006615844388581724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006531831626631905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00642598965791577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006030969922274791}]
result = search.search('peach papaya cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #563 checking search results for 'peach papaya cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #563 checking search results for 'peach papaya cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #564 checking search results for 'peach papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'title': 'N-738', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html', 'title': 'N-804', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'title': 'N-68', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}]
result = search.search('peach papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #564 checking search results for 'peach papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #564 checking search results for 'peach papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #565 checking search results for 'blueberry tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01565724077618798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014935026865406676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013307002343955644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01043346265125782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009443019363923506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0069354555698375635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0055993451276181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.0055642404984289195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005450973730689284}]
result = search.search('blueberry tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #565 checking search results for 'blueberry tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #565 checking search results for 'blueberry tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #566 checking search results for 'blueberry tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'title': 'N-27', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html', 'title': 'N-940', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-342.html', 'title': 'N-342', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-255.html', 'title': 'N-255', 'score': 1.0}]
result = search.search('blueberry tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #566 checking search results for 'blueberry tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #566 checking search results for 'blueberry tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #567 checking search results for 'kiwi coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014629099954114573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012162184798584356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011184066283882214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010412959514839398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009183727677204854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008357931909783553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007643896345875256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0070726328680207826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0059699722563999495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005376723346915141}]
result = search.search('kiwi coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #567 checking search results for 'kiwi coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #567 checking search results for 'kiwi coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #568 checking search results for 'kiwi coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-209.html', 'title': 'N-209', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html', 'title': 'N-295', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html', 'title': 'N-445', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 1.0}]
result = search.search('kiwi coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #568 checking search results for 'kiwi coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #568 checking search results for 'kiwi coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #569 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #569 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #569 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #570 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #570 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #570 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #571 checking search results for 'blueberry blueberry cherry lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016007192673838346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014250778648342382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013041896873752932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010085895983155218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007647788917404771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007335527084096544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0062744188229438645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00599123720148827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005874643435214525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0054249489611073965}]
result = search.search('blueberry blueberry cherry lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #571 checking search results for 'blueberry blueberry cherry lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #571 checking search results for 'blueberry blueberry cherry lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #572 checking search results for 'blueberry blueberry cherry lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'title': 'N-369', 'score': 0.9996187273341272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 0.9995608176831957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9992974677457912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'title': 'N-57', 'score': 0.998175436903283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9970718561814297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html', 'title': 'N-45', 'score': 0.9969370671720121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html', 'title': 'N-29', 'score': 0.9963423161408963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html', 'title': 'N-965', 'score': 0.9958836660143234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9948686598979948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-588.html', 'title': 'N-588', 'score': 0.9948383546843664}]
result = search.search('blueberry blueberry cherry lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #572 checking search results for 'blueberry blueberry cherry lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #572 checking search results for 'blueberry blueberry cherry lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #573 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #573 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #573 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #574 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #574 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #574 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #575 checking search results for 'fig lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01591513148992107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015458374651140826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012772107716990921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010522734017794648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009861524839444932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008139688309713495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007662519672437822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007172227435151036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006396538699847119}]
result = search.search('fig lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #575 checking search results for 'fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #575 checking search results for 'fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #576 checking search results for 'fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html', 'title': 'N-56', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 1.0000000000000002}]
result = search.search('fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #576 checking search results for 'fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #576 checking search results for 'fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #577 checking search results for 'apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017495935503183513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01565472410022374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013172066540554205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010523785147567601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008949952629575611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008027466192654417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007651805446108983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006937878019581654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006517123537591563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006089791412513555}]
result = search.search('apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #577 checking search results for 'apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #577 checking search results for 'apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #578 checking search results for 'apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html', 'title': 'N-129', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-471.html', 'title': 'N-471', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 1.0000000000000002}]
result = search.search('apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #578 checking search results for 'apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #578 checking search results for 'apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #579 checking search results for 'peach orange blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018264002061276034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014538779740506404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012778506293286206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01022999535548577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009485070504710424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006788994684359253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006162901150967686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.005737876611361666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005366277935310603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005199101696967744}]
result = search.search('peach orange blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #579 checking search results for 'peach orange blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #579 checking search results for 'peach orange blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #580 checking search results for 'peach orange blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-405.html', 'title': 'N-405', 'score': 0.9996315873118998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 0.9995514314076033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html', 'title': 'N-988', 'score': 0.9995318609457422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'title': 'N-773', 'score': 0.9995157384628534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 0.9994723070938865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html', 'title': 'N-712', 'score': 0.9994400994013379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'title': 'N-177', 'score': 0.9994367685351555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html', 'title': 'N-789', 'score': 0.9994337319389521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html', 'title': 'N-824', 'score': 0.9993217400635704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 0.9993143530936403}]
result = search.search('peach orange blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #580 checking search results for 'peach orange blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #580 checking search results for 'peach orange blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #581 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01577388481661061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01501594023931479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012561653025473225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010480901831233711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008682569352348589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.0078025765443094485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0069673910880397065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00622641297417823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006139738345580611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005322695057681177}]
result = search.search('kiwi apricot coconut tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #581 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #581 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #582 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html', 'title': 'N-754', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'title': 'N-749', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html', 'title': 'N-670', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-637.html', 'title': 'N-637', 'score': 1.0}]
result = search.search('kiwi apricot coconut tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #582 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #582 checking search results for 'kiwi apricot coconut tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #583 checking search results for 'banana apricot fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014902483337966376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012700386358253338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011932756144592343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010152341792154868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008829402001299903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006902958072586201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006857292985551132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006757454468475511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006000721445608159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005651129560192068}]
result = search.search('banana apricot fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #583 checking search results for 'banana apricot fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #583 checking search results for 'banana apricot fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #584 checking search results for 'banana apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-591.html', 'title': 'N-591', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'title': 'N-211', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html', 'title': 'N-321', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html', 'title': 'N-739', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html', 'title': 'N-322', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html', 'title': 'N-859', 'score': 1.0}]
result = search.search('banana apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #584 checking search results for 'banana apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #584 checking search results for 'banana apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #585 checking search results for 'cherry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018441350764611456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01570413341180749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013265727436601857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010225433169995992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008058475906186306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007782354156845975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0073066124624036055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006796019569364065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005800703394430255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00552086020011209}]
result = search.search('cherry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #585 checking search results for 'cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #585 checking search results for 'cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #586 checking search results for 'cherry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html', 'title': 'N-940', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}]
result = search.search('cherry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #586 checking search results for 'cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #586 checking search results for 'cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #587 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #587 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #587 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #588 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #588 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #588 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #589 checking search results for 'kiwi kiwi banana apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017742119114651185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015691968741112238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010616315981103788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.010468659698315069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00945582106727085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009065082331561407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007165339034641332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006436261704948918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006138017533833244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005817099155842063}]
result = search.search('kiwi kiwi banana apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #589 checking search results for 'kiwi kiwi banana apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #589 checking search results for 'kiwi kiwi banana apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #590 checking search results for 'kiwi kiwi banana apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-442.html', 'title': 'N-442', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-520.html', 'title': 'N-520', 'score': 0.9997440638679513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 0.9997173519967952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9996046386586384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-994.html', 'title': 'N-994', 'score': 0.9995674236717758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 0.9995501301096336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9992501876523844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 0.999131725744486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html', 'title': 'N-459', 'score': 0.9983123360530907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9975890494915503}]
result = search.search('kiwi kiwi banana apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #590 checking search results for 'kiwi kiwi banana apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #590 checking search results for 'kiwi kiwi banana apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #591 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #591 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #591 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #592 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #592 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #592 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #593 checking search results for 'kiwi blueberry lime tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019322534361195545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014417610242148835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.010808735752811492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009674866439517081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00903294862073473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007927618261109302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007092972402308859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006440551356389314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0056498885348771535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005644074794078632}]
result = search.search('kiwi blueberry lime tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #593 checking search results for 'kiwi blueberry lime tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #593 checking search results for 'kiwi blueberry lime tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #594 checking search results for 'kiwi blueberry lime tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 0.9998496918416377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-547.html', 'title': 'N-547', 'score': 0.9998033607678182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html', 'title': 'N-947', 'score': 0.9998033607678182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.999766651110689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.9997391548432779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html', 'title': 'N-814', 'score': 0.999703989521183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9996964853960908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 0.9996646061383002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 0.99964189426927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html', 'title': 'N-263', 'score': 0.9996338081104873}]
result = search.search('kiwi blueberry lime tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #594 checking search results for 'kiwi blueberry lime tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #594 checking search results for 'kiwi blueberry lime tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #595 checking search results for 'cherry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.020339578018588912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013249580661798111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.012865796197382606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009893691441367338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008144591433535204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007008201687837978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00670547562812001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.005987541472078051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.00575230169456356}]
result = search.search('cherry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #595 checking search results for 'cherry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #595 checking search results for 'cherry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #596 checking search results for 'cherry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-964.html', 'title': 'N-964', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'title': 'N-176', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-261.html', 'title': 'N-261', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'title': 'N-280', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html', 'title': 'N-804', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html', 'title': 'N-526', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'title': 'N-175', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}]
result = search.search('cherry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #596 checking search results for 'cherry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #596 checking search results for 'cherry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #597 checking search results for 'kiwi banana coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013468765460458972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012125569673855521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011395755690131475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010486337956748387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008306960209405266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008028352424879334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007676064749552208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006182847666225432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006045119826240381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005301810400783367}]
result = search.search('kiwi banana coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #597 checking search results for 'kiwi banana coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #597 checking search results for 'kiwi banana coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #598 checking search results for 'kiwi banana coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html', 'title': 'N-534', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html', 'title': 'N-468', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html', 'title': 'N-795', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'title': 'N-676', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998426224097115}]
result = search.search('kiwi banana coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #598 checking search results for 'kiwi banana coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #598 checking search results for 'kiwi banana coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #599 checking search results for 'fig peach pear lime apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01660174866641072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01451596761293881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012458862980802869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010483291940721997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009188312875520632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00724264003812475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006522804481487976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00583442465360035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005674158249414345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005409167974249673}]
result = search.search('fig peach pear lime apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #599 checking search results for 'fig peach pear lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #599 checking search results for 'fig peach pear lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #600 checking search results for 'fig peach pear lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9984036778636265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9982198660845653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9975754014401623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9975587649837766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9971235311531006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9963771097762252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.996260094451802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9962013161365705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9953298673260305}]
result = search.search('fig peach pear lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #600 checking search results for 'fig peach pear lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #600 checking search results for 'fig peach pear lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #601 checking search results for 'orange orange tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('orange orange tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #601 checking search results for 'orange orange tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #601 checking search results for 'orange orange tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #602 checking search results for 'orange orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('orange orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #602 checking search results for 'orange orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #602 checking search results for 'orange orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #603 checking search results for 'coconut tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014047325222444196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013328542958131748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010428059197353044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009433033776199723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008329941991833546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007759985252067018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006286194236918289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005746840590906174}]
result = search.search('coconut tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #603 checking search results for 'coconut tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #603 checking search results for 'coconut tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #604 checking search results for 'coconut tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}]
result = search.search('coconut tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #604 checking search results for 'coconut tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #604 checking search results for 'coconut tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #605 checking search results for 'lime lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #605 checking search results for 'lime lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #605 checking search results for 'lime lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #606 checking search results for 'lime lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('lime lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #606 checking search results for 'lime lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #606 checking search results for 'lime lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #607 checking search results for 'apricot apple apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01514362260707827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014543708706366015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012111661628372123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010381317558868258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00971396224127608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007391823922637443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006765200094636795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006408359456414945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005499818466908993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005399468954766673}]
result = search.search('apricot apple apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #607 checking search results for 'apricot apple apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #607 checking search results for 'apricot apple apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #608 checking search results for 'apricot apple apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'title': 'N-154', 'score': 0.9998708372260742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html', 'title': 'N-731', 'score': 0.9998588236581499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9996167287007279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html', 'title': 'N-932', 'score': 0.9995196323143675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-910.html', 'title': 'N-910', 'score': 0.9994931955331019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.999469079567407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-802.html', 'title': 'N-802', 'score': 0.999469079567407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.9994470087561994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.9994080853302016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'title': 'N-222', 'score': 0.9993993001436143}]
result = search.search('apricot apple apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #608 checking search results for 'apricot apple apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #608 checking search results for 'apricot apple apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
