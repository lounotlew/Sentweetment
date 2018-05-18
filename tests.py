#
#
#

# Tests for get_twitter_data().

data = get_twitter_data('realDonaldTrump')

assert(len(data) != 0)
assert(type(data) == list)
