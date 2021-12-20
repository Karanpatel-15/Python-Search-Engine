
import testingtools
import crawler
import searchdata
import search

output = open('fruits4-all-failed.txt', 'w')
success_output = open('fruits4-all-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')



#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-428.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-499.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-499.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-499.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-499.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-325.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-675.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-363.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-816.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-809.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-630.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-437.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-655.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-696.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-696.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-696.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-696.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-654.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-915.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-504.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-915.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-915.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-915.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-891.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-514.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-866.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-727.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-291.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-881.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html\n\n')
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









#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-630.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-966.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-582.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-491.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-582.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-582.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-582.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-205.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-618.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-629.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-371.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-704.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-808.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-81.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-808.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-808.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-808.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-881.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-883.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-469.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-265.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-474.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-692.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-692.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-692.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-692.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-626.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-612.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-19.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-229.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-653.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-653.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-653.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-653.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-275.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-182.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-221.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-940.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-782.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-782.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-782.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-782.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-233.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html\n\n')
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









#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html
expected = 0.0004027470567067805
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html
expected = 0.0004352379703917491
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html
expected = 0.001740199750135717
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html
expected = 0.0026583053562453758
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html
expected = 0.0019726418622828864
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html
expected = 0.0021012846759179624
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-595.html
expected = 0.0003552093406647403
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-595.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html
expected = 0.00038670251912442416
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html
expected = 0.0006572869123447069
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
expected = 0.0012731184975007107
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html
expected = 0.0008979873265528278
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html
expected = 0.0009070308407884013
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html
expected = 0.0006878928584126768
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html
expected = 0.000947877427171233
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html
expected = 0.0006637459115153692
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-355.html
expected = 0.0006329318762076587
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-355.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-355.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-355.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html
expected = 0.0010165303767860805
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html
expected = 0.0004013974907998719
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html
expected = 0.0009535580762248015
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html
expected = 0.00040251060543402813
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html
expected = 0.0003707731661078087
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html
expected = 0.0006488509392697962
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html
expected = 0.0006299779462615781
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html
expected = 0.000648407745114711
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html
expected = 0.0006829270773183403
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html
expected = 0.0008806576836876279
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html
expected = 0.00035354688111047223
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html
expected = 0.000441131679077663
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html
expected = 0.0010043355755214563
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-963.html
expected = 0.0003627824664744897
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-963.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-963.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-963.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-425.html
expected = 0.0004239694149702218
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-425.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-425.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-425.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html
expected = 0.0004045481977572299
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html
expected = 0.00035568557373642676
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html
expected = 0.0003644917082039723
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html
expected = 0.0009044603726386546
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html
expected = 0.0008735456423477145
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html
expected = 0.0003556433712095456
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html
expected = 0.0003867935175830476
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
expected = 0.0003623083658577291
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html
expected = 0.0003556433712095456
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html
expected = 0.00035634209394409263
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html
expected = 0.0006666142577418365
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html
expected = 0.0018429528954152189
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html
expected = 0.0012359020103505332
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
expected = 0.0006687476543114109
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html
expected = 0.0010039331588543238
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html
expected = 0.0006474475474262095
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html
expected = 0.001249428760204216
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html
expected = 0.000703298024627594
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html
expected = 0.0026612963165194192
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
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









#Test #153 checking IDF for word peach
expected = 0.1795146570136211
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apricot
expected = 0.14560532224689926
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word cherry
expected = 0.18114943910456646
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word papaya
expected = 0.16974467583231712
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word orange
expected = 0.17136841831198113
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word banana
expected = 0.16650266314016507
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word lime
expected = 0.18278607574167338
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word kiwi
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word apple
expected = 0.18114943910456646
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word fig
expected = 0.17462139610706884
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word fig\n\n')
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









#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word kiwi
expected = 0.0851063829787234
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apricot
expected = 0.1276595744680851
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word blueberry
expected = 0.0425531914893617
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apple
expected = 0.0851063829787234
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word peach
expected = 0.06382978723404255
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word lime
expected = 0.06382978723404255
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word papaya
expected = 0.06382978723404255
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word fig
expected = 0.0851063829787234
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word coconut
expected = 0.1276595744680851
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word kiwi
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apricot
expected = 0.09615384615384616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word blueberry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apple
expected = 0.09615384615384616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word lime
expected = 0.09615384615384616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word papaya
expected = 0.019230769230769232
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word fig
expected = 0.057692307692307696
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word coconut
expected = 0.09615384615384616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word banana
expected = 0.057692307692307696
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word kiwi
expected = 0.14814814814814814
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apricot
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apple
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word peach
expected = 0.037037037037037035
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word lime
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word papaya
expected = 0.14814814814814814
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word fig
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word coconut
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word banana
expected = 0.14814814814814814
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word kiwi
expected = 0.044444444444444446
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apricot
expected = 0.08888888888888889
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word blueberry
expected = 0.08888888888888889
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apple
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word peach
expected = 0.044444444444444446
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word lime
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word papaya
expected = 0.15555555555555556
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word fig
expected = 0.044444444444444446
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word coconut
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word banana
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word kiwi
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apricot
expected = 0.0641025641025641
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word blueberry
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apple
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word peach
expected = 0.02564102564102564
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word lime
expected = 0.14102564102564102
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word papaya
expected = 0.11538461538461539
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word fig
expected = 0.038461538461538464
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word coconut
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word kiwi
expected = 0.08974358974358974
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apricot
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word blueberry
expected = 0.11538461538461539
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apple
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word peach
expected = 0.038461538461538464
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word lime
expected = 0.0641025641025641
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word papaya
expected = 0.08974358974358974
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word fig
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word coconut
expected = 0.0641025641025641
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word kiwi
expected = 0.13793103448275862
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apricot
expected = 0.06896551724137931
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word blueberry
expected = 0.10344827586206896
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apple
expected = 0.10344827586206896
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word lime
expected = 0.13793103448275862
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word papaya
expected = 0.13793103448275862
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word fig
expected = 0.034482758620689655
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word coconut
expected = 0.06896551724137931
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word banana
expected = 0.06896551724137931
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word kiwi
expected = 0.0759493670886076
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apricot
expected = 0.08860759493670886
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word blueberry
expected = 0.0379746835443038
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apple
expected = 0.08860759493670886
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word peach
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word lime
expected = 0.06329113924050633
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word papaya
expected = 0.17721518987341772
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word fig
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word coconut
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word banana
expected = 0.06329113924050633
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word kiwi
expected = 0.021505376344086023
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apricot
expected = 0.043010752688172046
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word blueberry
expected = 0.08602150537634409
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apple
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word peach
expected = 0.08602150537634409
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word lime
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word papaya
expected = 0.10752688172043011
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word fig
expected = 0.11827956989247312
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word coconut
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word banana
expected = 0.03225806451612903
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word kiwi
expected = 0.08080808080808081
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apricot
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word blueberry
expected = 0.0707070707070707
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apple
expected = 0.10101010101010101
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word peach
expected = 0.04040404040404041
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word lime
expected = 0.08080808080808081
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word papaya
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word fig
expected = 0.08080808080808081
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word coconut
expected = 0.08080808080808081
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word banana
expected = 0.08080808080808081
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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









#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apple
expected = 0.01803083143464337
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word fig
expected = 0.005927930494563267
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word papaya
expected = 0.01139227741975401
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word peach
expected = 0.012047981850290268
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word lime
expected = 0.04065023797077812
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apricot
expected = 0.009772184115323799
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word kiwi
expected = 0.022704515524875027
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word banana
expected = 0.04188187458782153
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word blueberry
expected = 0.01705727094203789
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word fig
expected = 0.07247442756085826
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word peach
expected = 0.07450531433083264
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apple
expected = 0.01472746789489379
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word fig
expected = 0.007198358916554508
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word papaya
expected = 0.010422415549942709
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word peach
expected = 0.014594559943985659
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word lime
expected = 0.03233079201731818
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apricot
expected = 0.017515480664911234
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word coconut
expected = 0.01828321522775487
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word kiwi
expected = 0.017460094684880564
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word banana
expected = 0.010223354204836508
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word blueberry
expected = 0.03346076182249858
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apple
expected = 0.07518381020172445
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word kiwi
expected = 0.1274906188935943
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apple
expected = 0.02324583819071895
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig
expected = 0.01699017313790581
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya
expected = 0.01383926398426604
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach
expected = 0.02848857144544599
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime
expected = 0.02063546154499968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot
expected = 0.011871185250485018
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word coconut
expected = 0.026011402595412052
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi
expected = 0.011346388939316525
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana
expected = 0.013574943060696364
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry
expected = 0.01934647588310838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apple
expected = 0.02120162550173131
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word fig
expected = 0.030066482304400493
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word papaya
expected = 0.019866818609535777
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word peach
expected = 0.01762481974340443
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word lime
expected = 0.02815520251728193
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apricot
expected = 0.01704156263799243
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word coconut
expected = 0.01081575299645028
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word kiwi
expected = 0.020247116501240493
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word banana
expected = 0.01634729705897792
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word blueberry
expected = 0.013550370054205254
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word fig
expected = 0.05621553337532014
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apricot
expected = 0.024741984592812714
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word kiwi
expected = 0.07947890900608984
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apple
expected = 0.014389509232181368
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word fig
expected = 0.022711353171790856
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word papaya
expected = 0.026263336698030448
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word lime
expected = 0.01918697387189764
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apricot
expected = 0.011566081237033673
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word coconut
expected = 0.014389509232181368
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word kiwi
expected = 0.018159102981910077
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word banana
expected = 0.017477711222307107
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word blueberry
expected = 0.034756408446622505
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apple
expected = 0.01803083143464337
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word fig
expected = 0.013146917900152629
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word papaya
expected = 0.02094350812335236
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word peach
expected = 0.00908812214310185
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word lime
expected = 0.0046674592799658375
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apricot
expected = 0.021380887666865602
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word coconut
expected = 0.01803083143464337
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word kiwi
expected = 0.025402677717233188
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word banana
expected = 0.01253567369899127
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word blueberry
expected = 0.012902007293798208
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apple
expected = 0.017143416668721788
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word fig
expected = 0.04306861547516751
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word papaya
expected = 0.016064105522351383
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word peach
expected = 0.01698870600173781
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word lime
expected = 0.021451216468158306
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apricot
expected = 0.0035305717849440275
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word coconut
expected = 0.017143416668721788
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word kiwi
expected = 0.008320022829471826
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word banana
expected = 0.008007827067304593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word blueberry
expected = 0.038708939515020295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html and word tomato\n\n')
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


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
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


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
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









#Test #409 checking search results for 'pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018499444562731084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01680083548414488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015434265632480957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01353422443500625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008505129405986682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008180341455822932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007598337846207587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065590720673769426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006120732331037637}]
result = search.search('pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-931.html', 'title': 'N-931', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html', 'title': 'N-741', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'title': 'N-366', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-328.html', 'title': 'N-328', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}]
result = search.search('pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'lime apple cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017265438457789054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016831548451509873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016808565943160013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013974224739692589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009212812065704795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007819028012353534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007676155235631234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007663641770815302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006050998565051241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005822206485465446}]
result = search.search('lime apple cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'lime apple cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'lime apple cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'lime apple cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-891.html', 'title': 'N-891', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html', 'title': 'N-625', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html', 'title': 'N-212', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.998694088002918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-108.html', 'title': 'N-108', 'score': 0.9986794065878584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9982502313482158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9979768299168261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 0.9976997501005003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9972545018839816}]
result = search.search('lime apple cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'lime apple cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'lime apple cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'apple orange blueberry tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018463831423963385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017524664360182393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015686911562443503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014112530146855918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008424236896849485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0076835324549363124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006396624642690145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006183860864543579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005286804808939641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.00521947905810396}]
result = search.search('apple orange blueberry tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'apple orange blueberry tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'apple orange blueberry tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'apple orange blueberry tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html', 'title': 'N-833', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html', 'title': 'N-824', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'title': 'N-102', 'score': 0.9987921266407664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.9984150407975549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9983254630763033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9983144893092224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9980146206184596}]
result = search.search('apple orange blueberry tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'apple orange blueberry tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'apple orange blueberry tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'lime cherry tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018378603257576894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018026200747054154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01672332371802704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015154101643268168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010258105559173527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007818464504709454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007778231239579677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007314668319300705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006498266448323919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005921254440647707}]
result = search.search('lime cherry tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'lime cherry tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'lime cherry tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'lime cherry tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-462.html', 'title': 'N-462', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 1.0000000000000002}]
result = search.search('lime cherry tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'lime cherry tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'lime cherry tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'tomato cherry coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018196452475104017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01706281105033496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016599036392528282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014992719353940795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008130169987071138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007890966666308688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007777946085812415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006963175334091235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006170495411668846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005273121926464191}]
result = search.search('tomato cherry coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'tomato cherry coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'tomato cherry coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'tomato cherry coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'title': 'N-238', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html', 'title': 'N-478', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html', 'title': 'N-335', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html', 'title': 'N-441', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html', 'title': 'N-978', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html', 'title': 'N-389', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html', 'title': 'N-511', 'score': 1.0}]
result = search.search('tomato cherry coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'tomato cherry coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'tomato cherry coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'papaya blueberry coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01782407571809242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01770751670068344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016555597615179683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015207746383614612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009068557263074279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007848680198362953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007340285379096978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006607255717242407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006097665248035505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005871324461507032}]
result = search.search('papaya blueberry coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'papaya blueberry coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'papaya blueberry coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'papaya blueberry coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html', 'title': 'N-507', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html', 'title': 'N-105', 'score': 0.9985680148885747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.9984199741537244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9973858208157379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.997351458386734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html', 'title': 'N-327', 'score': 0.9972944520135623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9972298036385038}]
result = search.search('papaya blueberry coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'papaya blueberry coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'papaya blueberry coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'orange orange orange blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016479389127572158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.014978290258764466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01182978850055467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.010928050460291275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007303660958839414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006562091953497638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006148378459343851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006070085264215339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0050538735510362405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.00496047800344451}]
result = search.search('orange orange orange blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'orange orange orange blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'orange orange orange blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'orange orange orange blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html', 'title': 'N-925', 'score': 0.9999999667589803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9999985900598316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html', 'title': 'N-864', 'score': 0.9993949928037307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'title': 'N-178', 'score': 0.9988978976586775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html', 'title': 'N-709', 'score': 0.9988114181883485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html', 'title': 'N-771', 'score': 0.9988114181883485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-612.html', 'title': 'N-612', 'score': 0.9987898831305114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html', 'title': 'N-869', 'score': 0.9983605458858965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 0.9976115894839503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html', 'title': 'N-247', 'score': 0.9966738318103843}]
result = search.search('orange orange orange blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'orange orange orange blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'orange orange orange blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'apricot blueberry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01836789690724459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017117315433169942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01673636235621074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015400010477187073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008392065586628326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008381950773717325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007595448933222333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006209309701017743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00619280441823368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005637695433761908}]
result = search.search('apricot blueberry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'apricot blueberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'apricot blueberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'apricot blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'title': 'N-75', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html', 'title': 'N-643', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'title': 'N-315', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html', 'title': 'N-116', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html', 'title': 'N-204', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html', 'title': 'N-454', 'score': 1.0000000000000002}]
result = search.search('apricot blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'apricot blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'apricot blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018555053066004683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01729539344415871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016830619865428692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01546177643832643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008311765693826526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007808567464579176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007701017398524902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006172754390821582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005284819842062077}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html', 'title': 'N-259', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html', 'title': 'N-733', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-225.html', 'title': 'N-225', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'title': 'N-218', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html', 'title': 'N-441', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0}]
result = search.search('coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'cherry peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018152640933875874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016575840034459985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015908222002470634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01498672741895143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008865396940060673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00788739257714948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007785022561131532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007778089682376726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005735155726071404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005378955282641956}]
result = search.search('cherry peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'cherry peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'cherry peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'cherry peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html', 'title': 'N-321', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html', 'title': 'N-76', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html', 'title': 'N-506', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 1.0}]
result = search.search('cherry peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'cherry peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'cherry peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'pear tomato kiwi lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018012970497545532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01655740197236332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015284590391903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012299622122020206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010483179175665271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008603407665436765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00805544282279811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007358134934900487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006481353694364361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005585574870343905}]
result = search.search('pear tomato kiwi lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'pear tomato kiwi lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'pear tomato kiwi lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'pear tomato kiwi lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.998567919034092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-809.html', 'title': 'N-809', 'score': 0.998208914487852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9968689902484249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9962141274932146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'title': 'N-682', 'score': 0.9961872946715848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9953895852903515}]
result = search.search('pear tomato kiwi lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'pear tomato kiwi lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'pear tomato kiwi lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'pear cherry apricot orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01820312488891179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016129654073720436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015167515109523046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01465346032250566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009307025785161113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008048875542864858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007524647623114537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007155838654319946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006480700691936843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006205806027598531}]
result = search.search('pear cherry apricot orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'pear cherry apricot orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'pear cherry apricot orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'pear cherry apricot orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-725.html', 'title': 'N-725', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9999999999999998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html', 'title': 'N-924', 'score': 0.9999999999999998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'title': 'N-449', 'score': 0.9987681626047441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html', 'title': 'N-806', 'score': 0.9987035554019461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 0.99842247086338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979307351562136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html', 'title': 'N-892', 'score': 0.997823077709447}]
result = search.search('pear cherry apricot orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'pear cherry apricot orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'pear cherry apricot orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'pear kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017706397034864495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01665214363486242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015433580282010877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013173295939452866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010477198277785614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0087391241293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007855290007264617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00702585250240981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006438100705934343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006172767701326973}]
result = search.search('pear kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'pear kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'pear kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html', 'title': 'N-357', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html', 'title': 'N-116', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html', 'title': 'N-684', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html', 'title': 'N-839', 'score': 1.0000000000000002}]
result = search.search('pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'cherry pear tomato banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01755165220503059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016600987777818807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015692312847635056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014636030731197916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008061283782283109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007797242907478708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00773058258054705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007267504439274297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006209517434835331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005437508499772557}]
result = search.search('cherry pear tomato banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'cherry pear tomato banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'cherry pear tomato banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'cherry pear tomato banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-437.html', 'title': 'N-437', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html', 'title': 'N-51', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-734.html', 'title': 'N-734', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html', 'title': 'N-962', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-811.html', 'title': 'N-811', 'score': 0.997962139186573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979583781719515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979291637944201}]
result = search.search('cherry pear tomato banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'cherry pear tomato banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'cherry pear tomato banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'orange fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01727116833989226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016782871111705337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014032592557746056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.012926969240012406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008220571449529958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006556617987824895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006179564554730351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00579439612019923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0056237013593022425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005471662864879731}]
result = search.search('orange fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'orange fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'orange fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'orange fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html', 'title': 'N-508', 'score': 0.9999999197799115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-198.html', 'title': 'N-198', 'score': 0.999997593760435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9999970126848345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9999961242182495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.9999953548282159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html', 'title': 'N-641', 'score': 0.9999951634651112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.9999889921853711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 0.9999855066046512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html', 'title': 'N-107', 'score': 0.9999749280355497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.9999104618147969}]
result = search.search('orange fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'orange fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'orange fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'tomato banana kiwi coconut blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.0176235789455563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017605387007642404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016288717070420785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015451282790405701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007954613748142571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007796269412661767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007397389699998705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006595823570039995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005862646539552498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005408713193256927}]
result = search.search('tomato banana kiwi coconut blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'tomato banana kiwi coconut blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'tomato banana kiwi coconut blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'tomato banana kiwi coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-312.html', 'title': 'N-312', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html', 'title': 'N-150', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html', 'title': 'N-507', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 0.9986317694901908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9985687812678091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html', 'title': 'N-564', 'score': 0.9984041952309995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html', 'title': 'N-867', 'score': 0.9982724938815407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html', 'title': 'N-360', 'score': 0.997940367976749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9974691657940119}]
result = search.search('tomato banana kiwi coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'tomato banana kiwi coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'tomato banana kiwi coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017987856620882155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017824962627894424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016024680327195485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007992048400248364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007847002935925197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0077363230304852235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006624341646345239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006116208657602171}]
result = search.search('orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-402.html', 'title': 'N-402', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html', 'title': 'N-524', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html', 'title': 'N-531', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0}]
result = search.search('orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'fig kiwi fig apricot apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016837588069568355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01537697353105187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014926776267000416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.014888821506044085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010488563615343581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008188628412367862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007926263570777513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0072668189173993375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005776500242280315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005555275341448955}]
result = search.search('fig kiwi fig apricot apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'fig kiwi fig apricot apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'fig kiwi fig apricot apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'fig kiwi fig apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 0.999858172312647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 0.9998562569259946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html', 'title': 'N-969', 'score': 0.9998149023267149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 0.9997874384977611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9997763643784394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 0.9997763643784394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html', 'title': 'N-27', 'score': 0.9997713512568467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 0.9997622213998438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.9997622213998438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html', 'title': 'N-201', 'score': 0.9997580539401241}]
result = search.search('fig kiwi fig apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'fig kiwi fig apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'fig kiwi fig apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'pear fig banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017589599774676168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016551452116353702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015216786146621917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014479251728585473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008684694304541574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008457458302732609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008103015464449356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007290304892973255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065282310658576655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.0053618857301347385}]
result = search.search('pear fig banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'pear fig banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'pear fig banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'pear fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html', 'title': 'N-715', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-906.html', 'title': 'N-906', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html', 'title': 'N-419', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 1.0}]
result = search.search('pear fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'pear fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'pear fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'peach papaya coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01856160957193966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017071690799675777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016359468699245355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015025755816280982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008472725083051852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008109623726721835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00778583429195606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007521425372468552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005921263914253284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005334936350934291}]
result = search.search('peach papaya coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'peach papaya coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'peach papaya coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'peach papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html', 'title': 'N-200', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html', 'title': 'N-879', 'score': 1.0}]
result = search.search('peach papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'peach papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'peach papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #463 checking search results for 'pear apricot cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01776015651285882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016666745830773693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.0161026344169821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014878635274840124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010364721443463093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007996743971088136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007509688947034706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007466694918495041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006333295210297879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0062076855002623586}]
result = search.search('pear apricot cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #463 checking search results for 'pear apricot cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #463 checking search results for 'pear apricot cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #464 checking search results for 'pear apricot cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html', 'title': 'N-576', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9988788665315973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 0.9984331249137531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9984272211984175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9980171189661522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9979328458110456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html', 'title': 'N-642', 'score': 0.9976316195563966}]
result = search.search('pear apricot cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #464 checking search results for 'pear apricot cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #464 checking search results for 'pear apricot cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #465 checking search results for 'fig apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017366188074778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017165271081213688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016766886057199244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015469306806042084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010431647208908549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00818106700460555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008179787111589124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007815436408332991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006509610465760151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('fig apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #465 checking search results for 'fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #465 checking search results for 'fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #466 checking search results for 'fig apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'title': 'N-680', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html', 'title': 'N-736', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'title': 'N-190', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'title': 'N-568', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-375.html', 'title': 'N-375', 'score': 1.0000000000000002}]
result = search.search('fig apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #466 checking search results for 'fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #466 checking search results for 'fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #467 checking search results for 'coconut kiwi cherry cherry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01637779218517407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015415899210606498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014265869577037592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013536852516349712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010773074633257359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008292279745124214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008187058062586853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006728242775301145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005896044433335687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005685044677736811}]
result = search.search('coconut kiwi cherry cherry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #467 checking search results for 'coconut kiwi cherry cherry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #467 checking search results for 'coconut kiwi cherry cherry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #468 checking search results for 'coconut kiwi cherry cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9998718343932632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'title': 'N-208', 'score': 0.9995478368543789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html', 'title': 'N-145', 'score': 0.9985350038454658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9982613694893443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.9972635172791041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html', 'title': 'N-59', 'score': 0.9970221762654703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html', 'title': 'N-538', 'score': 0.9965131691752356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.996496042870019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'title': 'N-241', 'score': 0.9957100311740805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9953144640824265}]
result = search.search('coconut kiwi cherry cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #468 checking search results for 'coconut kiwi cherry cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #468 checking search results for 'coconut kiwi cherry cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #469 checking search results for 'orange banana pear peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015928089766420205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014733033984602283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014050396326892683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012499714968023129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008483115703168528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008060600623754036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007319888350824673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006179773339967612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005626202021668242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005581835373791964}]
result = search.search('orange banana pear peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #469 checking search results for 'orange banana pear peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #469 checking search results for 'orange banana pear peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #470 checking search results for 'orange banana pear peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9997033315113746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-423.html', 'title': 'N-423', 'score': 0.9996732030414354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html', 'title': 'N-20', 'score': 0.9985304681768281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html', 'title': 'N-163', 'score': 0.9982934626990904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html', 'title': 'N-813', 'score': 0.9977630014624915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9966919022315658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.9962540833602271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-889.html', 'title': 'N-889', 'score': 0.9951932287949271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-794.html', 'title': 'N-794', 'score': 0.9951352782699882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9946851482209347}]
result = search.search('orange banana pear peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #470 checking search results for 'orange banana pear peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #470 checking search results for 'orange banana pear peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #471 checking search results for 'tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #471 checking search results for 'tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #471 checking search results for 'tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #472 checking search results for 'tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #472 checking search results for 'tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #472 checking search results for 'tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #473 checking search results for 'blueberry papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018514409470286576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01673880828852505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.0150833545766569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01336173377039391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009556623051602762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008721352433837913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006903395682934941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006794084475695152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0063959121824616865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006242389818313149}]
result = search.search('blueberry papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #473 checking search results for 'blueberry papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #473 checking search results for 'blueberry papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #474 checking search results for 'blueberry papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.999997040614159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9999964665603869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9999926377848621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9999917524319684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'title': 'N-95', 'score': 0.9999899169251489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.99998212905851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-636.html', 'title': 'N-636', 'score': 0.999921761248599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html', 'title': 'N-290', 'score': 0.9999210038815769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'title': 'N-134', 'score': 0.9999102513294398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.999905820414893}]
result = search.search('blueberry papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #474 checking search results for 'blueberry papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #474 checking search results for 'blueberry papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #475 checking search results for 'banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #475 checking search results for 'banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #475 checking search results for 'banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #476 checking search results for 'banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #476 checking search results for 'banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #476 checking search results for 'banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #477 checking search results for 'pear blueberry cherry lime apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01760540830807012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016800705157522067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01537780317985101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014606613935871609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008431645344957462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007974805482305456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007521951965735853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006865203665063065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005955493895947797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005838555210703967}]
result = search.search('pear blueberry cherry lime apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #477 checking search results for 'pear blueberry cherry lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #477 checking search results for 'pear blueberry cherry lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #478 checking search results for 'pear blueberry cherry lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html', 'title': 'N-191', 'score': 0.9979926234084873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html', 'title': 'N-904', 'score': 0.9974611102403576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9974442834910083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.99622872613119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-338.html', 'title': 'N-338', 'score': 0.9961506542372615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9960881839764203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.994878307264375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9944605979888678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html', 'title': 'N-716', 'score': 0.9943771545455001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9942667923854492}]
result = search.search('pear blueberry cherry lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #478 checking search results for 'pear blueberry cherry lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #478 checking search results for 'pear blueberry cherry lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #479 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #480 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #480 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #481 checking search results for 'fig kiwi cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01604269804304713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01555962033014143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013728576708345682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013307781705384414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010790967527112201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008686801424616192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008166427661499335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006551820231224933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0060489287975150074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005925179282519021}]
result = search.search('fig kiwi cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #481 checking search results for 'fig kiwi cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #481 checking search results for 'fig kiwi cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #482 checking search results for 'fig kiwi cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.999968234807257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html', 'title': 'N-73', 'score': 0.99961817101567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-678.html', 'title': 'N-678', 'score': 0.99961817101567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-827.html', 'title': 'N-827', 'score': 0.999600056055316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.999540973197745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 0.9995220020700268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.9994717113720196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9994539957525752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9993858042136212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'title': 'N-208', 'score': 0.9993495531253332}]
result = search.search('fig kiwi cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #482 checking search results for 'fig kiwi cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #482 checking search results for 'fig kiwi cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #483 checking search results for 'fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01836887615323217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016916930873335206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014759130498437193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0104658581649076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008513027875913006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008180618936444051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007760674684138653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065577838755536515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.00570177532996004}]
result = search.search('fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #483 checking search results for 'fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #483 checking search results for 'fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #484 checking search results for 'fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html', 'title': 'N-516', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}]
result = search.search('fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #484 checking search results for 'fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #484 checking search results for 'fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #485 checking search results for 'lime orange orange cherry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018239534501797022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017389484453158424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014090978515816968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.013433000617901949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008022634172294738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006822358174694114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006435918299196534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00639105462813238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006001556518665382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005536192773006492}]
result = search.search('lime orange orange cherry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #485 checking search results for 'lime orange orange cherry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #485 checking search results for 'lime orange orange cherry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #486 checking search results for 'lime orange orange cherry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-118.html', 'title': 'N-118', 'score': 0.9998833145104559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html', 'title': 'N-212', 'score': 0.9997566931501859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html', 'title': 'N-506', 'score': 0.9997437791562941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 0.9997234678265505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 0.999667419961512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'title': 'N-517', 'score': 0.999667419961512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-81.html', 'title': 'N-81', 'score': 0.9996600383425709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-229.html', 'title': 'N-229', 'score': 0.9996409237568857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html', 'title': 'N-390', 'score': 0.9996173751166896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html', 'title': 'N-56', 'score': 0.9995898200637502}]
result = search.search('lime orange orange cherry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #486 checking search results for 'lime orange orange cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #486 checking search results for 'lime orange orange cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #487 checking search results for 'banana apricot fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017256324227697233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016775558683220438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01655642311449757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015313212856969157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008416183107018223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008162864816207201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0080849548170132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007762198232044199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006493845650052013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.0054068430103232186}]
result = search.search('banana apricot fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #487 checking search results for 'banana apricot fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #487 checking search results for 'banana apricot fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #488 checking search results for 'banana apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'title': 'N-75', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html', 'title': 'N-203', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html', 'title': 'N-436', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 1.0}]
result = search.search('banana apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #488 checking search results for 'banana apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #488 checking search results for 'banana apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #489 checking search results for 'pear peach blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017081648989863772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01654854604075109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015205372864825985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015163204692984465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00796580235232967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007937208742053172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007426025036184099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0064152409497374345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006169393019837656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.0052176719803543594}]
result = search.search('pear peach blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #489 checking search results for 'pear peach blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #489 checking search results for 'pear peach blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #490 checking search results for 'pear peach blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9981488494661039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9980024873976225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html', 'title': 'N-554', 'score': 0.9979912588803599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9972684738899613}]
result = search.search('pear peach blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #490 checking search results for 'pear peach blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #490 checking search results for 'pear peach blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #491 checking search results for 'lime fig apricot coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017915010510824263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01654249580963326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015450785596336314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015344318872293676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010453583512305336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008203645909790098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0077396351510228166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007714560679901151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006373640646283988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005695582963106208}]
result = search.search('lime fig apricot coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #491 checking search results for 'lime fig apricot coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #491 checking search results for 'lime fig apricot coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #492 checking search results for 'lime fig apricot coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html', 'title': 'N-996', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-964.html', 'title': 'N-964', 'score': 0.9991537491348931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9989889899869644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-783.html', 'title': 'N-783', 'score': 0.998012346146502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9979800636513598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html', 'title': 'N-728', 'score': 0.9979777242193132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9972844839364489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9970164347117008}]
result = search.search('lime fig apricot coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #492 checking search results for 'lime fig apricot coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #492 checking search results for 'lime fig apricot coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #493 checking search results for 'kiwi pear apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016763448693209296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016649951877204344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015072270819256262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014019553356741198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010577636274759706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008392457283051815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007934841041679592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007237251118325067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0062704096192912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00619018135079634}]
result = search.search('kiwi pear apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #493 checking search results for 'kiwi pear apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #493 checking search results for 'kiwi pear apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #494 checking search results for 'kiwi pear apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-961.html', 'title': 'N-961', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html', 'title': 'N-730', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-675.html', 'title': 'N-675', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-751.html', 'title': 'N-751', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html', 'title': 'N-606', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html', 'title': 'N-234', 'score': 1.0000000000000002}]
result = search.search('kiwi pear apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #494 checking search results for 'kiwi pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #494 checking search results for 'kiwi pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #495 checking search results for 'apricot coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017074192025783988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016675334991417986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015383983894178613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010426696372393808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00827246628147235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008180134437547724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007714737958891829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006206840591026342}]
result = search.search('apricot coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #495 checking search results for 'apricot coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #495 checking search results for 'apricot coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #496 checking search results for 'apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'title': 'N-75', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-513.html', 'title': 'N-513', 'score': 1.0}]
result = search.search('apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #496 checking search results for 'apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #496 checking search results for 'apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #497 checking search results for 'papaya cherry banana fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017824818073112238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016852472051912117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01662393031978943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01486168842055214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008986841492457454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00817481694212735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008024305526063646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007521718725439253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006464570468383773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005190404955853803}]
result = search.search('papaya cherry banana fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #497 checking search results for 'papaya cherry banana fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #497 checking search results for 'papaya cherry banana fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #498 checking search results for 'papaya cherry banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html', 'title': 'N-624', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.998387684596654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9981566403203544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html', 'title': 'N-579', 'score': 0.9981264877772578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-469.html', 'title': 'N-469', 'score': 0.9979742084596608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html', 'title': 'N-633', 'score': 0.9979648867489518}]
result = search.search('papaya cherry banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #498 checking search results for 'papaya cherry banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #498 checking search results for 'papaya cherry banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #499 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #499 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #499 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #500 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #500 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #500 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #501 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #501 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #501 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #502 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #502 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #502 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #503 checking search results for 'pear tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018427787178793013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016800010055715187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01529583343924976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013110385528746564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008092838601935923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007864371201524039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007846151567708575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006173198517708175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005954129294865544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005578059977073146}]
result = search.search('pear tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #503 checking search results for 'pear tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #503 checking search results for 'pear tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #504 checking search results for 'pear tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'title': 'N-178', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html', 'title': 'N-357', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html', 'title': 'N-68', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html', 'title': 'N-639', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html', 'title': 'N-54', 'score': 1.0000000000000002}]
result = search.search('pear tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #504 checking search results for 'pear tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #504 checking search results for 'pear tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #505 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #505 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #505 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #506 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #506 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #506 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #507 checking search results for 'lime papaya peach cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01648736281116279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015319476332213344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014960607002795685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013560675122951308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010028577441643543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00861247981480278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007815201711263785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006775436224899076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005537279188925707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005208036818378282}]
result = search.search('lime papaya peach cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #507 checking search results for 'lime papaya peach cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #507 checking search results for 'lime papaya peach cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #508 checking search results for 'lime papaya peach cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9997202407699712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-307.html', 'title': 'N-307', 'score': 0.9996345236348011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.9982315704242452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.997294040215977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 0.9965562411437983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html', 'title': 'N-564', 'score': 0.9964421279950093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9958365112336193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-473.html', 'title': 'N-473', 'score': 0.9942057491416658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9941210092562369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html', 'title': 'N-956', 'score': 0.9940977551945495}]
result = search.search('lime papaya peach cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #508 checking search results for 'lime papaya peach cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #508 checking search results for 'lime papaya peach cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #509 checking search results for 'lime kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01871768717745311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018155672906293684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016818720434010833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010492234168285418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008590638396457436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008109040444974187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007530904684652348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006582680597841577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005833491522712972}]
result = search.search('lime kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #509 checking search results for 'lime kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #509 checking search results for 'lime kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #510 checking search results for 'lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html', 'title': 'N-652', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html', 'title': 'N-145', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'title': 'N-821', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}]
result = search.search('lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #510 checking search results for 'lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #510 checking search results for 'lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #511 checking search results for 'cherry apricot peach apricot peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017709399142739574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017019672487377402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016468187018802212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015462898384213173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007801489515254296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007699055024988823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006844513343499115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00610206453015958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006089760143437385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005770671847939184}]
result = search.search('cherry apricot peach apricot peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #511 checking search results for 'cherry apricot peach apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #511 checking search results for 'cherry apricot peach apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #512 checking search results for 'cherry apricot peach apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html', 'title': 'N-862', 'score': 0.9998350672887422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9998111300297904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-153.html', 'title': 'N-153', 'score': 0.9997989126200784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html', 'title': 'N-607', 'score': 0.999795142833768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'title': 'N-452', 'score': 0.9997680369898043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 0.9997666750431381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html', 'title': 'N-671', 'score': 0.9997324323914603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 0.9997291321361246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'title': 'N-69', 'score': 0.9997174629407515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 0.9990685366022064}]
result = search.search('cherry apricot peach apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #512 checking search results for 'cherry apricot peach apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #512 checking search results for 'cherry apricot peach apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #513 checking search results for 'papaya lime fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018434551965080263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016416034239529868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015508130589273658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015127241234254055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010471656311762778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008194589263198061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007929957460859862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0075931347713148935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006527536958631276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005719952724887357}]
result = search.search('papaya lime fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #513 checking search results for 'papaya lime fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #513 checking search results for 'papaya lime fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #514 checking search results for 'papaya lime fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-673.html', 'title': 'N-673', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html', 'title': 'N-633', 'score': 0.9979904612475603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'title': 'N-117', 'score': 0.9973918205558956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'title': 'N-102', 'score': 0.9968795602553365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9967335205856659}]
result = search.search('papaya lime fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #514 checking search results for 'papaya lime fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #514 checking search results for 'papaya lime fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #515 checking search results for 'kiwi pear cherry orange banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017450938021990447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015773209857791366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015308084148278655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015263491554752547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008086866277820211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007841518478417294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007801875717151896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006875237309692372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006370583515490854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0055733580982146435}]
result = search.search('kiwi pear cherry orange banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #515 checking search results for 'kiwi pear cherry orange banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #515 checking search results for 'kiwi pear cherry orange banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #516 checking search results for 'kiwi pear cherry orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-520.html', 'title': 'N-520', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979843251988714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.996766806358345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9962252583330639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9951279047430008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-811.html', 'title': 'N-811', 'score': 0.9951063849271571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html', 'title': 'N-94', 'score': 0.9948947257952623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html', 'title': 'N-836', 'score': 0.9948074072646274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9947991810767791}]
result = search.search('kiwi pear cherry orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #516 checking search results for 'kiwi pear cherry orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #516 checking search results for 'kiwi pear cherry orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #517 checking search results for 'fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018163169204821663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016307122922031465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015383324841057151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01535036172731807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0087391241293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008105974711685128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007760879864471845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006438100705934343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #517 checking search results for 'fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #517 checking search results for 'fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #518 checking search results for 'fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html', 'title': 'N-983', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}]
result = search.search('fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #518 checking search results for 'fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #518 checking search results for 'fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #519 checking search results for 'blueberry apple lime peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017744096734125338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017057019588987782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01663271505856665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014412763862498217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008627231879966047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007383570018270508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0068343991029899635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005733183282298119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005620474367814127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005233174630569525}]
result = search.search('blueberry apple lime peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #519 checking search results for 'blueberry apple lime peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #519 checking search results for 'blueberry apple lime peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #520 checking search results for 'blueberry apple lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'title': 'N-268', 'score': 0.9987155630035016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.998355230403715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-322.html', 'title': 'N-322', 'score': 0.9983428617277577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9979397720385143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html', 'title': 'N-96', 'score': 0.9973634475684359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html', 'title': 'N-922', 'score': 0.996702295840749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html', 'title': 'N-259', 'score': 0.9965579139202335}]
result = search.search('blueberry apple lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #520 checking search results for 'blueberry apple lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #520 checking search results for 'blueberry apple lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #521 checking search results for 'apple blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018549032816775488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017090521404198818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016799772820063362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013513688420503203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008699935603936271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007073339593895828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005677498091252456}]
result = search.search('apple blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #521 checking search results for 'apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #521 checking search results for 'apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #522 checking search results for 'apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html', 'title': 'N-296', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-799.html', 'title': 'N-799', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-301.html', 'title': 'N-301', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}]
result = search.search('apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #522 checking search results for 'apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #522 checking search results for 'apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #523 checking search results for 'apple lime lime coconut papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01685639639904577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016075143547494147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014576647591767066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014399852529729022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009713680379975925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008298043576657872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007720184942509571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007025460631423907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006043276961659192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00598149203010816}]
result = search.search('apple lime lime coconut papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #523 checking search results for 'apple lime lime coconut papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #523 checking search results for 'apple lime lime coconut papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #524 checking search results for 'apple lime lime coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 0.9994898535955845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'title': 'N-485', 'score': 0.998801716834074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-973.html', 'title': 'N-973', 'score': 0.9985174166416776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html', 'title': 'N-820', 'score': 0.9982769075213972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html', 'title': 'N-699', 'score': 0.9982725095382062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.9978694543899966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9977610523417731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-988.html', 'title': 'N-988', 'score': 0.997490768292419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html', 'title': 'N-986', 'score': 0.9972834782706346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.9965949553007268}]
result = search.search('apple lime lime coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #524 checking search results for 'apple lime lime coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #524 checking search results for 'apple lime lime coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #525 checking search results for 'apricot apricot apple cherry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016279364671967857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015570096404976618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015288399438960662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014438004284076227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008749321102210203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0075482018316263945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007441349845112729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0071640489822450285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006150488977248173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005876555015183282}]
result = search.search('apricot apricot apple cherry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #525 checking search results for 'apricot apricot apple cherry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #525 checking search results for 'apricot apricot apple cherry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #526 checking search results for 'apricot apricot apple cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-307.html', 'title': 'N-307', 'score': 0.9990202176490851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-570.html', 'title': 'N-570', 'score': 0.9966694284996607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 0.996269970745178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'title': 'N-95', 'score': 0.996197688513614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-988.html', 'title': 'N-988', 'score': 0.995996959294571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9949595701395105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html', 'title': 'N-723', 'score': 0.9948730021141406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.9948729334821993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9946310631793507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html', 'title': 'N-327', 'score': 0.9946199499464025}]
result = search.search('apricot apricot apple cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #526 checking search results for 'apricot apricot apple cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #526 checking search results for 'apricot apricot apple cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #527 checking search results for 'banana peach banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018220276666473204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01677981761643075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014293790509295561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013916585578975316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008347015278470689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007786994267140358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007443205668983613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005194425888812885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.004755376270626736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.004657367148601536}]
result = search.search('banana peach banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #527 checking search results for 'banana peach banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #527 checking search results for 'banana peach banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #528 checking search results for 'banana peach banana coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html', 'title': 'N-879', 'score': 0.9996123432015714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 0.9995297742087441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-887.html', 'title': 'N-887', 'score': 0.9975365079895359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 0.9970652295886937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.9963607737678851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-858.html', 'title': 'N-858', 'score': 0.996071434103635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9953157503045937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-968.html', 'title': 'N-968', 'score': 0.9952950828275149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html', 'title': 'N-927', 'score': 0.9947827424258662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-737.html', 'title': 'N-737', 'score': 0.9943614384658738}]
result = search.search('banana peach banana coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #528 checking search results for 'banana peach banana coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #528 checking search results for 'banana peach banana coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #529 checking search results for 'papaya peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017364792453945174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016086190011278985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014772580276144571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008586279488591043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007998867659950544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007553009524476125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007530797065995532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0057951933158775495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005697888956557006}]
result = search.search('papaya peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #529 checking search results for 'papaya peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #529 checking search results for 'papaya peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #530 checking search results for 'papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html', 'title': 'N-729', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html', 'title': 'N-861', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html', 'title': 'N-516', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0}]
result = search.search('papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #530 checking search results for 'papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #530 checking search results for 'papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #531 checking search results for 'fig apple pear lime kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017975948670552355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016600692900150302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014575309680138239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013860913146475426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009324551456476057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008475174430891613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007995063999135526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007448521502022306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0061271106180462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005621043019862772}]
result = search.search('fig apple pear lime kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #531 checking search results for 'fig apple pear lime kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #531 checking search results for 'fig apple pear lime kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #532 checking search results for 'fig apple pear lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-809.html', 'title': 'N-809', 'score': 0.9975439172525761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9963484710133499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.9947335061738166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9946386411952656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html', 'title': 'N-552', 'score': 0.9945747579211794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 0.994531131170528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-965.html', 'title': 'N-965', 'score': 0.9934869700567092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9934196722595668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9933045982821842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9925956895440242}]
result = search.search('fig apple pear lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #532 checking search results for 'fig apple pear lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #532 checking search results for 'fig apple pear lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #533 checking search results for 'banana lime apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017300619805966127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01702162482765968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016459265112658605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014196716460071706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008677587852484198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007851247681968194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00763809387712909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0075707276301367355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005937143654429494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005236161399893994}]
result = search.search('banana lime apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #533 checking search results for 'banana lime apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #533 checking search results for 'banana lime apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #534 checking search results for 'banana lime apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'title': 'N-184', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9986108913599487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.998591375248645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-801.html', 'title': 'N-801', 'score': 0.9982157118871954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.998190380801599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9979674809976987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979446662621143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9978658011139468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9978643306883035}]
result = search.search('banana lime apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #534 checking search results for 'banana lime apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #534 checking search results for 'banana lime apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #535 checking search results for 'banana pear peach kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017963792626222636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01625036684086867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015314793644227984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014012458867464522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008314215248713137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008297947787142917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007670090690359989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007323766149424609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005641385837474875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005301843002793149}]
result = search.search('banana pear peach kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #535 checking search results for 'banana pear peach kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #535 checking search results for 'banana pear peach kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #536 checking search results for 'banana pear peach kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9975199098663529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9972623501792709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 0.9970072455946138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html', 'title': 'N-554', 'score': 0.995939344809328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9949538110467065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9946543382707993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9946417754878263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.994575108617865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-940.html', 'title': 'N-940', 'score': 0.9943010371495854}]
result = search.search('banana pear peach kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #536 checking search results for 'banana pear peach kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #536 checking search results for 'banana pear peach kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #537 checking search results for 'fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018163169204821663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016307122922031465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015383324841057151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01535036172731807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0087391241293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008105974711685128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007760879864471845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006438100705934343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #537 checking search results for 'fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #537 checking search results for 'fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #538 checking search results for 'fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html', 'title': 'N-983', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}]
result = search.search('fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #538 checking search results for 'fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #538 checking search results for 'fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #539 checking search results for 'fig orange kiwi kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01772975425826276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016563385676708765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014450565068155723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014018003036663895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008806790486073973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00803931290731115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0073082259221131955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006570419093965882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00649232418769092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005160496167803616}]
result = search.search('fig orange kiwi kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #539 checking search results for 'fig orange kiwi kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #539 checking search results for 'fig orange kiwi kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #540 checking search results for 'fig orange kiwi kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html', 'title': 'N-579', 'score': 0.9999386226820954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 0.9997904115034103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 0.9996662147678594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 0.9996527492669266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html', 'title': 'N-548', 'score': 0.9996003024521508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html', 'title': 'N-254', 'score': 0.9995714089421865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html', 'title': 'N-828', 'score': 0.9994798987762745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.9994619307483952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9978717188912296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9966242974629014}]
result = search.search('fig orange kiwi kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #540 checking search results for 'fig orange kiwi kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #540 checking search results for 'fig orange kiwi kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #541 checking search results for 'blueberry tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01669490332425404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016058478899224213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015451202277677918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008698911021167278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008069992927224478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006284870347783221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005446197209621002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005423949332687884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005190417958698911}]
result = search.search('blueberry tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #541 checking search results for 'blueberry tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #541 checking search results for 'blueberry tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #542 checking search results for 'blueberry tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}]
result = search.search('blueberry tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #542 checking search results for 'blueberry tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #542 checking search results for 'blueberry tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #543 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #543 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #543 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #544 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #544 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #544 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #545 checking search results for 'fig cherry tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018371834207656954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016459795342189616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016455544085068025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014988130695513831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009708436254912361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007818365543402657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007625290261651368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007597658627688621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0064297942624007755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005854522927634276}]
result = search.search('fig cherry tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #545 checking search results for 'fig cherry tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #545 checking search results for 'fig cherry tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #546 checking search results for 'fig cherry tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html', 'title': 'N-978', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-462.html', 'title': 'N-462', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-274.html', 'title': 'N-274', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html', 'title': 'N-762', 'score': 1.0000000000000002}]
result = search.search('fig cherry tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #546 checking search results for 'fig cherry tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #546 checking search results for 'fig cherry tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #547 checking search results for 'kiwi blueberry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017534826547438927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017050373924210657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01671816510004117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014183831332995132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00827577703663935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0067955189775445995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0063344504463659045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006266229807723177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005976399109101698}]
result = search.search('kiwi blueberry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #547 checking search results for 'kiwi blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #547 checking search results for 'kiwi blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #548 checking search results for 'kiwi blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'title': 'N-429', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html', 'title': 'N-589', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-240.html', 'title': 'N-240', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.9999999999999999}]
result = search.search('kiwi blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #548 checking search results for 'kiwi blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #548 checking search results for 'kiwi blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #549 checking search results for 'kiwi banana peach blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017707914880782508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016968628629810988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016080149158168782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015378998832280805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008152298949060555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007553913773810688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006983181805516904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006848693939227971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005513932107498598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005394846214843343}]
result = search.search('kiwi banana peach blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #549 checking search results for 'kiwi banana peach blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #549 checking search results for 'kiwi banana peach blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #550 checking search results for 'kiwi banana peach blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9974399690956396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-859.html', 'title': 'N-859', 'score': 0.9964829554422757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'title': 'N-429', 'score': 0.9962511979356725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'title': 'N-433', 'score': 0.994835887027208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9945468511929935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9944700952534125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html', 'title': 'N-387', 'score': 0.9932977341323792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9932612836211646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9929633233297125}]
result = search.search('kiwi banana peach blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #550 checking search results for 'kiwi banana peach blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #550 checking search results for 'kiwi banana peach blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #551 checking search results for 'apple orange papaya blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018189760419250994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01749616620328129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015987496272209183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014287341698637993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008292760225212362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007520721650644505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006116077025759167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005857524344377629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005678564310670443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005378696622809419}]
result = search.search('apple orange papaya blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #551 checking search results for 'apple orange papaya blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #551 checking search results for 'apple orange papaya blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #552 checking search results for 'apple orange papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html', 'title': 'N-577', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html', 'title': 'N-983', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html', 'title': 'N-936', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-85.html', 'title': 'N-85', 'score': 0.9988913210607775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html', 'title': 'N-497', 'score': 0.998416847564033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9983818251278621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9982878927886911}]
result = search.search('apple orange papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #552 checking search results for 'apple orange papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #552 checking search results for 'apple orange papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #553 checking search results for 'peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017999618669297012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016472118750122066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015129369814932995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013417002455314322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00807019310952003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00799460989410079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007665272601708714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007596239445336568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006171249361220714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #553 checking search results for 'peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #553 checking search results for 'peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #554 checking search results for 'peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'title': 'N-252', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-298.html', 'title': 'N-298', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html', 'title': 'N-593', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html', 'title': 'N-839', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html', 'title': 'N-79', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-689.html', 'title': 'N-689', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html', 'title': 'N-993', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html', 'title': 'N-907', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html', 'title': 'N-283', 'score': 1.0000000000000002}]
result = search.search('peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #554 checking search results for 'peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #554 checking search results for 'peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #555 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018576625341197427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018550979173833602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01640754086111273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013803037917696093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007673712811489487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007581824303266141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006275262757339211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005246135096679755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005011939250590545}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #555 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #555 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #556 checking search results for 'apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html', 'title': 'N-861', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html', 'title': 'N-447', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'title': 'N-251', 'score': 1.0000000000000002}]
result = search.search('apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #556 checking search results for 'apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #556 checking search results for 'apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #557 checking search results for 'apricot pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017800448041321994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014903759262042841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.011987021655716778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00818106700460555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007228299910266451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006509610465760151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('apricot pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #557 checking search results for 'apricot pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #557 checking search results for 'apricot pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #558 checking search results for 'apricot pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'title': 'N-680', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html', 'title': 'N-321', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html', 'title': 'N-874', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}]
result = search.search('apricot pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #558 checking search results for 'apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #558 checking search results for 'apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #559 checking search results for 'peach banana fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01826174166876603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01679197918116157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015886471801560727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015351848569483835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00824662885649099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0077886038382672515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007638604491157195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007556819661831437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005340577856074543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005316004746529177}]
result = search.search('peach banana fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #559 checking search results for 'peach banana fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #559 checking search results for 'peach banana fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #560 checking search results for 'peach banana fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-850.html', 'title': 'N-850', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'title': 'N-433', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html', 'title': 'N-862', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-939.html', 'title': 'N-939', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-859.html', 'title': 'N-859', 'score': 0.9973835757868932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html', 'title': 'N-929', 'score': 0.997371316971851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9972939569281287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.997263517772796}]
result = search.search('peach banana fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #560 checking search results for 'peach banana fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #560 checking search results for 'peach banana fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #561 checking search results for 'fig pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01849818506465135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016767485423591168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015124780697016046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013235403531305583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01047428670193717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008181168187271427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007284338125666095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006619208394874289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005647163929064623}]
result = search.search('fig pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #561 checking search results for 'fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #561 checking search results for 'fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #562 checking search results for 'fig pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html', 'title': 'N-418', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html', 'title': 'N-768', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'title': 'N-821', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'title': 'N-680', 'score': 1.0000000000000002}]
result = search.search('fig pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #562 checking search results for 'fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #562 checking search results for 'fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #563 checking search results for 'kiwi cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017816847739658727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017688045625616815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016650105232957953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015205111539230837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009968453003063349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008576597215919565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007456539193354069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007313935970066565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006435377501097614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('kiwi cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #563 checking search results for 'kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #563 checking search results for 'kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #564 checking search results for 'kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html', 'title': 'N-440', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html', 'title': 'N-254', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html', 'title': 'N-497', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0000000000000002}]
result = search.search('kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #564 checking search results for 'kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #564 checking search results for 'kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #565 checking search results for 'banana apple blueberry apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017804471698290632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016797809329345284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015066828461830589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.010049863349792139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008039908412736328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00613157029342491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005476859859116748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00526368439788176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005206750075296378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005159365559095958}]
result = search.search('banana apple blueberry apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #565 checking search results for 'banana apple blueberry apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #565 checking search results for 'banana apple blueberry apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #566 checking search results for 'banana apple blueberry apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-91.html', 'title': 'N-91', 'score': 0.9999935213325002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9996014030612715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html', 'title': 'N-888', 'score': 0.9994572469113358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html', 'title': 'N-476', 'score': 0.9994117229355708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html', 'title': 'N-110', 'score': 0.9993000102215741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html', 'title': 'N-255', 'score': 0.9991773400279641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-278.html', 'title': 'N-278', 'score': 0.9989779106209767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 0.9988651304448466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html', 'title': 'N-943', 'score': 0.9988497271671612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-941.html', 'title': 'N-941', 'score': 0.998821196807685}]
result = search.search('banana apple blueberry apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #566 checking search results for 'banana apple blueberry apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #566 checking search results for 'banana apple blueberry apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #567 checking search results for 'cherry tomato apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01871768717745311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01782728395435368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014413379291093244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01083096028635217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0081285540929742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007921573470605577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007539895840669399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006512528636033623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006168120884373373}]
result = search.search('cherry tomato apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #567 checking search results for 'cherry tomato apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #567 checking search results for 'cherry tomato apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #568 checking search results for 'cherry tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'title': 'N-195', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'title': 'N-680', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html', 'title': 'N-736', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'title': 'N-190', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 1.0000000000000002}]
result = search.search('cherry tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #568 checking search results for 'cherry tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #568 checking search results for 'cherry tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #569 checking search results for 'cherry orange coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018258292400976105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017728775401460756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.0155724633637093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014944316226205756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008251577893241109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007884493528092264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007436469697625918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006493244965151277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006491170988645262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006194072202924945}]
result = search.search('cherry orange coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #569 checking search results for 'cherry orange coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #569 checking search results for 'cherry orange coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #570 checking search results for 'cherry orange coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'title': 'N-558', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html', 'title': 'N-700', 'score': 1.0}]
result = search.search('cherry orange coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #570 checking search results for 'cherry orange coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #570 checking search results for 'cherry orange coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #571 checking search results for 'pear peach cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018099614210321666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016542657091217057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01501224635224806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014898706259230145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008859683211233062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0078992068406821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007681928147270676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0074246775733268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00617179687011536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005564360288936984}]
result = search.search('pear peach cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #571 checking search results for 'pear peach cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #571 checking search results for 'pear peach cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #572 checking search results for 'pear peach cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html', 'title': 'N-511', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'title': 'N-82', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html', 'title': 'N-23', 'score': 0.9977080848602168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'title': 'N-238', 'score': 0.9974498882104571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9972624676841162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9972491575341951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9972400107835702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9968505894552833}]
result = search.search('pear peach cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #572 checking search results for 'pear peach cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #572 checking search results for 'pear peach cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #573 checking search results for 'tomato papaya coconut peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018516293736439628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017497948927757256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016367854108921748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01414778119945649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00827309437259332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00759014112025507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0075089798405945435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007293131843496877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0058664050948023915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00508590993335376}]
result = search.search('tomato papaya coconut peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #573 checking search results for 'tomato papaya coconut peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #573 checking search results for 'tomato papaya coconut peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #574 checking search results for 'tomato papaya coconut peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html', 'title': 'N-879', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-667.html', 'title': 'N-667', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html', 'title': 'N-864', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9987428485488539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9985187699937248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9980255685940002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9975286023072439}]
result = search.search('tomato papaya coconut peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #574 checking search results for 'tomato papaya coconut peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #574 checking search results for 'tomato papaya coconut peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #575 checking search results for 'kiwi kiwi apricot papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01774481463277721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016776494389190696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015669873809743717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014138559344501542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009242167800328074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008691488039273913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007547417034251702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006918919019705351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006480006349756379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005133106931532329}]
result = search.search('kiwi kiwi apricot papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #575 checking search results for 'kiwi kiwi apricot papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #575 checking search results for 'kiwi kiwi apricot papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #576 checking search results for 'kiwi kiwi apricot papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-883.html', 'title': 'N-883', 'score': 0.9999008122227652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html', 'title': 'N-685', 'score': 0.999857974502629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html', 'title': 'N-23', 'score': 0.9996871947719995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'title': 'N-40', 'score': 0.9996681525050318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-858.html', 'title': 'N-858', 'score': 0.9995833773408894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'title': 'N-366', 'score': 0.9995632182667611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-850.html', 'title': 'N-850', 'score': 0.9995372661951452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-617.html', 'title': 'N-617', 'score': 0.9995200547585076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html', 'title': 'N-671', 'score': 0.9994999868634457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html', 'title': 'N-199', 'score': 0.999488654389736}]
result = search.search('kiwi kiwi apricot papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #576 checking search results for 'kiwi kiwi apricot papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #576 checking search results for 'kiwi kiwi apricot papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #577 checking search results for 'apple kiwi papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01857465887042773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.0166357216001913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016466745088985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014327987228586874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008494349562321792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008385204391909503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007809578066757186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0077004133905364805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0058698649051421225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00573104743676864}]
result = search.search('apple kiwi papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #577 checking search results for 'apple kiwi papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #577 checking search results for 'apple kiwi papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #578 checking search results for 'apple kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-411.html', 'title': 'N-411', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html', 'title': 'N-583', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-611.html', 'title': 'N-611', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-778.html', 'title': 'N-778', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html', 'title': 'N-879', 'score': 1.0}]
result = search.search('apple kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #578 checking search results for 'apple kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #578 checking search results for 'apple kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #579 checking search results for 'pear tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('pear tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #579 checking search results for 'pear tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #579 checking search results for 'pear tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #580 checking search results for 'pear tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('pear tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #580 checking search results for 'pear tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #580 checking search results for 'pear tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #581 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #581 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #581 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #582 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #582 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #582 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #583 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #583 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #583 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #584 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #584 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #584 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #585 checking search results for 'blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018404748949653934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018284476619512068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016803577758538277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015383130606559575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00874995412765785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007912355114364769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007118130024199721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006264475346122091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006168183850648891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #585 checking search results for 'blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #585 checking search results for 'blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #586 checking search results for 'blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0000000000000002}]
result = search.search('blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #586 checking search results for 'blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #586 checking search results for 'blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #587 checking search results for 'orange cherry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01850122132480022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016564099293469303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015818126058234058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015202424694081715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008996965138345957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007880951272198334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007437800815806536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007378439513520963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065685058042324026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005912374569260538}]
result = search.search('orange cherry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #587 checking search results for 'orange cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #587 checking search results for 'orange cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #588 checking search results for 'orange cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-933.html', 'title': 'N-933', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html', 'title': 'N-215', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html', 'title': 'N-873', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html', 'title': 'N-248', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-569.html', 'title': 'N-569', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 1.0}]
result = search.search('orange cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #588 checking search results for 'orange cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #588 checking search results for 'orange cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #589 checking search results for 'lime fig papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01825922821436506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016154612522766634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015949029982976398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01489718870298936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009249088832309611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0079751874166958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007742735055384058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0071771353073337265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065789614970569255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005710888273353766}]
result = search.search('lime fig papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #589 checking search results for 'lime fig papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #589 checking search results for 'lime fig papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #590 checking search results for 'lime fig papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'title': 'N-184', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-673.html', 'title': 'N-673', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html', 'title': 'N-139', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-612.html', 'title': 'N-612', 'score': 0.9981973293106461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html', 'title': 'N-579', 'score': 0.9981524445503321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html', 'title': 'N-135', 'score': 0.9976332565906639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 0.9969198249475412}]
result = search.search('lime fig papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #590 checking search results for 'lime fig papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #590 checking search results for 'lime fig papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #591 checking search results for 'blueberry apple cherry kiwi fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01754501315139984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01665739257639472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016597802722546955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014386810777589115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008090198131729117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007527116967509628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007236105369339295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006797731133920649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0061439980731005355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091017}]
result = search.search('blueberry apple cherry kiwi fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #591 checking search results for 'blueberry apple cherry kiwi fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #591 checking search results for 'blueberry apple cherry kiwi fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #592 checking search results for 'blueberry apple cherry kiwi fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9973341939065521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html', 'title': 'N-886', 'score': 0.9972849827788196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9972743049867755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9950376502863767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-85.html', 'title': 'N-85', 'score': 0.995037614280858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html', 'title': 'N-752', 'score': 0.9948623302075271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'title': 'N-102', 'score': 0.9946809502197854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9944710937331658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-406.html', 'title': 'N-406', 'score': 0.9944413553411116}]
result = search.search('blueberry apple cherry kiwi fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #592 checking search results for 'blueberry apple cherry kiwi fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #592 checking search results for 'blueberry apple cherry kiwi fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #593 checking search results for 'apple fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01828756551934272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01742322126625632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016459795342189616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014072230948730424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008921581048478941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008135997631034043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007749752503211453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007596977948160174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005854522927634276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00583323965702325}]
result = search.search('apple fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #593 checking search results for 'apple fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #593 checking search results for 'apple fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #594 checking search results for 'apple fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html', 'title': 'N-996', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-481.html', 'title': 'N-481', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-772.html', 'title': 'N-772', 'score': 1.0000000000000002}]
result = search.search('apple fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #594 checking search results for 'apple fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #594 checking search results for 'apple fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #595 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #595 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #595 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #596 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #596 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #596 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #597 checking search results for 'peach papaya fig lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018369214566865952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01621603717688416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016209546879206234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015065130586106718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009142678199301538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008327375050699061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007736483534607275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007593300632880829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005659586651761879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0055519420851141725}]
result = search.search('peach papaya fig lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #597 checking search results for 'peach papaya fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #597 checking search results for 'peach papaya fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #598 checking search results for 'peach papaya fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html', 'title': 'N-775', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html', 'title': 'N-735', 'score': 0.9985926384001936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9983376970075187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9982937200188937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html', 'title': 'N-42', 'score': 0.9981748330393029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9978323189444972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9972423089891428}]
result = search.search('peach papaya fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #598 checking search results for 'peach papaya fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #598 checking search results for 'peach papaya fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #599 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #599 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #599 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #600 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #600 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #600 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #601 checking search results for 'papaya fig peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018369214566865952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016216037176884156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016209546879206234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015065130586106716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009142678199301538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008327375050699061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007736483534607276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00759330063288083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005659586651761879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0055519420851141725}]
result = search.search('papaya fig peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #601 checking search results for 'papaya fig peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #601 checking search results for 'papaya fig peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #602 checking search results for 'papaya fig peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html', 'title': 'N-775', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html', 'title': 'N-735', 'score': 0.9985926384001934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9983376970075187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9982937200188937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html', 'title': 'N-42', 'score': 0.9981748330393029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9978323189444972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9972423089891428}]
result = search.search('papaya fig peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #602 checking search results for 'papaya fig peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #602 checking search results for 'papaya fig peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #603 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #603 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #603 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #604 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #604 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #604 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #605 checking search results for 'kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017032108404584127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016819016702439023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016795326189389222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015450935058471154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008203853975826467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007810020720919612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007121445437211306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0062864358590972004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005554073191544973}]
result = search.search('kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #605 checking search results for 'kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #605 checking search results for 'kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #606 checking search results for 'kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'title': 'N-77', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html', 'title': 'N-867', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}]
result = search.search('kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #606 checking search results for 'kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #606 checking search results for 'kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #607 checking search results for 'blueberry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018427787178793013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01680001005571519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015295833439249762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013110385528746568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008092838601935923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00786437120152404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007846151567708575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006173198517708176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005954129294865545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005578059977073146}]
result = search.search('blueberry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #607 checking search results for 'blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #607 checking search results for 'blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #608 checking search results for 'blueberry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html', 'title': 'N-303', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-493.html', 'title': 'N-493', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html', 'title': 'N-841', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}]
result = search.search('blueberry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #608 checking search results for 'blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #608 checking search results for 'blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
