# Analyze Text with a TextAnalyzer object!
#
# By:
# Who did you work with:

import unittest # import the library needed for testing

class TextAnalyzer:

    def __init__(self, filepath):
        """Initializes the TextAnalyzer object, using the file at filepath""" 
        pass       

    def line_count(self):
        """Returns the number of lines in the file"""
        pass

    def word_count(self):
        """Returns the number of words in the file. A word is defined as any 
        text that is separated by whitespace (spaces, newlines, or tabs).
        followed by punctuation (like ? or !)."""
        pass

    def vocabulary(self):
        """Returns a list of the unique words in the text, sorted in 
        alphabetical order. Capitalization should be ignored, so 'Cat' is the
        same word as 'cat'. The returned words should be all lower-case."""
        pass

    def num_unique_words(self):
        """Returns the number of unique words in the text. Capitalization 
        should be ignored, so 'Cat' is the same word as 'cat'."""
        pass
        
    def frequencies(self):
        """Returns a dictionary of the words in the text and the count of how 
        many times they appear. The words are the keys, and the counts are the
        values. All the words should be lower case. The order of the keys 
        doesn't matter."""
        pass

    def frequency_of(self, word):
        """Returns the number of times word appears in the text. Capitalization 
        should be ignored, so 'Cat' is the same word as 'cat'."""
        pass

    def percent_frequencies(self):
        """Returns a dictionary of the words in the text and the fraction of 
        the text. The words are the keys, and the counts are the
        values. All the words should be lower case. The order of the keys 
        doesn't matter."""
        pass
    

    def most_common(self, n=1):
        """Returns a list of the most common n words in the text. By default,
        n is 1. The returned words should be in alphabetical order.
        
        There might be a case where multiple words have the same frequency,
        but you can only return some of them due to the n value. In that case,
        return the ones that come first alphabetically."""
        pass


    def similarity_with(self, other_text_analyzer, n=10):
        """Extra credit. Calculates the similarity between this text and 
        the other text using cosine similarity. See project specification
        for details."""
        pass
   

# These are the tests. The main() is all the way at the bottom.

class TestLineCount(unittest.TestCase):

    def test_line_count_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.line_count(), 1)
        self.assertEqual(ta.line_count(), 1) # Check that it works when called a second time
        
    def test_line_count_tiny3(self):    
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.line_count(), 3)
        self.assertEqual(ta.line_count(), 3) # Check that it works when called a second time

    def test_line_count_the_victors(self):    
        ta = TextAnalyzer("the_victors.txt")
        self.assertEqual(ta.line_count(), 33)
        self.assertEqual(ta.line_count(), 33) # Check that it works when called a second time


class TestWordCount(unittest.TestCase):
    
    def test_word_count_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.word_count(), 3)
        self.assertEqual(ta.word_count(), 3) # Check that it works when called a second time
        
    def test_word_count_tiny3(self):    
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.word_count(), 8)
        self.assertEqual(ta.word_count(), 8) # Check that it works when called a second time

    def test_word_count_the_victors(self):    
        ta = TextAnalyzer("the_victors.txt")
        self.assertEqual(ta.word_count(), 175)
        self.assertEqual(ta.word_count(), 175) # Check that it works when called a second time

class TestFrequencies(unittest.TestCase):

    def test_frequencies_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.frequencies()['i'], 1)
        self.assertEqual(ta.frequencies()['love'], 1)
        self.assertEqual(ta.frequencies()['cats'], 1)

    def test_frequencies_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.frequencies()['i'], 1)
        self.assertEqual(ta.frequencies()['love'], 1)
        self.assertEqual(ta.frequencies()['cats'], 1)
        self.assertEqual(ta.frequencies()['so'], 4)
        self.assertEqual(ta.frequencies()['much'], 1)

    def test_frequencies_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.frequencies()['i'], 3)
        self.assertEqual(ta.frequencies()['love'], 3)
        self.assertEqual(ta.frequencies()['cats'], 1)
        self.assertEqual(ta.frequencies()['so'], 12)
        self.assertEqual(ta.frequencies()['much'], 3)
        self.assertEqual(ta.frequencies()['dogs'], 1)
        self.assertEqual(ta.frequencies()['parakeets'], 1)

class TestFrequencyOf(unittest.TestCase):

    def test_frequency_of_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.frequency_of('i'), 1)
        self.assertEqual(ta.frequency_of('love'), 1)
        self.assertEqual(ta.frequency_of('cats'), 1)
        self.assertEqual(ta.frequency_of('dogs'), 0)
        self.assertEqual(ta.frequency_of('I'), 1)
        self.assertEqual(ta.frequency_of('LOVE'), 1)

    def test_frequency_of_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.frequency_of('i'), 1)
        self.assertEqual(ta.frequency_of('love'), 1)
        self.assertEqual(ta.frequency_of('cats'), 1)
        self.assertEqual(ta.frequency_of('so'), 4)
        self.assertEqual(ta.frequency_of('much'), 1)
        self.assertEqual(ta.frequency_of('dogs'), 0)

    def test_frequency_of_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.frequency_of('i'), 3)
        self.assertEqual(ta.frequency_of('love'), 3)
        self.assertEqual(ta.frequency_of('cats'), 1)
        self.assertEqual(ta.frequency_of('so'), 12)
        self.assertEqual(ta.frequency_of('much'), 3)
        self.assertEqual(ta.frequency_of('dogs'), 1)
        self.assertEqual(ta.frequency_of('parakeets'), 1)
        self.assertEqual(ta.frequency_of('ferrets'), 0)

class TestVocabulary(unittest.TestCase):

    def test_vocabulary_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.vocabulary(), ['cats', 'i', 'love'])

    def test_vocabulary_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.vocabulary(), ['cats', 'i', 'love', 'much', 'so'])

    def test_vocabulary_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.vocabulary(), ['cats', 'dogs', 'i', 'love', 'much', 'parakeets', 'so'])

class TestNumUniqueWords(unittest.TestCase):

    def test_num_unique_words_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.num_unique_words(), 3)

    def test_num_unique_words_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.num_unique_words(), 5)

    def test_num_unique_words_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.num_unique_words(), 7)

    def test_num_unique_words_thevictors(self):
        ta = TextAnalyzer("the_victors.txt")
        self.assertEqual(ta.num_unique_words(), 56)

class TestPercentFrequencyOf(unittest.TestCase):

    def test_percent_frequency_of_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertIn('i', ta.percent_frequencies())
        self.assertIn('love', ta.percent_frequencies())
        self.assertIn('cats', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 1/3)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 1/3)
        self.assertAlmostEqual(ta.percent_frequencies()['cats'], 1/3)

    def test_percent_frequency_of_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertIn('i', ta.percent_frequencies())
        self.assertIn('love', ta.percent_frequencies())
        self.assertIn('cats', ta.percent_frequencies())
        self.assertIn('so', ta.percent_frequencies())
        self.assertIn('much', ta.percent_frequencies())
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 1/8)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 1/8)
        self.assertAlmostEqual(ta.percent_frequencies()['cats'], 1/8)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 4/8)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 1/8)

    def test_percent_frequency_of_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertAlmostEqual(ta.percent_frequencies()['i'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['love'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['cats'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['so'], 12/24)
        self.assertAlmostEqual(ta.percent_frequencies()['much'], 3/24)
        self.assertAlmostEqual(ta.percent_frequencies()['dogs'], 1/24)
        self.assertAlmostEqual(ta.percent_frequencies()['parakeets'], 1/24)

class TestMostCommon1(unittest.TestCase):

    def test_most_common_1_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.most_common(), ['so'])

    def test_most_common_1_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.most_common(), ['so'])

class TestMostCommonOutOfRange(unittest.TestCase):

    def test_most_common_oor_multiple_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.most_common(0), [])
        self.assertEqual(ta.most_common(4), ['cats', 'i', 'love'])

class TestMostCommonMultipleClearCases(unittest.TestCase):

    def test_most_common_multiple_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.most_common(3), ['cats', 'i', 'love'])

    def test_most_common_multiple_tiny4(self):
        ta = TextAnalyzer("tinyfile_4.txt")
        self.assertEqual(ta.most_common(4), ['i', 'love', 'much', 'so'])

class TestMostCommonMultiple(unittest.TestCase):

    def test_most_common_multiple_inbetween_tiny1(self):
        ta = TextAnalyzer("tinyfile_1.txt")
        self.assertEqual(ta.most_common(1), ['cats'])
        self.assertEqual(ta.most_common(2), ['cats', 'i'])

    def test_most_common_multiple_inbetween_tiny3(self):
        ta = TextAnalyzer("tinyfile_3.txt")
        self.assertEqual(ta.most_common(2), ['cats', 'so'])
        self.assertEqual(ta.most_common(3), ['cats', 'i', 'so'])
        self.assertEqual(ta.most_common(4), ['cats', 'i', 'love', 'so'])

# Uncomment the lines below to run the unit tests for the extra credit
'''
class TestSimilarity(unittest.TestCase):
    def test_similarity_when_all_same(self):
        ta1 = TextAnalyzer("tinyfile_1.txt")
        ta2 = TextAnalyzer("tinyfile_1.txt") 
        self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 1.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 1.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 1.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2), 1.0)

    def test_similarity_when_all_different(self):
        ta1 = TextAnalyzer("tinyfile_1.txt")
        ta2 = TextAnalyzer("tinyfile_2.txt") 
        self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 0.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 0.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 0.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2), 0.0)

    def test_similarity_when_somewhat_different(self):
        ta1 = TextAnalyzer("tinyfile_1.txt")
        ta2 = TextAnalyzer("tinyfile_3.txt") 
        self.assertAlmostEqual(ta1.similarity_with(ta2, 1), 0.0)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 2), 0.171498585)
        self.assertAlmostEqual(ta1.similarity_with(ta2, 3), 0.272165527)
        self.assertAlmostEqual(ta1.similarity_with(ta2), 0.3872983346)
'''


def main():
    
    # You can uncomment out some of these lines to do some simple tests
    # with print statements before you are ready to run all the unit tests 
    # Or, use your own print statements here as well!
    fightsong = TextAnalyzer("fightsong.txt")
    print("Line count is ", fightsong.line_count())
    #print("Word count is ", fightsong.word_count())
    #print("Vocabulary is ", fightsong.vocabulary())
    #print("Frequencies are ", fightsong.frequencies())
    #print("Percent frequencies are ", fightsong.percent_frequencies())
    #print("Most common is ", fightsong.most_common())
    #print("Most common 3 are ", fightsong.most_common(3))

    # Un-comment this line when you are ready to run the unit tests.
    #unittest.main(verbosity=2)

    # Un-comment the lines below when you want to test the extra credit
    # or uncomment the class TestSimilarity above
    #ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    #ta2 = TextAnalyzer("files_for_testing/tinyfile_1.txt") 
    #print(ta1.similarity_with(ta2, 3))
    #ta1 = TextAnalyzer("files_for_testing/tinyfile_1.txt")
    #ta2 = TextAnalyzer("files_for_testing/tinyfile_2.txt") 
    #print(ta1.similarity_with(ta2, 3))

if __name__ == "__main__":
    main()
