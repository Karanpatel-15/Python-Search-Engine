
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-outgoing-links-failed.txt', 'w')
success_output = open('fruits5-outgoing-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-129.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-129.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-389.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-229.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-878.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-589.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-449.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-470.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-643.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-510.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-510.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-510.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-510.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-697.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-936.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-936.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-936.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-936.html\n\n')
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


output.close()
success_output.close()
