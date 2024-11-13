# test_vote_counter.py

import unittest
from unittest.mock import patch, mock_open
from vote_counter import VoteCounter

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            vote_counter = VoteCounter("votes.csv")
            vote_counter.display_results()
            vote_counter.display_winner()
        
        # Expected output after tallying votes
        mock_print.assert_any_call("Alice: 3200 votes")
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simulate a CSV file with invalid votes data
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            vote_counter = VoteCounter("votes.csv")
            vote_counter.display_results()
            vote_counter.display_winner()

        # Expect Alice to be skipped due to invalid data, only Bob's votes should print correctly
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Alice: 2000 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)
    
    @patch("builtins.print")
    def test_count_votes_tie(self, mock_print):
        # Case with a tie between candidates
        mock_csv = """city,candidate,votes
        Springfield,Alice,1500
        Springfield,Bob,1500
        Shelbyville,Alice,2000
        Shelbyville,Bob,2000"""
        
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            vote_counter = VoteCounter("votes.csv")
            vote_counter.display_results()
            vote_counter.display_winner()

        # Expect both Alice and Bob to be tied
        mock_print.assert_any_call("Alice: 3500 votes")
        mock_print.assert_any_call("Bob: 3500 votes")
        mock_print.assert_any_call("winners are: Alice, Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_empty_file(self, mock_print):
        # Empty file case
        mock_csv = """city,candidate,votes"""
        
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            vote_counter = VoteCounter("votes.csv")
            vote_counter.display_results()
            vote_counter.display_winner()

        # Expect no output for candidates and no winner
        mock_print.assert_any_call("No winner")
        self.assertEqual(mock_print.call_count, 1) 

if __name__ == "__main__":
    unittest.main()

