import write_your_name as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is())  > 1 

# Test for Non - empty string
def test_non_empty_string():
    assert name_point.hi_my_name_is() != ""

# Test for Presence of specific words
def test_presence_of_words():
    required_words = ["Karthikeyan","Muthusamy"]
    for words in required_words:
        assert words in name_point.hi_my_name_is().split()


