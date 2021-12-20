
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-incoming-links-failed.txt', 'w')
success_output = open('fruits5-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-785.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-940.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-290.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-467.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-613.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-646.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-929.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-396.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-935.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-715.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-447.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-643.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-453.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-947.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-975.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-708.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-220.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-589.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html\n\n')
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
