
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-all-failed.txt', 'w')
success_output = open('fruits5-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-929.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-994.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-479.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-708.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-775.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-301.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-468.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-491.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-491.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-491.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-491.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-864.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html\n\n')
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









#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-694.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-549.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-663.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-761.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-251.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-534.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-454.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-552.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-290.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-170.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-258.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-763.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-227.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-579.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-982.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-541.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-331.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-935.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-551.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-82.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-452.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-856.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-993.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html\n\n')
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









#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html
expected = 0.0003713530604975169
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html
expected = 0.0003801652233801167
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html
expected = 0.001456743834260273
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html
expected = 0.0009618890568630007
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html
expected = 0.0006325046863019859
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html
expected = 0.0004104182013565704
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html
expected = 0.0006558403633696143
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html
expected = 0.0009452306368058312
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html
expected = 0.002080860004670832
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html
expected = 0.0003676170308978384
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html
expected = 0.0006619918318946972
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html
expected = 0.0009185184398499259
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html
expected = 0.000994319886062199
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html
expected = 0.0008912071586356777
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html
expected = 0.0012810357978514807
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html
expected = 0.002110864034022044
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html
expected = 0.0006253718521702853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html
expected = 0.0007559546643606753
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html
expected = 0.00036046979920233027
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html
expected = 0.0006299527942065828
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html
expected = 0.0006057208435914266
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html
expected = 0.0011706148736942389
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html
expected = 0.0011731334297283356
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html
expected = 0.000933913143987986
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html
expected = 0.0007842102579696278
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html
expected = 0.00035816970936534325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html
expected = 0.0015332899184783136
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html
expected = 0.0003927442616676161
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-702.html
expected = 0.0003591615108148512
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-702.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-702.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-702.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html
expected = 0.0029863525627415173
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html
expected = 0.0006735601922348767
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html
expected = 0.0003660404020985391
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html
expected = 0.0009600987000536588
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html
expected = 0.000364422637088999
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html
expected = 0.00035474686013413495
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html
expected = 0.0030725738873122943
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html
expected = 0.0010304641619843422
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-925.html
expected = 0.0003773451373111397
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-925.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-925.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-925.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html
expected = 0.001992261020904825
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
expected = 0.003145577267715368
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html
expected = 0.0007756732301099296
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html
expected = 0.0004352366610068793
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html
expected = 0.0013217555439922208
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html
expected = 0.0003551766785333776
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-941.html
expected = 0.00036421229280495605
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-941.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-941.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-941.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html
expected = 0.0004234654237771032
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html
expected = 0.00035816970936534325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html
expected = 0.0008986465520233277
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html
expected = 0.0006277864342867645
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html
expected = 0.0006046760136765321
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html\n\n')
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
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word peach
expected = 0.1600404125104682
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word pear
expected = 0.16812275880832706
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word orange
expected = 0.16650266314016507
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word blueberry
expected = 0.1729939903610231
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word lime
expected = 0.16326791954086414
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word banana
expected = 0.16326791954086414
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word coconut
expected = 0.1600404125104682
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word cherry
expected = 0.15682010974282581
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word apricot
expected = 0.1729939903610231
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word apple
expected = 0.15521264992094008
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word papaya
expected = 0.16650266314016507
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word papaya\n\n')
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









#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word lime
expected = 0.14516129032258066
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word kiwi
expected = 0.03225806451612903
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word fig
expected = 0.08064516129032258
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word banana
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word orange
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word blueberry
expected = 0.04838709677419355
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word coconut
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word apple
expected = 0.03225806451612903
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word cherry
expected = 0.04838709677419355
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word peach
expected = 0.12903225806451613
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word lime
expected = 0.02702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word kiwi
expected = 0.1891891891891892
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word banana
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word orange
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word blueberry
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word coconut
expected = 0.10810810810810811
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word apple
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word cherry
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word peach
expected = 0.02702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word lime
expected = 0.03333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word kiwi
expected = 0.13333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word fig
expected = 0.08888888888888889
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word banana
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word orange
expected = 0.044444444444444446
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word blueberry
expected = 0.08888888888888889
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word coconut
expected = 0.07777777777777778
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word apple
expected = 0.03333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word cherry
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word peach
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word lime
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word kiwi
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word fig
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word banana
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word orange
expected = 0.19047619047619047
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word blueberry
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word coconut
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word apple
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word cherry
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word peach
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word orange
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word cherry
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word lime
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word kiwi
expected = 0.023809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word banana
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word orange
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word blueberry
expected = 0.11904761904761904
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word coconut
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word apple
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word peach
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word lime
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word kiwi
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word fig
expected = 0.16
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word banana
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word orange
expected = 0.16
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word blueberry
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word coconut
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word apple
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word cherry
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word peach
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word lime
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word kiwi
expected = 0.12698412698412698
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word fig
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word banana
expected = 0.06349206349206349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word orange
expected = 0.07936507936507936
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word blueberry
expected = 0.07936507936507936
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word coconut
expected = 0.06349206349206349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word apple
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word cherry
expected = 0.06349206349206349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word peach
expected = 0.06349206349206349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word lime
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word kiwi
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word fig
expected = 0.13043478260869565
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word banana
expected = 0.13043478260869565
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word orange
expected = 0.021739130434782608
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word blueberry
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word coconut
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word apple
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word cherry
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word peach
expected = 0.10869565217391304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word lime
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word fig
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word banana
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word blueberry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word apple
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word cherry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word peach
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
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


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
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









#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word apple
expected = 0.005032223466986546
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word lime
expected = 0.030110616041823857
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word pear
expected = 0.02610580365020783
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word papaya
expected = 0.0447041062050655
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word peach
expected = 0.015229002829130773
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word kiwi
expected = 0.011094162973435432
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word fig
expected = 0.010677871968460022
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word banana
expected = 0.025351952823775708
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word orange
expected = 0.010677871968460022
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word coconut
expected = 0.010263445655086793
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word apple
expected = 0.015449195653503047
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word papaya
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word peach
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word kiwi
expected = 0.048456986672874264
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word fig
expected = 0.032075918518253574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word banana
expected = 0.031452761085442586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word orange
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word coconut
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word apple
expected = 0.01378432166206501
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word lime
expected = 0.0073614059198126944
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word pear
expected = 0.022065193013251137
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word papaya
expected = 0.021852564313417096
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word peach
expected = 0.017633719608384665
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word kiwi
expected = 0.01536346947207686
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word fig
expected = 0.018345749237999174
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word banana
expected = 0.010957595129481424
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word orange
expected = 0.014786979460008884
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word coconut
expected = 0.017633719608384665
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word apple
expected = 0.01723346422005665
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word lime
expected = 0.009238274956658295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word pear
expected = 0.027487857933061795
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word papaya
expected = 0.03565235033561855
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word kiwi
expected = 0.009788610360804058
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word banana
expected = 0.009238274956658295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word orange
expected = 0.009421308162867265
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word coconut
expected = 0.009055651221051234
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word apple
expected = 0.024906146989808718
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word lime
expected = 0.006827893080495147
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word pear
expected = 0.013863765868768701
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word papaya
expected = 0.02671779526008907
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word peach
expected = 0.025680832331164163
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word kiwi
expected = 0.021103627598489452
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word fig
expected = 0.006963170626144982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word banana
expected = 0.013463425335388893
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word orange
expected = 0.013730169280254405
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word coconut
expected = 0.03167829964507522
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word apple
expected = 0.022637899477057997
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word lime
expected = 0.0049590424881996555
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word pear
expected = 0.015007871152357993
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word papaya
expected = 0.019620089449017584
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word peach
expected = 0.01885860051541483
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word kiwi
expected = 0.029985325638845553
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word fig
expected = 0.0050572934550305905
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word banana
expected = 0.01923891861627544
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word orange
expected = 0.010010305351485284
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word coconut
expected = 0.01885860051541483
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word apple
expected = 0.015273499669342926
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word lime
expected = 0.016066168037153453
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word pear
expected = 0.01919474684479503
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word papaya
expected = 0.03172240474376973
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word peach
expected = 0.018271977124627414
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word kiwi
expected = 0.014265458145399314
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word fig
expected = 0.019009778869994116
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word banana
expected = 0.013463425335388893
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word orange
expected = 0.019009778869994116
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word coconut
expected = 0.010617480239358122
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word apple
expected = 0.0299009530416653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word lime
expected = 0.013089246038499619
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word pear
expected = 0.019946840068772714
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word papaya
expected = 0.013348576560758857
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word peach
expected = 0.006504359964199269
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word kiwi
expected = 0.007030819074386683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word fig
expected = 0.02599426288654461
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word banana
expected = 0.025489257297414712
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word orange
expected = 0.013348576560758857
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word coconut
expected = 0.030830997742012325
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word apple
expected = 0.019068921384461226
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word lime
expected = 0.005177039558695577
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word pear
expected = 0.015653809937296027
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word papaya
expected = 0.010445670339545651
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word peach
expected = 0.019662044595291313
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word kiwi
expected = 0.01085290865595697
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word fig
expected = 0.015502963794576245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word banana
expected = 0.005177039558695577
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word orange
expected = 0.03930584382634521
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word coconut
expected = 0.01004025616504377
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word apple
expected = 0.01736719042308989
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word lime
expected = 0.011130219408265167
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word pear
expected = 0.01516430448276819
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word papaya
expected = 0.011350736740089741
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word peach
expected = 0.01790738268353072
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word kiwi
expected = 0.01560367889581459
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word fig
expected = 0.029152402922362774
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word banana
expected = 0.018268517740610793
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word orange
expected = 0.018630462518227475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word coconut
expected = 0.021328030573227835
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
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


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
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









#Test #409 checking search results for 'orange pear lime peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013994003405213932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013753037434234137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00861265836939209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008509400676560148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007443311702664015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007408120553041873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006693527996278233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006537344326340538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005509779814381281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.0051337030095117975}]
result = search.search('orange pear lime peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'orange pear lime peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'orange pear lime peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'orange pear lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-301.html', 'title': 'N-301', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9986075570772972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html', 'title': 'N-506', 'score': 0.9983258898421853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9981086509189501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9980951979411625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html', 'title': 'N-79', 'score': 0.9978642905467471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9974662017822369}]
result = search.search('orange pear lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'orange pear lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'orange pear lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'banana apple coconut apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014424006027442307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00845416480749134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008281806424425428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007192859440402176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006602803773137045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00640234710700228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005326443305091466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005135795744845916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00503340955504127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005015611801099957}]
result = search.search('banana apple coconut apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'banana apple coconut apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'banana apple coconut apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'banana apple coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html', 'title': 'N-926', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'title': 'N-894', 'score': 0.9984576627337234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9982377618426775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9977762935067521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.997656060014274}]
result = search.search('banana apple coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'banana apple coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'banana apple coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'kiwi apricot lime apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019978055694359842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014323088365428975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007701778966641112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007537694334408707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007218596039757118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00702854722878528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006444843730324607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005938249500163212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005277916728176536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.004878730484408592}]
result = search.search('kiwi apricot lime apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'kiwi apricot lime apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'kiwi apricot lime apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'kiwi apricot lime apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'title': 'N-83', 'score': 0.9997180883305372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9981517247213916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.9981372466620997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 0.9980823965623913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html', 'title': 'N-748', 'score': 0.9961635781466519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 0.9960935200024961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.9956806468960364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html', 'title': 'N-509', 'score': 0.9937334127804747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9937108385491148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html', 'title': 'N-335', 'score': 0.9936830714506485}]
result = search.search('kiwi apricot lime apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'kiwi apricot lime apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'kiwi apricot lime apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'pear coconut banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014160845880991597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007958038357919216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007034953547617369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0068561280630818735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.006755789757906551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005735286905705026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.005705985434374328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005476176720414155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005147028312740328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004785585477057077}]
result = search.search('pear coconut banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'pear coconut banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'pear coconut banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'pear coconut banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'title': 'N-56', 'score': 0.9997939005062418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'title': 'N-150', 'score': 0.999688179935051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9996411642018201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html', 'title': 'N-753', 'score': 0.9996258556836237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-848.html', 'title': 'N-848', 'score': 0.9996120752843511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'title': 'N-645', 'score': 0.9996018066887447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html', 'title': 'N-409', 'score': 0.9995648889919552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0.9995236827342882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html', 'title': 'N-719', 'score': 0.9995110345040599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html', 'title': 'N-341', 'score': 0.9995012745374197}]
result = search.search('pear coconut banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'pear coconut banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'pear coconut banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'apricot cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013344890210348083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00866038207540058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008230099641992174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007275090154899206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007217069008063256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006950726727262668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005720166621326257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005704531874527407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00523177685796281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005059773121328764}]
result = search.search('apricot cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'apricot cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'apricot cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'apricot cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html', 'title': 'N-134', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html', 'title': 'N-215', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-981.html', 'title': 'N-981', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}]
result = search.search('apricot cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'apricot cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'apricot cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'orange peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013692144575381184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008893938092107867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00849192384023668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007485732435160227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007357780214854544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006880183862835963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006082358505998806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005210107438757277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005162014559694473}]
result = search.search('orange peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'orange peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'orange peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'orange peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0}]
result = search.search('orange peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'fig fig apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.023921620749454215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012223845404672015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007981793558129781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.0076881447494163615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0073695632332581315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00693852611548278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006764153925570073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00648718233945708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006186280560689189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004779001169591915}]
result = search.search('fig fig apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'fig fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'fig fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'fig fig apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'title': 'N-195', 'score': 0.9999952646357481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html', 'title': 'N-662', 'score': 0.9999910216667248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'title': 'N-411', 'score': 0.9999755946732214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9999097878388385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9999076944353765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9999054814651953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html', 'title': 'N-530', 'score': 0.9999043270474012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html', 'title': 'N-821', 'score': 0.9998966390389291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9998873686078243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.999881988573843}]
result = search.search('fig fig apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'fig fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'fig fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'lime lime apple cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02042345954372802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014287993168503897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007778213207518296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007497564507432366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007093519100785846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00702037306312657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006171713405434117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005528162653285501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0052679851345095955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0048912589627719}]
result = search.search('lime lime apple cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'lime lime apple cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'lime lime apple cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'lime lime apple cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 0.9998407300010744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html', 'title': 'N-813', 'score': 0.9997399385219103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-348.html', 'title': 'N-348', 'score': 0.9996961687208296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-52.html', 'title': 'N-52', 'score': 0.9996961687208296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html', 'title': 'N-789', 'score': 0.9996961687208296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-118.html', 'title': 'N-118', 'score': 0.9994973220551601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html', 'title': 'N-299', 'score': 0.9992270094873968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-289.html', 'title': 'N-289', 'score': 0.9983318323584842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-873.html', 'title': 'N-873', 'score': 0.9982403383193905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9981728268468756}]
result = search.search('lime lime apple cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'lime lime apple cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'lime lime apple cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'apple pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014461573016530194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008928969981629422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008209016180963109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007153645024737878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00698814462047899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006265960479711157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005436730372873302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005407095961921865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005320191395844885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005152076450230817}]
result = search.search('apple pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'apple pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'apple pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'apple pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-764.html', 'title': 'N-764', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html', 'title': 'N-951', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'title': 'N-150', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0}]
result = search.search('apple pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'apple pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'apple pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'apple coconut kiwi apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013817270207861344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008723297432049274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008383443606450235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007101222953121558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006794788949864952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.005888272649649275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005080543428384343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00501713860356281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004624503436962587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.004622453306765576}]
result = search.search('apple coconut kiwi apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'apple coconut kiwi apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'apple coconut kiwi apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'apple coconut kiwi apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 0.9996124675627298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-607.html', 'title': 'N-607', 'score': 0.9995299529774035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9974763469274588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 0.9962879131952684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'title': 'N-473', 'score': 0.9962432771805979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html', 'title': 'N-241', 'score': 0.9948139025166677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'title': 'N-29', 'score': 0.9940399089965288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 0.9936115240729333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html', 'title': 'N-724', 'score': 0.9931233231558335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'title': 'N-352', 'score': 0.9929948980032068}]
result = search.search('apple coconut kiwi apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'apple coconut kiwi apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'apple coconut kiwi apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'tomato papaya cherry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.016256695121624677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01358827037480748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008435280525477401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007891902440310135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007516955439568053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007350894190339693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006018238980833334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005917898281897569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005697583526537973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005157742572257804}]
result = search.search('tomato papaya cherry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'tomato papaya cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'tomato papaya cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'tomato papaya cherry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html', 'title': 'N-706', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-534.html', 'title': 'N-534', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html', 'title': 'N-902', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html', 'title': 'N-428', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html', 'title': 'N-409', 'score': 1.0}]
result = search.search('tomato papaya cherry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'tomato papaya cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'tomato papaya cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'cherry tomato banana apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014169017626527839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008120456663549354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007924193383087554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007066355851767382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007058447408870866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0058060531067316125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005769005785511855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0057254988119584335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005152927270294518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005006244520460688}]
result = search.search('cherry tomato banana apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'cherry tomato banana apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'cherry tomato banana apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'cherry tomato banana apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'title': 'N-107', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-348.html', 'title': 'N-348', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 1.0000000000000002}]
result = search.search('cherry tomato banana apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'cherry tomato banana apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'cherry tomato banana apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008904284110532115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698917378646351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007404620178416595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00659603485468099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006337194041189021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005746968466638174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005208716022108618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005161326974356845}]
result = search.search('peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html', 'title': 'N-419', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'title': 'N-988', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'title': 'N-635', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'title': 'N-368', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-564.html', 'title': 'N-564', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'title': 'N-516', 'score': 1.0000000000000002}]
result = search.search('peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'papaya fig kiwi kiwi pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015147141553580129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01393136588477922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008728170625653543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008563220842187184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007330988242988315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007318310633567839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006270635599180728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0055782310336244915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00545562790243829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0049456267045939846}]
result = search.search('papaya fig kiwi kiwi pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'papaya fig kiwi kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'papaya fig kiwi kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'papaya fig kiwi kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 0.9996545199261818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html', 'title': 'N-934', 'score': 0.9996184188756467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 0.9995546314296936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9984715119012577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 0.9982731779883677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9979782525678724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9973803492433155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9966208565528186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'title': 'N-352', 'score': 0.9965431643147955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9964742464091867}]
result = search.search('papaya fig kiwi kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'papaya fig kiwi kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'papaya fig kiwi kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'apricot apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'apricot apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'apricot apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'orange kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01558467177041877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013783952111422401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008720310103784904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008380290743278836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007486801522582085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007467268142873773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006991336312727861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006679224718218902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005779038744051266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005133552387309325}]
result = search.search('orange kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'orange kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'orange kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'orange kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'title': 'N-121', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'title': 'N-920', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html', 'title': 'N-687', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html', 'title': 'N-86', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html', 'title': 'N-734', 'score': 1.0}]
result = search.search('orange kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'orange kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'orange kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01456183739875891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009127572540961207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008770733795356868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007233552206223568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0071511356635441704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070123354005586225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006876340113481271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005468175741979357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005027497894470612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004831456740889294}]
result = search.search('blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'title': 'N-433', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'title': 'N-451', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'title': 'N-196', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}]
result = search.search('blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'banana fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.016421453893429357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014468272194609855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00861959746702084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008584995212966011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007670675252613979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007218280630581335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00694037950789385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006246140756815161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006080847160657238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005284088882704033}]
result = search.search('banana fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'banana fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'banana fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'banana fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html', 'title': 'N-930', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html', 'title': 'N-214', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html', 'title': 'N-962', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html', 'title': 'N-426', 'score': 1.0000000000000002}]
result = search.search('banana fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'banana fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'banana fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014558247340647017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008876792757873259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007598885617369492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007431552992537413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0067796036349541625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067394492017669476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006080554032725778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005430448110738531}]
result = search.search('fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'title': 'N-451', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'title': 'N-97', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 1.0000000000000002}]
result = search.search('fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'pear pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014118518165169574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008872732362372793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00881468552668238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007406013458594202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007402785958000581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006239220287332047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006107175580784971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006060330507507571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005150639720882286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005137813727720782}]
result = search.search('pear pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'pear pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'pear pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'pear pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html', 'title': 'N-388', 'score': 0.9999973978324258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9999959322219028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.999994569395153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.999994569395153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html', 'title': 'N-748', 'score': 0.9999624326708397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html', 'title': 'N-681', 'score': 0.9999481489221225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-424.html', 'title': 'N-424', 'score': 0.9999264205182716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9999184245440982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9999135628149152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9999125060169373}]
result = search.search('pear pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'pear pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'pear pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'lime coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019792678824805714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014578217103481284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008759987301724396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008672520822113639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00725488972087977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006902748859108898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006691175221368855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005329399002309876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005291352322939725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0050555029668536925}]
result = search.search('lime coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'lime coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'lime coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'lime coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html', 'title': 'N-325', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-468.html', 'title': 'N-468', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html', 'title': 'N-144', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-58.html', 'title': 'N-58', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0}]
result = search.search('lime coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'lime coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'lime coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'cherry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013975587608642773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008350186148847688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008110232231998544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007594846358933274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007065104409528041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007011160176183811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006063707002572326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005137378631206668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005029248487485744}]
result = search.search('cherry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'cherry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'cherry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-280.html', 'title': 'N-280', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html', 'title': 'N-299', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-599.html', 'title': 'N-599', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html', 'title': 'N-545', 'score': 1.0000000000000002}]
result = search.search('cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'blueberry fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.022335859703798786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01406067486537114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009039555504678365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008298103586484215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007624846053790199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006981331122332366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006669898190556312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005975305140922621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005308763772218504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.00494698933128137}]
result = search.search('blueberry fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'blueberry fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'blueberry fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'blueberry fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html', 'title': 'N-907', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html', 'title': 'N-395', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-958.html', 'title': 'N-958', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-349.html', 'title': 'N-349', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 1.0}]
result = search.search('blueberry fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'blueberry fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'blueberry fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321568}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'apricot orange kiwi apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014088210019028198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008803524783139031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008744087540651162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007406956202146241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006959251443727673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00649819274558613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0061571685150521695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005582019960111209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005051011858987999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004869067770464816}]
result = search.search('apricot orange kiwi apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'apricot orange kiwi apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'apricot orange kiwi apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'apricot orange kiwi apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-305.html', 'title': 'N-305', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html', 'title': 'N-260', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-294.html', 'title': 'N-294', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html', 'title': 'N-488', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9983688765582184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'title': 'N-836', 'score': 0.9979826572837273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9979542250255392}]
result = search.search('apricot orange kiwi apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'apricot orange kiwi apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'apricot orange kiwi apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'banana blueberry apricot orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014000149786033112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008983714585028791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008202108748697524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007213213914376796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007049849643410205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006880332453368173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0064720778922497234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0051616370227377225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.004925933846575495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.00485180793060449}]
result = search.search('banana blueberry apricot orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'banana blueberry apricot orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'banana blueberry apricot orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'banana blueberry apricot orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html', 'title': 'N-173', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'title': 'N-193', 'score': 0.9988412458424346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 0.9983367563082383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 0.9981705527610664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 0.9979162206251949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9972888264828853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9972444024868059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'title': 'N-316', 'score': 0.997221568262601}]
result = search.search('banana blueberry apricot orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'banana blueberry apricot orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'banana blueberry apricot orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'peach kiwi apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014622749920812105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009101152143083319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008845987554787245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0070886331231578125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006745052043280208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005804103378289006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005777849657910083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005150451398020083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004981904170788394}]
result = search.search('peach kiwi apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'peach kiwi apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'peach kiwi apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'peach kiwi apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'title': 'N-633', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html', 'title': 'N-123', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-647.html', 'title': 'N-647', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}]
result = search.search('peach kiwi apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'peach kiwi apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'peach kiwi apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'pear blueberry peach papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01390588936139424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.012366553237160868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008623368218699473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008602989718650526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007292400888926825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0071269293422324435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006564136489403878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006224539932182874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005234494914305682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005156145834676858}]
result = search.search('pear blueberry peach papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'pear blueberry peach papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'pear blueberry peach papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'pear blueberry peach papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9986000909045853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9974931929153759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9962531926837547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9961852574054185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html', 'title': 'N-249', 'score': 0.9949213143602299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 0.994867602659758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9942663274130357}]
result = search.search('pear blueberry peach papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'pear blueberry peach papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'pear blueberry peach papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'apple cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012197350416019695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007612203895038767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0074383273384642885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006469839709715069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0061835320765737025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006091805691636445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.005829898826519669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005393084680566809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005110726777046612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004991904754149033}]
result = search.search('apple cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'apple cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'apple cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'apple cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9999992409058738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html', 'title': 'N-314', 'score': 0.9999973956340058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'title': 'N-147', 'score': 0.9999966985534778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'title': 'N-192', 'score': 0.9999966985534778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'title': 'N-41', 'score': 0.9999960117636384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.9999935697168754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9999919191990556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'title': 'N-411', 'score': 0.9999767827535628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9999233212413715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.999914034156304}]
result = search.search('apple cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'apple cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'apple cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #475 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'cherry coconut peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014153982897971791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008620603572057258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007765999189695931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007304940862872533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0070783209701138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006223840218208513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0059235139273948875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005690156090009468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005323476646742458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0051325491255987425}]
result = search.search('cherry coconut peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'cherry coconut peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'cherry coconut peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'cherry coconut peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html', 'title': 'N-134', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html', 'title': 'N-472', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-401.html', 'title': 'N-401', 'score': 0.9984092781357341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html', 'title': 'N-900', 'score': 0.9983761482703559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9983694585834664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9979802308072897}]
result = search.search('cherry coconut peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'cherry coconut peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'cherry coconut peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #479 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #479 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #480 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'apricot apple banana blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013789625259923924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008640674862679993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008123463706216126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007337704837091034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006215184287576602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005887432791921198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005850297431644236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005074397878369834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004953453015719355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004457979867279489}]
result = search.search('apricot apple banana blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'apricot apple banana blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'apricot apple banana blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'apricot apple banana blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html', 'title': 'N-146', 'score': 0.9997771982312755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'title': 'N-83', 'score': 0.9997224975409025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.9996909514366621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 0.9995629659950189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-605.html', 'title': 'N-605', 'score': 0.9994355634788971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html', 'title': 'N-711', 'score': 0.9983631322939905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9983345142284739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'title': 'N-189', 'score': 0.9979194310797402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html', 'title': 'N-252', 'score': 0.9975920652920955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9967158071045362}]
result = search.search('apricot apple banana blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'apricot apple banana blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'apricot apple banana blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'peach orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013692144575381184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008893938092107867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00849192384023668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007485732435160227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007357780214854544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006880183862835963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006082358505998806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005210107438757277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005162014559694473}]
result = search.search('peach orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'peach orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'peach orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0}]
result = search.search('peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'apricot cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014547939061338156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008945976553153405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008921461607189526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007736251550203249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007406811719173675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006837370464451142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006833291606306573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005382290831980222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005150038087870794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004804780913016418}]
result = search.search('apricot cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'apricot cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'apricot cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'apricot cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'title': 'N-155', 'score': 0.9999999839692983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html', 'title': 'N-668', 'score': 0.9999999000719008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-181.html', 'title': 'N-181', 'score': 0.9999961519256123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html', 'title': 'N-476', 'score': 0.9999948074919853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-276.html', 'title': 'N-276', 'score': 0.9999903042854414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-554.html', 'title': 'N-554', 'score': 0.9999891721163817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'title': 'N-334', 'score': 0.9999691221809834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html', 'title': 'N-485', 'score': 0.9999267959604583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9999227693151803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html', 'title': 'N-567', 'score': 0.9999218981619094}]
result = search.search('apricot cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'apricot cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'apricot cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'blueberry tomato lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015684213215903416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014264106586685718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009083508250856994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0075540174259372565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007446176140583461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0070172780460935795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006917976475771376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.0051600517899213485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005138798970625547}]
result = search.search('blueberry tomato lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #489 checking search results for 'blueberry tomato lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'blueberry tomato lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'blueberry tomato lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'title': 'N-517', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html', 'title': 'N-631', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html', 'title': 'N-507', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html', 'title': 'N-143', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'title': 'N-22', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html', 'title': 'N-665', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-237.html', 'title': 'N-237', 'score': 1.0000000000000004}]
result = search.search('blueberry tomato lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #490 checking search results for 'blueberry tomato lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'blueberry tomato lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #491 checking search results for 'peach coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01621469502651059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014580752041584537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008635291874759405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007840179954961212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00731390463239558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0070316979635792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006857114303773152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005777818409574877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005491311727527766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005328124333620112}]
result = search.search('peach coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #491 checking search results for 'peach coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #491 checking search results for 'peach coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #492 checking search results for 'peach coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html', 'title': 'N-154', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html', 'title': 'N-253', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 1.0}]
result = search.search('peach coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #492 checking search results for 'peach coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #492 checking search results for 'peach coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #493 checking search results for 'orange banana kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013531824575120139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008516910907621038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007429335590801707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.006793714009680316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067014060014604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006106863724335155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006021877659105837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005551611252538702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005116700858604222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004907255633606021}]
result = search.search('orange banana kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #493 checking search results for 'orange banana kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #493 checking search results for 'orange banana kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #494 checking search results for 'orange banana kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 0.9998730717849706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 0.9995639981652258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html', 'title': 'N-789', 'score': 0.9995002448578305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9994475285301452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 0.9994245076989585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9994245076989585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html', 'title': 'N-815', 'score': 0.9994102201529889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html', 'title': 'N-653', 'score': 0.9994033694809547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-592.html', 'title': 'N-592', 'score': 0.9994033694809547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9993747346605911}]
result = search.search('orange banana kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #494 checking search results for 'orange banana kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #494 checking search results for 'orange banana kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #495 checking search results for 'cherry papaya blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.016091629094498877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013854247576386876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00859701554319807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008099450282419778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007621802233062167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006778454480185223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0061572606122694395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005908837840979032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005433871097870374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.0051492887025927905}]
result = search.search('cherry papaya blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #495 checking search results for 'cherry papaya blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #495 checking search results for 'cherry papaya blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #496 checking search results for 'cherry papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html', 'title': 'N-116', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-389.html', 'title': 'N-389', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html', 'title': 'N-215', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-425.html', 'title': 'N-425', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-466.html', 'title': 'N-466', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html', 'title': 'N-960', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 1.0}]
result = search.search('cherry papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #496 checking search results for 'cherry papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #496 checking search results for 'cherry papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #497 checking search results for 'papaya fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014558247340647017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007133814807464265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0067796036349541625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0062080696600869635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006080554032725778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005220665216727086}]
result = search.search('papaya fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #497 checking search results for 'papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #497 checking search results for 'papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #498 checking search results for 'papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'title': 'N-420', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'title': 'N-633', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'title': 'N-870', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 1.0000000000000002}]
result = search.search('papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #498 checking search results for 'papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #498 checking search results for 'papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #499 checking search results for 'peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008894119933733423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007712663764776628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007252324937386241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006916355030588826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006670918301976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00589831791952273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005462078929717828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005167188317844448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005076599140264299}]
result = search.search('peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #499 checking search results for 'peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #499 checking search results for 'peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #500 checking search results for 'peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'title': 'N-72', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html', 'title': 'N-152', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 1.0000000000000002}]
result = search.search('peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #500 checking search results for 'peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #500 checking search results for 'peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #501 checking search results for 'apple lime tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.016375488448574598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014526950497898976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008594351013828447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.0085908478249933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007060598887272954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006626475950231341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005853487003752009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005835114287950698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005085893922923415}]
result = search.search('apple lime tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #501 checking search results for 'apple lime tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #501 checking search results for 'apple lime tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #502 checking search results for 'apple lime tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html', 'title': 'N-735', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html', 'title': 'N-123', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html', 'title': 'N-391', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-162.html', 'title': 'N-162', 'score': 1.0000000000000002}]
result = search.search('apple lime tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #502 checking search results for 'apple lime tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #502 checking search results for 'apple lime tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #503 checking search results for 'kiwi lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015684213215903416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014264106586685718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00891182594205441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0077279972694932015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007146614806648442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007044480250098583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006903717940796843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005762463002982315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005160051789921348}]
result = search.search('kiwi lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #503 checking search results for 'kiwi lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #503 checking search results for 'kiwi lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #504 checking search results for 'kiwi lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'title': 'N-115', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html', 'title': 'N-926', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html', 'title': 'N-224', 'score': 1.0000000000000002}]
result = search.search('kiwi lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #504 checking search results for 'kiwi lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #504 checking search results for 'kiwi lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #505 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #505 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #505 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #506 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #506 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #506 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #507 checking search results for 'tomato lime apricot lime pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02163597094862289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014229792641381621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007594787871258156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007424053512353093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007423706610884876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007145868027009016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006905446123213433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006848169761486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0053192319338310305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.0047589830316963865}]
result = search.search('tomato lime apricot lime pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #507 checking search results for 'tomato lime apricot lime pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #507 checking search results for 'tomato lime apricot lime pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #508 checking search results for 'tomato lime apricot lime pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-615.html', 'title': 'N-615', 'score': 0.9999712217254076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html', 'title': 'N-565', 'score': 0.9997334454954093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.999701800847439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 0.9996871869635465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.999686011397502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 0.9996699600227026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html', 'title': 'N-691', 'score': 0.9996520896592709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-840.html', 'title': 'N-840', 'score': 0.9996520896592709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html', 'title': 'N-650', 'score': 0.9996355895289963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'title': 'N-250', 'score': 0.9995968298783682}]
result = search.search('tomato lime apricot lime pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #508 checking search results for 'tomato lime apricot lime pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #508 checking search results for 'tomato lime apricot lime pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #509 checking search results for 'fig peach peach fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.018514929251315062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013568869134398967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008522134357932839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00767724676722878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007612859391993227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006873075076680324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006864041340223327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006772917219554589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005737580973902207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005101900246393417}]
result = search.search('fig peach peach fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #509 checking search results for 'fig peach peach fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #509 checking search results for 'fig peach peach fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #510 checking search results for 'fig peach peach fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'title': 'N-46', 'score': 0.9998115835114019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 0.9997982148010743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 0.9997922204826818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-452.html', 'title': 'N-452', 'score': 0.9997866274138951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html', 'title': 'N-989', 'score': 0.9997635038632642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'title': 'N-382', 'score': 0.9997493393881725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-381.html', 'title': 'N-381', 'score': 0.9997433143754159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 0.9992823177939181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9991147212404489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html', 'title': 'N-822', 'score': 0.9990863461408769}]
result = search.search('fig peach peach fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #510 checking search results for 'fig peach peach fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #510 checking search results for 'fig peach peach fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #511 checking search results for 'banana fig apricot papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015549249220646575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013119495939983829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008584464121230281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007418177829939466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007324546897381216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006557332290647423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006056775387066164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00593084849396912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0056074232547853615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004587531570573964}]
result = search.search('banana fig apricot papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #511 checking search results for 'banana fig apricot papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #511 checking search results for 'banana fig apricot papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #512 checking search results for 'banana fig apricot papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html', 'title': 'N-923', 'score': 0.9998759855498082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.9997890142004243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 0.9997178091572348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 0.9996502490919692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9996312139806032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html', 'title': 'N-165', 'score': 0.9995822529304266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 0.9977224199035196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9976102073161269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html', 'title': 'N-837', 'score': 0.9965656946517105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.996498897962856}]
result = search.search('banana fig apricot papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #512 checking search results for 'banana fig apricot papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #512 checking search results for 'banana fig apricot papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #513 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #513 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #513 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #514 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #514 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #514 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #515 checking search results for 'kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}]
result = search.search('kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #515 checking search results for 'kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #515 checking search results for 'kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #516 checking search results for 'kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #516 checking search results for 'kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #516 checking search results for 'kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #517 checking search results for 'apricot tomato papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015893442883558057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013768144858497996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008907268976094108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008312029358118846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007595993909688911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0072745710635475904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006482365148728844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006401056456289176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005733959955847242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005190060524226074}]
result = search.search('apricot tomato papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #517 checking search results for 'apricot tomato papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #517 checking search results for 'apricot tomato papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #518 checking search results for 'apricot tomato papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-435.html', 'title': 'N-435', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html', 'title': 'N-17', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html', 'title': 'N-845', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html', 'title': 'N-54', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html', 'title': 'N-432', 'score': 1.0}]
result = search.search('apricot tomato papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #518 checking search results for 'apricot tomato papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #518 checking search results for 'apricot tomato papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #519 checking search results for 'banana lime pear kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013099223058175449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.010797462921511783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00824299381155112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007310100372880486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.006917846912249844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006769284395320511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006547637560937095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006382756464071375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005054309386607115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004891313645588512}]
result = search.search('banana lime pear kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #519 checking search results for 'banana lime pear kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #519 checking search results for 'banana lime pear kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #520 checking search results for 'banana lime pear kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 0.9997309416940596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9996503755701305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9996313489515802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html', 'title': 'N-375', 'score': 0.9995552925307899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'title': 'N-338', 'score': 0.9995209311202169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.9992572332989718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'title': 'N-870', 'score': 0.9975582993431454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html', 'title': 'N-886', 'score': 0.9970791969064423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html', 'title': 'N-524', 'score': 0.9962028422415774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9961265559346176}]
result = search.search('banana lime pear kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #520 checking search results for 'banana lime pear kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #520 checking search results for 'banana lime pear kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #521 checking search results for 'tomato orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014558247340647017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008876792757873259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007598885617369492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007431552992537413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0067796036349541625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067394492017669476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006080554032725778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005430448110738531}]
result = search.search('tomato orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #521 checking search results for 'tomato orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #521 checking search results for 'tomato orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #522 checking search results for 'tomato orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'title': 'N-451', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'title': 'N-97', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 1.0000000000000002}]
result = search.search('tomato orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #522 checking search results for 'tomato orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #522 checking search results for 'tomato orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #523 checking search results for 'fig papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.022629847494400338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014561904486885784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008879016312943412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007628957471291234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007074142380287366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006815892291065831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006407481796354644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006104055804307712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005062520990214681}]
result = search.search('fig papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #523 checking search results for 'fig papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #523 checking search results for 'fig papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #524 checking search results for 'fig papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html', 'title': 'N-818', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html', 'title': 'N-582', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-171.html', 'title': 'N-171', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-715.html', 'title': 'N-715', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 1.0}]
result = search.search('fig papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #524 checking search results for 'fig papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #524 checking search results for 'fig papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #525 checking search results for 'papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02027329998570049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013901485750197376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008762199700292342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008246505031990871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006996105582976808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006966028269649784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006932040922398027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00560246023882333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005178264606465154}]
result = search.search('papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #525 checking search results for 'papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #525 checking search results for 'papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #526 checking search results for 'papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'title': 'N-716', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'title': 'N-829', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html', 'title': 'N-438', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html', 'title': 'N-95', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0000000000000002}]
result = search.search('papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #526 checking search results for 'papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #526 checking search results for 'papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #527 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #527 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #527 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #528 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #528 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #528 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #529 checking search results for 'pear apricot blueberry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01458339549519273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008965431442629733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008805986650089002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007276127893811338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006887958729403192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006221922152057925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0060680323305953195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005042267754855447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004955008849884304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004883241757318417}]
result = search.search('pear apricot blueberry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #529 checking search results for 'pear apricot blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #529 checking search results for 'pear apricot blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #530 checking search results for 'pear apricot blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-840.html', 'title': 'N-840', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html', 'title': 'N-753', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html', 'title': 'N-768', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 0.9999999999999998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.998487998756252}]
result = search.search('pear apricot blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #530 checking search results for 'pear apricot blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #530 checking search results for 'pear apricot blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #531 checking search results for 'pear blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014620584532414079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008957207194358581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008866630617779708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007237677690811102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007138969174558063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006949061311214818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006876910079512763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005220890244637338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005173257257766003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005032889075430583}]
result = search.search('pear blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #531 checking search results for 'pear blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #531 checking search results for 'pear blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #532 checking search results for 'pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'title': 'N-278', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 1.0000000000000002}]
result = search.search('pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #532 checking search results for 'pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #532 checking search results for 'pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #533 checking search results for 'lime cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.0199887476659456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013381195260971637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008766006021201296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007670140320088476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007257649476434414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007039650072681608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006009539021524176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005544133813061745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005387987691060049}]
result = search.search('lime cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #533 checking search results for 'lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #533 checking search results for 'lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #534 checking search results for 'lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'title': 'N-151', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'title': 'N-870', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html', 'title': 'N-265', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html', 'title': 'N-152', 'score': 1.0}]
result = search.search('lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #534 checking search results for 'lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #534 checking search results for 'lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #535 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #535 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #535 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #536 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #536 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #536 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #537 checking search results for 'apple cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013924832138538621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008490737282670423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007530761968475131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007251060267352524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00695518005822097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0055702000827855215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005432534236678246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005151494683647729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005031504267136297}]
result = search.search('apple cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #537 checking search results for 'apple cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #537 checking search results for 'apple cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #538 checking search results for 'apple cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'title': 'N-382', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html', 'title': 'N-808', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'title': 'N-829', 'score': 1.0000000000000002}]
result = search.search('apple cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #538 checking search results for 'apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #538 checking search results for 'apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #539 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #539 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #539 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #540 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #540 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #540 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #541 checking search results for 'cherry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013975587608642773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008230025112318119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008059761411042332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007671778542997344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007266259855552638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0059123800457855395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005461921551805112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005029248487485744}]
result = search.search('cherry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #541 checking search results for 'cherry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #541 checking search results for 'cherry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #542 checking search results for 'cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html', 'title': 'N-901', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-162.html', 'title': 'N-162', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-599.html', 'title': 'N-599', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-904.html', 'title': 'N-904', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}]
result = search.search('cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #542 checking search results for 'cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #542 checking search results for 'cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #543 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #543 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #543 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #544 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #544 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #544 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #545 checking search results for 'kiwi fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01579383786018747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01406067486537114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00872003385903541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008580142167558162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007486917829030421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007455619379261758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00682811830596576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006774832398999399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0061057261993098235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005378015338934607}]
result = search.search('kiwi fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #545 checking search results for 'kiwi fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #545 checking search results for 'kiwi fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #546 checking search results for 'kiwi fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'title': 'N-959', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html', 'title': 'N-960', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html', 'title': 'N-657', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html', 'title': 'N-182', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html', 'title': 'N-455', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html', 'title': 'N-497', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 1.0}]
result = search.search('kiwi fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #546 checking search results for 'kiwi fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #546 checking search results for 'kiwi fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #547 checking search results for 'orange pear fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.014055102589632785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01397769235930794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008756051546495417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008364433827914554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007396656651503017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006906070068098295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0065050069134523995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005690385516673809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0055358357708231495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005350801283049635}]
result = search.search('orange pear fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #547 checking search results for 'orange pear fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #547 checking search results for 'orange pear fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #548 checking search results for 'orange pear fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html', 'title': 'N-532', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9999999999999998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.9985265257361319}]
result = search.search('orange pear fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #548 checking search results for 'orange pear fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #548 checking search results for 'orange pear fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #549 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #549 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #549 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #550 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #550 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #550 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #551 checking search results for 'fig tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('fig tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #551 checking search results for 'fig tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #551 checking search results for 'fig tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #552 checking search results for 'fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #552 checking search results for 'fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #552 checking search results for 'fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #553 checking search results for 'papaya cherry cherry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012593038480861454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.012384531138527317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007491696770874604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007412480625050065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0070829558684407995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006163020806530525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005538292784498668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005260826435750768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0051056882734613245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.004806878872731171}]
result = search.search('papaya cherry cherry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #553 checking search results for 'papaya cherry cherry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #553 checking search results for 'papaya cherry cherry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #554 checking search results for 'papaya cherry cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'title': 'N-65', 'score': 0.9999713261824256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.9998792299049052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9998646433806591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html', 'title': 'N-471', 'score': 0.9996357542564035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9996161087924398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html', 'title': 'N-472', 'score': 0.9995939632105728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html', 'title': 'N-768', 'score': 0.9995939632105728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9995618232073235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'title': 'N-590', 'score': 0.9995363833718582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 0.9994913018161916}]
result = search.search('papaya cherry cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #554 checking search results for 'papaya cherry cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #554 checking search results for 'papaya cherry cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #555 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013808982497664915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008515803679606682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008490333677243589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007327547266418108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006546519234532374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006545958995525339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006396068183196792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00518655027343803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004903486993100805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.00473492931973044}]
result = search.search('banana kiwi blueberry apricot blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #555 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #555 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #556 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'title': 'N-83', 'score': 0.9997201118763765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 0.9996958897185949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.9996882663914126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 0.9996736508238443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html', 'title': 'N-111', 'score': 0.999625475568064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 0.9995590252024842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html', 'title': 'N-252', 'score': 0.9972150101419476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 0.9968397971935526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.9954623448627841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-292.html', 'title': 'N-292', 'score': 0.9950628386958943}]
result = search.search('banana kiwi blueberry apricot blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #556 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #556 checking search results for 'banana kiwi blueberry apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #557 checking search results for 'fig tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014558247340647017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008876792757873259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007598885617369492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007431552992537413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0067796036349541625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067394492017669476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006080554032725778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005430448110738531}]
result = search.search('fig tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #557 checking search results for 'fig tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #557 checking search results for 'fig tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #558 checking search results for 'fig tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'title': 'N-451', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'title': 'N-97', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 1.0000000000000002}]
result = search.search('fig tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #558 checking search results for 'fig tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #558 checking search results for 'fig tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #559 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014046513934844332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008004493061428109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007395545382678593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00672342062440062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006519758817520054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.005954621646220927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00540330879309873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005102020536221335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005002870452728596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0049223326673548265}]
result = search.search('coconut blueberry apricot coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #559 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #559 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #560 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-647.html', 'title': 'N-647', 'score': 0.9997729264256927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9996665060204473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html', 'title': 'N-157', 'score': 0.9996491539645029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9987705243951676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html', 'title': 'N-681', 'score': 0.9981590423124828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.9981175342673444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-487.html', 'title': 'N-487', 'score': 0.9975840266335665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 0.9975716717062606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'title': 'N-192', 'score': 0.9974909573296601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html', 'title': 'N-722', 'score': 0.9972978440939364}]
result = search.search('coconut blueberry apricot coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #560 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #560 checking search results for 'coconut blueberry apricot coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #561 checking search results for 'banana kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014508975432977165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009129170033410556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00776872349844939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007038887584123178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007011289820488283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006903518865250007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006083288764162688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00533207186489617}]
result = search.search('banana kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #561 checking search results for 'banana kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #561 checking search results for 'banana kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #562 checking search results for 'banana kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'title': 'N-207', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html', 'title': 'N-437', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 1.0}]
result = search.search('banana kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #562 checking search results for 'banana kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #562 checking search results for 'banana kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #563 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #563 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #563 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #564 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #564 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #564 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #565 checking search results for 'papaya kiwi apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.016140924399588884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014108294411062938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008626279275632117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008581603683235869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007127992733307003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007105777262297311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006768881000554975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005806020108304689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005420518492593492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}]
result = search.search('papaya kiwi apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #565 checking search results for 'papaya kiwi apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #565 checking search results for 'papaya kiwi apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #566 checking search results for 'papaya kiwi apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html', 'title': 'N-509', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html', 'title': 'N-51', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 1.0}]
result = search.search('papaya kiwi apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #566 checking search results for 'papaya kiwi apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #566 checking search results for 'papaya kiwi apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #567 checking search results for 'lime kiwi orange banana apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013972536047294752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01205558615094437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008856467145399387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008220435749402927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007510925649569858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007213887059832639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006999585876949517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006565338577444922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005673638666628862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0050761840592678355}]
result = search.search('lime kiwi orange banana apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #567 checking search results for 'lime kiwi orange banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #567 checking search results for 'lime kiwi orange banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #568 checking search results for 'lime kiwi orange banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-794.html', 'title': 'N-794', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9973809572995223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9965335403843404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html', 'title': 'N-606', 'score': 0.9965280781461393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9963541838163212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html', 'title': 'N-569', 'score': 0.9957432158347255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9956132100992819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9951103887185906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-863.html', 'title': 'N-863', 'score': 0.9949444487350073}]
result = search.search('lime kiwi orange banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #568 checking search results for 'lime kiwi orange banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #568 checking search results for 'lime kiwi orange banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #569 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321568}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #569 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #569 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #570 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #570 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #570 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #571 checking search results for 'blueberry cherry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014143809384626074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008323700171315548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007960290651034386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007225568846474127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007196608038070033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005838826820111662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005754197201898433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005135467990060071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005126557105478085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005075630153413899}]
result = search.search('blueberry cherry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #571 checking search results for 'blueberry cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #571 checking search results for 'blueberry cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #572 checking search results for 'blueberry cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'title': 'N-799', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}]
result = search.search('blueberry cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #572 checking search results for 'blueberry cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #572 checking search results for 'blueberry cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #573 checking search results for 'fig orange apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019833336521743107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013665403144578115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008684303969996829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008076822919199114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007464412624872198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007130594109458539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0066436837615403204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006024491275753241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005639157903167646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005147359598660477}]
result = search.search('fig orange apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #573 checking search results for 'fig orange apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #573 checking search results for 'fig orange apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #574 checking search results for 'fig orange apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html', 'title': 'N-533', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9983524765913273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9983498505392225}]
result = search.search('fig orange apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #574 checking search results for 'fig orange apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #574 checking search results for 'fig orange apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #575 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #575 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #575 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #576 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #576 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #576 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #577 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #577 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #577 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #578 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #578 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #578 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #579 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #579 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #579 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #580 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #580 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #580 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #581 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008904284110532115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698917378646351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007404620178416595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00659603485468099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006337194041189021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005746968466638174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005208716022108618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005161326974356845}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #581 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #581 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #582 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html', 'title': 'N-419', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'title': 'N-988', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'title': 'N-635', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'title': 'N-368', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-564.html', 'title': 'N-564', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'title': 'N-516', 'score': 1.0000000000000002}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #582 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #582 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #583 checking search results for 'banana pear blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014474079327624012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008948388941600618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008094638587247977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007333296469800969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006918392112900344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006888705123211101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006659170940013657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005187678277023559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005162014830565029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005078563839536835}]
result = search.search('banana pear blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #583 checking search results for 'banana pear blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #583 checking search results for 'banana pear blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #584 checking search results for 'banana pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html', 'title': 'N-367', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-892.html', 'title': 'N-892', 'score': 1.0000000000000002}]
result = search.search('banana pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #584 checking search results for 'banana pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #584 checking search results for 'banana pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #585 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #585 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #585 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #586 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #586 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #586 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #587 checking search results for 'apricot apple papaya banana fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.017688929536802116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013940655278080534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008510969530883598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008479317148104917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00721767744004625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007143912627386255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006471984447199143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0057415128559306534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005721436936278571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005001901584912295}]
result = search.search('apricot apple papaya banana fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #587 checking search results for 'apricot apple papaya banana fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #587 checking search results for 'apricot apple papaya banana fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #588 checking search results for 'apricot apple papaya banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9979515609801834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9964978564131813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9964689755797769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9962561441318106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9953381182865246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9948578384520833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html', 'title': 'N-604', 'score': 0.9930319802148838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9927811617805494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9925270079278559}]
result = search.search('apricot apple papaya banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #588 checking search results for 'apricot apple papaya banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #588 checking search results for 'apricot apple papaya banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #589 checking search results for 'cherry peach lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.014064345738439683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013849011593757028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008238010293476926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008195678650204112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007695597151235414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00711899465615997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070174209808563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006315417926949522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005852850985407925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005181774392962385}]
result = search.search('cherry peach lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #589 checking search results for 'cherry peach lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #589 checking search results for 'cherry peach lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #590 checking search results for 'cherry peach lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html', 'title': 'N-945', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html', 'title': 'N-770', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0}]
result = search.search('cherry peach lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #590 checking search results for 'cherry peach lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #590 checking search results for 'cherry peach lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #591 checking search results for 'pear papaya tomato blueberry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014148200346212832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01381834371036601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008564758457810713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008218051230230177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006920160767919885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006890669059681001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006527604177705155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005226875278957438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005198871496424887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005028626089243844}]
result = search.search('pear papaya tomato blueberry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #591 checking search results for 'pear papaya tomato blueberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #591 checking search results for 'pear papaya tomato blueberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #592 checking search results for 'pear papaya tomato blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-389.html', 'title': 'N-389', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-184.html', 'title': 'N-184', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html', 'title': 'N-206', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html', 'title': 'N-768', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html', 'title': 'N-365', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9982822305485979}]
result = search.search('pear papaya tomato blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #592 checking search results for 'pear papaya tomato blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #592 checking search results for 'pear papaya tomato blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #593 checking search results for 'banana coconut peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01406084556499957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008319885207409188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007765248741157441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007184814446488171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007134871911269466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006326687811383721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00605930299483427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005947069629997008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005328730585225366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005083162094350106}]
result = search.search('banana coconut peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #593 checking search results for 'banana coconut peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #593 checking search results for 'banana coconut peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #594 checking search results for 'banana coconut peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html', 'title': 'N-351', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-483.html', 'title': 'N-483', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-172.html', 'title': 'N-172', 'score': 1.0}]
result = search.search('banana coconut peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #594 checking search results for 'banana coconut peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #594 checking search results for 'banana coconut peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #595 checking search results for 'apricot banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014248984533193048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009129170033410558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008064081151278048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007699031217816939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00729329495022515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00703888758412318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0068754967347565326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005876929438680797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005127088861940444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005016850531842438}]
result = search.search('apricot banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #595 checking search results for 'apricot banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #595 checking search results for 'apricot banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #596 checking search results for 'apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html', 'title': 'N-54', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html', 'title': 'N-818', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html', 'title': 'N-926', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html', 'title': 'N-99', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'title': 'N-204', 'score': 1.0000000000000002}]
result = search.search('apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #596 checking search results for 'apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #596 checking search results for 'apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #597 checking search results for 'peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019792678824805714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014578217103481284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008501619396847302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008488297108337222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007052769349148549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006815925861997122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005883300353498685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005387160801070893}]
result = search.search('peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #597 checking search results for 'peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #597 checking search results for 'peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #598 checking search results for 'peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-468.html', 'title': 'N-468', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html', 'title': 'N-490', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html', 'title': 'N-747', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html', 'title': 'N-858', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 1.0}]
result = search.search('peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #598 checking search results for 'peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #598 checking search results for 'peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #599 checking search results for 'blueberry peach pear orange banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014169193136887602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008773442805521529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008332229825905086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007309468006457846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007133790390593452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006650516092745103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006559523718927942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0051924612559901325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00511480539853904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005003059219080613}]
result = search.search('blueberry peach pear orange banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #599 checking search results for 'blueberry peach pear orange banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #599 checking search results for 'blueberry peach pear orange banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #600 checking search results for 'blueberry peach pear orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html', 'title': 'N-367', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 0.9986738476750034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9981590156705983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html', 'title': 'N-388', 'score': 0.9975799492214202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9974567988869039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9971467708126929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9967001741355332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9962889537554795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9948861492795728}]
result = search.search('blueberry peach pear orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #600 checking search results for 'blueberry peach pear orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #600 checking search results for 'blueberry peach pear orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #601 checking search results for 'apricot orange banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013768144858497996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008907268976094108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008357992971308575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007353173823242124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007043533054956235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006991336312727861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006401056456289176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005733959955847241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005057752760696048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0048883251074399135}]
result = search.search('apricot orange banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #601 checking search results for 'apricot orange banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #601 checking search results for 'apricot orange banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #602 checking search results for 'apricot orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'title': 'N-204', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html', 'title': 'N-173', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'title': 'N-57', 'score': 1.0}]
result = search.search('apricot orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #602 checking search results for 'apricot orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #602 checking search results for 'apricot orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #603 checking search results for 'kiwi papaya pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015743929489952093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.0140416784442117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008764885877026873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008648394601728303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007601225180839045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007154063772611696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006514407480222951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006019712859357613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00593494557494177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005144043402926189}]
result = search.search('kiwi papaya pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #603 checking search results for 'kiwi papaya pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #603 checking search results for 'kiwi papaya pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #604 checking search results for 'kiwi papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html', 'title': 'N-706', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-137.html', 'title': 'N-137', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html', 'title': 'N-875', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0}]
result = search.search('kiwi papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #604 checking search results for 'kiwi papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #604 checking search results for 'kiwi papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #605 checking search results for 'blueberry tomato orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01579383786018747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01406067486537114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009039555504678365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008443227343722912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007597486523209644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00741201195861455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006703708987475465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006669898190556312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005281595684742098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005133125008455152}]
result = search.search('blueberry tomato orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #605 checking search results for 'blueberry tomato orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #605 checking search results for 'blueberry tomato orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #606 checking search results for 'blueberry tomato orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html', 'title': 'N-93', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'title': 'N-959', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'title': 'N-430', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html', 'title': 'N-395', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-958.html', 'title': 'N-958', 'score': 1.0000000000000002}]
result = search.search('blueberry tomato orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #606 checking search results for 'blueberry tomato orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #606 checking search results for 'blueberry tomato orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #607 checking search results for 'kiwi pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014622152241975004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009104767398421377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00887568908735779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007422900542789047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007019198916682898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006395965585038795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005666559741002843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005546157347946988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005167126572730029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005075430508127907}]
result = search.search('kiwi pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #607 checking search results for 'kiwi pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #607 checking search results for 'kiwi pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #608 checking search results for 'kiwi pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html', 'title': 'N-260', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'title': 'N-334', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 1.0000000000000002}]
result = search.search('kiwi pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #608 checking search results for 'kiwi pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #608 checking search results for 'kiwi pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
