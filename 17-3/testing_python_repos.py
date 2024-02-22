import unittest
import python_repos_visual as pr

class Test(unittest.TestCase):
    """Test python repos."""
    
    def setUp(self):
        """set the class attributes."""
        self.res = pr.api_call()
        self.dicts = pr.extract_info(self.res)
        self.data = pr.set_data(self.dicts)
        self.layout = pr.set_layout()
        
    def test_status_code(self):
        """Make sure the api call was succesfull."""
        self.assertEqual(self.res.status_code, 200)
        
    def test_items_length(self):
        """Make sure items are fully returned."""
        self.assertEqual(len(self.dicts["items"]), 30)
        
    def test_repo_dicts(self):
        """Test the exact key in the response dict."""
        keys = ["name", "stargazers_count", "html_url"]
        for key in keys:
            self.assertTrue(key in self.dicts["items"][0].keys())
            
            
    
    
        
        

        
        
if __name__ == "__main__":
    unittest.main()